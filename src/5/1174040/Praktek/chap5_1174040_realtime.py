import serial
import time
import csv

def Nomor1() :
	arduino = serial.Serial('COM7', 9600)   
	a = input()
	conv = str.encode(str(a))
	time.sleep(2)
	print(conv)
	arduino.write(conv)
	reachedPos = str(arduino.readline())
	print(reachedPos)

def Nomor3() :
	arduino = serial.Serial('COM7', 9600)   
	a = input()
	conv = str.encode(str(a))
	time.sleep(2)
	print(conv)
	arduino.write(conv)
	reachedPos = str(arduino.readline())
	print(reachedPos)
	with open('1174040_realtime2.csv', mode='w') as file_tulis:
		employee_writer = csv.writer(file_tulis, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		employee_writer.writerow([a])
