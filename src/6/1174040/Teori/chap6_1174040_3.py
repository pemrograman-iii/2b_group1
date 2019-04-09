# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 09:40:00 2019

@author: Haganz
"""

import matplotlib.pyplot as plt
x = (4,8,13,17,20)
y = (54, 67, 98, 78, 45)
#PLot Garis
plt.plot(x,y)
plt.show()
#Plot Selebaran
x = (4,8,13,17,20)
y = (54, 67, 98, 78, 45)
plt.scatter(x,y)
plt.show()
#Plot Histogram
b=[2,4,6,5,42,543,5,3,73,64,42,97,63,76,63,8,73,97,23,45,56,89,45,3,23,2,5,78,23,56,67,78,8,3,78,34,67,23,324,234,43,544,54,33,223,443,444,234,76,432,233,23,232,243,222,221,254,222,276,300,353,354,387,364,309]
num_bins = 6
n, bins, patches = plt.hist(b, num_bins, facecolor = 'green')
plt.show()

#Pie
labels = 'Jalan Jalan', 'Main', 'Makan', 'Belajar'
sizes = [15, 30, 45, 10]
explode = (0, 0.1, 0, 0)  

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.0f%%',
        shadow=True, startangle=90)
ax1.axis('equal') 

plt.show()