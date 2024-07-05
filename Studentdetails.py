import tkinter as tk
from tkinter import messagebox

class StudentMarksApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Marks Management")

        # Create and pack widgets
        self.label_name = tk.Label(root, text="Student Name:")
        self.entry_name = tk.Entry(root)

        self.label_units = tk.Label(root, text="Enter Marks for Each Unit:")
        self.entry_units = tk.Entry(root)

        self.btn_add = tk.Button(root, text="Add Marks", command=self.add_marks)
        self.btn_display = tk.Button(root, text="Display Marks", command=self.display_marks)

        self.label_name.pack(pady=10)
        self.entry_name.pack(pady=10)
        self.label_units.pack(pady=10)
        self.entry_units.pack(pady=10)
        self.btn_add.pack(pady=10)
        self.btn_display.pack(pady=10)

        # Student marks dictionary
        self.student_marks = {}

    def add_marks(self):
        name = self.entry_name.get()
        units_input = self.entry_units.get()

        try:
            # Parse unit marks as a comma-separated string and convert to a list of integers
            unit_marks = [int(mark.strip()) for mark in units_input.split(",")]

            if name and unit_marks:
                self.student_marks[name] = unit_marks
                messagebox.showinfo("Success", "Marks added successfully!")
                self.clear_entries()
            else:
                messagebox.showwarning("Error", "Please enter both name and unit marks.")
        except ValueError:
            messagebox.showwarning("Error", "Invalid input for unit marks. Use comma-separated integers.")

    def display_marks(self):
        if not self.student_marks:
            messagebox.showinfo("Info", "No student marks to display.")
        else:
            display_text = "Student Marks:\n"
            for name, marks in self.student_marks.items():
                display_text += f"{name}: {', '.join(map(str, marks))}\n"

            messagebox.showinfo("Student Marks", display_text)

    def clear_entries(self):
        self.entry_name.delete(0, tk.END)
        self.entry_units.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentMarksApp(root)
    root.mainloop()