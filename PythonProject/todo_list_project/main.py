import os
import sys

# Import functions from task_manager .
from src.task_manager import add_task, view_tasks, mark_task_done, remove_task, clear_tasks

def main():
    while True:
        print("\n===== To-Do List =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Remove Task")
        print("5. Clear All Tasks")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            # Add Task
            task = input("Enter the task: ").strip()
            if task:
                add_task(task)
                print("Task added successfully!")
            else:
                print("Task cannot be empty!")

        elif choice == "2":
            # View Tasks
            view_tasks()

        elif choice == "3":
            # Mark Task as Done
            view_tasks()
            user_input = input("Enter task number to mark as done: ").strip()
            try:
                task_number = int(user_input)
                mark_task_done(task_number)
            except ValueError:
                print("Invalid input! Please enter a valid number.")

        elif choice == "4":
            # Remove a Task
            view_tasks()
            user_input = input("Enter task number to remove: ").strip()
            try:
                task_number = int(user_input)
                remove_task(task_number)
            except ValueError:
                print("Invalid input! Please enter a valid number.")

        elif choice == "5":
            # Clear All Tasks
            confirm = input("Are you sure you want to clear all tasks? (yes/no): ").strip().lower()
            if confirm == "yes":
                clear_tasks()

        elif choice == "6":
            print("Exiting... Have a great day!")
            break

        else:
            print("Invalid choice! Please enter a number from 1 to 6.")

if __name__ == "__main__":
    # Wrapping main() call in try/except ensures any unhandled error is shown,
    # and the console doesn't immediately close afterward.
    try:
        main()
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
    input("\nPress Enter to exit...")
