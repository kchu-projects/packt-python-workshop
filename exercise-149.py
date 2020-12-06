import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from sklearn import tree
from sklearn.ensemble import RandomForestRegressor


housing_df = pd.read_csv("data/HousingData.csv")

# drop null values
housing_df = housing_df.dropna()

X = housing_df.iloc[:, :-1]
y = housing_df.iloc[:, -1]


def regression_model_cv(model, k=5):
    scores = cross_val_score(model, X, y, scoring="neg_mean_squared_error", cv=k)
    rmse = np.sqrt(-scores)
    print(f"Reg rmse: {rmse}")
    print(f"Reg mean: {rmse.mean()}")


regression_model_cv(RandomForestRegressor(n_jobs=-1, n_estimators=100, random_state=0))

param_grid = {
    "max_depth": [None, 10, 30, 50, 70, 100, 200, 400],
    "min_samples_split": [2, 3, 4, 5],
    "min_samples_leaf": [1, 2, 3],
    "max_features": ["auto", "sqrt"]
}

reg = RandomForestRegressor(n_jobs=-1, random_state=0)
reg_tuned = RandomizedSearchCV(reg, param_grid, cv=5, scoring="neg_mean_squared_error")
reg_tuned.fit(X, y)

p = reg_tuned.best_params_
print(f"Best n_neighbors: {p}")
score = reg_tuned.best_score_
rsm = np.sqrt(-score)
print(f"Best score: {rsm}")

regression_model_cv(RandomForestRegressor(n_jobs=-1, n_estimators=500, random_state=0))
