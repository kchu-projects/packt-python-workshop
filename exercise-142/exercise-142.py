import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


housing_df = pd.read_csv("data/HousingData.csv")

sns.set()

corr = housing_df.corr()
plt.figure()
sns.heatmap(corr,
    xticklabels=corr.columns.values,
    yticklabels=corr.columns.values,
    cmap="Blues",
    linewidths=1.25,
    alpha=0.8)
plt.show()
