def ErrorCoba():
	import csv
	try:
		with open('chap4_1174035_csv.csv', newline='') as csvfile:
			reader = csv.DictReader(csvfile)
			for row in reader:
				print(row['NP'], row['Nama'], row['Jurusan'])
	except KeyError : 
		print("Kunci ada yang salah")
ErrorCoba()