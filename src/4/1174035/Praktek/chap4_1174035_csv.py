import csv
def CSVModeList():		
	with open('chap4_1174035_csv.csv', 'r') as f:
		reader = csv.reader(f)
		your_list = list(reader)
	return your_list

def CSVModeDict():	
	with open('chap4_1174035_csv.csv', newline='') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			print(row['NPM'], row['Nama'], row['Jurusan'])		
def WriteCSV(list):
	import csv	
	with open('chap4_1174035_csv_CSVWrite.csv', mode='w') as mhsFile:
		mhs = csv.writer(mhsFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		mhs.writerows(list)
		mhs.writerow(['Data1', 'Data2', 'Data3', '17/02/1999'])
print(CSVModeList())
CSVModeDict()
WriteCSV(CSVModeList())
