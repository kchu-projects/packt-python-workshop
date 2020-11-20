import pandas as pd


housing_df = pd.read_csv("data/HousingData.csv")
print(housing_df.isnull().any())

print(housing_df.loc[:5, housing_df.isnull().any()])
print(housing_df.loc[:5, housing_df.isnull().any()].describe())
