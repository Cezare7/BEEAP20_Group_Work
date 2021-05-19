# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 10:04:16 2021

@author: Jackymakupala88
"""
import tkinter as tk
import requests, base64

class OpenWeatherMap:
    APPID = 'd06c490037444511f4b9f40c91b918df'

    def __init__(self):
        self.url = "http://api.openweathermap.org/data/2.5/weather?appid={appid}&q=Tampere&units=metric"
        self.json = {}

    def get_city(self, city):
        url = self.url.format(appid=OpenWeatherMap.APPID, city=city)
        self.json = requests.get(url).json()
        return self.json

    def get(self, key):
        return self.json['main'][key]

    def get_icon_data(self):
        icon_id = self.json['weather'][0]['icon']
        url = 'http://openweathermap.org/img/wn/{icon}.png'.format(icon=icon_id)
        response = requests.get(url, stream=True)
        return base64.encodebytes(response.raw.read())


class OpenWeatherMap:
    APPID = 'd06c490037444511f4b9f40c91b918df'

    def __init__(self):
        self.url = "http://api.openweathermap.org/data/2.5/weather?appid={appid}&q=valkeakoski&units=metric"
        self.json = {}

    def get_city(self, city):
        url = self.url.format(appid=OpenWeatherMap.APPID, city=city)
        self.json = requests.get(url).json()
        return self.json

    def get(self, key):
        return self.json['main'][key]

    def get_icon_data(self):
        icon_id = self.json['weather'][0]['icon']
        url = 'http://openweathermap.org/img/wn/{icon}.png'.format(icon=icon_id)
        response = requests.get(url, stream=True)
        return base64.encodebytes(response.raw.read())


class OWIconLabel(tk.Label):
    def __init__(self, parent, **kwargs):
        weather_icon = kwargs.pop('weather_icon', None)
        if weather_icon is not None:
            self.photo = tk.PhotoImage(data=weather_icon)
            kwargs['image'] = self.photo

        super().__init__(parent, **kwargs)
        
        
