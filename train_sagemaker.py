import os
import math
import argparse
import torch
import torch.nn as nn
import torch.nn.functional as F
from pytorch_lightning import Trainer
from pytorch_lightning.strategies import DDPStrategy
from pytorch_lightning.plugins.environments.lightning_environment import LightningEnvironment

from model import Retriever
from dataloader import ICTDataModule


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
    train_test_split = 0.9
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
    
    ddp = DDPStrategy(cluster_environment=env, accelerator="gpu")
    
    trainer = Trainer(max_steps=500, min_steps=2, strategy=ddp, devices=num_gpus, num_nodes=num_nodes, default_root_dir = args.model_dir)

    trainer.fit(model, dm)
