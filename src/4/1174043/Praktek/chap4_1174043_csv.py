# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 18:17:47 2019

@author: Irvan
"""

import csv

def nomor1():
    with open('chap4_1174043_csv.csv', mode='r') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            print(row)
            
def nomor2():
    with open('chap4_1174043_csv.csv', mode='r') as csvfile:
        readCSV = csv.DictReader(csvfile)
        for row in readCSV:
            print(row)
            
def WriteCSV():
    with open('chap4_1174043_csvbuat.csv', 'w', newline='') as myfile:
     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
     wr.writerow(['Name', 'Profession'])
     wr.writerow(['Derek', 'Software Developer'])
     wr.writerow(['Steve', 'Software Developer'])
     wr.writerow(['Paul', 'Manager'])
     

#nomor1()
#nomor2()
#WriteCSV()