from abc import abstractmethod, ABC
from recommender import Recommender
import pandas as pd

class BaseUser(ABC):
    @abstractmethod
    def search(self):
        pass

class User(BaseUser):
    def __init__(self, preference:dict, recommender:object) -> None:
        self.preference=preference
        self.recommender=recommender
        super().__init__()
    
    def search(self, query:str):
        self.recommender.recommend(self, query)

if __name__ == "__main__":
    df = pd.read_pickle("../data/master_data.pkl")
    tfidf = Recommender(data=df)

    query = "Attention mechanism, gpt"
    res = tfidf.recommend(query)

    print(res.shape)
    print(res)