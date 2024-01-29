# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 15:06:41 2022

@author: habib
"""

import numpy as np
import matplotlib.pyplot as plt
##q2a
N = 16
Lx = 4.0
Ly = 4.0

dx = Lx/np.sqrt(N)
dy = Ly/np.sqrt(N)

x_grid = np.arange(dx/2, Lx, dx)
y_grid = np.arange(dy/2, Ly, dy)

xx_grid, yy_grid = np.meshgrid(x_grid, y_grid)

x_initial = xx_grid.flatten()
y_initial = yy_grid.flatten()

#calculating the force on each particle i as a sum of the interaction forces
#between particle ‘i’ and all other particles

def f(x,y):
    #initial positions for particles in x and y direction
    a_x = np.zeros(N, float)
    a_y = np.zeros(N,float)
    for i in range(len(x)): #loop over all particles
        for j in range(len(x)):
            if i != j: #the particle doesnt interact with itself
                #calculating distance between particles i and j in x and y direction
                dx = x[i]-x[j]
                dy = y[i]-y[j]
                #acceleration formula derived from equatoin given in question
                acc = 48/((dx**2 + dy**2)**7) - 24/((dx**2 + dy**2)**4)
                #sum of the total force on each particle from all other N-1 particles
                a_x[i] += acc*dx
                a_y[i] += acc*dy
    return a_x,a_y

#since mass is 1 kinetic energy is ke=v^2/2
def k(vx,vy):
    ke=0
    for i in range(len(vx)):
        ke += 0.5*vx[i]**2 
        ke += 0.5*vy[i]**2 #must add for both x and y directions
        
    return ke

#the potential energy is V(r) as stated in the lab handout
def u(x,y):
    pot = 0
    
    for i in range(len(x)):
        for j in range(len(y)):
            if i!=j:
                dx = x[i]-x[j]
                dy = y[i]-y[j]
                #total potential energy
                #r = sqrt(dx^2+dy^2)
                pot += 4/((dx**2+dy**2)**6) - 4/((dx**2+dy**2)**3)
    return pot/2 #potential energy for 1 particle
#create empty arrays for the trajectories of the particles
x_points = []
y_points = []

for i in range(0,N):
    
    x_points.append([]) #each particle will get its own array
    y_points.append([])
    
    x_points[i].append(x_initial[i]) 
    y_points[i].append(y_initial[i])
    
h = 0.01 #setting time step
time = np.arange(0,10,h)
    #verlet method
vx = np.zeros(N,float) #arrays for v(t+h)
vy = np.zeros(N,float)
    
vx_half = np.zeros(N,float) #arrays for v(t+0.5h)
vy_half = np.zeros(N,float)
    
kx,ky = f(x_initial,y_initial) #need k to find v(t+0.5h)
    
    #loop over all particles and calculate v at time t+h/2
for i in range(N):
   vx_half[i] += h*0.5*kx[i]
   vy_half[i] += h*0.5*ky[i]
#more arrays needed for verlet method 
x = np.zeros(N,float)
y = np.zeros(N,float)
x = x_initial
y = y_initial

potential=[]
kinetic=[]
    #calculate r(t+h)
for t in time:
    for i in range(N):
        x[i] += h*vx_half[i]
        y[i] += h*vy_half[i]
        
        x_points[i].append(x[i]) #updating trajectory of particles
        y_points[i].append(y[i])
        
    kx = h*f(x,y)[0][:] #(new kx and ky because we have updated our x and y points)
    ky = h*f(x,y)[1][:]          
       
    for i in range(N): #find v(t+h) and v(t+3h/2)
        vx[i] = vx_half[i] + 0.5*kx[i]
        vy[i] = vy_half[i] + 0.5*ky[i]
        
        vx_half[i] += kx[i]
        vy_half[i] += ky[i]
    potential.append(u(x,y)) #calculating this now because if we do it later outside a forloop we just get 1 value
    kinetic.append(k(vx,vy)) #instead of a value at every iteration for all the particles interacting with one another
    
              
#plotting trajecory of each particle
plt.figure()
for i in range(N):
    #loop through every particle and plot its trajectory
    plt.plot(x_points[i],y_points[i], '-.', label = '%i'%i)
plt.legend(fontsize = 7, loc='center right')
plt.title('Trajectories of the 16 particles')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

##q2b
#the energies were calculated above in the for loop since we had to find them at each time step
total = []
for i in range(len(potential)): #adding potential and kinetic energy to get the total
    total.append(potential[i]+kinetic[i])

plt.figure()
plt.plot(potential, '-', label = 'Potential energy')
plt.plot(kinetic,'-', label = 'Kinetic energy')
plt.plot(total,'-', label = 'Total energy') #should show a straight line because of energy conservation
plt.legend(fontsize=9)
plt.ylabel('Energy')
plt.title('Total, kinetic, and potential energies of the 16 particle system')
plt.show()