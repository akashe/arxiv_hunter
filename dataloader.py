import torch
import torch.nn as nn
from torch.utils.data import IterableDataset

from utils import get_all_files_with_extension

# create dataset class that inherits from IterableDataset
class ICTDataset(IterableDataset):
    """
    This class stores creates and iterable dataset for all the downloaded
    papers.
    """
    def __init__(self, global_rank):


# collate_fn
