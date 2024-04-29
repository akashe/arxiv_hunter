"""Implementation of TFIDF Recommender"""

import os.path
import pdb
import pickle
import numpy as np
from abc import abstractmethod, ABC
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.snowball import SnowballStemmer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

nltk.download("stopwords")
nltk.download("punkt")


class LearnVocabularyBase(ABC):
    """Parent Recommender Class"""

    @abstractmethod
    def preprocess(self, text):
        """Preprocess data for tfidf"""

    @abstractmethod
    def learn_vocabulary(self):
        """Learn tfidf vocabulary"""

    @abstractmethod
    def transform_data(self):
        """Transform data wrt the Learnt Vocabulary"""


class LearnTransformVocabulary(LearnVocabularyBase):
    """Recommender Implementation"""

    def __init__(self, data_path="data/master_data.pkl") -> None:
        self.data = pd.read_pickle(data_path)
        self.corpus = self.data["pdf_text"]
        self.learn_vocabulary()
        self.transform_data()
        super().__init__()
        print("...LearnVocabulary initialized...")

    # tokenize, stem and remove punctuation
    def preprocess(self, text):
        """word tokenization, snowball stemming and punctuation removal"""
        stemmer = SnowballStemmer("english")
        return [stemmer.stem(token) for token in word_tokenize(text) if token.isalpha()]

    def learn_vocabulary(self):
        english_stopwords = stopwords.words("english")
        self.vectorizer = TfidfVectorizer(
            lowercase=True,
            tokenizer=self.preprocess,
            stop_words=english_stopwords,
            ngram_range=(1, 1),
        )
        self.vocabulary = self.vectorizer.fit(self.corpus)

    def transform_data(self):
        self.transformed_data = self.vectorizer.transform(self.corpus)

        try:
            # load the vectorizer and the transformed data from the pickle files
            with open("data/vectorizer.pkl", "rb") as f:
                self.vectorizer = pickle.load(f)
            with open("data/transformed_data.pkl", "rb") as f:
                self.transformed_data = pickle.load(f)
        except FileNotFoundError:
            with open("data/vectorizer.pkl", "wb") as f:
                pickle.dump(self.vectorizer, f)
            with open("data/transformed_data.pkl", "wb") as f:
                pickle.dump(self.transformed_data, f)


class Recommender:
    def __init__(self, vectorizer_path: str, vocabulary_path: str):
        # load the vectorizer and the learnt vocabulary from the pickle files
        with open(vectorizer_path, "rb") as f:
            self.vectorizer = pickle.load(f)
        with open(vocabulary_path, "rb") as f:
            self.learnt_transformed_vocabulary = pickle.load(f)

    # def recommend(self, query: str):
    #     # use the vectorizer to transform the query
    #     transformed_query = self.vectorizer.transform([query])
    #     # create a cosine similarity matrix with the transformed query and the learnt vocabulary
    #     cosine_similarities = cosine_similarity(
    #         X=transformed_query, Y=self.learnt_transformed_vocabulary
    #     )
    #     # sort the results by similarity score
    #     result = sorted(
    #         list(enumerate(cosine_similarities[0])), reverse=True, key=lambda x: x[1]
    #     )
    #     # return the top 10 results
    #     return result

    def top100(self, arr, results=100):
        kth_largest = (results + 1) * -1
        return np.argsort(arr)[:kth_largest:-1]

    def recommend(self, query: str):
        query = query.replace("+", " ")
        transformed_query = self.vectorizer.transform([query])
        cosine_similarities = cosine_similarity(
            X=self.learnt_transformed_vocabulary,
            Y=transformed_query
        ).flatten()
        top_related_indices = self.top100(cosine_similarities)
        return top_related_indices

if __name__ == "__main__":
    # vocabulary = LearnTransformVocabulary(
    #     data_path = "data/master_data.pkl"
    # )
    recommender = Recommender(
        vectorizer_path="data/vectorizer.pkl",
        vocabulary_path="data/transformed_data.pkl",
    )

    recommendations = recommender.recommend(query="LLM , Attention, Mechanism, GPT, Mamba, Model")
    print(recommendations)
    df = pd.read_pickle("data/master_data.pkl")
    print(len(df))

    for index in recommendations:
        paper_data = df.iloc[index].to_dict()
        print(paper_data['title'])

    # # Create a parser object
    # parser = argparse.ArgumentParser(
    #     description="A recommender system based on tf-idf and cosine similarity"
    # )

    # # Add an argument for the query
    # parser.add_argument(
    #     "-q", "--query", type=str, help="The query to get recommendations for"
    # )
    # parser.add_argument(
    #     "data_loc",
    #     help="Location for stored data",
    #     nargs="?",
    #     default="data/master_data.pkl",
    # )

    # # Parse the arguments
    # args = parser.parse_args()

    # # Get the query from the argument
    # user_query = args.query
    # data_loc = args.data_loc

    # assert os.path.exists(data_loc), "Data path seems to be missing"

    # df = pd.read_pickle(data_loc)
    # recommender = Recommender(data=df)
    # res = recommender.recommend(user_query)
    # print(res)
