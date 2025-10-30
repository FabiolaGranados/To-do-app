
tasks = []  

# Show the main menu options
def show_menu():
    print("\n------ TO-DO LIST APP ------")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Delete a task")
    print("4. Quit")

# Add a new task to the list
def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"Added: {task}")

# Show all tasks in the list
def view_tasks():
    if len(tasks) == 0:
        print("There are no tasks to show.")
        return

    print("\nYour Tasks:")
    for i, task in enumerate(tasks):
        print(f"{i + 1}. {task}")

# Remove a task by its number
def delete_task():
    if len(tasks) == 0:
        print("No tasks to delete.")
        return

    try:
        view_tasks()
        num = int(input("Enter task number to delete: "))
        removed = tasks.pop(num - 1)
        print(f"Removed: {removed}")
    except ValueError:
        print("Invalid input. Please enter a number.")
    except IndexError:
        print("Task does not exist.")


def main():
    while True:
        show_menu()
        try:
            choice = int(input("Choose an option: "))
        except ValueError:
            print("Invalid choice. Enter a number.")
            continue

        if choice == 1:
            add_task()
        elif choice == 2:
            view_tasks()
        elif choice == 3:
            delete_task()
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("That option does not exist.")

    print("Thanks for using the app!")

# Main loop of the app
if __name__ == "__main__":
    main()
