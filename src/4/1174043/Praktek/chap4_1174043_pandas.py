# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 18:11:41 2019

@author: Irvan
"""

import pandas as pd

def nomor3():
    df = pd.read_csv('chap4_1174043_csv.csv')
    print(df)
    
def nomor4():
    df = pd.read_csv('chap4_1174043_csv.csv', usecols=['nomor'])
    result = df.to_dict(orient='records')
    print(result)
    
def nomor5():
    df = pd.read_csv('chap4_1174043_csv.csv', parse_dates=[1])
    print(df)
    
def nomor6():
    df = pd.read_csv('chap4_1174043_csv.csv')
    df.rename(columns={'nomor':'No.'}, inplace=True)
    print(df)
    
def nomor7():
    df = pd.read_csv('chap4_1174043_csv.csv')
    df.rename(columns={'nomor':'No.'}, inplace=True)
    print(df)