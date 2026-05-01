import json
import os
import sys

TODO_FILE = "ToDo_Py/todos.json"

def load_tasks(filename=TODO_FILE):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks, filename=TODO_FILE):
    # Ensure the directory exists
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task(tasks, task_text, filename=TODO_FILE):
    tasks.append(task_text)
    save_tasks(tasks, filename)
    print(f"Added task: {task_text}")

def delete_task(tasks, task_num, filename=TODO_FILE):
    if 1 <= task_num <= len(tasks):
        removed = tasks.pop(task_num - 1)
        save_tasks(tasks, filename)
        print(f"Deleted task: {removed}")
        return True, removed
    else:
        print(f"Error: Invalid task number {task_num}.")
        return False, None

def main():
    tasks = load_tasks()
    
    if len(sys.argv) < 2:
        print("Welcome to your TODO App!")
        print(f"You have {len(tasks)} tasks.")
        print("Usage: python todo.py add \"task name\"")
        return

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 3:
            print("Error: Please provide a task description.")
        else:
            task_text = sys.argv[2]
            add_task(tasks, task_text)
    elif command == "list":
        if not tasks:
            print("Your TODO list is empty.")
        else:
            print("Your TODO List:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
    elif command == "delete":
        if len(sys.argv) < 3:
            print("Error: Please provide the task number to delete.")
        else:
            try:
                task_num = int(sys.argv[2])
                delete_task(tasks, task_num)
            except ValueError:
                print("Error: Task number must be an integer.")
    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()
