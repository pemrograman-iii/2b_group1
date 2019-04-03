def BacaCSV():
	import csv
	with open('chap5_1174035_csv_CSVWrite.csv', 'r') as f:
		reader = csv.reader(f)
		your_list = list(reader)
	return your_list