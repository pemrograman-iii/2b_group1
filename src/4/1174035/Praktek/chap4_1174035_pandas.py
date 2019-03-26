import pandas as pd
def PandasModeList():
	print("Pandas Mode List : ")	
	df = pd.read_csv('chap4_1174035_csv.csv', delimiter=',')
	print(df)
def PandasModeDict():
	print('Pandas Mode Dictionary : ')	
	df = pd.read_csv('chap4_1174035_csv.csv', delimiter=',')
	res = df.to_dict(orient='records')
	print(res)
def PandasDateToStandardDT():	
	df = pd.read_csv('chap4_1174035_csv.csv', parse_dates=['ttl'])
	print(df)
def PandasIndexCol():
	df = pd.read_csv('chap4_1174035_csv.csv', index_col='Nama')
	print(df)
def PandasNameAttribute():
	df = pd.read_csv('chap4_1174035_csv.csv', header=0, names=['Nomor Mahasiswa', 'Nama', 'Prodi', 'Tanggal Lahir'])
	print(df)
def PandasWrite():
	df = pd.read_csv('chap4_1174035_csv.csv', index_col='NPM')
	df.to_csv('chap4_1174035_csv_pandaswrite.csv')
PandasModeList()
PandasModeDict()
PandasDateToStandardDT()
PandasIndexCol()
PandasNameAttribute()
PandasWrite()

	