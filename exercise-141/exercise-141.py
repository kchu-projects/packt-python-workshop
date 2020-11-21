import pandas as pd
import matplotlib.pyplot as plt


housing_df = pd.read_csv("data/HousingData.csv")

x = housing_df["RM"]
y = housing_df["MEDV"]
plt.scatter(x, y)
plt.show()
