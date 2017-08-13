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
name = 'gasolineras_'+datetime.datetime.now().date().__str__()+'.json'
url = 'https://sedeaplicaciones.minetur.gob.es/ServiciosRESTCarburantes/PreciosCarburantes/EstacionesTerrestres/'

import requests
import json

#r = requests.get(url)

with open(name, 'w') as outfile:
    json.dump(r.json(), outfile)
    
outfile.close()
