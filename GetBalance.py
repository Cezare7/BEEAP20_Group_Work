# -*- coding: utf-8 -*-
"""
Created on Mon May 17 10:20:31 2021

@author: Beni Fucking Demoa
"""

import pandas as pd


def BalanceSum():
    Tdf = pd.read_csv('Transactions.csv')
    Tdf = Tdf.assign(Balance=lambda col: (col['Rent']
                                          + col['Travel']
                                          + col['Groceries']
                                          + col['Subscriptions']
                                          + col['Guilty Pleasures']
                                          + col['Salery']
                                          + col['Sponsor']
                                          + col['Other bussiness']))
    Tdf.to_csv('Transactions.csv', index=False)
    return Tdf['Balance'].sum()
<<<<<<< HEAD
=======

>>>>>>> f3ab0c348cefee3f2fc970a5eec2b291abaffc25


BalanceSum()
