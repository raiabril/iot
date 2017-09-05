#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 20:47:30 2017

@author: raimundoabrillopez
"""

import os
import datetime
import pandas as pd

PATH = '/home/pi/logs/gasolineras'
os.chdir(PATH)
    
name = 'gasolineras_'+datetime.datetime.now().date().__str__()+'_'+datetime.datetime.now().hour.__str__().zfill(2)+'-'+datetime.datetime.now().minute.__str__().zfill(2)
url = 'https://sedeaplicaciones.minetur.gob.es/ServiciosRESTCarburantes/PreciosCarburantes/EstacionesTerrestres/'

import requests
import json

sample = True

while sample:
    r = requests.get(url)
    if len(r.text) > 100:
        sample = False
r.close()
    
json_data = r.json()
json_string = json.dumps(json_data['ListaEESSPrecio'], ensure_ascii=False)
with open(name+'.json', 'w', encoding='utf-8') as outfile:
#    json.dump(json_data,outfile,ensure_ascii=False)
    outfile.write(json_string)
    
outfile.close()

PATH = '/home/pi/logs/gasolineras'
os.chdir(PATH)

files = os.listdir()
files.sort()
file = files[-1]

data = pd.read_json(file)
data['DATE'] = datetime.datetime.strptime(file.split('.')[0].split('_')[1]+' '+file.split('.')[0].split('_')[2].replace('-',':'), '%Y-%m-%d %H:%M')
data['% BioEtanol']=data['% BioEtanol'].str.replace(',','.').astype(float)
data['% Éster metílico']=data['% Éster metílico'].str.replace(',','.').astype(float)
data['Latitud']=data['Latitud'].str.replace(',','.').astype(float)
data['Longitud (WGS84)']=data['Longitud (WGS84)'].str.replace(',','.').astype(float)
data['Precio Biodiesel']=data['Precio Biodiesel'].str.replace(',','.').astype(float)
data['Precio Bioetanol']=data['Precio Bioetanol'].str.replace(',','.').astype(float)
data['Precio Gas Natural Comprimido']=data['Precio Gas Natural Comprimido'].str.replace(',','.').astype(float)
data['Precio Gas Natural Licuado']=data['Precio Gas Natural Licuado'].str.replace(',','.').astype(float)
data['Precio Gases licuados del petróleo']=data['Precio Gases licuados del petróleo'].str.replace(',','.').astype(float)
data['Precio Gasoleo A']=data['Precio Gasoleo A'].str.replace(',','.').astype(float)
data['Precio Gasoleo B']=data['Precio Gasoleo B'].str.replace(',','.').astype(float)
data['Precio Gasolina  98']=data['Precio Gasolina  98'].str.replace(',','.').astype(float)
data['Precio Gasolina 95 Protección']=data['Precio Gasolina 95 Protección'].str.replace(',','.').astype(float)
data['Precio Nuevo Gasoleo A']=data['Precio Nuevo Gasoleo A'].str.replace(',','.').astype(float)

PATH = '/home/pi/logs/gasolineras_csv'
os.chdir(PATH)
data.to_csv(file.replace('.json','.csv'), encoding='utf-8')







