import tkinter as tk
from tkinter import messagebox


def submit_action():
    name = name_entry.get()
    roll_no = roll_no_entry.get()
    department = department_entry.get()

    if name and roll_no and department:
        messagebox.showinfo("Submission", f"Name: {name}\nRoll No: {roll_no}\nDepartment: {department}")
    else:
        messagebox.showwarning("Incomplete Information", "Please fill out all fields")


root = tk.Tk()
root.title("Login Page")

tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=10)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Roll No:").grid(row=1, column=0, padx=10, pady=10)
roll_no_entry = tk.Entry(root)
roll_no_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Department:").grid(row=2, column=0, padx=10, pady=10)
department_entry = tk.Entry(root)
department_entry.grid(row=2, column=1, padx=10, pady=10)

submit_button = tk.Button(root, text="Submit", command=submit_action)
submit_button.grid(row=3, columnspan=2, pady=10)

root.mainloop()
