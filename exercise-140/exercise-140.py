import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


housing_df = pd.read_csv("data/HousingData.csv")

sns.set()

title = "Median Boston Housing Prices"
plt.figure(figsize=(10, 6))
plt.hist(housing_df["MEDV"])
plt.title(title, fontsize=15)
plt.xlabel("1980 Median Value in Thousands")
plt.ylabel("Count")
plt.savefig(title, dpi=300)
plt.show()
