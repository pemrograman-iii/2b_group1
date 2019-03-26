# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 09:06:49 2019

@author: Haganz
"""


import pandas
dt = pandas.read_csv('1174040_csvpandas.csv').T.to_dict()
print(dt)
