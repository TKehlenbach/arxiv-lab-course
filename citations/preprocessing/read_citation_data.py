import pandas as pd

name = "../citation-network-dataset/reference_data.feather"
df = pd.read_feather(name)
print(df.head())
print(df.info)
