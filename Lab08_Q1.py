# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 14:07:40 2022

@author: habib
"""

import numpy as np
import matplotlib.pyplot as plt
from time import time
##Q1a

M=100 #grid squares
target=1e-6 #target accuracy
V = 0.0 #voltage at the walls
V2 = 1.0 #voltage of the plate at 20
V3 = -1 #voltage of the palte at 80

phi = np.zeros([M+1,M+1],float) #create an array ot calculate the potentials
phi[0,:] = V #set the walls to 0V
phi[M,:]= V 
phi[20:80, 20] = V2 #Set the 2 plates to +/- 1V
phi[20:80, 80] = V3

delta = 1.0

start = time() #setting start time to calculate how long it takes to converge using this method

while delta>target:
    phip = phi.copy()
    for i in range(M+1):
        for j in range(M+1):
            if i == 0 or j == M or i == M or j == 0: #setting the boundary conditions
                phi[i,j] = phi[i,j]
            elif (j ==20 or j==80) and (i >=20 and i<=80): #making sure the charged 
            #plates stay at voltages +/- 1V
                phi[i,j] = phi[i,j]
            else: #calcualting the new values of the potential
                phi[i,j] = (phi[i+1,j] + phi[i-1,j] + phi[i,j+1] + phi[i,j-1])/4
    delta = np.max(np.abs(phi-phip)) #precision at each grid point
    
end = time() #stopping the time clock
diff = end-start #calculating how long it took to converge using gauss-seidel
print('it took', diff, 'seconds to run Gauss Seidel')

x = np.arange(0, M+1, 1) #arrays we need to plot a contour graph, going from 0-100
y = np.arange(0, M+1, 1) #because our grid is 100mmx100mm
l = np.linspace(-1,1,20) #the levels we will use for the contour lines
#add contour lines
#plotting the contour plot of the 2 metal plates
plt.figure()
cs = plt.contour(x, y, phi,cmap=plt.cm.viridis ,levels = l, linestyles='dashed')
plt.clabel(cs, inline=True, fontsize=15)
plt.colorbar() #adding a colorbar to see what value each color represents
plt.title("Parallel charged plates using Gauss-Seidei without overrelaxation")
plt.xlabel('X (mm)')
plt.ylabel('Y (mm)')

##Q1b
#Gauss-Seidel with over-relaxation
phi = np.zeros([M+1,M+1],float)
phi[0,:] = V
phi[M,:]= V 
phi[20:80, 20] = V2
phi[20:80, 80] = V3
#parameters we're going to use for over-relaxation
omega = 0.1
omega2 = 0.5

start = time()
delta = 1.0

#same as above but modified to include the over-relaxation parameter
while delta>target:
    
    phip = phi.copy()
    
    for i in range(M+1):
        for j in range(M+1):
            if i==0 or j==0 or i==M or j==M:
                phi[i,j] = phi[i,j]
            
            elif (i>=20 and i<= 80) and (j==20 or j==80):
                phi[i,j] = phi[i,j]
            
            else: #the only difference here is adding the omega into the equation to overshoot the new values of phi
                phi[i,j] = (1+omega)*(phi[i-1,j] + phi[i+1,j] + phi[i,j-1] + phi[i,j+1])/4 - omega*phi[i,j]
    delta = np.max(np.abs(phi-phip))

end = time()
diff = end-start
print('Using relaxation parameter w=0.1, it took', diff, 'seconds to run')
  
plt.figure()
cs = plt.contour(x, y, phi,cmap=plt.cm.viridis, levels = l, linestyles='dashed')
plt.clabel(cs, inline=True, fontsize=15)
plt.colorbar()
plt.title("Parallel charged plates using Gauss-Seidei \n Overrelaxation parameter w=0.1")
plt.xlabel('X (mm)')
plt.ylabel('Y (mm)')

phi = np.zeros([M+1,M+1],float)
phi[0,:] = V
phi[M,:]= V 
phi[20:80, 20] = V2
phi[20:80, 80] = V3

delta = 1.0
start = time()

#Same as above but changing the omega parameter to 0.5
while delta>target:
    
    phip = phi.copy()
    
    for i in range(M+1):
        for j in range(M+1):
            if i==0 or j==0 or i==M or j==M:
                phi[i,j] = phi[i,j]
            
            elif (i>=20 and i<= 80) and (j==20 or j==80):
                phi[i,j] = phi[i,j]
            
            else:
                phi[i,j] = (1+omega2)*(phi[i-1,j] + phi[i+1,j] + phi[i,j-1] + phi[i,j+1])/4 - omega2*phi[i,j]
    delta = np.max(np.abs(phi-phip))
      
end = time()
diff = end-start
print('Using relaxation parameter w=0.5, it took', diff, 'seconds to run')

plt.figure()
cs = plt.contour(x, y, phi, cmap=plt.cm.viridis, levels = l, linestyles='dashed')
plt.clabel(cs, inline=True, fontsize=15)
plt.colorbar()
plt.title("Parallel charged plates using Gauss-Seidei \n Overrelaxation parameter w=0.5")
plt.xlabel('X (mm)')
plt.ylabel('Y (mm)')              
        