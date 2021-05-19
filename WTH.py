# -*- coding: utf-8 -*-
"""
Created on Wed May 19 11:18:32 2021

@author: Beni Fucking Demoa
"""
import requests


res = requests.get('http://api.openweathermap.'
                   'org/data/2.5/weather?q=Tampere'
                   '&appid=a1c86d677225cae3648789045729a448&units='
                   'metric')
res = res.json()

city = 'Tampere'
Temperature = ("{}'s temperature:\t {}°C ".
               format(city, res['main']['temp']))
WindSpeed = ("Wind speed:\t\t {} m/s".
             format(res['wind']['speed']))
Discription = ("Description:\t\t {}".
               format(res['weather'][0]['description']))
Weather = ("Weather:\t\t\t {}". format(res['weather'][0]['main']))
