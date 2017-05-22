import pandas as pd

data = pd.read_csv("census.csv")
print(data[(data['workclass'] == "Private")])