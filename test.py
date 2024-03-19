import pandas as pd
df = pd.read_pickle("data/master_data3.pkl")
print(df.shape)
print(df.head(20))
print(df.columns)