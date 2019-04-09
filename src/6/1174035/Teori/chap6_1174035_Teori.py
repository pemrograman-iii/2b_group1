def Soal2():
	import matplotlib.pyplot as plt
	x = [10,20,5]
	y = [5,9,12]
	plt.plot(x,y,linewidth=1.0)
	plt.show()

def Soal3Garis1():
	import matplotlib.pyplot as plt
	plt.plot([1,2,3,4])
	plt.ylabel('Angka')
	plt.show()

def Soal3Garis2():
	import matplotlib.pyplot as plt
	plt.plot([1,2,3,4], [3,2,1,5])
	plt.ylabel('Angka')
	plt.show()

def Soal3Titik():
	from matplotlib import style
	import matplotlib.pyplot as plt

	plt.plot([1,2,3,4], [1,4,9,16], 'ro')
	plt.axis([0,6,0,20])
	plt.show()

def Soal3Batang():
	import matplotlib.pyplot as plt
	plt.bar([1,2,3,4], [1,2,4,2])
	plt.show()

def Soal3Lingkaran():
	import matplotlib.pyplot as plt	
	labels = 'Tidur', 'Belajar', 'Main'
	sizes = [15, 11, 20]
	explode = (0, 0.1, 0) 

	fig1, ax1 = plt.subplots()
	ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
			shadow=True, startangle=90)
	ax1.axis('equal') 
	plt.show()
	
def Soal4Label():
	import matplotlib.pyplot as plt
	xxx =[1,2,3]
	yyy =[4,5,6]
	plt.plot(xxx,yyy)
	plt.xlabel("X")
	plt.ylabel("Y")
	plt.show()
def Soal4Legend():
	import matplotlib.pyplot as plt
	x = [5,8,10]
	y = [12,16,6]
	plt.plot(x,y,'g', label="Garis Satu", linewidth=1)
	plt.legend()
	plt.show()
def Soal5():
	import numpy as np
	import matplotlib.pyplot as plt

	def f(t):
		return np.exp(-t) * np.cos(2*np.pi*t)
	t1 = np.arange(0.0, 5.0, 0.1)
	t2 = np.arange(0.0, 5.0, 0.02)
	#Baris 1 Kolom 1
	plt.subplot(331)
	plt.plot(t1, f(t1), 'bo', t2, f(t2))
	
	#Baris 1 Kolom 2
	plt.subplot(332)
	plt.plot(t2, np.cos(2*np.pi*t2))
	
	#Baris 1 Kolom 3
	plt.subplot(333)
	plt.plot(t1, f(t1), 'bo', t2, f(t2))
	
	#Baris 2 Kolom 1
	plt.subplot(334)
	plt.plot(t2, np.cos(2*np.pi*t2))
	
	#Baris 2 Kolom 2
	plt.subplot(335)
	plt.plot(t1, f(t1), 'bo', t2, f(t2))
	
	#Baris 2 Kolom 3
	plt.subplot(336)
	plt.plot(t2, np.cos(2*np.pi*t2))
	
	#Baris 3 Kolom 1
	plt.subplot(337)
	plt.plot(t1, f(t1), 'bo', t2, f(t2))	
	
	#Baris 3 Kolom 2
	plt.subplot(338)
	plt.plot(t1, f(t1), 'bo', t2, f(t2))
	
	#Baris 3 Kolom 3
	plt.subplot(339)
	plt.plot(t2, np.cos(2*np.pi*t2))
	plt.show()
	
def	Soal7Hist():
	import numpy as np
	import matplotlib.mlab as mlab
	import matplotlib.pyplot as plt
	 
	x = [10, 10, 10, 10, 40, 20, 15, 25, 40, 75, 60, 50, 30]
	num_bins = 5
	n, bins, patches = plt.hist(x, num_bins, facecolor='blue', alpha=0.5)
	plt.show()
Soal7Hist()