import pandas as pd


test_dict = {
    "Corey": [63, 75, 88],
    "Kevin": [48, 98, 92],
    "Akshay": [87, 86, 85]
}

df = pd.DataFrame(test_dict)
print(df)

df = df.T
print(df)
