# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 19:29:31 2019

@author:   TOSHIBA
"""

def ErrorGais():
	import csv
	try:
		with open('1174050csv.py', newline='') as csvfile:
			reader = csv.DictReader(csvfile)
			for row in reader:
				print(row['npm'], row['nama'], row['key'])
	except KeyError : 
		print("ERRROOOOORRRRRRR")
        
ErrorGais()