#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 20:47:30 2017

@author: raimundoabrillopez
"""

import os
import datetime

PATH = '/Volumes/Macintosh HD/_Drive/_data'
os.chdir(PATH)
name = 'gasolineras_'+datetime.datetime.now().date().__str__()+'_'+datetime.datetime.now().hour.__str__().zfill(2)+'-'+datetime.datetime.now().minute.__str__().zfill(2)+'.json'
url = 'https://sedeaplicaciones.minetur.gob.es/ServiciosRESTCarburantes/PreciosCarburantes/EstacionesTerrestres/'

import requests
import json

r = requests.get(url)
json_data = r.json()

json_string = json.dumps(json_data['ListaEESSPrecio'], ensure_ascii=False)

with open(name, 'w', encoding='utf-8') as outfile:
#    json.dump(json_data,outfile,ensure_ascii=False)
    outfile.write(json_string)
    
outfile.close()