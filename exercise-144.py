import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

housing_df = pd.read_csv("data/HousingData.csv")

# drop null values
housing_df = housing_df.dropna()

X = housing_df.iloc[:, :-1]
y = housing_df.iloc[:, -1]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# create the regressor
reg = LinearRegression()

# fit the regressor to the training data
reg.fit(X_train, y_train)

# predict on the test data
y_pred = reg.predict(X_test)

# compute and print RMSE
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print(f"Root Mean Squared Error: {rmse}")
