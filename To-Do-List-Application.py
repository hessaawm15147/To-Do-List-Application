import tkinter as tk
from tkinter import messagebox
import json

# Step 1: Initialize the Tkinter application
root = tk.Tk()
root.title("To-Do List")

# Load existing tasks
try:
    with open('tasks.json', 'r') as file:
        tasks = json.load(file)
except FileNotFoundError:
    tasks = []

# Step 2: Define functions
def add_task():
    task = task_entry.get()  # Task entry field (will be created in Step 3)
    if task:
        tasks.append(task)
        save_tasks()
        update_task_list()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task")

def save_tasks():
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file, indent=4)

def update_task_list():
    task_list.delete(0, tk.END)  # Task list (will be created in Step 3)
    for task in tasks:
        task_list.insert(tk.END, task)

