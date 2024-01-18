import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class TFIDF:
    def __init__(self, corpus:list[str]):
        self.corpus = corpus
        self.nlp = spacy.load('en_core_web_sm')

    def spacy_tokenizer(self,doc):
        with nlp.disable_pipes(*["ner", "parser"]):
            return [t.lemma_ for t in self.nlp(doc) if not t.is_punct and not t.is_space and t.is_alpha]

    def top_k(self, arr, k):
        kth_largest = (k + 1) * -1
        return np.argsort(arr)[:kth_largest:-1]

    def create_tfidf_features(self):
        vectorizer = TfidfVectorizer(tokenizer=self.spacy_tokenizer)
        features = vectorizer.fit_transform(self.corpus)
        return vectorizer, features

    def recommend(self, query, max_result):
        vectorizer, features=self.create_tfidf_features()
        query_tfidf = vectorizer.transform(query)
        cosine_similarities = cosine_similarity(features, query_tfidf).flatten()

        top_related_indices = self.top_k(cosine_similarities, max_result)
        top_related_cs=cosine_similarities[top_related_indices]
        return df.iloc[top_related_indices]

if __name__=="__main__":
    df=pd.read_pickle("../data/master_data.pkl")
    tfidf=TFIDF(corpus=df["pdf_text"].values)

    query="Attention mechanism, gpt"
    max_result=5
    
    res=tfidf.recommend(query,max_result)
    print(res.shape)
    print(res)
