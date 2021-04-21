import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
import tkinter.messagebox as tkBox
import tkinter.font as tkFont
import time


# %% Class application
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
# %% Lable date
        t = time.localtime()
        current_date = time.strftime("%A %d %B %Y", t)
        current_time = time.strftime("%H:%M", t)
        self.__TimeandWeather = tk.Label(root)
        ft = tkFont.Font(family='Times', size=11)
        self.__TimeandWeather["font"] = ft
        self.__TimeandWeather["fg"] = "#333333"
        self.__TimeandWeather["justify"] = "right"
        self.__TimeandWeather["text"] = current_date
        self.__TimeandWeather.place(x=350, y=50, width=170, height=25)
# %% lable time
        self.__TimeandWeather = tk.Label(root)
        ft = tkFont.Font(family='Times', size=11)
        self.__TimeandWeather["font"] = ft
        self.__TimeandWeather["fg"] = "#333333"
        self.__TimeandWeather["justify"] = "right"
        self.__TimeandWeather["text"] = current_time
        self.__TimeandWeather.place(x=290, y=70, width=170, height=25)


# %% call
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
