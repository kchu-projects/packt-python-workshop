import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


salary_df = pd.read_csv("data/UKStatistics.csv")

sns.set()
# print(salary_df.shape)

x = salary_df["Salary Cost of Reports (£)"]
y = salary_df["Actual Pay Floor (£)"]
plt.hist(y)
# plt.scatter(x, y)
# plt.boxplot(x)
plt.show()
