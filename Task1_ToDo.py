import pickle
import os

# File to store tasks and introduction flag
DATA_FILE = 'todo_list.pkl'

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'rb') as f:
            return pickle.load(f)
    else:
        return {'tasks': [], 'intro_shown': False}

def save_data(data):
    with open(DATA_FILE, 'wb') as f:
        pickle.dump(data, f)

def show_introduction():
    print("Welcome to the To Do List Program!")
    print("This program allows you to add, view, and manage your tasks.")
    print("You will only see this introduction once.\n")

def add_task(tasks):
    task = input("Enter the task you want to add: ")
    tasks.append(task)
    print(f"Task '{task}' added.\n")

def view_tasks(tasks):
    if not tasks:
        print("Your to-do list is empty.\n")
    else:
        print("Your to-do list:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")
        print()

def main():
    data = load_data()

    # Show introduction if not shown before
    if not data['intro_shown']:
        show_introduction()
        data['intro_shown'] = True
        save_data(data)

    while True:
        print("To Do List Menu:")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_task(data['tasks'])
            save_data(data)
        elif choice == '2':
            view_tasks(data['tasks'])
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
