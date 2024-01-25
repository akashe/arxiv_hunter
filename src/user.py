from abc import abstractmethod, ABC
from recommender import Recommender
import pandas as pd
import argparse

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
    # Create a parser object
    parser = argparse.ArgumentParser(description="A recommender system based on tf-idf and cosine similarity")

    # Add an argument for the query
    parser.add_argument("query", type=str, help="The query to get recommendations for")

    # Parse the arguments
    args = parser.parse_args()

    # Get the query from the argument
    query = args.query

    df = pd.read_pickle("../data/master_data.pkl")
    recommender = Recommender(data=df)
    res = recommender.recommend(query)
    print(res)