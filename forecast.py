#!/usr/bin/python3
import os
import sys
import requests
import json
import traceback
#i2c connection to arduino
import smbus
import cgi
import time


apikey = "72821847a8eaa6dddb530e13886b905b"
latitude = 45.388
longitude = -75.699
language = 'en'
units = 'si'

weather_url = "https://api.darksky.net/forecast/%s/%s,%s?lang=%s&units=%s" % (apikey, latitude, longitude, language, units)
r = requests.get(weather_url)
weather_obj = json.loads(r.text)

temp = weather_obj['currently']['temperature']
windspeed = weather_obj['currently']['windSpeed']
uvIndex = weather_obj['currently']['uvIndex']
cloud = weather_obj['currently']['cloudCover']
print temp
print uvIndex
print cloud
print windspeed

#Doing test case to see how to optimize power efficiency of the project.
#This will measure the current measurements from Darksky Api
#With these numbers, if the UVIndex, WindSpeed and Cloud Cover is within a certain threshold

def testcase(temp, cloud, windspeed):
    if uvIndex >= 0.5 and windspeed >= 0.5 and cloud <= 0.05:
        return 1
    else:
        return 0

print testcase(temp,cloud,windspeed)


#establishing i2c connection

address = 0x04

def writeNumber(value):
    bus.write_byte(address,value)
    return testcase(temp,cloud,windspeed)

writeNumber(testcase(temp,cloud,windspeed))
