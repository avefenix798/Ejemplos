# -*- coding: utf-8 -*-
"""
Created on Fri May  1 09:03:53 2020

@author: EmmanuelLap
"""
import pandas as pd 


df = pd.read_csv('Ventas.csv' , sep=r'\s*,\s*',header=0, encoding='ascii', engine='python')

totales = df.groupby(['Sucursal']).sum() 

print(totales)

total =df['Venta'].sum() 

print ('Total = ' + str( total))







