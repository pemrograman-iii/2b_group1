# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 09:40:39 2019

@author: Haganz
"""

import pandas
df = pandas.read_csv('1174040_csvpandas.csv', 
            index_col='Employee', 
            parse_dates=['Hired'], 
            header=0, 
            names=['Employee', 'Hired','Salary', 'Hari Sakit'])
print(df)