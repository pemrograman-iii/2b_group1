# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 19:28:38 2019

@author: Irvan
"""

import csv

def Bacacsv(file) :
    with open(file) as csv_file:
        baca = csv.reader(csv_file, delimiter=',')
        for row in baca:
            b = print(row)
    return(b)
x = Bacacsv(input())