import tkinter as tk
from tkinter import *
from tkinter import ttk, Menu
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

# %% Drop down mainmenu

        self.mainmenu = Menu(root)

        self.filemenu = Menu(self.mainmenu, tearoff=0)
        self.filemenu.add_command(label="Open")  # not yet coded
        self.filemenu.add_command(label="Save")  # not yet coded
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=root.destroy)
        self.mainmenu.add_cascade(label="File", menu=self.filemenu)

        root.config(menu=self.mainmenu)

# %% Lable date

        t = time.localtime()
        current_date = time.strftime("%A %d %B %Y", t)
        current_time = time.strftime("%H:%M", t)
        self.__Time = tk.Label(root)
        ft = tkFont.Font(family='Times', size=11)
        self.__Time["font"] = ft
        self.__Time["fg"] = "#333333"
        self.__Time["justify"] = "left"
        self.__Time["text"] = current_date
        self.__Time.place(x=350, y=50, width=170, height=25)

# %% lable time

        self.__Time = tk.Label(root)
        ft = tkFont.Font(family='Times', size=11)
        self.__Time["font"] = ft
        self.__Time["fg"] = "#333333"
        self.__Time["justify"] = "right"
        self.__Time["text"] = current_time
        self.__Time.place(x=350, y=70, width=170, height=25)


# %% call
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
