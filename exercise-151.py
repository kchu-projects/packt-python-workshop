import pandas as pd
import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression


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

X = df.iloc[:, 0:8]
y = df.iloc[:, 8]

def clf_model(model):
    clf = model
    scores = cross_val_score(clf, X, y)
    print(f"Scores: {scores}")
    print(f"Mean score: {scores.mean()}")

clf_model(LogisticRegression(random_state=0))
