# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 14:01:09 2019

@author: Irvan
"""

import matplotlib.pyplot as plt

print('Jumlah Subplot Sesuai NPM mod 3 + 2 =', 1174043%3+2)

labels = 'test1', 'test2', 'test3', 'test4'
sizes = [25,35,20,20]

plt.subplot(2,2,1)
plt.title('subplot(2,2,1)')
plt.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')

plt.subplot(2,2,2)
plt.title('subplot(2,2,1)')
plt.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')

plt.subplot(2,2,3)
plt.title('subplot(2,2,1)')
plt.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')

plt.subplot(2,2,4)
plt.title('subplot(2,2,1)')
plt.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')