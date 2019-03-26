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
            print(row)
            
def Writecsv(fil) :
    with open(fil, mode='w') as file_tulis:
        employee_writer = csv.writer(file_tulis, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        Nama = input("Nama : ")
        Jurusan = input("Jurusan : ")
        Bulan = input("Bulan Lahir: ")
        employee_writer.writerow([Nama, Jurusan, Bulan])        