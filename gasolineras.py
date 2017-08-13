#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 20:47:30 2017

@author: raimundoabrillopez
"""

import os
import datetime
import pandas as pd

PATH = '/Volumes/Macintosh HD/_Drive/_data'
os.chdir(PATH)
name = 'gasolineras_'+datetime.datetime.now().date().__str__()+'_'+datetime.datetime.now().hour.__str__().zfill(2)+'-'+datetime.datetime.now().minute.__str__().zfill(2)
url = 'https://sedeaplicaciones.minetur.gob.es/ServiciosRESTCarburantes/PreciosCarburantes/EstacionesTerrestres/'

import requests
import json

r = requests.get(url)
json_data = r.json()

json_string = json.dumps(json_data['ListaEESSPrecio'], ensure_ascii=False)

with open(name+'.json', 'w', encoding='utf-8') as outfile:
#    json.dump(json_data,outfile,ensure_ascii=False)
    outfile.write(json_string)
    
outfile.close()

# Conversion
data = pd.read_json(name+'.json',encoding='utf-8')
data['% BioEtanol']=pd.to_numeric(data['% BioEtanol'].str.replace(',','.'), errors='coerce')
data['% Éster metílico']=pd.to_numeric(data['% Éster metílico'].str.replace(',','.'), errors='coerce')
data['Latitud']=pd.to_numeric(data['Latitud'].str.replace(',','.'), errors='coerce')
data['Longitud (WGS84)']=pd.to_numeric(data['Longitud (WGS84)'].str.replace(',','.'), errors='coerce')
data['Precio Biodiesel']=pd.to_numeric(data['Precio Biodiesel'].str.replace(',','.'), errors='coerce')
data['Precio Bioetanol']=pd.to_numeric(data['Precio Bioetanol'].str.replace(',','.'), errors='coerce')
data['Precio Gas Natural Comprimido']=pd.to_numeric(data['Precio Gas Natural Comprimido'].str.replace(',','.'), errors='coerce')
data['Precio Gas Natural Licuado']=pd.to_numeric(data['Precio Gas Natural Licuado'].str.replace(',','.'), errors='coerce')
data['Precio Gases licuados del petróleo']=pd.to_numeric(data['Precio Gases licuados del petróleo'].str.replace(',','.'), errors='coerce')
data['Precio Gasoleo A']=pd.to_numeric(data['Precio Gasoleo A'].str.replace(',','.'), errors='coerce')
data['Precio Gasoleo B']=pd.to_numeric(data['Precio Gasoleo B'].str.replace(',','.'), errors='coerce')
data['Precio Gasolina  98']=pd.to_numeric(data['Precio Gasolina  98'].str.replace(',','.'), errors='coerce')
data['Precio Gasolina 95 Protección']=pd.to_numeric(data['Precio Gasolina 95 Protección'].str.replace(',','.'), errors='coerce')
data['Precio Nuevo Gasoleo A']=pd.to_numeric(data['Precio Nuevo Gasoleo A'].str.replace(',','.'), errors='coerce')

data.to_csv(name+'.csv', encoding='utf-8')








