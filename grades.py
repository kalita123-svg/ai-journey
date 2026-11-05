def grade(score):
    if score >= 90:
        return 'A'
    elif score >= 70:
        return 'B'
    else:
        return 'C'

scores = [95, 82, 70, 66, 40]
counts = {"A": 0, "B": 0, "C": 0}

for s in scores:
    letter = grade(s)
    counts[letter] = counts[letter] + 1

print(counts)