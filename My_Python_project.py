
from tkinter import *
from tkinter import messagebox
import os
root = Tk()
root.title("📝 To-Do List Application")
root.geometry("450x550")
root.resizable(False, False)
root.config(bg="#f0f0f0")
task_file = "tasks.txt"
def load_tasks():
    if os.path.exists(task_file):
        with open(task_file, "r") as f:
            for task in f:
                task = task.strip()
                if task:
                    task_listbox.insert(END, task)

def save_tasks():
    tasks = task_listbox.get(0, END)
    with open(task_file, "w") as f:
        for task in tasks:
            f.write(task + "\n")

def add_task():
    task = task_entry.get()
    if task.strip():
        task_listbox.insert(END, "🔹 " + task.strip())
        task_entry.delete(0, END)
        save_tasks()
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def delete_task():
    try:
        index = task_listbox.curselection()
        task_listbox.delete(index)
        save_tasks()
    except:
        messagebox.showwarning("Delete Error", "Please select a task to delete.")

def mark_done():
    try:
        index = task_listbox.curselection()
        task = task_listbox.get(index)
        if "✔" not in task:
            task_listbox.delete(index)
            task_listbox.insert(END, task + " ✔")
            save_tasks()
    except:
        messagebox.showwarning("Mark Done Error", "Please select a task to mark as done.")

#Title
title_label = Label(root, text="📌 TO-DO LIST", font=("Helvetica", 24, "bold"), bg="#f0f0f0", fg="#333")
title_label.pack(pady=20)

#Input Frame
input_frame = Frame(root, bg="#f0f0f0")
input_frame.pack(pady=10)

task_entry = Entry(input_frame, font=("Helvetica", 14), width=25, bd=2, relief=GROOVE)
task_entry.grid(row=0, column=0, padx=10)

add_btn = Button(input_frame, text="Add", width=10, bg="#4caf50", fg="white", font=("Arial", 11, "bold"), command=add_task)
add_btn.grid(row=0, column=1)

#Listbox
task_listbox = Listbox(root, font=("Helvetica", 13), width=38, height=13, bd=2, relief=RIDGE, selectbackground="#aee1f9", activestyle='none')
task_listbox.pack(pady=20)

#Buttons
btn_frame = Frame(root, bg="#f0f0f0")
btn_frame.pack(pady=5)

done_btn = Button(btn_frame, text="Mark Done", width=15, bg="#2196f3", fg="white", font=("Arial", 11, "bold"), command=mark_done)
done_btn.grid(row=0, column=0, padx=10)

delete_btn = Button(btn_frame, text="Delete Task", width=15, bg="#f44336", fg="white", font=("Arial", 11, "bold"), command=delete_task)
delete_btn.grid(row=0, column=1, padx=10)
load_tasks()
root.mainloop()
