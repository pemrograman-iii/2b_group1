def BacaSerial():
	import serial
	ser = serial.Serial('COM4', 9600, timeout=2)
	x = ser.readline()
	return x

#Simpan Dengan Loop
def BacaSimpan():
	import csv
	with open('chap5_1174035_csv_CSVWrite.csv', mode='w') as mhsFile:
		mhs = csv.writer(mhsFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		lis = []
		lis.append(str(BacaSerial()))
		import serial
		ser = serial.Serial('COM4', 9600, timeout=2)
		x = ser.readline()
		mhs.writerow(lis)

#SimpanTanpaLoop
def BacaLoop():
	import csv
	with open('chap5_1174035_csv_CSVWrite.csv', mode='w') as mhsFile:
		mhs = csv.writer(mhsFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
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
		for x in lis:
			exlis = []
			exlis.append(x)
			mhs.writerow(exlis)