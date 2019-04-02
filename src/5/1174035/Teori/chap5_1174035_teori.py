#Fungsi Reader
def ReadSerial(line):
	ser.open()
	a=ser.readline(size=-1)
	ser.writelines(line)
	return a