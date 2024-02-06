"""User Implementation"""

from abc import abstractmethod, ABC
from typing import Optional, List
import argparse
import pandas as pd
from src.logics.recommender import Recommender


class BaseUser(ABC):
    """Base User Class"""

    @abstractmethod
    def search(self, query: str):
        """search feature"""

    @abstractmethod
    def feed(self):
        """feed feature"""


class User(BaseUser):
    """User Class Implementation"""

    def __init__(self, keywords: Optional[List[str]], recommender: object) -> None:
        self.keywords = keywords
        self.recommender = recommender
        super().__init__()

    def search(self, query: str):
        self.recommender.recommend(self, query)

    def feed(self):
        return "feed"


if __name__ == "__main__":
    # Create a parser object
    parser = argparse.ArgumentParser(
        description="A recommender system based on tf-idf and cosine similarity"
    )

    # Add an argument for the query
    parser.add_argument("query", type=str, help="The query to get recommendations for")

    # Parse the arguments
    args = parser.parse_args()

    # Get the query from the argument
    user_query = args.query

    df = pd.read_pickle("../data/master_data.pkl")
    tfidf_recommender = Recommender(data=df)
    res = tfidf_recommender.recommend(user_query)
    print(res)
