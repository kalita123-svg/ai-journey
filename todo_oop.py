from task import Task

tasks = []
def load_tasks():
    try:
        with open("tasks.txt", "r") as f:
            for line in f:
                parts = line.strip().split(",", 1)
                title = parts[1]
                t = Task(title)
                done = parts[0] == "True"
                t.done = done
                tasks.append(t)
    except FileNotFoundError:
        pass
def save_tasks():
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(f"{task.done},{task.title}\n")
def add_task(title):
    tasks.append(Task(title))
    save_tasks()


def show_tasks():
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. ", end="")
        task.show()

def done_task(number):
    if number > 0 and number <= len(tasks):
        tasks[number - 1].complete()
        save_tasks()

def remove_task(number):
   if number > 0 and number <= len(tasks):
        tasks.pop(number - 1)
        save_tasks()

load_tasks()
while True:
    answer = input("Type 'add', 'show', 'remove', 'done' or 'quit': ")
    if answer == "add":
        task = input("Enter the task: ")
        add_task(task)
    elif answer == "show":
        show_tasks()
    elif answer == "done":
        try:
            number = int(input("Enter the task number to mark as done: "))
            done_task(number)
        except ValueError:
            print("Please type a number, not a letter")
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