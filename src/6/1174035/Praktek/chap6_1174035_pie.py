def PiePanggil(npm):
	import matplotlib.pyplot as plt
	import random as rand
	i = (int(npm)%3)+2
	row = ""
	col = ""	
	if i%2==0:
		row=i/2
		col="2"
	if i%3==0:
		row=i/3
		col="3"
	a=1
	labels = 'Anjing', 'Kucing', 'Kakatua', 'Jerapah'
	# Make figure and axes
	fig, axs = plt.subplots(int(row), int(col))		
	while a<=i:
		c=0
		fracs = []			
		tot=0
		while c!=3:
			num = rand.randint(1,33)
			tot = tot+num
			fracs.append(num)
			c+=1
		fracs.append(100-tot)
		plt.subplot(str(int(row)),col,a)
		plt.pie(fracs,labels=labels,startangle=90,shadow= True,explode=[0,0,0,0.1],autopct='%1.1f%%')			
		a+=1		
	plt.show()
	return i
a = PiePanggil("1174035")