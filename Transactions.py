"""
Created on Tue May 11 10:00:50 2021

@author: Beni Fucking Demoa
"""

from tkinter import Tk, Frame, Entry, Button, Toplevel, Label, ttk
from tkcalendar import DateEntry


# %% Expense button command
def Expense():  # Input expense and submit it to the csv file
    # %% Submit command
    def Submit():  # Fuction that saves the inputed data in csv file

        EnteredExpense = float((ExpenseEntry.get()))
        EnteredDate = (Ecal.get())
        if isinstance(EnteredExpense, (int, float)):
            if EnteredExpense >= 0:
                print("yes", EnteredDate)
        else:
            print(EnteredExpense, "no")
# %% Expense window properties
    Expensewindow = Toplevel()  # Window properties
    width = 300
    height = 180
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2,
                                (screenheight - height) / 2)
    Expensewindow.geometry(alignstr)
    Expensewindow.resizable(width=False, height=False)
    Expensewindow.title("Add Expense")

    TransactionTypes = ['Rent',  'Travel', 'Groceries', 'Subscriptions',
                        'Guilty Pleasure']

# %% Combo box for selecting transission type
    CategorySelection = ttk.Combobox(Expensewindow, values=TransactionTypes,
                                     justify="center")
    CategorySelection.set('Pick a Category')
    CategorySelection.pack(padx=5, pady=5)

# %% Entry for Value of Expense
    ExpenseEntry = Entry(Expensewindow, width=23, justify="center")
    ExpenseEntry.insert(0, "Amount")
    ExpenseEntry.pack(padx=5, pady=15)

# %% Date Selection Tool
    Ecal = DateEntry(Expensewindow, width=20, background='darkblue',
                     foreground='white', borderwidth=2,
                     date_pattern='dd-mm-yyyy', justify="center")
    Ecal.pack(padx=5, pady=5)

# %% Button for submiting value
    ESubmitButton = Button(Expensewindow, width=20, text="Submit",
                           command=Submit)
    ESubmitButton.pack(padx=5, pady=15)


# %% income command
def Income():  # Function for Income button command

    # %% Income window properties
    Incomewindow = Toplevel()
    width = 300
    height = 180
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2,
                                (screenheight - height) / 2)
    Incomewindow.geometry(alignstr)
    Incomewindow.resizable(width=False, height=False)
    Incomewindow.title("Add Income")

    IncomeTypes = ['Rent',  'Salery', 'Sponsors', 'Other bussiness']

# %% Combo box for selecting transission type
    CategorySelection = ttk.Combobox(Incomewindow, values=IncomeTypes,
                                     justify="center")
    CategorySelection.set('Pick a Category')
    CategorySelection.pack(padx=5, pady=5)

# %% Entry for Value of Income
    IncomeEntry = Entry(Incomewindow, width=23, justify="center")
    IncomeEntry.insert(0, "Amount")
    IncomeEntry.pack(padx=5, pady=15)

# %% Date Selection Tool
    Ical = DateEntry(Incomewindow, width=20, background='darkblue',
                     foreground='white', borderwidth=2,
                     date_pattern='dd-mm-yyyy', justify="center")
    Ical.pack(padx=5, pady=5)

# %% Button for submiting value
    ISubmitButton = Button(Incomewindow, width=20, text="Submit",
                           command=Incomewindow.destroy)
    ISubmitButton.pack(padx=5, pady=5)


# %% Root Window
root = Tk()
root.title('Transaction')
width = 500
height = 300
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2,
                            (screenheight - height) / 2)
root.geometry(alignstr)
root.resizable(width=False, height=False)
frame = Frame(root)
frame.pack()

# %% Expense button
Button_Expense = Button(frame, text="Add Expense", command=Expense)
Button_Expense.pack(padx=5, pady=5, side="left")

# %% Income Button
Button_Income = Button(frame, text="Add Income", command=Income)
Button_Income.pack(padx=5, pady=5, side="left")

# %% Main loop
root.mainloop()
