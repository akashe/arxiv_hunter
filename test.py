import pandas as pd
df:pd.DataFrame = pd.read_pickle("data/master_data3.pkl")
# df.to_json("data/master_data.json")
df = pd.read_json("data/master_data.json")
print(df.shape)
print(df.head(20))
print(df.columns)