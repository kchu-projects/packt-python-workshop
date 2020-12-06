import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import GridSearchCV


housing_df = pd.read_csv("data/HousingData.csv")

# drop null values
housing_df = housing_df.dropna()

X = housing_df.iloc[:, :-1]
y = housing_df.iloc[:, -1]

neighbors = np.linspace(1, 20, 20)
k = neighbors.astype(int)
param_grid = {"n_neighbors": k}
knn = KNeighborsRegressor()
knn_tuned = GridSearchCV(knn, param_grid, cv=5, scoring="neg_mean_squared_error")
knn_tuned.fit(X, y)

k = knn_tuned.best_params_
print(f"Best n_neighbors: {k}")
score = knn_tuned.best_score_
rsm = np.sqrt(-score)
print(f"Best score: {rsm}")
