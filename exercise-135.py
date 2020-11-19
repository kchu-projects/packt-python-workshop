import pandas as pd


# Create dictionary of test scores
test_dict = {
    "Corey": [63, 75, 88],
    "Kevin": [48, 98, 92],
    "Akshay": [87, 86, 85]
}

# Create DataFrame
df = pd.DataFrame(test_dict)

# Limit first two rows
print(df[0:2])

# Transpose
df = df.T
print(df)

# Rename columns
df.columns = ["Quiz_1", "Quiz_2", "Quiz_3"]
print(df)

# New DataFrame from first two rows and last two columns
rows = ["Corey", "Kevin"]
cols = ["Quiz_2", "Quiz_3"]
df_spring = df.loc[rows, cols]
print(df_spring)

# Select first two rows and last two columns using index numbers
print(df.iloc[[0, 1], [1, 2]])
print(df.iloc[0:2, 1:3])

# Make new column as mean of other columns
df["Quiz_Avg"] = df.mean(axis=1)
print(df)

# Add a new Quiz
df["Quiz_4"] = [92, 95, 88]
print(df)

del df["Quiz_Avg"]
print(df)
