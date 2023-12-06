class Task:
    def __init__(self, title, description, due_date, status="To Do"):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def __str__(self):
        return f"Title: {self.title}, Description: {self.description}, Due Date: {self.due_date}, Status: {self.status}"

class User:
    def __init__(self, username):
        self.username = username
        self.tasks = []

    def add_task(self, title, description, due_date):
        task = Task(title, description, due_date)
        self.tasks.append(task)

    def view_tasks(self):
        if self.tasks:
            for i, task in enumerate(self.tasks, 1):
                print(f"Task {i}: {task}")
        else:
            print("No tasks found.")

class TaskManager:
    def __init__(self):
        self.users = {}

    def add_user(self, username):
        if username not in self.users:
            self.users[username] = User(username)
        else:
            print(f"User '{username}' already exists.")

    def get_user(self, username):
        if username in self.users:
            return self.users[username]
        else:
            print(f"User '{username}' not found.")
            return None

if __name__ == "__main__":
    task_manager = TaskManager()
    
    while True:
        print("\nTask Manager Menu:")
        print("1. Create User")
        print("2. Add Task")
        print("3. View Tasks")
        print("4. Quit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter your username: ")
            task_manager.add_user(username)
        elif choice == "2":
            username = input("Enter your username: ")
            user = task_manager.get_user(username)
            if user:
                title = input("Enter task title: ")
                description = input("Enter task description: ")
                due_date = input("Enter due date: ")
                user.add_task(title, description, due_date)
        elif choice == "3":
            username = input("Enter your username: ")
            user = task_manager.get_user(username)
            if user:
                user.view_tasks()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please select a valid option.")
