"""
Created on Tue May 11 10:00:50 2021

@author: Beni Fucking Demoa
"""

from tkinter import Tk, Frame, Entry, Button, Toplevel, Label, ttk
from tkcalendar import DateEntry


def Expense():
    
    def Submit():
        
        EnteredExpense = float((ExpenseEntry.get()))

        if isinstance(EnteredExpense,(int, float)):
            if EnteredExpense >= 0:
                print("yes")
        else:
            print(EnteredExpense, "no")
        
     
        
    Expensewindow = Toplevel()
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
    CategorySelection = ttk.Combobox(Expensewindow, values=TransactionTypes,
                                     justify="center")
    CategorySelection.set('Pick a Category')
    CategorySelection.pack(padx=5, pady=5)

    ExpenseEntry = Entry(Expensewindow, width=23, justify="center")
    ExpenseEntry.insert(0, "Amount")
    ExpenseEntry.pack(padx=5, pady=15)

    Ecal = DateEntry(Expensewindow, width=20, background='darkblue',
                     foreground='white', borderwidth=2,
                     date_pattern='dd-mm-yyyy', justify="center")
    Ecal.pack(padx=5, pady=5)

    ESubmitButton = Button(Expensewindow, width=20, text="Submit",
                           command=Submit)
    ESubmitButton.pack(padx=5, pady=15)


def Income():

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
    CategorySelection = ttk.Combobox(Incomewindow, values=IncomeTypes,
                                     justify="center")
    CategorySelection.set('Pick a Category')
    CategorySelection.pack(padx=5, pady=5)

    IncomeEntry = Entry(Incomewindow, width=23, justify="center")
    IncomeEntry.insert(0, "Amount")
    IncomeEntry.pack(padx=5, pady=15)

    Ical = DateEntry(Incomewindow, width=20, background='darkblue',
                     foreground='white', borderwidth=2,
                     date_pattern='dd-mm-yyyy', justify="center")
    Ical.pack(padx=5, pady=5)

    ISubmitButton = Button(Incomewindow, width=20, text="Submit",
                           command=Incomewindow.destroy)
    ISubmitButton.pack(padx=5, pady=5)


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

Button_Expense = Button(frame, text="Add Expense", command=Expense)
Button_Expense.pack(padx=5, pady=5, side="left")

Button_Income = Button(frame, text="Add Income", command=Income)
Button_Income.pack(padx=5, pady=5, side="left")

root.mainloop()
