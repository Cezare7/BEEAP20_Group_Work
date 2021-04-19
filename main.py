import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
import tkinter.messagebox as tkBox
import tkinter.font as tkFont
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#%% Class application
class App:

    def __init__(self, root):

        root.title("Montly Economy Calculator")
        width = 600
        height = 500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2,
                                    (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
# %% Lable        
        self.__Lable_01 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=11)
        self.__Lable_01["font"] = ft
        self.__Lable_01["fg"] = "#333333"
        self.__Lable_01["justify"] = "right"
        self.__Lable_01["text"] = "present time and weather"
        self.__Lable_01.place(x=350, y=50, width=170, height=25)
        
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()