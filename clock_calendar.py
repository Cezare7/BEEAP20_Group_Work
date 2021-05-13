# -*- coding: utf-8 -*-
"""
Created on Tue May 11 08:23:25 2021

@author: Jackymakupala88
"""
import tkinter as tk
import tkinter.messagebox as tkBox
import numpy as np 
import tkcalendar as tkcal
import calendar as calendar
import time            


window = tk.Tk()
window.geometry("300x350")
window.title("calendar") 
def update_clock():
    hours = time.strftime('%H')
    minutes = time.strftime('%M')
    time_text = hours + ':' + minutes 
    digital_clock_lbl.config(text=time_text)
    digital_clock_lbl.after(1000, update_clock)
digital_clock_lbl = tk.Label(window, text='00:00',
                             font='Helvetica 30 bold')
digital_clock_lbl.pack()


update_clock()

mycal = tkcal.Calendar(window, setmode='day', date_pattern='d/m/yy')
mycal.pack(padx=10, pady=1)

 
window.mainloop()
