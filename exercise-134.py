import pandas as pd


# Create dictionary of test scores
test_dict = {
    "Corey": [63, 75, 88],
    "Kevin": [48, 98, 92],
    "Akshay": [87, 86, 85]
}

# Create DataFrame
df = pd.DataFrame(test_dict)
df = df.T

# Rename Columns
df.columns = ["Quiz_1", "Quiz_2", "Quiz_3"]
print(df)

# Access first row
print(df.iloc[0])
print(df.iloc[0, :])

# Access column by name
print(df["Quiz_1"])

# Access column by dot notation
print(df.Quiz_1)

# Access column by index
print(df.iloc[:, 0])
