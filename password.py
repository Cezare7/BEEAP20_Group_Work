# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 12:24:50 2021

@author: Beni Fucking Demoa
"""
import tkinter as tk
import tkinter.messagebox as tkBox
import numpy as np
from tkinter import Tk, Frame, Entry, Button


def Log_in():

    Entered_Username = (Username.get())
    Entered_Password = (Password.get())
    if Entered_Username in Usernames:
        Username_Index = (Usernames.index(Username.get()))
        print(Username_Index)
        print(Entered_Username)
        print(Entered_Password)
        print(Passwords[Username_Index])
        if Entered_Password == (Passwords[Username_Index]):
            root.destroy()
        else:
            tkBox.showinfo('Acces denied',
                           'Wrong password or username')
    else:
        tkBox.showinfo('Acces denied',
                       'Wrong password or username')


root = Tk()
root.geometry("200x150")
root.title('Log in')
width = 300
height = 150
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2,
                            (screenheight - height) / 2)
root.geometry(alignstr)
root.resizable(width=False, height=False)
frame = Frame(root)
frame.pack()

fUsername = tk.Label(frame, text="Username")
fUsername.pack(padx=2, pady=0)

Username = Entry(frame, width=20)
Username.insert(0, "")
Username.pack(padx=5, pady=5)

fPassword = tk.Label(frame, text="Password")
fPassword.pack(padx=2, pady=0)

Password = Entry(frame, width=15, show="*")
Password.insert(0, '')
Password.pack(padx=5, pady=5)

Button = Button(frame, text="Log in", command=Log_in)
Button.pack(padx=5, pady=5)

Usernames = ["Jack", "Benjamin"]
Passwords = np.array(["Enter", "Qwerty"])


root.mainloop()
