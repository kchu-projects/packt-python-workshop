import pandas as pd


housing_df = pd.read_csv("data/HousingData.csv")
print(housing_df.describe())
print(housing_df.info())
print(housing_df.shape)
