# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 19:27:01 2019

@author: Irvan
"""

import time
import serial
import csv

def No1() :
	arduino = serial.Serial('COM6', 9600)   
	x = input()
	c = str.encode(str(x))
	time.sleep(2)
	print(c)
	arduino.write(c)
	s = str(arduino.readline())
	print(s)

def No3() :
	arduino = serial.Serial('COM6', 9600)   
	x = input()
	c = str.encode(str(x))
	time.sleep(2)
	print(c)
	arduino.write(c)
	s = str(arduino.readline())
	print(s)
	with open('csvFile_1174043.csv', mode='w') as file_tulis:
		employee_writer = csv.writer(file_tulis, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		employee_writer.writerow([x])
