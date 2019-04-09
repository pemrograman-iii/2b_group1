# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 11:23:23 2019

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

plt.subplot(3,3,1)
plt.title('subplot(3,3,1)')
plt.plot(x,y)

plt.subplot(3,3,2)
plt.title('subplot(3,3,2)')
plt.plot(x,y)

plt.subplot(3,3,3)
plt.title('subplot(3,3,3)')
plt.plot(x,y)

plt.subplot(3,3,4)
plt.title('subplot(3,3,4)')
plt.plot(x,y)

plt.subplot(3,3,5)
plt.title('subplot(3,3,5)')
plt.plot(x,y)

plt.subplot(3,3,6)
plt.title('subplot(3,3,6)')
plt.plot(x,y)

plt.subplot(3,3,7)
plt.title('subplot(3,3,7)')
plt.plot(x,y)

plt.subplot(3,3,8)
plt.title('subplot(3,3,8)')
plt.plot(x,y)

plt.subplot(3,3,9)
plt.title('subplot(3,3,9)')
plt.plot(x,y)