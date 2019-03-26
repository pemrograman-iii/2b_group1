# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 13:05:18 2019

@author: Haganz
"""

import pandas_1174040
##read
x = pandas_1174040
file = '1174040_csvpandas.csv'
hasil = x.Readpandas(file)

##write
fil = '1174040_writepandas.csv'
result = x.Writepandas(fil)