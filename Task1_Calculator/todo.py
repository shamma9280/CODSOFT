import tkinter as tk
from tkinter import messagebox

tasks = []

def add_task():
    task = task_entry.get()
    if task:
        tasks.append(task)
        update_listbox()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        del tasks[selected_task_index]
        update_listbox()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete!")

def update_listbox():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_listbox.insert(tk.END, task)

# GUI Window
root = tk.Tk()
root.title("To-Do List")
root.geometry("300x400")

# Input field
task_entry = tk.Entry(root, font=("Arial", 14))
task_entry.pack(pady=10)

# Add Button
add_button = tk.Button(root, text="Add Task", width=15, command=add_task)
add_button.pack(pady=5)

# Delete Button
delete_button = tk.Button(root, text="Delete Task", width=15, command=delete_task)
delete_button.pack(pady=5)

# Task List
task_listbox = tk.Listbox(root, font=("Arial", 14), width=25, height=10)
task_listbox.pack(pady=10)

root.mainloop()
