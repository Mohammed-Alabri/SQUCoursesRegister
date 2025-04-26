import os
import sys
from threading import Thread
import tkinter as tk
from tkinter import messagebox, ttk
from functions import login, add_course, status
import requests as rq
import sv_ttk
from ctypes import windll

windll.shcore.SetProcessDpiAwareness(1)


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(
        os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


root = tk.Tk()
root.title("SQU Auto Courses Adder")
ss = ttk.Style()

lbl_username = ttk.Label(text="Username:", font=('Arial', 12))
lbl_username.grid(padx=(30, 0), column=0)

ent_username = ttk.Entry(width=20, font=('Arial', 16))
ent_username.grid(padx=(0, 30), pady=10, row=0, column=1)

lbl_password = ttk.Label(text="Password:", font=('Arial', 12))
lbl_password.grid(padx=(30, 0), pady=10, row=1, column=0)

ent_password = ttk.Entry(width=20, font=('Arial', 16))
ent_password.grid(padx=(0, 30), pady=10, row=1, column=1)

lbl_courses = ttk.Label(text="courses:", font=('Arial', 12))
lbl_courses.grid(padx=(30, 0), pady=10, row=2, column=0)

card = ttk.Frame(root, style='Card.TFrame', padding=(5, 6, 7, 8))
txt_courses = tk.Text(card, width=28, height=7,
                      font=('Arial', 12), borderwidth=0)
txt_courses.pack()
card.grid(padx=(0, 30), pady=10, row=2, column=1)


def clicked():
    btn_register.state(["disabled"])
    username = ent_username.get()
    password = ent_password.get()
    box = txt_courses.get("1.0", tk.END)
    if username == "" or password == "" or box == "\n":
        messagebox.showerror("ERROR", "Please fill all entries.")
        btn_register.state(["!disabled"])
        return
    s = rq.Session()
    ids = rq.get(
        "https://raw.githubusercontent.com/Mohammed-Alabri/python-projects/main/abcbufc.txt")
    if username.lower() not in ids.text.split():
        messagebox.showerror("ERROR", "Please contact with developer.")
        btn_register.state(["!disabled"])
        return
    values = {
        "username": username,
        "password": password
    }
    if not login(values, s):
        messagebox.showerror("ERROR", "Username or password is incorrect.")
        btn_register.state(["!disabled"])
        return
    box = box.split("\n")
    message = "Registration status: " + \
        ("open" if status(s) else "closed") + '\n'
    for course in box:
        course = course.split()
        if 2 <= len(course) <= 3:
            course[0] = course[0].upper()
            r = add_course(course, s)
            if r == True:
                message += f"{course[0]} ✔️\n"
            else:
                message += f"{course[0]} ❌\n"
    messagebox.showinfo("Result", message)
    btn_register.state(["!disabled"])


def start_clicked():
    t = Thread(target=clicked, daemon=True)
    t.start()


ss.configure('TButton', font=('Arial', 12))
btn_register = ttk.Button(root, text='Register',
                          width=40, command=start_clicked, style='TButton')
btn_register.grid(pady=5, row=3, column=0, columnspan=2)
ss.configure('my.TButton', font=('Arial', 12))
lbl_maker = ttk.Label(text="Made by: Mohammed Al-Abri.", font=('Arial', 12))
lbl_maker.grid(padx=(30, 0), column=0, pady=(0, 10), columnspan=2)

root.resizable(height=False, width=False)
sv_ttk.set_theme("dark")

root.mainloop()
