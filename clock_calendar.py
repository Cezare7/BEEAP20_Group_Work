# -*- coding: utf-8 -*-
"""
Created on Tue May 11 08:23:25 2021

@author: Jackymakupala88
"""
import tkinter as tk
<<<<<<< HEAD


import tkcalendar as tkcal

import time


#  create a tk window to show the date and time
window = tk.Tk()
window.geometry("350x400")
window.title("calendar")

=======
import tkinter.messagebox as tkBox
import numpy as np 
import tkcalendar as tkcal
import calendar as calendar
import time            
import requests, base64


#create a tk window to show the date and time 
window = tk.Tk()
window.geometry("350x400")
window.title("calendar") 
>>>>>>> 83b8bae85bc2cbaa01e29b124a6771a9a734453c

# create a 24hr digital clock face
def update_clock():
    hours = time.strftime('%H')
    minutes = time.strftime('%M')
<<<<<<< HEAD
    #  am_or_pm = time.strftime('%p')
    time_text = hours + ':' + minutes
    digital_clock_lbl.config(text=time_text)
    digital_clock_lbl.after(1000, update_clock)  # update the time every second


=======
    am_or_pm = time.strftime('%p') 
    time_text = hours + ':' + minutes 
    digital_clock_lbl.config(text=time_text)
    digital_clock_lbl.after(1000, update_clock)# update the time every second
>>>>>>> 83b8bae85bc2cbaa01e29b124a6771a9a734453c
digital_clock_lbl = tk.Label(window, text='00:00',
                             font='Helvetica 30 bold')
digital_clock_lbl.pack()

<<<<<<< HEAD
=======

>>>>>>> 83b8bae85bc2cbaa01e29b124a6771a9a734453c
update_clock()

# create a calendar and place in window
mycal = tkcal.Calendar(window, setmode='day', date_pattern='d/m/yy')
mycal.pack(padx=10, pady=1)


<<<<<<< HEAD
window.mainloop()
=======
window.mainloop()
>>>>>>> 83b8bae85bc2cbaa01e29b124a6771a9a734453c
