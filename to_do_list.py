class Task:
    def __init__(self, title, describtion, priority):
        self.title = title
        self.describtion = describtion
        self.pripriority = priority

    def __str__(self):
        return f"{self.title} | {self.describtion} | {self.pripriority}"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)