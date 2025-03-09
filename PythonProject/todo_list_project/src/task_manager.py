import os
import sys

def get_app_folder():
    """
    Returns the folder where the .exe or script is running.
    This handles both normal Python execution and PyInstaller 'frozen' mode.
    """
    if getattr(sys, 'frozen', False):
        # If we're in a PyInstaller bundle, sys.executable is the .exe
        return os.path.dirname(sys.executable)
    else:
        # If running normally (not bundled), use this file's directory
        return os.path.dirname(os.path.abspath(__file__))

# Define our data folder and file path .
APP_FOLDER = get_app_folder()
DATA_FOLDER = os.path.join(APP_FOLDER, "data")
TASK_FILE = os.path.join(DATA_FOLDER, "tasks.txt")

# Ensure the data folder exists
os.makedirs(DATA_FOLDER, exist_ok=True)

def add_task(task):
    """
    Adds a new task to the tasks.txt file (UTF-8).
    """
    with open(TASK_FILE, "a", encoding="utf-8") as file:
        file.write(task + "\n")
    print(f'Task added: "{task}"')

def view_tasks():
    """
    Displays all tasks, reading from tasks.txt (UTF-8).
    """
    if not os.path.exists(TASK_FILE):
        print("No tasks found.")
        return

    with open(TASK_FILE, "r", encoding="utf-8") as file:
        tasks = [line.strip() for line in file if line.strip()]

    if not tasks:
        print("No tasks found.")
        return

    print("\nYour Tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def mark_task_done(task_number):
    """
    Marks a task as done by prepending [✓] to it, then rewriting tasks.txt.
    """
    if not os.path.exists(TASK_FILE):
        print("No tasks found.")
        return

    with open(TASK_FILE, "r", encoding="utf-8") as file:
        tasks = [line.strip() for line in file if line.strip()]

    if not tasks:
        print("No tasks found.")
        return

    if not (1 <= task_number <= len(tasks)):
        print("Invalid task number.")
        return

    # Check if already marked
    if tasks[task_number - 1].startswith("[✓]"):
        print("Task is already marked as done!")
        return

    # Mark it
    tasks[task_number - 1] = "[✓] " + tasks[task_number - 1]

    with open(TASK_FILE, "w", encoding="utf-8") as file:
        for t in tasks:
            file.write(t + "\n")

    print(f"Task {task_number} marked as done!")

def remove_task(task_number):
    """
    Removes the specified task from tasks.txt.
    """
    if not os.path.exists(TASK_FILE):
        print("No tasks found.")
        return

    with open(TASK_FILE, "r", encoding="utf-8") as file:
        tasks = [line.strip() for line in file if line.strip()]

    if not tasks:
        print("No tasks found.")
        return

    if not (1 <= task_number <= len(tasks)):
        print("Invalid task number.")
        return

    removed_task = tasks.pop(task_number - 1)

    with open(TASK_FILE, "w", encoding="utf-8") as file:
        for t in tasks:
            file.write(t + "\n")

    print(f'Task removed: "{removed_task}"')

def clear_tasks():
    """
    Clears all tasks by truncating tasks.txt.
    """
    with open(TASK_FILE, "w", encoding="utf-8"):
        pass  # Just create/overwrite an empty file
    print("All tasks cleared!")
