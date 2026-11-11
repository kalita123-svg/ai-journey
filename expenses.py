import csv

with open("expenses.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["date"], row["category"], row["amount"])