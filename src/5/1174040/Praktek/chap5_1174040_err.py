# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 12:19:17 2019

@author: Haganz
"""

import csv

def Readcsv(file) :
    with open(file) as file_csv:
        csv_reader = csv.reader(file_csv, delimiter=',')
        for row in csv_reader:
            b = print(row)
    return(b)
try :
    x = Readcsv(input())
except FileNotFoundError:
    print("Nama file nya salah, yang benar adalah 1174040_realtime2.csv")