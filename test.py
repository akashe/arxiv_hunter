import pandas as pd
df = pd.read_json("./data/master_data.json")
print(df.shape)
print(df.title.tail(20).iloc[5])