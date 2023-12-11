import os

class Todo:
    def __init__(self):
        self.tasks = self.load_tasks()

    def load_tasks(self):
        tasks = []
        if os.path.exists("TodoTasks.txt"):
            with open("TodoTasks.txt", "r") as file:
                tasks = [line.strip() for line in file.readlines()]
        return tasks

    def save_tasks(self):
        with open("TodoTasks.txt", "w") as file:
            file.write("\n".join(self.tasks))

    def show_tasks(self):
        if not self.tasks:
            print("No tasks.")
        else:
            print("Tasks:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully.")

    def mark_completed(self, index):
        if 0 <= index < len(self.tasks):
            completed_task = self.tasks.pop(index)
            print(f"Task '{completed_task}' marked as completed.")
        else:
            print("Invalid task number.")

def main():
    todo = Todo()

    while True:
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Completed")
        print("4. Save and Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            todo.show_tasks()
        elif choice == "2":
            task = input("Enter the task: ")
            todo.add_task(task)
        elif choice == "3":
            todo.show_tasks()
            index = int(input("Enter the task number to mark as completed: ")) - 1
            todo.mark_completed(index)
        elif choice == "4":
            todo.save_tasks()
            print("Tasks saved. Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
