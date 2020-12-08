import pandas as pd
import numpy as np


df = pd.read_csv("data/HTRU_2.csv", header=None)
df.columns = [[
    "Mean of integrated profile",
    "Standard deviation of integrated profile",
    "Excess kurtosis of integrated profile",
    "Skewness of integrated profile",
    "Mean of DM-SNR curve",
    "Standard deviation of DM-SNR curve",
    "Excess kurtosis of DM-SNR curve",
    "Skewness of DM-SMR curve",
    "Class"
]]
print(df.head())
print(df.info())
print(len(df))
