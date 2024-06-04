import time
import pandas as pd


class Cache:
    def __init__(self, data_path, expiration=3600):  # default expiration time in seconds
        self.data = None
        self.expiration = expiration
        self.timestamp = 0
        self.data_path = data_path
        self.data_loaded = False

    def load_data(self):
        # Load your data from the file
        self.data = pd.read_pickle(self.data_path)
        self.timestamp = time.time()
        self.data_loaded = True

    def get_data(self):
        current_time = time.time()
        if not self.data_loaded or (current_time - self.timestamp > self.expiration):
            self.load_data()
        return self.data
