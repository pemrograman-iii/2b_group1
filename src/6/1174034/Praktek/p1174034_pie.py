# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 22:30:40 2019

@author: Ichsan Hizman
"""

from matplotlib import pyplot as plt

print(1174034%3+2)

def pie_chart(): 
    aktivity = [1,6,2,4]
    game = [14,1,9]
    txt = [9,2,9,17]
    siapa = ['najib','alit','dika','isan']
    dimana = ['rumah','kampus','kosan']
    apa = ['makan','skip','kelas','kost']
    cols = ['y','c','m','b']

    plt.subplot(221)
    plt.pie(aktivity,
             labels=siapa,
             colors=cols,
             startangle=0,
             shadow= True,
             explode=(0.2,0,0,0),
             autopct='%1.1f%%')
    plt.title('Pie Chart Siapa')
    
    plt.subplot(222)
    plt.pie(game,
             labels=dimana,
             colors=cols,
             startangle=90,
             shadow=True,
             explode=(.3,0.1,0),
             autopct='%1.1f%%')
    plt.title('Pie Chart Dimana')
    
    plt.subplot(223)
    plt.pie(txt,
             labels=apa,
             colors=cols,
             startangle=90,
             shadow=True,
             explode=(.1,0,0,0),
             autopct='%1.1f%%')
    plt.title('Pie Chart Apa')
    plt.show()