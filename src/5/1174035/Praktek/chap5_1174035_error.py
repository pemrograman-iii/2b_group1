def BacaSerialLoop():
	import serial
	try:
		ser = serial.Serial('COM4', 9600, timeout=2)
		lis = []
		while True:
			x = ser.readline()
			if x:
				print(x)
				lis.append(x)
			else:
				break
		return lis
	except serial.SerialException:
		print("Arduino Belum Terhubung")