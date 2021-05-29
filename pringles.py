#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  2 19:47:25 2021

@author: karanoberoi
"""

from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

a = 3.0
b = 2.0

x = np.linspace(-1.0, 1.0, 100)
y = np.linspace(-1.0, 1.0, 100)
X,Y = np.meshgrid(x,y)
z = (X**2 / a**2) - (Y**2 / b**2)

fig = plt.figure(figsize=(14,8))
ax1 = fig.add_subplot(projection = '3d')

mycmap = plt.get_cmap('gist_earth')
ax1.set_title('Pringles')
surf1 = ax1.plot_surface(X, Y, z, cmap = mycmap)
fig.colorbar(surf1,ax=ax1,shrink = 0.5, aspect = 5)
plt.show()


