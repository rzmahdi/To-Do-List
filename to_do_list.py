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
            return True
        else:
            print("there is no task yet.")
            return False

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
        
        except Exception as e:
            print(e)
            return False


if __name__ == "__main__":
    todo = ToDoList()

    while True:
        print("*** To Do List ***")
        print("1. add task")
        print("2. remove task")
        print("3. show all tasks")
        print("4. load tasks")
        print("5. save tasks")
        print("6. Exit")
        user_choice = input("enter your choise: ")


        # add task
        if user_choice == '1':
            print()
            task_title = input("title: ")
            task_description = input("description: ")
            task_priority = input("priority [low, medium, high]: ")

            task = Task(task_title, task_description, task_priority)
            todo.add_task(task)

            print()
            todo.show_tasks()
            print()


        # remove task
        elif user_choice == '2':
            print()

            if todo.show_tasks():
                print()
                try:
                    task_index = int(input("task id: "))
                except:
                    print("\nEnter a valid index!")
                else:
                    if todo.remove_task(task_index):
                        print(f"\ntask [{task_index}] properly remove.")
                    else:
                        print(f"\ntask id [{task_index}] is out of range!")

            print()


        # show tasks
        elif user_choice == '3':
            print()
            todo.show_tasks()
            print()


        # load tasks
        elif user_choice == '4':
            print()

            print("example.csv")
            file_addres = input("file addres: ")
            if todo.load_tasks(file_addres):
                todo.show_tasks()
            
            print()


        # save tasks
        elif user_choice == '5':
            print()

            print("example.csv")
            file_addres = input("file addres: ")
            if file_addres.endswith(".csv"):
                if todo.save_tasks(file_addres):
                    print("file save properly.")
            else:
                print("it must be .csv file!")

            print()


        # Exit
        elif user_choice == '6':
            break


        else:
            print()
            print("choose between [1-6] !!! ")
            print()