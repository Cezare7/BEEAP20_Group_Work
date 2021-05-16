# -*- coding: utf-8 -*-
"""
Created on Wed May 12 19:50:39 2021

@author: Jackymakupala88
"""
import tkinter as tk
import requests, base64
from My_weather_app import OpenWeatherMap, OWIconLabel

class App(tk.Tk):
  def __init__(self):
        super().__init__()
        self.geometry("300x200")
        self.configure(bg='white')

        owm = OpenWeatherMap()
        owm.get_city('Tampere')

        temperature = owm.get('temp')

        temp_icon = OWIconLabel(self, weather_icon=owm.get_icon_data())
        temp_icon.grid(row=0, column=0)
       
        self.temp = tk.Label(self,
                             text='{} deg celcius'.format(temperature),
                             font=("Helvetica", 15), bg='black', fg='white')
        self.temp.grid(row=1, column=3)


if __name__ == '__main__':
    App().mainloop()