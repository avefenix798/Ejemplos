# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 15:30:13 2020

@author: Emmanuel
"""


import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize = (10,8))
ax = fig.add_subplot(111, projection='3d')

# grid del cilindro
x=np.linspace(-1, 1, 200)
z=np.linspace(-2, 2, 200)
Xc, Zc=np.meshgrid(x, z)
Yc = np.sqrt(1-Xc**2)


# Plot del cilindro en dos partes
ax.plot_surface(Xc, Yc, Zc, alpha=0.2, rstride=10, cstride=10) # Mitad delantera
ax.plot_surface(Xc, -Yc, Zc, alpha=0.2, rstride=10, cstride=10) # Mitad trasera

plt.show()
x=0

