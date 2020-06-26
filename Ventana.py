# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 12:14:12 2020

@author: Emmanuel
"""

import tkinter as tk 
from tkinter import ttk

ventana = tk.Tk()

ventana.title("Hola mundo")
#ventana.resizable (0,0)

ttk.Label(ventana,text='Hola crayola').grid(column=0,row=0)


ventana.mainloop()
