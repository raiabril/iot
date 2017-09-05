#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 01:33:59 2017

@author: raimundoabrillopez
"""

import os
import datetime
import pandas as pd

PATH = '/home/pi/logs/gasolineras'
os.chdir(PATH)

files = os.listdir()
files.sort()
dataList = []

for file in files:
    data = pd.read_json(file)
    data['DATE'] = datetime.datetime.strptime(file.split('.')[0].split('_')[1]+' '+file.split('.')[0].split('_')[2].replace('-',':'), '%Y-%m-%d %H:%M')
    
data = pd.concat(dataList)
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

PATH = '/home/pi/logs'
os.chdir(PATH)
data.to_csv(datetime.datetime.now().date().__str__()+'.csv', encoding='utf-8')