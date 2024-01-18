import pandas as pd
from tfidf import TFIDF

df=pd.read_pickle("../data/master_data.pkl")

tfidf=TFIDF(corpus=df["pdf_text"].values)

query="Attention mechanism, gpt"
max_result=5

res=tfidf.recommend(query,max_result)

print(res.shape)
print(res)
