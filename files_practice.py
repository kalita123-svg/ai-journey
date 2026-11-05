with open ('notes.txt', 'a') as f:
    f.write("first line\n")
    f.write("second line\n")
    f.write("third line\n")

with open("notes.txt", "r") as f:
        n = 1
        for line in f:

            print(f"{n}: {line.strip()}")
            n += 1