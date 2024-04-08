class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date

    def __str__(self):
        return f"Title: {self.title}\nDescription: {self.description}\nDue Date: {self.due_date}\n"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def display_tasks(self):
        for i, task in enumerate(self.tasks, start=1):
            print(f"Task {i}:")
            print(task)

    # Add more functionality like delete_task, update_task, etc. as needed


def main():
    todo_list = ToDoList()

    while True:
        print("1. Add Task")
        print("2. Display Tasks")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date: ")
            task = Task(title, description, due_date)
            todo_list.add_task(task)
            print("Task added successfully!\n")

        elif choice == "2":
            todo_list.display_tasks()

        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()
