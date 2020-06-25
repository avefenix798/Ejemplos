# -*- coding: utf-8 -*-
import pandas as pd 

datos = pd.read_csv('Ventas.csv')

print('Total de Ventas = '+ str( datos['Venta'].sum()))

print('Total de sucursal =  ' + str( datos['Sucursal'].sum()))

datos.hist()