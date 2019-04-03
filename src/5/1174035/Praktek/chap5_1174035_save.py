def BacaSerialLoop():
	import serial
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