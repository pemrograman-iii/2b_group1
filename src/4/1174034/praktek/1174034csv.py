# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 19:54:33 2019

@author: Ichsan Hizman
"""

import csv

#Jawaban No. 1
with open('1174034teori.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Kolom nya adalah {", ".join(row)}')
                line_count += 1
            else:
                print(f'\t{row[0]} kerja di {row[1]} lahir pada bulan {row[2]}.')
                line_count += 1
                print(f'Processed {line_count} lines.')

#Jawaban No. 2            
def bukaModeDictCsv():
    with open('1174034teori.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            print(row['npm'], row['nama'], row['kelas'])

def tulisCsv():
    with open('teori6.csv', mode='w') as csv_file:
        fieldnames = ['npm', 'nama', 'kelas', 'tanggal lahir']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
        writer.writeheader()
        writer.writerow({'npm': '1174007', 'nama': 'Bruce', 'kelas': 'D4TI2C', 'tanggal lahir': '05/05/1999'})
        writer.writerow({'npm': '1174005', 'nama': 'Clark', 'kelas': 'D4TI2B', 'tanggal lahir': '06/06/1999'})