import os
import math
import argparse
import torch
import torch.nn as nn
import torch.nn.functional as F
from pytorch_lightning import Trainer

from model import Retriever
from dataloader import ICTDataModule


class TrainConfig(object):
    tokenizer = 'bert-base-uncased'
    batch_size = 8
    dropout = 0.2
    query_max_len = 64
    passage_max_len = 288
    num_workers = 1
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

def main():
    config = TrainConfig()

    model = Retriever(config)
    dm = ICTDataModule(config)
    trainer = Trainer()

    trainer.fit(model, dm)


if __name__ == "__main__":
    main()
