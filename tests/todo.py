# # Initial to-do list
# todo_task = ["clean", "cook", "bath", "make a meal", "study"]

# while True:
#     print("\nYour To-Do List:")
#     for i, task in enumerate(todo_task, start=1):
#         print(f"{i}. {task}")
    
#     # Ask user what they want to do
#     action = input("\nDo you want to remove a task or add a new task? (remove/add/exit): ").lower()
    
#     if action == "remove":
#         remove_input = input("Enter task numbers to remove (comma separated, e.g., 1,3): ")
#         numbers = remove_input.split(",")
#         numbers = [int(num.strip()) for num in numbers]  # Convert input to integers
#         # Remove tasks starting from the highest index to avoid shifting problems
#         for num in sorted(numbers, reverse=True):
#             if 1 <= num <= len(todo_task):
#                 removed_task = todo_task.pop(num - 1)
#                 print(f"Removed: {removed_task}")
#             else:
#                 print(f"Task number {num} is invalid.")
    
#     elif action == "add":
#         new_task = input("Enter the new task: ")
#         todo_task.append(new_task)
#         print(f"Added: {new_task}")
    
#     elif action == "exit":
#         print("Exiting the to-do list. Goodbye!")
#         break
    
#     else:
#         print("Invalid action. Please type 'remove', 'add', or 'exit'.")
import tkinter as tk
from tkinter import simpledialog, messagebox

# Create main window
root = tk.Tk()
root.title("To-Do List")

# Initial tasks
todo_task = ["clean", "cook", "bath", "make a meal", "study"]

# Function to update the listbox
def update_listbox():
    listbox.delete(0, tk.END)
    for task in todo_task:
        listbox.insert(tk.END, task)

# Function to remove selected tasks
def remove_task():
    selected = listbox.curselection()  # Get selected indexes
    if not selected:
        messagebox.showinfo("Info", "Please select a task to remove")
        return
    for i in reversed(selected):  # Remove from last to first
        todo_task.pop(i)
    update_listbox()

# Function to add a new task
def add_task():
    new_task = simpledialog.askstring("Add Task", "Enter the new task:")
    if new_task:
        todo_task.append(new_task)
        update_listbox()

# Create listbox to show tasks
listbox = tk.Listbox(root, selectmode=tk.MULTIPLE, width=50)
listbox.pack(pady=10)

# Create buttons
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

remove_button = tk.Button(root, text="Remove Selected Task(s)", command=remove_task)
remove_button.pack(pady=5)

# Initialize listbox
update_listbox()

# Run the GUI
root.mainloop()
