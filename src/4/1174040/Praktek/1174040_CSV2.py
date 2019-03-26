# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 09:10:54 2019

@author: Haganz
"""

import csv

with open('1174040_csv.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        print(row)