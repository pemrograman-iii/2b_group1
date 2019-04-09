# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 11:05:56 2019

@author: Irvan
"""

import matplotlib.pyplot as plt

x = [4,8,13,20,23]
y = [54,67,99,78,80]
y2 = [60,80,69,65,95]

plt.plot(x,y, label='contoh')
plt.plot(x,y2, label='contoh2')
plt.xlabel('label1')
plt.ylabel('label2')
plt.legend()
plt.show()