def BarPanggil(npm):
	try:
		import matplotlib.pyplot as plt
		import random as rand
		i = (int(npm)%3)+2
		rowcol = ""
		if i%2==0:
			row=i/2
			rowcol=str(int(row))+"2"
		if i%3==0:
			row=i/3
			rowcol=str(int(row))+"3"
		a=1
		while a<=i:
			y = [rand.randint(1,10),rand.randint(1,10),rand.randint(1,10),rand.randint(1,10)]
			plt.subplot(int(rowcol+str(4)))
			#plt.subplot(int(rowcol+str(a)))
			plt.bar([1,2,3,4], y)
			a+=1
		plt.show()
	except ValueError:
		print("Salah pada index subplot")
	return i
BarPanggil("1174035")
