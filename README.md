# To-Do List Application

This is a simple To-Do List application built using Python and Tkinter. The application allows users to add tasks, view them in a list, and save them to a file for future use. Tasks are stored in a JSON file and are reloaded each time the application is run.

## Features

- **Add Tasks:** Users can add new tasks to the list by typing in the input field and clicking the "Add Task" button.
- **View Tasks:** All tasks are displayed in a list within the application.
- **Save Tasks:** Tasks are automatically saved to a `tasks.json` file whenever a new task is added.
- **Persistent Storage:** The application loads the existing tasks from `tasks.json` when it starts, so tasks are preserved between sessions.

## Prerequisites

- Python 3.x
- Tkinter (usually included with Python)
  
## How to Run

How It Works
Starting the Application: When you run the application, it opens a window titled "To-Do List". If a tasks.json file exists, the tasks are loaded and displayed.

Adding a Task: Type your task into the input field at the top of the window and click "Add Task". The task will appear in the list below, and it will be saved to the tasks.json file.

Persistent Task Storage: Every time you add a task, the list is saved to tasks.json. This ensures that your tasks are available the next time you open the application.

File Structure
todo_list.py: The main Python script containing the application logic.
tasks.json: The JSON file where tasks are stored. This file is created automatically when you add your first task.
Example

Troubleshooting
tasks.json not found: If the application can't find tasks.json, it will create an empty task list. Ensure the application has write permissions in the directory where it's running.
No tasks appearing: Ensure you are running the application in the same directory where tasks.json is located, or check if the file has been corrupted.



