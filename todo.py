tasks = []

def add_task(task):
    tasks.append(task)

def show_tasks():
    n = 1
    for t in tasks:
        print(f"{n}. {t}")
        n = n + 1

def remove_task(number):
    if number > 0 and number <= len(tasks):
        tasks.pop(number - 1)

while True:
    answer = input("Type 'add', 'show', 'remove', or 'quit': ")
    if answer == "add":
        task = input("Enter the task: ")
        add_task(task)
    elif answer == "show":
        show_tasks()
    elif answer == "remove":
        try:
            number = int(input("Enter the task number to remove: "))
            remove_task(number)
        except ValueError:
            print("Please type a number, not a letter")
    elif answer == "quit":
        break
    else:
        print("I don't understand")