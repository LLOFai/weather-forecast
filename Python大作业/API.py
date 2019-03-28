# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 23:01:06 2019

@author: LLOql
"""

import requests
import json
import urllib.parse

def diaoyong(CityName):
    
    data=urllib.parse.quote(CityName) #转换成utf8
    api='http://apis.juhe.cn/simpleWeather/query?city='+data+'&key=c53b2cd749def12a11cceda58280f56c' #调用API
   
    r = requests.get(api)
    
    forecast = json.loads(r.text)

    return forecast   #以dict形式return
    
