#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 02:45:31 2017

@author: raimundoabrillopez
"""

import os
import pandas as pd
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

os.chdir('/Volumes/Macintosh HD/_data/gasolineras')
files = os.listdir()

data = pd.read_csv(files[1],encoding='utf-8')
data.describe()

myMap = Basemap()
myMap.drawcoastlines(linewidth=0.5)
myMap.scatter(data['Longitud (WGS84)'],data['Latitud'])
plt.show()