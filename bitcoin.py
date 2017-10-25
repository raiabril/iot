#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 20:47:30 2017

@author: raimundoabrillopez
"""

import os
import datetime

PATH = '/media/pi/RAI/logs/bitcoin'
os.chdir(PATH)

name = 'coindesk_'+datetime.datetime.now().date().__str__()+'_'+datetime.datetime.now().hour.__str__().zfill(2)+'-'+datetime.datetime.now().minute.__str__().zfill(2)
url = 'https://api.coindesk.com/v1/bpi/currentprice/EUR.json'

import requests
import json

sample = True

while sample:
    r = requests.get(url)
    if len(r.text) > 100:
        sample = False
r.close()

json_data = r.json()
json_string = json.dumps(json_data, ensure_ascii=False)

with open(name+'.json', 'w', encoding='utf-8') as outfile:
#    json.dump(json_data,outfile,ensure_ascii=False)
    outfile.write(json_string)

outfile.close()
