import unittest
import os
import json
from todo import load_tasks, save_tasks, add_task, delete_task

class TestTodoApp(unittest.TestCase):
    TEST_FILE = "ToDo_Py/test_todos.json"

    def setUp(self):
        # Clean up before each test
        if os.path.exists(self.TEST_FILE):
            os.remove(self.TEST_FILE)

    def tearDown(self):
        # Clean up after each test
        if os.path.exists(self.TEST_FILE):
            os.remove(self.TEST_FILE)

    def test_add_task(self):
        tasks = []
        add_task(tasks, "Test Task", self.TEST_FILE)
        
        # Check if task was added to the list
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0], "Test Task")
        
        # Check if task was saved to the file
        loaded_tasks = load_tasks(self.TEST_FILE)
        self.assertEqual(len(loaded_tasks), 1)
        self.assertEqual(loaded_tasks[0], "Test Task")

    def test_load_empty_file(self):
        tasks = load_tasks("non_existent_file.json")
        self.assertEqual(tasks, [])

    def test_save_and_load(self):
        tasks = ["Task 1", "Task 2"]
        save_tasks(tasks, self.TEST_FILE)
        loaded_tasks = load_tasks(self.TEST_FILE)
        self.assertEqual(tasks, loaded_tasks)

    def test_delete_task(self):
        tasks = load_tasks(self.TEST_FILE)
        
        # Logic as requested:
        # If there is no task item in list, create a dummy task first.
        if not tasks:
            add_task(tasks, "dummy task", self.TEST_FILE)
            tasks = load_tasks(self.TEST_FILE)
        
        # Check that we have at least one task now
        self.assertGreaterEqual(len(tasks), 1)
        initial_count = len(tasks)
        
        # Delete the first TODO item
        success, removed = delete_task(tasks, 1, self.TEST_FILE)
        
        # Verify success
        self.assertTrue(success)
        self.assertEqual(len(tasks), initial_count - 1)
        
        # Verify the file is also updated
        loaded_tasks = load_tasks(self.TEST_FILE)
        self.assertEqual(len(loaded_tasks), initial_count - 1)

if __name__ == "__main__":
    unittest.main()
