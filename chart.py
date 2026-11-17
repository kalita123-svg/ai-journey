import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("expenses.csv")
totals = df.groupby("category")["amount"].sum()

plt.bar(totals.index, totals.values)
plt.xlabel("Category")
plt.ylabel("Total Amount")
plt.title("Expenses by Category")
plt.savefig("expenses.png")
plt.show()