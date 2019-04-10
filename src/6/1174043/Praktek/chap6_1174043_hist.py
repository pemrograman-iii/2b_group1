# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 13:48:08 2019

@author: Irvan
"""

import matplotlib.pyplot as plt

print('Jumlah Subplot Sesuai NPM mod 3 + 2 =', 1174043%3+2)

x = [2,4,6,5,42,543,5,3,73,64,42,97,63,76,63,8,73,97,23,45,56,89,45,3,23,2,5,78,23,56,67,78,8,3,78,34,67,23,324,234,43,544,54,33,223,443,444,234,76,432,233,23,232,243,222,221,254,222,276,300,353,354,387,364,309]
num_bins = 6
n, bins, patches = plt.hist(x, num_bins, facecolor = 'green')

plt.subplot(2,2,1)
plt.title('subplot(2,2,1)')
plt.hist(x, num_bins, facecolor = 'green')

plt.subplot(2,2,2)
plt.title('subplot(2,2,2)')
plt.hist(x, num_bins, facecolor = 'green')

plt.subplot(2,2,3)
plt.title('subplot(2,2,3)')
plt.hist(x, num_bins, facecolor = 'green')

plt.subplot(2,2,4)
plt.title('subplot(2,2,4)')
plt.hist(x, num_bins, facecolor = 'green')