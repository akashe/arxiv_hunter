import os
import math
import argparse
import torch
import torch.nn as nn
import torch.nn.functional as F
import pytorch_lightning as pl
from pytorch_lightning import Trainer
from pytorch_lightning.strategies import DDPStrategy
from pytorch_lightning.plugins.environments.lightning_environment import LightningEnvironment
from pytorch_lightning.loggers import TensorBoardLogger

from model import Retriever
from dataloader import ICTDataModule

from pytorch_lightning.callbacks.early_stopping import EarlyStopping
from pytorch_lightning.callbacks.model_checkpoint import ModelCheckpoint

from pytorch_lightning.trainer.states import RunningStage


class TrainConfig(object):
    tokenizer = 'bert-base-uncased'
    batch_size = 8
    dropout = 0.2
    query_max_len = 64
    passage_max_len = 288
    num_workers = 12
    projection = True
    projection_dims = 128
    loss_scaling = True
    model_hidden_dims = 768
    scale_factor = 1
    topk = [1, 5]
    query_encoder = 'bert-base-uncased'
    passage_encoder = 'bert-base-uncased'
    lr = 0.000001
    beta1 = 0.9
    beta2 = 0.999
    weight_decay = 0.01
    clip = 1.0
    train_test_split = 0.99
    data_dir = "data/extract_json"
    data_file = "data/processed.tar.gz"    

    
def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("--hosts", type=list, default=os.environ["SM_HOSTS"])
    parser.add_argument("--current-host", type=str, default=os.environ["SM_CURRENT_HOST"])
    parser.add_argument("--model-dir", type=str, default=os.environ["SM_MODEL_DIR"])
    parser.add_argument("--num-gpus", type=int, default=int(os.environ["SM_NUM_GPUS"]))

    parser.add_argument("--num_nodes", type=int, default = len(os.environ["SM_HOSTS"]))
           
    # num gpus is per node
    world_size = int(os.environ["SM_NUM_GPUS"]) * len(os.environ["SM_HOSTS"])
                 
    parser.add_argument("--world-size", type=int, default=world_size)
    
    args = parser.parse_args()
    
    return args


class ValEveryNSteps(pl.Callback):
    """
    This call back ensures that the validation step is done after a specific number of global steps
    Currently the behaviour of validation is geared for epoch based training and not step based training
    """
    
    def __init__(self, every_n_steps):                                             
        self.last_run = None                                                     
        self.every_n_steps = every_n_steps                                                                                                                                                                          
    def on_batch_end(self, trainer, pl_module):                                  
        # Prevent Running validation many times in gradient accumulation                                       
        if trainer.global_step == self.last_run:                                                
            return                                                                  
        else:                                                                    
            self.last_run = None                                                          
        if trainer.global_step % self.every_n_steps == 0 and trainer.global_step != 0:   
            trainer.training = False                                               
            stage = trainer.state.stage                                           
            trainer.state.stage = RunningStage.VALIDATING                          
            trainer._run_evaluate()                                               
            trainer.state.stage = stage                                             
            trainer.training = True                                               
            trainer._logger_connector._epoch_end_reached = False                   
            self.last_run = trainer.global_step


if __name__ == "__main__":
    
    # parse env variables
    args = parse_args()
    
    # initializing config object
    config = TrainConfig()
    
    # create datamodule object
    dm = ICTDataModule(config)
    
    # creating model
    model = Retriever(config)
    
    
    local_rank = os.environ["LOCAL_RANK"]
    torch.cuda.set_device(int(local_rank))
    
    num_nodes = args.num_nodes
    num_gpus = args.num_gpus
    
    env = LightningEnvironment()
    
    env.world_size = lambda: int(os.environ.get("WORLD_SIZE", 0))
    env.global_rank = lambda: int(os.environ.get("RANK", 0))
    
    ddp = DDPStrategy(cluster_environment=env, accelerator="gpu",find_unused_parameters=False)
    
    os.makedirs(os.path.join("/opt/tb_logs","my_model"), exist_ok =True)
    
    logger = TensorBoardLogger(save_dir="/opt/tb_logs", name="my_model")
    
    early_stop_callback = EarlyStopping(monitor='train_loss',min_delta=0.01,patience=100,mode='min')
    
    model_checkpoint_callback= ModelCheckpoint(dirpath=args.model_dir, monitor='val_loss', mode='min', save_top_k=1, every_n_train_steps = 1001)
    
    val_every_n_steps_callback = ValEveryNSteps(every_n_steps=1000)
    
    # auto_lr_find doesnt work for strategy ddp
    
    trainer = Trainer(max_steps=50000,
                      min_steps=2,
                      strategy=ddp,
                      devices=num_gpus,
                      num_nodes=num_nodes,
                      auto_scale_batch_size = "binsearch",
                      default_root_dir = args.model_dir,
                      logger= logger, callbacks=[early_stop_callback, model_checkpoint_callback, val_every_n_steps_callback],
                      log_every_n_steps=50,
                      enable_checkpointing=True)
    
    trainer.fit(model, dm)
    
    with open(os.path.join(args.model_dir, 'final_model_state.pt'), 'wb') as f:
        torch.save(model.state_dict(), f)
