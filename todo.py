tasks = []

def load_tasks():
    try:
        with open("tasks.txt", "r") as f:
            for line in f:
                tasks.append(line.strip())
    except FileNotFoundError:
        pass
def save_tasks():
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(task + "\n")
def add_task(task):
    tasks.append(task)
    save_tasks()


def show_tasks():
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def remove_task(number):
   if number > 0 and number <= len(tasks):
        tasks.pop(number - 1)
        save_tasks()

load_tasks()
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