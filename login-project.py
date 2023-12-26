from tkinter import *
from tkinter import messagebox
import mysql.connector
import os
import time

# Connecting to the database
db = mysql.connector.connect(host="localhost", user="root", passwd="grisha", database="my_projects")
mycur = db.cursor()

def error_destroy():
    err.destroy()

def succ_destroy():
    succ.destroy()
    root1.destroy()

def error():
    global err
    err = Toplevel(root1)
    err.title("Error")
    err.geometry("200x100")
    err.config(bg="#FFD700")  # Light goldenrod yellow
    Label(err, text="All fields are required..", fg="red", font=("Arial", 12, "bold"), bg="#FFD700").pack()
    Label(err, text="").pack()
    Button(err, text="Ok", bg="#4CAF50", fg="white", width=8, height=1, command=error_destroy).pack()

def success():
    global succ
    succ = Toplevel(root1)
    succ.title("Success")
    succ.geometry("200x100")
    succ.config(bg="#FFD700")  # Light goldenrod yellow
    Label(succ, text="Registration successful...", fg="green", font=("Arial", 12, "bold"), bg="#FFD700").pack()
    Label(succ, text="").pack()
    Button(succ, text="Ok", bg="#4CAF50", fg="white", width=8, height=1, command=succ_destroy).pack()

def register_user():
    username_info = username.get()
    password_info = password.get()
    if not username_info or not password_info:
        error()
    else:
        sql = "insert into login values(%s, %s)"
        t = (username_info, password_info)
        mycur.execute(sql, t)
        db.commit()
        Label(root1, text="").pack()
        time.sleep(0.50)
        success()

def registration():
    global root1
    root1 = Toplevel(root)
    root1.title("Registration Portal")
    root1.geometry("300x250")
    root1.config(bg="#FFD700")  # Light goldenrod yellow
    global username
    global password
    Label(root1, text="Register your account", bg="#4CAF50", fg="white", font=("Arial", 14, "bold"), width=300).pack()
    username = StringVar()
    password = StringVar()
    Label(root1, text="").pack()
    Label(root1, text="Username :", font=("Arial", 12, "bold"), bg="#FFD700").pack()
    Entry(root1, textvariable=username).pack()
    Label(root1, text="").pack()
    Label(root1, text="Password :", font=("Arial", 12, "bold"), bg="#FFD700").pack()
    Entry(root1, textvariable=password, show="*").pack()
    Label(root1, text="").pack()
    Button(root1, text="Register", bg="#4CAF50", fg="white", command=register_user).pack()

def login():
    global root2
    root2 = Toplevel(root)
    root2.title("Log-In Portal")
    root2.geometry("300x300")
    root2.config(bg="#FFD700")  # Light goldenrod yellow
    global username_varify
    global password_varify
    Label(root2, text="Log-In Portal", bg="#4CAF50", fg="white", font=("Arial", 14, "bold"), width=300).pack()
    username_varify = StringVar()
    password_varify = StringVar()
    Label(root2, text="").pack()
    Label(root2, text="Username :", font=("Arial", 12, "bold"), bg="#FFD700").pack()
    Entry(root2, textvariable=username_varify).pack()
    Label(root2, text="").pack()
    Label(root2, text="Password :", font=("Arial", 12, "bold"), bg="#FFD700").pack()
    Entry(root2, textvariable=password_varify, show="*").pack()
    Label(root2, text="").pack()
    Button(root2, text="Log-In", bg="#4CAF50", fg="white", command=login_varify).pack()

def logg_destroy():
    logg.destroy()
    root2.destroy()

def fail_destroy():
    fail.destroy()

def logged():
    global logg
    logg = Toplevel(root2)
    logg.title("Welcome")
    logg.geometry("200x100")
    logg.config(bg="#FFD700")  # Light goldenrod yellow
    Label(logg, text="Welcome {} ".format(username_varify.get()), fg="green", font=("Arial", 12, "bold"), bg="#FFD700").pack()
    Label(logg, text="").pack()
    Button(logg, text="Log-Out", bg="#4CAF50", fg="white", width=8, height=1, command=logg_destroy).pack()

def failed():
    global fail
    fail = Toplevel(root2)
    fail.title("Invalid")
    fail.geometry("200x100")
    fail.config(bg="#FFD700")  # Light goldenrod yellow
    Label(fail, text="Invalid credentials...", fg="red", font=("Arial", 12, "bold"), bg="#FFD700").pack()
    Label(fail, text="").pack()
    Button(fail, text="Ok", bg="#4CAF50", fg="white", width=8, height=1, command=fail_destroy).pack()

def login_varify():
    user_varify = username_varify.get()
    pas_varify = password_varify.get()
    sql = "select * from login where user = %s and password = %s"
    mycur.execute(sql, [(user_varify), (pas_varify)])
    results = mycur.fetchall()
    if results:
        for i in results:
            logged()
            break
    else:
        failed()

def main_screen():
    global root
    root = Tk()
    root.title("Log-IN Portal")
    root.geometry("300x300")
    root.config(bg="#FFD700")  # Light goldenrod yellow
    Label(root, text="Welcome to Log-In Portal", font=("Arial", 14, "bold"), bg="#4CAF50", fg="white", width=300).pack()
    Label(root, text="").pack()
    frame = Frame(root, bg="#FFD700")  # Light goldenrod yellow
    frame.pack()
    Button(frame, text="Log-IN", width="8", height="1", bg="#4CAF50", font=("Arial", 12, "bold"), fg="white", command=login).pack(side=TOP, pady=10)
    Button(frame, text="Registration", height="1", width="15", bg="#4CAF50", font=("Arial", 12, "bold"), fg="white", command=registration).pack(side=TOP, pady=10)

    Label(root, text="LOGIN SYSTEM", font=("Arial", 14, "bold"), bg="#FFD700").pack()

main_screen()
root.mainloop()

