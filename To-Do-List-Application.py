import tkinter as tk
from tkinter import messagebox
import json

# Step 1: Initialize the Tkinter application
root = tk.Tk()  # Create the main application window
root.title("To-Do List")  # Set the title of the window

# Load existing tasks from a JSON file
try:
    with open('tasks.json', 'r') as file:  # Attempt to open the tasks file
        tasks = json.load(file)  # Load tasks from the file if it exists
except FileNotFoundError:
    tasks = []  # If the file doesn't exist, start with an empty task list

# Step 2: Define functions

# Function to add a new task
def add_task():
    task = task_entry.get()  # Get the task from the entry field
    if task:  # If the entry field is not empty
        tasks.append(task)  # Add the task to the list
        save_tasks()  # Save the updated list to the file
        update_task_list()  # Refresh the displayed task list
        task_entry.delete(0, tk.END)  # Clear the entry field
    else:
        messagebox.showwarning("Warning", "Please enter a task")  # Show a warning if no task was entered

# Function to save the task list to a JSON file
def save_tasks():
    with open('tasks.json', 'w') as file:  # Open the file in write mode
        json.dump(tasks, file, indent=4)  # Write the task list to the file with indentation for readability

# Function to update the displayed task list
def update_task_list():
    task_list.delete(0, tk.END)  # Clear the current task list display
    for task in tasks:  # Loop through the list of tasks
        task_list.insert(tk.END, task)  # Insert each task into the displayed list

# Step 3: Create GUI elements

# Entry widget for typing new tasks
task_entry = tk.Entry(root, width=50)
task_entry.pack(pady=10)  # Add padding around the entry widget

# Button to add the typed task to the list
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)  # Add padding around the button

# Listbox widget to display the list of tasks
task_list = tk.Listbox(root, width=50, height=10)
task_list.pack(pady=10)  # Add padding around the listbox

# Populate the listbox with existing tasks
update_task_list()

# Step 4: Run the application
root.mainloop()  # Start the Tkinter event loop to run the application
