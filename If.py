# -*- coding: utf-8 -*-
"""
Created on Thu May  7 12:43:16 2020

@author: EmmanuelLap
"""
import pylab  as ptl

x = [1.3,22,33,-4]

print(x)

print('La suma es = ' + str(sum(x)))
print('El maximo es  = ' + str(max(x)))

ptl.plot(x)
ptl.title("Título")
input()