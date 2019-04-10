# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 13:57:31 2019

@author: Irvan
"""

import matplotlib.pyplot as plt

print('Jumlah Subplot Sesuai NPM mod 3 + 2 =', 1174043%3+2)

x = [4,8,13,20,23]
y = [54,67,99,78,80]

plt.subplot(2,2,1)
plt.title('subplot(2,2,1)')
plt.scatter(x,y)

plt.subplot(2,2,2)
plt.title('subplot(2,2,2)')
plt.scatter(x,y)

plt.subplot(2,2,3)
plt.title('subplot(2,2,3)')
plt.scatter(x,y)

plt.subplot(2,2,4)
plt.title('subplot(2,2,4)')
plt.scatter(x,y)