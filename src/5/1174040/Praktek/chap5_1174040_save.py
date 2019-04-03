import serial
import time

arduino = serial.Serial('COM7', 9600)
def Nomor2() :
	while True:  
		a = input()
		conv = str.encode(str(a))
		time.sleep(2)
		print(conv)
		arduino.write(conv)
		reachedPos = str(arduino.readline())
		print(reachedPos)

x = Nomor2()
