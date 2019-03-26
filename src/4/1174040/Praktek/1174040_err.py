# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 13:19:17 2019

@author: Haganz
"""
import pandas
try :
    df = pandas.read_csv('1174040_csvapandas.csv', index_col='Hire Date')
    print(df)
except FileNotFoundError:
    print("Nama file nya salah, yang benar adalah 1174040_csvpandas.txt")