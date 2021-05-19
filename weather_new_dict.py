# -*- coding: utf-8 -*-
"""
Created on Tue May 11 08:23:25 2021

@author: Jackymakupala88
"""
import requests
from tkinter import *
import requests
import json
import datetime
from PIL import ImageTk, Image
import tkinter as tk




def weather_data1(query):
    res = requests.get('http://api.openweathermap.'
                       'org/data/2.5/weather?'
                       + query +
                       '&appid=a1c86d677225cae3648789045729a448&units='
                       'metric')
    return res.json()


def print_weather1(result, city):
    Temperature = ("{}'s temperature: {}°C ".
                   format(city, result['main']['temp']))
    WindSpeed = ("Wind speed: {} m/s".
                 format(result['wind']['speed']))
    Discription = ("Description: {}".
                   format(result['weather'][0]['description']))
    Weather = ("Weather: {}".format(result['weather'][0]['main']))
    print(Temperature)
    print(WindSpeed)
    print(Discription)
    print(Weather)
    return Temperature


def main1():
    city = 'Tampere'
    print()
    try:
        query = 'q='+city
        w_data = weather_data1(query)
        print_weather1(w_data, city)
        print()
    except:
        print('City name not found...')
        
        
        
        
        
def weather_data2(query):
    res = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Valkeakoski,Finland'
                       + query +
                       '&appid=d06c490037444511f4b9f40c91b918df&units='
                       'metric')
    return res.json()


def print_weather2(result, city):
    Temperature = ("{}'s temperature: {}°C ".
                   format(city, result['main']['temp']))
    WindSpeed = ("Wind speed: {} m/s".
                 format(result['wind']['speed']))
    Discription = ("Description: {}".
                   format(result['weather'][0]['description']))
    Weather = ("Weather: {}".format(result['weather'][0]['main']))
    print(Temperature)
    print(WindSpeed)
    print(Discription)
    print(Weather)
    return Temperature


def main2():
    city = 'Valkeakoski'
    print()
    try:
        query = 'q='+city
        w_data = weather_data2(query)
        print_weather2(w_data, city)
        print()
    except:
        print('City name not found...')


if __name__ == '__main__':
    main1()
    main2()
