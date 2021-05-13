# -*- coding: utf-8 -*-
"""
Created on Tue May 11 10:53:08 2021

@author: Jackymakupala88
"""

import tkinter as tk
import tkinter.messagebox as tkBox
from tkinter import Tk, Frame, Entry, Button, Toplevel, Label
from trasactions import 

def Sign_up():

    def Submit():

        Entered_newPassword1 = (eNewPassword1.get())
        Entered_newPassword2 = (eNewPassword2.get())
        Entered_newUsername = (eNewUsername.get())

        if Entered_newUsername in Usernames:
            tkBox.showinfo('Error', 'Username Exists')

        elif Entered_newPassword1 == Entered_newPassword2:
            Usernames.append(Entered_newUsername)
            Passwords.append(Entered_newPassword1)
            print(Usernames, Passwords)
            window.destroy()

        else:
            tkBox.showinfo('Error', 'Password does not match')

    window = Toplevel()
    width = 300
    height = 250
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2,
                                (screenheight - height) / 2)
    window.geometry(alignstr)
    window.resizable(width=False, height=False)
    window.title("Sign Up")

    lnewUsername = Label(window, text="Enter Username")
    lPassword = Label(window, text="Enter Password")
    lPassword2 = Label(window, text="Re-Enter Password")

    eNewUsername = Entry(window, width=20)
    eNewUsername.insert(0, "")

    eNewPassword1 = Entry(window, width=15, show="*")
    eNewPassword1.insert(0, '')

    eNewPassword2 = Entry(window, width=15, show="*")
    eNewPassword2.insert(0, '')

    Button_Submit = Button(window, width=10, text="Submit", command=Submit)

    Button_Cancel = Button(window, width=10, text="Cancel",
                           command=window.destroy, bg="red")

    lnewUsername.pack(padx=5, pady=5)
    eNewUsername.pack(padx=5, pady=5)
    lPassword.pack(padx=5, pady=5)
    eNewPassword1.pack(padx=5, pady=5)
    lPassword2.pack(padx=5, pady=5)
    eNewPassword2.pack(padx=5, pady=5)
    Button_Cancel.pack(padx=18, pady=5, side="right")
    Button_Submit.pack(padx=0, pady=5, side="right")


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
            tkBox.showinfo('Welcome', "Welcome!")
            root.destroy()
        else:
            tkBox.showinfo('Access denied',
                           'Incorrect password or username')
    else:
        tkBox.showinfo('Access denied',
                       'Incorrect password or username')


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

lUsername = tk.Label(frame, text="Username")
lUsername.pack(padx=2, pady=0)

Username = Entry(frame, width=20)
Username.insert(0, "")
Username.pack(padx=5, pady=5)

lPassword = tk.Label(frame, text="Password")
lPassword.pack(padx=2, pady=0)

Password = Entry(frame, width=15, show="*")
Password.insert(0, '')
Password.pack(padx=5, pady=5)

Button_LogIn = Button(frame, text="Log in", command=Log_in, justify="left")
Button_LogIn.pack(padx=5, pady=5, side="left")

Button_SignUp = Button(frame, text="Sign Up", command=Sign_up, justify="right")
Button_SignUp.pack(padx=5, pady=5, side="right")

Usernames = ["Jack", "Benjamin", "123"]
Passwords = ["Enter", "Qwerty", "123"]
Weathers = ["Valkeakoski", "Tampere"]

root.mainloop()