import tkinter as tk
from tkinter import messagebox

students = []

def add_student():
    name = name_entry.get()
    grade = grade_entry.get()

    if name == "" or grade == "":
        messagebox.showwarning("Input Error", "Please enter name and grade")
        return

    if len(students) >= 10:
        messagebox.showwarning("Limit Reached", "Only 10 students allowed")
        return

    try:
        grade = float(grade)
    except:
        messagebox.showwarning("Input Error", "Grade must be a number")
        return

    students.append((name, grade))
    update_listbox()

    name_entry.delete(0, tk.END)
    grade_entry.delete(0, tk.END)

def update_listbox():
    listbox.delete(0, tk.END)
    for s in students:
        listbox.insert(tk.END, f"{s[0]} - {s[1]}")

def compute_average():
    if not students:
        messagebox.showinfo("Average", "No students yet")
        return

    avg = sum(g for _, g in students) / len(students)
    messagebox.showinfo("Average Grade", f"Average: {avg:.2f}")

def sort_grades():
    global students
    students = sorted(students, key=lambda x: x[1])
    update_listbox()

def search_student():
    name = search_entry.get()

    for s in students:
        if s[0].lower() == name.lower():
            messagebox.showinfo("Student Found", f"{s[0]} - Grade: {s[1]}")
            return

    messagebox.showinfo("Search", "Student not found")

root = tk.Tk()
root.title("Student Grade Manager")
root.geometry("400x400")

# Name input
tk.Label(root, text="Student Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

# Grade input
tk.Label(root, text="Grade").pack()
grade_entry = tk.Entry(root)
grade_entry.pack()

# Add button
tk.Button(root, text="Add Student", command=add_student).pack(pady=5)

# List display
listbox = tk.Listbox(root, width=40)
listbox.pack(pady=10)

# Buttons
tk.Button(root, text="Compute Average", command=compute_average).pack(pady=3)
tk.Button(root, text="Sort Grades (Ascending)", command=sort_grades).pack(pady=3)

# Search
tk.Label(root, text="Search Student").pack()
search_entry = tk.Entry(root)
search_entry.pack()

tk.Button(root, text="Search", command=search_student).pack(pady=5)

root.mainloop()