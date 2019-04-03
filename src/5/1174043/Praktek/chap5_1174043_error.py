# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 19:34:28 2019

@author: Irvan
"""

import csv

def Bacacsv(file) :
    with open(file) as csv_file:
        baca = csv.reader(csv_file, delimiter=',')
        for row in baca:
            x = print(row)
    return(x)
try :
    y = Bacacsv(input())
except FileNotFoundError:
    print("Nama File CSV SALAH !")