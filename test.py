import pandas as pd
df:pd.DataFrame = pd.read_pickle("data/master_data_2 years.pkl")
# df.to_json("data/master_data.json")
df = pd.read_json("data/master_data.json")
print(df.shape)
print(df.columns)
print(pd.to_datetime(df["published_date"]))