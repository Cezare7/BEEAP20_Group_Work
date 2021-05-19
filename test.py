
# -*- coding: utf-8 -*-
"""
Created on Mon May 17 13:03:40 2021

@author: Beni Fucking Demoa
"""
from tkinter import Tk, Frame, Entry, Button, Toplevel, Label, ttk
from tkcalendar import DateEntry
import pandas as pd
from GetBalance import BalanceSum
from WTH import *
import time
import datetime as dt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

def StartWindow():

    def Expense():  # Input expense and submit it to the csv file
        # %% Submit command
        def Submit_Expense():  # Saves the inputed data in csv file

            # Get imput data from user
            EnteredDate = (Ecal.get())
            EnteredExpense = float((ExpenseEntry.get()))
            EnteredCategory = CategorySelection.get()

    #  import CSV file to dataframe
            Tdf = pd.read_csv('Transactions.csv')
            #  Tdf = Tdf.fillna(0)
            DateTdf = Tdf[Tdf['Date'] == EnteredDate]
            DateTdf = DateTdf[EnteredCategory]

    #  Make transaction if all fields is filled correctly
            if isinstance(EnteredExpense, (int, float)):
                if EnteredExpense >= 0:
                    DateTdf = DateTdf + (EnteredExpense * -1)
                    Tdf.update(DateTdf)
                    Tdf.to_csv('Transactions.csv', index=False)
                    root.destroy()
                    BalanceSum()
                    StartWindow()
                    Expensewindow.destroy()
            else:
                print("no")
    # %% Expense window properties
        Expensewindow = Toplevel()  # Window properties
        width = 300
        height = 180
        screenwidth = Expensewindow.winfo_screenwidth()
        screenheight = Expensewindow.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2,
                                    (screenheight - height) / 2)
        Expensewindow.geometry(alignstr)
        Expensewindow.resizable(width=False, height=False)
        Expensewindow.title("Add Expense")

        TransactionTypes = ['Rent',  'Travel', 'Groceries', 'Subscriptions',
                            'Guilty Pleasures']

    # %% Combo box for selecting transission type
        CategorySelection = ttk.Combobox(Expensewindow,
                                         values=TransactionTypes,
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

    def Income():  # Function for Income button command

        def Submit_Income():  # Fuction that saves the inputed data in csv file

            #  Get imput data from user
            EnteredDate = (Ical.get())
            EnteredIncome = float((IncomeEntry.get()))
            EnteredCategory = CategorySelection.get()

    #  import CSV file to dataframe
            Tdf = pd.read_csv('Transactions.csv')
            #  Tdf = Tdf.fillna(0)
            # print(Tdf)
            IncomeTdf = Tdf[Tdf['Date'] == EnteredDate]
            IncomeTdf = IncomeTdf[EnteredCategory]

            #  Make transaction if all fields is filled correctly
            if isinstance(EnteredIncome, (int, float)):
                if EnteredIncome >= 0:
                    IncomeTdf = IncomeTdf + EnteredIncome
                    Tdf.update(IncomeTdf)
    #  save to the csv file
                    Tdf.to_csv('Transactions.csv', index=False)
                    root.destroy()
                    BalanceSum()
                    StartWindow()
                    Incomewindow.destroy()

            else:
                print("no")
    # %% Income window properties
        Incomewindow = Toplevel()
        width = 300
        height = 180
        screenwidth = Incomewindow.winfo_screenwidth()
        screenheight = Incomewindow.winfo_screenheight()
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

    # %% Time and date
    def update_clock():
        hours = time.strftime('%H')
        minutes = time.strftime('%M')
        #  am_or_pm = time.strftime('%p')
        time_text = hours + ':' + minutes
        digital_clock_lbl.config(text=time_text)
        digital_clock_lbl.after(1000, update_clock)

    root = Tk()
    root.title('Transaction')
    width = 650
    height = 400
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2,
                                (screenheight - height) / 2)
    root.geometry(alignstr)
    root.resizable(width=False, height=False)
    frame = Frame(root)
    frame.pack()

    # %% Expense button
    Button_Expense = Button(root, text="Add Expense", command=Expense)
    Button_Expense.place(x=550, y=15)

    # %% Income Button
    Button_Income = Button(root,
                           text="Add Income ",
                           command=Income)
    Button_Income.place(x=550, y=45)
    # %% Balance Lable

    Tdf = pd.read_csv('Transactions.csv')
    Balance = round(Tdf['Balance'].sum(), 2)
    Lable_Balance = Label(root, text=Balance, font='Helvetica 30 bold')
    Lable_Balance.place(x=320, y=30)
    Lable_Balancet = Label(root, text="Balance ")
    Lable_Balancet.place(x=350, y=13)
    Mx = 0
    My = -25
    Lable_Temperature = Label(root, text=Temperature)
    Lable_Temperature.place(x=25+Mx, y=300+My)
    Lable_Wind = Label(root, text=WindSpeed)
    Lable_Wind.place(x=25+Mx, y=320+My)
    Lable_Discription = Label(root, text=Discription)
    Lable_Discription.place(x=25+Mx, y=340+My)
    Lable_Weather = Label(root, text=Weather)
    Lable_Weather.place(x=25+Mx, y=360+My)

    # %% Time And Date Label
    digital_clock_lbl = Label(root, text='00:00',
                              font='Helvetica 30 bold')
    digital_clock_lbl.place(x=25, y=35)

    update_clock()
    ts = dt.datetime.now()
    Date = ts.strftime('%A'' ' '%d''/''%m''/''%Y')

    Lable_Date = Label(root, text=Date)
    Lable_Date.place(x=25, y=15)

    # %% Date Entery for Graph
    Startcal = DateEntry(root, width=20,
                         background='darkblue',
                         foreground='white',
                         borderwidth=2,
                         date_pattern='d.m.yyyy',
                         justify="center",
                         year=2021, month=5, day=2)
    Startcal.place(x=25, y=100)

    Endcal = DateEntry(root, width=20,
                       background='darkblue',
                       foreground='white',
                       borderwidth=2,
                       date_pattern='d.m.yyyy',
                       justify="center")
    Endcal.place(x=25, y=125)

    # %% Graph
    def Graph():
        Tdf["Date"] = pd.to_datetime(Tdf['Date'], infer_datetime_format=True)
        StartDate = Tdf[Tdf['Date'] == Startcal.get()].index.values
        EndDate = Tdf[Tdf['Date'] == Endcal.get()].index.values
        TdfDate = (Tdf.iloc[int(StartDate[0]):int(EndDate[-1])+1, ])
        GraphBalance = TdfDate["Balance"]
        figure1 = plt.figure(dpi=50)
        ax1 = figure1.add_subplot(111)
        bar1 = FigureCanvasTkAgg(figure1, root)
        bar1.get_tk_widget().place(x=300, y=130, width=330, height=255)
        GraphBalance.plot.bar(ax=ax1)
        ax1.set_title("Balance")
        plt.ylabel('Euro')
        ax1.set(xticklabels=[])

    Button_Expense = Button(root, text="Set Dates", command=Graph)
    Button_Expense.place(x=25, y=150, width=143)
    Graph()
    # %% Main loop
    root.mainloop()


StartWindow()
