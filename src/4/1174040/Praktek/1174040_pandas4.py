# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 15:04:46 2019

@author: Haganz
"""

import pandas
df = pandas.read_csv('1174040_csvpandas.csv', index_col='Hire Date')
print(df)