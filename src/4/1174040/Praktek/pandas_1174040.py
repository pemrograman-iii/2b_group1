# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 13:03:39 2019

@author: Haganz
"""

import pandas

def Readpandas(file) :
    df = pandas.read_csv(file)
    print(df)
    
def Writepandas(fil) :
    df = pandas.read_csv('1174040_csvpandas.csv', 
            index_col='Karyawan', 
            parse_dates=['Tanggal Masuk'],
            header=0, 
            names=['Karyawan', 'Tanggal Masuk', 'Gaji', 'Hari Sakit'])
    df.to_csv(fil)