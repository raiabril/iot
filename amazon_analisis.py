# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 12:05:53 2017

@author: root
"""

import pandas as pd
import os
os.chdir('/home/pi/logs')

import matplotlib.pyplot as plt
matplotlib.style.use('ggplot')

data = pd.read_csv('amazon_logs.csv',delimiter=',',encoding='utf-8',parse_dates=1,index_col=1)
data['BRAND']= data.PRODUCT.str.split()
data['BRAND'] = data.BRAND.apply(lambda x: x[0])

pivot = data.pivot_table(index='ASIN', columns=data.index, values='PRICE')

data.hist()
plt.show()
