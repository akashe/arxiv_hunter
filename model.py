import os
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from pytorch_lightning import LightningModule, Trainer

from transformers import AutoModel


class Retriever(LightningModule):
    def __init__(self, config):
        super(Retriever, self).__init__()

        self.config = config

        self.query_encoder = AutoModel.from_pretrained(config.query_encoder)
        self.passage_encoder = AutoModel.from_pretrained(config.passage_encoder).requires_grad_(False)

        if config.projection:
            self.fc_query = nn.Linear(self.query_encoder.config.hidden_size, config.projection_dims)
            self.fc_passage = nn.Linear(self.passage_encoder.config.hidden_size, config.projection_dims)

        self.layer_norm_query = nn.LayerNorm(config.projection_dims)
        self.layer_norm_passage = nn.LayerNorm(config.projection_dims)

        self.dropout = nn.Dropout(config.dropout)

        self.topk = config.topk
        self.scale = config.loss_scaling
        self.scaling_factor = config.scale_factor*math.sqrt(config.model_hidden_dims)

        self.correct_index = nn.Parameter(torch.arange(0,1000), requires_grad=False)

    def forward(self, tokenized_queries, tokenized_passages):

        batch_size = tokenized_queries["input_ids"].shape[0]

        encoded_query = self.query_encoder(**tokenized_queries)
        encoded_query_representation = encoded_query.pooler_output

        encoded_passage = self.passage_encoder(**tokenized_passages)
        encoded_passage_representation = encoded_passage.pooler_output

        if self.config.projection:
            encoded_query_representation = self.fc_query(encoded_query_representation)
            encoded_passage_representation = self.fc_passage(encoded_passage_representation)

        encoded_query_representation = self.layer_norm_query(encoded_query_representation)
        encoded_passage_representation = self.layer_norm_passage(encoded_passage_representation)

        if self.training:
            encoded_query_representation = self.dropout(encoded_query_representation)
            encoded_passage_representation = self.dropout(encoded_passage_representation)

        # calculate loss
        scores = torch.matmul(encoded_query_representation, torch.transpose(encoded_passage_representation, 0, 1))
        if self.scale:
            scores /= self.scaling_factor

        softmax_scores = F.log_softmax(scores, dim=1)

        return softmax_scores

    def get_accuracy(self, softmax_scores, batch_size):
        # calculate accuracy
        with torch.no_grad():
            maxk = max(self.topk)
            _, pred = softmax_scores.topk(maxk, 1, True, True)
            pred = pred.t()

            correct = (pred == self.correct_index.unsqueeze(dim=0)).expand_as(pred)

            acc = []
            for k in self.topk:
                correct_k = correct[:k].reshape(-1).float().sum(0, keepdim=True)
                acc.append(correct_k.mul_(1.0 / batch_size))

        return acc

    def training_step(self, train_batch, batch):

        tokenized_queries, tokenized_passages = train_batch
        batch_size = tokenized_queries["input_ids"].shape[0]

        softmax_scores = self(tokenized_queries, tokenized_passages)

        loss = F.nll_loss(softmax_scores, self.correct_index[:batch_size], reduction="sum")

        acc = self.get_accuracy(softmax_scores)

        self.log("train_loss", loss)
        self.log("train_acc", acc)

        return loss

    def validation_step(self, train_batch, batch):

        tokenized_queries, tokenized_passages = train_batch
        batch_size = tokenized_queries["input_ids"].shape[0]

        softmax_scores = self(tokenized_queries, tokenized_passages)

        loss = F.nll_loss(softmax_scores, self.correct_index[:batch_size], reduction="sum")

        acc = self.get_accuracy(softmax_scores)

        self.log("val_loss", loss)
        self.log("val_acc", acc)

        return loss

    def configure_optimizers(self):
        optimizer = torch.optim.Adam(self.parameters(), lr = self.config.lr,
                                     betas = (self.config.beta1,self.config.beta2),
                                     weight_decay=self.config.weight_decay)

        return optimizer

    def backward(
        self, loss, optimizer, optimizer_idx, *args, **kwargs
    ) -> None:
        loss.backward()

    def optimizer_step(
        self,
        epoch,
        batch_idx,
        optimizer,
    ) -> None:
        optimizer.step()
