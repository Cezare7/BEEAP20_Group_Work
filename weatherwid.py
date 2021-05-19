# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 11:39:01 2021

@author: Jackymakupala88
"""

import xml.etree.ElementTree as ET

def main():
    tree = ET.parse('valkeakoski.xml')
    root = tree.getroot()
    
    for elem in root:
        print(elem.tag, elem.attrib)
        print("\n\n")
        
        for elem in root:
            if elem.tag == "forecast":
                print(elem.tag, elem.attrib)
                for subelem in elem:
                    print(subelem.tag, ":", subelem.attrib)
                    for sub2elem in subelem:
                        if sub2elem.tag == "temperature":
                            print("\tMax Temp", sub2elem.tag, ":", sub2elem.attrib['max'])
                        if sub2elem.tag == "humidity":
                            print("\tHumid:", sub2elem.attrib['value'], sub2elem.attrib['unit'])

#%%
import tkinter as tk
import requests
hi = 500
wi=600
root = tk.Tk()

#def test_fun(entry):
    #print(entry)

def fr(weather):
    try:
        name = weather['name']
        des = weather['weather'][0]['description']
        temp = weather['main']['temp']

        fs='City: %s \nConditions: %s \nTemp (C*): %s' % (name, des, temp)
    except Exception:
        fs="That's error 404. Type correctly "

    return fs

def weather1(city):
    key='aba06543f5f70442cc5b3efe6674d2b4'
    url='https://api.openweathermap.org/data/2.5/weather?q=Valkeakoski&units=metric&appid=d06c490037444511f4b9f40c91b918df&mode=json'
    p={'APPID': key, 'q': city, 'units': 'metric'}
    r= requests.get(url, params=p)
    w=r.json()
    label['text'] = fr(w)
    print(w['name'])
    print(w['weather'][0]['description'])
    print(w['main']['temp'])



canvas = tk.Canvas (root, height=hi, width= wi)
canvas.pack()  

frame = tk.Frame(root, bg='#000080', bd=2,)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n') 

button = tk.Button(frame, text=" weather", font=36, command=lambda: weather1(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)                                        

entry=tk.Entry(frame, font=30)
#entry.place(relwidth=0.69, relheight=1)

frame2 = tk.Frame(root, bg='#000080', bd=2)
frame2.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label=tk.Label(frame2, bg='#00CED1')
label.place(relwidth=1, relheight=1)

root.mainloop()