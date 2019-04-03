# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 19:18:16 2019

@author: Irvan
"""

import time
import serial

arduino = serial.Serial('COM6', 9600)
def No2() :
	while True:  
		x = input()
		c = str.encode(str(x))
		time.sleep(2)
		print(c)
		arduino.write(c)
		s = str(arduino.readline())
		print(s)

test = No2()
