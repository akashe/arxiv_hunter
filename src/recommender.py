from abc import abstractmethod, ABC
import numpy as np
import pandas as pd
import nltk
import argparse
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.snowball import SnowballStemmer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

nltk.download("stopwords")

class BaseRecommender(ABC):
    @abstractmethod
    def preprocess(self):
        pass

    @abstractmethod
    def learn_vocabulary(self):
        pass

    @abstractmethod
    def transform_data(self):
        pass

    @abstractmethod
    def recommend(self):
        pass


class Recommender(BaseRecommender):
    def __init__(self, data:pd.DataFrame) -> None:
        self.data=data
        self.corpus=self.data["pdf_text"]
        self.learn_vocabulary()
        self.transform_data()
        super().__init__()
    
    # tokenize, stem and remove punctuation
    def preprocess(self,text):
        """word tokenization, snowball stemming and punctuation removal"""
        stemmer=SnowballStemmer("english")
        return [stemmer.stem(token) for token in word_tokenize(text) if token.isalpha()]
    
    def learn_vocabulary(self): 
        english_stopwords=stopwords.words("english")
        self.vectorizer=TfidfVectorizer(
            lowercase=True,
            tokenizer=self.preprocess,
            stop_words=english_stopwords,
            ngram_range=(1,2)
        )
        self.vocabulary=self.vectorizer.fit(self.corpus)

    def transform_data(self):
        self.transformed_data=self.vectorizer.transform(self.corpus)

    def recommend(self, query:str):
        transformed_query=self.vectorizer.transform([query]) 
        cosine_similarities = cosine_similarity(
            X=transformed_query,
            Y=self.transformed_data
        )
        result=sorted(list(enumerate(cosine_similarities[0])), reverse=True, key=lambda x:x[1])
        return result[:10]

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
