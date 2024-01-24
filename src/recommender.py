from abc import abstractmethod, ABC
import numpy as np
import pandas as pd
import nltk
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
    def top10(self):
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
    
    def top10(self, arr, results=10):
        kth_largest = (results + 1) * -1
        return np.argsort(arr)[:kth_largest:-1]

    def recommend(self, query:str):
        transformed_query=self.vectorizer.transform(list(query)) 
        cosine_similarities = cosine_similarity(
            X=self.transformed_data,
            Y=transformed_query
        ).flatten()
        top_related_indices = self.top10(cosine_similarities)
        return top_related_indices
    
if __name__ == "__main__":
    df = pd.read_pickle("../data/master_data.pkl")
    tfidf = Recommender(data=df)

    query = "Attention mechanism, gpt"
    res = tfidf.recommend(query)

    print(res.shape)
    print(res)