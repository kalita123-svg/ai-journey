


class Task:
    def __init__(self, title):
        self.title = title
        self.done = False
    def complete(self):
        self.done = True
    def show(self):
        if self.done:
            print(f"[x] {self.title}")
        else:
            print(f"[ ] {self.title}")
a = Task("buy coffee")
b = Task("study python")
a.complete()
a.show()
b.show()