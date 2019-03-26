# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 12:25:57 2019

@author: Haganz
"""

## Read
import CSV_1174040
x = CSV_1174040
file = '1174040_csv.csv'
hasil = x.Readcsv(file)

##Write
fil = '1174040_writecsv.csv'
result = x.Writecsv(fil)