import pandas as pd

df = pd.read_csv("expenses.csv")
print(df)
print(df["amount"])
print(df["amount"].sum())
print(df.groupby("category")["amount"].sum())
high = df[df["amount"] > 10]
print(high)
food_expenses = df[df["category"] == "food"]
print(food_expenses)