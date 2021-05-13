"""
Created on Tue May 11 10:00:50 2021

@author: Beni Fucking Demoa
"""

from tkinter import Tk, Frame, Entry, Button, Toplevel, Label, ttk
from tkcalendar import DateEntry
import pandas as pd


# %% Expense button command
def Expense():  # Input expense and submit it to the csv file
    # %% Submit command
    def Submit_Expense():  # Fuction that saves the inputed data in csv file

        # Get imput data from user
        EnteredDate = (Ecal.get())
        EnteredExpense = float((ExpenseEntry.get()))
        EnteredCategory = CategorySelection.get()

        #  import CSV file to dataframe
        Tdf = pd.read_csv('Transactions.csv')
        #Tdf = Tdf.fillna(0)
        DateTdf = Tdf[Tdf['Date'] == EnteredDate]
        DateTdf = DateTdf[EnteredCategory]
        print(Tdf)
        #  Make transaction if all fields is filled correctly
        if isinstance(EnteredExpense, (int, float)):
            if EnteredExpense >= 0:
                DateTdf = DateTdf + (EnteredExpense * -1)
                Tdf.update(DateTdf)
                print(Tdf)
                Tdf.to_csv('Transactions.csv', index=False)
                Expensewindow.destroy()
        else:
            print("no")
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
                     date_pattern='d.m.yyyy', justify="center")
    Ecal.pack(padx=5, pady=5)

# %% Button for submiting value
    ESubmitButton = Button(Expensewindow, width=20, text="Submit",
                           command=Submit_Expense)
    ESubmitButton.pack(padx=5, pady=15)


# %% income command
def Income():  # Function for Income button command

    def Submit_Income():  # Fuction that saves the inputed data in csv file

        # Get imput data from user
        EnteredDate = (Ical.get())
        EnteredIncome = float((IncomeEntry.get()))
        EnteredCategory = CategorySelection.get()

        #  import CSV file to dataframe
        Tdf = pd.read_csv('Transactions.csv')
        Tdf = Tdf.fillna(0)
        print(Tdf)
        IncomeTdf = Tdf[Tdf['Date'] == EnteredDate]
        IncomeTdf = IncomeTdf[EnteredCategory]

        #  Make transaction if all fields is filled correctly
        if isinstance(EnteredIncome, (int, float)):
            if EnteredIncome >= 0:
                IncomeTdf = IncomeTdf + EnteredIncome
                Tdf.update(IncomeTdf)
                print(Tdf)
                Tdf.to_csv('Transactions.csv', index=False)
                Incomewindow.destroy()

        else:
            print("no")
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

    IncomeTypes = ['Rent',  'Salery', 'Sponsor', 'Other bussiness']

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
                     date_pattern='d.m.yyyy', justify="center")
    Ical.pack(padx=5, pady=5)

# %% Button for submiting value
    ISubmitButton = Button(Incomewindow, width=20, text="Submit",
                           command=Submit_Income)
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
