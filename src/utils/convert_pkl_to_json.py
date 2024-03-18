import pandas as pd

df:pd.DataFrame = pd.read_pickle("../../data/master_data3.pkl")
df.to_json("../../data/master_data.json")

new_df = pd.read_json("../../data/master_data.json")
print(new_df.shape)