# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 22:25:44 2019

@author: Ichsan Hizman
"""

def tryExceptError():
    try:
        from p1174009_titik import batang as bar
    except SyntaxError:
        print("hmmm error")

tryExceptError()