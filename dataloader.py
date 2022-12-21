import os, json
import tarfile
import random
from itertools import chain, cycle
from functools import partial
import spacy
nlp = spacy.load("en_core_web_sm")

from transformers import AutoTokenizer
from torch.utils.data import IterableDataset, get_worker_info, DataLoader
from pytorch_lightning import LightningDataModule

from utils import get_all_files_with_extension


# create dataset class that inherits from IterableDataset
class ICTDataset(IterableDataset):
    """
    This class stores creates and iterable dataset for all the downloaded
    papers.
    """
    def __init__(self, total_nodes, global_rank, files, mode= "train"):
        super().__init__()

        self.files = files[int(global_rank*len(files)/total_nodes):int((global_rank+1)*len(files)/total_nodes)]
        self.mode = mode

    def process_file(self, file_path):
        """
        Loads a json file and yields the paragraph and a query constructed from it
        :param file_path: file location of query
        :return: tuple of query and passage
        """
        with open(file_path, "r") as f:
            data = json.load(f)

        paras = data["paras"]
        for para in paras:
            if len(para)<30:
                continue
            try:
                query = self.construct_query(para)

                if query == None:
                    continue
            except:
                continue

            if random.random()>0.9:
                yield query, para
            else:
                yield query, para.replace(query,"")

    def __iter__(self):
        # Return a never ending stream of paragraphs created by processing files in a cycle
        if self.mode=="train":
            return chain.from_iterable(self.process_file(i) for i in cycle(self.files))
        else:
            return chain.from_iterable(self.process_file(i) for i in self.files)

    def construct_query(self, text):
        """
        Construct a query by selecting a random sentence from the paragraph
        :param text: input paragraph
        :return: a sentence of the paragraph
        """
        doc = nlp(text)
        sentences = [str(sentence) for sentence in doc.sents]

        assert len(sentences) != 0
        if len(sentences) < 2:
            return None

        # select a random sentence
        sentence_no = random.randint(0, len(sentences) - 1)

        return sentences[sentence_no]


def collate_fn(batch, tokenizer, query_max_len, passage_max_len):

    queries, passages = list(zip(*batch))

    tokenized_queries = tokenizer(list(queries), padding= True, truncation= True, max_length=query_max_len, return_tensors="pt").data
    tokenized_passages = tokenizer(list(passages), padding= True, truncation= True, max_length=passage_max_len, return_tensors="pt").data

    # to check max possible length
    #tokenized_queries = tokenizer(list(queries), padding="max_length", truncation=True, max_length=query_max_len, return_tensors="pt").data
    #tokenized_passages = tokenizer(list(passages), padding="max_length", truncation=True, max_length=passage_max_len, return_tensors="pt").data

    return tokenized_queries, tokenized_passages


def worker_init_fn(worker_id):

    worker_info = get_worker_info()

    dataset = worker_info.dataset
    file_list = dataset.files

    files_per_worker = int(len(file_list)/float(worker_info.num_workers))
    left_over_files = file_list[-int(len(file_list)%float(worker_info.num_workers)):]

    worker_id = worker_info.id
    dataset.files = file_list[worker_id*files_per_worker:(worker_id+1)*files_per_worker]

    if worker_id == 0:
        dataset.files.extend(left_over_files)


class ICTDataModule(LightningDataModule):

    def __init__(self, config):
        super(ICTDataModule, self).__init__()
        self.data_file = config.data_file

        if not os.path.exists(config.data_dir):
            print('creating ', config.data_dir)
            os.makedirs(config.data_dir)
        self.data_dir = config.data_dir

        self.train_json_files = None
        self.test_json_files = None

        self.train_test_split = config.train_test_split
        self.tokenizer = AutoTokenizer.from_pretrained(config.tokenizer)
        self.query_max_len = config.query_max_len
        self.passage_max_len = config.passage_max_len
        self.num_workers = config.num_workers
        self.batch_size = config.batch_size

    def prepare_data(self) -> None:
        """
        Untar the tar file containing all the json
        :return: None
        """
        with tarfile.open(self.data_file) as tar_file:
            tar_file.extractall(self.data_dir)
    
    def setup(self, stage):
        
        json_files = get_all_files_with_extension(self.data_dir,"json")
        
        # Not shuffling to have the same sequence of train and test files on each GPU
        # Other way would be to phyically save to disk
        #random.shuffle(json_files)

        self.train_json_files = json_files[:int(len(json_files)*self.train_test_split)]
        self.test_json_files = json_files[int(len(json_files)*self.train_test_split):]

    def train_dataloader(self):
        train_dataset = ICTDataset(self.trainer.num_nodes,self.trainer.global_rank, self.train_json_files, mode="train")

        collate_fn_ = partial(collate_fn, tokenizer=self.tokenizer, query_max_len=self.query_max_len, passage_max_len= self.passage_max_len)

        return DataLoader(train_dataset, num_workers=self.num_workers, batch_size= self.batch_size, worker_init_fn= worker_init_fn, collate_fn=collate_fn_, pin_memory= True)

    def val_dataloader(self):
        test_dataset = ICTDataset(self.trainer.num_nodes,self.trainer.global_rank, self.test_json_files, mode="test")

        collate_fn_ = partial(collate_fn, tokenizer=self.tokenizer, query_max_len=self.query_max_len, passage_max_len= self.passage_max_len)

        return DataLoader(test_dataset, num_workers=self.num_workers, batch_size= self.batch_size, worker_init_fn= worker_init_fn, collate_fn=collate_fn_, pin_memory= True)