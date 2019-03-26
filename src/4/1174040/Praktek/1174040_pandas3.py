# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 09:36:01 2019

@author: Haganz
"""

import pandas
df = pandas.read_csv('1174040_csvpandas.csv', index_col='Name', parse_dates=['Hire Date'])
print(df)