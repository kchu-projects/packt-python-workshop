import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.neighbors import KNeighborsRegressor


housing_df = pd.read_csv("data/HousingData.csv")

# drop null values
housing_df = housing_df.dropna()

X = housing_df.iloc[:, :-1]
y = housing_df.iloc[:, -1]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

def regression_model_cv(model, k=5):
    scores = cross_val_score(model, X, y, scoring="neg_mean_squared_error", cv=k)
    rmse = np.sqrt(-scores)
    print(f"Reg rmse: {rmse}")
    print(f"Reg mean: {rmse.mean()}")


regression_model_cv(KNeighborsRegressor())

regression_model_cv(KNeighborsRegressor(n_neighbors=4))

regression_model_cv(KNeighborsRegressor(n_neighbors=7))

regression_model_cv(KNeighborsRegressor(n_neighbors=10))
