# ToDo_Py

A simple, persistent CLI-based TODO application built with Python. This project was developed as a practice application to learn software engineering standards, unit testing, and version control.

## 🚀 Features
- **Add Tasks**: Add new items to your TODO list via the command line.
- **List Tasks**: View all your current tasks with their associated numbers.
- **Delete Tasks**: Remove tasks by their index number.
- **Persistence**: Tasks are saved to a `todos.json` file, so they remain even after the program is closed.
- **Automated Testing**: Includes a comprehensive test suite using Python's `unittest` framework.

## 🛠️ Installation
1. Ensure you have **Python 3.x** installed on your system.
2. Clone this repository:
   ```bash
   git clone https://github.com/iRoy7/ToDo_Py.git
   cd ToDo_Py
   ```

## 📖 Usage
Run the application using the following commands:

- **Add a task**:
  ```bash
  python todo.py add "Your task description"
  ```
- **List all tasks**:
  ```bash
  python todo.py list
  ```
- **Delete a task**:
  ```bash
  python todo.py delete 1
  ```

## 🧪 Testing
Following our engineering mandates, this project includes unit tests for all core functionality.

To run the tests and see a detailed report:
```bash
python test_todo.py -v
```

## 📜 Architecture
Significant architectural decisions are documented in the `ADR.md` file (where applicable), following the project's global engineering standards.
