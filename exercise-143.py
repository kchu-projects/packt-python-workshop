import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


housing_df = pd.read_csv("data/HousingData.csv")

sns.set()

x = housing_df["RM"]
# y = housing_df["MEDV"]
plt.boxplot(x)
plt.show()
