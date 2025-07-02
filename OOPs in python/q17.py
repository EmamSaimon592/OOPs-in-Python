import os

FILE_NAME = "todo.txt"

# Load tasks from file
def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return [line.strip() for line in file.readlines()]

# Save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Show menu
def show_menu():
    print("\n--- To-Do List App ---")
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")

# Main program
def main():
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            if not tasks:
                print("No tasks found.")
            else:
                print("\nYour Tasks:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")

        elif choice == "2":
            new_task = input("Enter new task: ")
            tasks.append(new_task)
            save_tasks(tasks)
            print("Task added!")

        elif choice == "3":
            if not tasks:
                print("No tasks to remove.")
                continue
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
            try:
                index = int(input("Enter task number to remove: "))
                if 1 <= index <= len(tasks):
                    removed = tasks.pop(index - 1)
                    save_tasks(tasks)
                    print(f"Task '{removed}' removed.")
                else:
                    print("Invalid number.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "4":
            print("Exiting To-Do List. Goodbye!")
            break

        else:
            print("Invalid choice. Please choose 1-4.")

if __name__ == "__main__":
    main()
