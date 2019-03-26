# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 09:10:54 2019

@author: Haganz
"""

import csv

with open('1174040_csv.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        print(row)