# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 19:52:41 2019

@author: Irvan
"""

def ErrorCoba():
	import csv
	try:
		with open('chap4_1174043_csv.csv', newline='') as csvfile:
			reader = csv.DictReader(csvfile)
			for row in reader:
				print(row['nomor'], row['poin'], row['tgl'])
	except KeyError : 
		print("Terdapat ERROR")
ErrorCoba()