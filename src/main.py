import pandas as pd
from tfidf import TFIDF

df = pd.read_pickle("../data/master_data.pkl")
corpus: list[str] = df[["pdf_text"]].values

tfidf = TFIDF(corpus=corpus)

query = "Attention mechanism, gpt"
max_result = 5

res = tfidf.recommend(query, max_result)

print(res.shape)
print(res)
