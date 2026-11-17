import csv

total = 0
with open("expenses.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["date"], row["category"], row["amount"])
        total += float(row["amount"])
print(f"Total expenses: ${total:.2f}")

by_category = {}
with open("expenses.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        category = row["category"]
        amount = float(row["amount"])
        if category not in by_category:
            by_category[category] = 0
        by_category[category] += amount

for category, amount in by_category.items():
    print(f"{category}: ${amount:.2f}")