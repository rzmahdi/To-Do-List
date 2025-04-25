import csv

class Task:
    def __init__(self, title, describtion, priority):
        self.title = title
        self.describtion = describtion
        self.priority = priority

    def __str__(self):
        return f"{self.title} | {self.describtion} | {self.priority}"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, index):
        try:
            del self.tasks[index]
            return True
        except IndexError:
            return False

    def show_tasks(self):
        if self.tasks:
            for i, task in enumerate(self.tasks):
                print(f"[{i}] {task}")
        else:
            print("there is no task yet.")

    def load_tasks(self, addres="./tasks.csv"):
        try:
            with open(addres, 'r') as data:
                reader = csv.reader(data)
                for line in reader:
                    task = Task(*line)
                    self.tasks.append(task)
            return True
        
        except FileNotFoundError:
            print(f"No such file: {addres}")
            return False
        
        except Exception as e:
            print(e)
            return False

    def save_tasks(self, addres="./tasks.csv"):
        try:
            with open(addres, "w") as file:
                writer = csv.writer(file)
                for task in self.tasks:
                    writer.writerow([task.title, task.describtion, task.priority])
            return True
        
        except FileNotFoundError:
            print(f"No such file: {addres}")
            return False
        
        except Exception as e:
            print(e)
            return False