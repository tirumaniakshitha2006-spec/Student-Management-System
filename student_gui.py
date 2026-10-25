import tkinter as tk
from tkinter import messagebox
import sqlite3

conn=sqlite3.connect("students.db")
cursor=conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
roll_no INTEGER PRIMARY KEY,
name TEXT NOT NULL
)

""")
conn.commit()
conn.close()

def add_student():
    roll_no=roll_var.get()
    name=name_var.get()

    if roll_no=="" or name=="":
        messagebox.showinfo(
            "Warning",
            "Please fill all fields"
        )
        return

    conn=sqlite3.connect("students.db")
    cursor=conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO students VALUES (?,?)",(roll_no,name)
        )
        conn.commit()
    
        messagebox.showinfo(
        "Success",
        "Student Added Successfully"
        )

        roll_var.set("")
        name_var.set("")

    except sqlite3.IntegrityError:
        messagebox.showerror(
            "Error",
            "Roll No Already Exists"
        )


conn.close()


def view_students():
    conn=sqlite3.connect("students.db")
    cursor=conn.cursor()

    cursor.execute(
        "SELECT* FROM students"
    )
    students=cursor.fetchall()
    conn.close()

    view_window=tk.Toplevel(window)
    view_window.title("All Students")
    view_window.geometry("300x300")

    if len(students)==0:
        tk.Label(
            view_window,
            text="no Students found"
        ).pack()

    else:
        for student in students:
            text=(
                f"Roll No:{student[0]}\n"
                f"Name:{student[1]}\n"
            )
            tk.Label(
                view_window,
                text=text
            ).pack()

def search_student():

    roll_no=roll_var.get()

    if roll_no=="":
        messagebox.showwarning(
            "Warning",
            "Enter roll number"
        )
        return

    conn=sqlite3.connect("students.db")
    cursor=conn.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE roll_no=?",(roll_no,)
    )

    student=cursor.fetchone()

    conn.close()

    if student:
        messagebox.showinfo(
            "Student Found",
            f"Roll No :{student[0]}\nName:{student[1]}"
        )
    else:
        messagebox.showerror(
            "Error",
            "Student not found"
        )

def update_student():

    roll_no=roll_var.get()
    name=name_var.get()

    if roll_no=="" or name=="":
        messagebox.showwarning(
            "Warning",
            "Please enter all fields"
        )
        return

    conn=sqlite3.connect("students.db")
    cursor=conn.cursor()

    cursor.execute(
        "UPDATE students SET name=? WHERE roll_no=?",(name,roll_no)
    )
    conn.commit()

    if cursor.rowcount==0:
        messagebox.showerror(
            "Error",
            "Student not found"
        )
    else:
        messagebox.showinfo(
            "Student Found",
            "Student updated successfully"
        )

    conn.close()


def delete_student():
    roll_no=roll_var.get()

    if roll_no=="":
        messagebox.showwarning(
            "Warning",
            "Enter  roll number"
        )
        return

    conn=sqlite3.connect("students.db")
    cursor=conn.cursor()

    cursor.execute(
        "DELETE FROM students WHERE roll_no=?",(roll_no,)
    )
    conn.commit()

    if cursor.rowcount==0:
        messagebox.showerror(
            "Error",
            "Student not found"
        )
    else:
        messagebox.showinfo(
            "Success",
            "Student deleted successfully"
        )

        roll_var.set("")
        name_var.set("")

    conn.close()

def exit_window():
    messagebox.showinfo(
        "Greet",
        "Thank You"
    )
    exit(0)


window=tk.Tk()

window.title("Student management system")
window.geometry("500x500")

roll_var=tk.StringVar()
name_var=tk.StringVar()

tk.Label(window,text="Roll No ").grid(row=0,column=0,padx=10,pady=10)
tk.Label(window,text="Name ").grid(row=1,column=0,padx=10,pady=10)



roll_entry=tk.Entry(window,textvariable=roll_var)
roll_entry.grid(row=0,column=1)

name_var=tk.Entry(window,textvariable=name_var)
name_var.grid(row=1,column=1)


add_button=tk.Button(
    window,
    text="Add Student",
    command=add_student)
add_button.grid(row=2,column=1,pady=20)

view_button=tk.Button(
    window,
    text="View students",
    command=view_students
)
view_button.grid(
    row=2,
    column=0,
    padx=20
)

search_button=tk.Button(
    window,
    text="Search student",
    command=search_student
)
search_button.grid(
    row=3,
    column=0,
    padx=20
)

update_button=tk.Button(
    window,
    text="Update Student",
    command=update_student
)
update_button.grid(
    row=3,
    column=1,
    padx=20
)

delete_button=tk.Button(
    window,
    text="Delete Student",
    command=delete_student
)
delete_button.grid(
    row=4,
    column=0,
    padx=20,
    pady=20
)

exit_button=tk.Button(
    window,
    text="Exit",
    command=exit_window
)
exit_button.grid(
    row=4,
    column=1,
    pady=20
)
window.mainloop()

