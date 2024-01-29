# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 20:01:24 2022

@author: habib
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as pc

##Q2a
#setting all constants
m = 9.1094e-31 
hbar = 1.0546e-34 
e = 1.6022e-19 
a = 5.2918e-11 
N = 1000 
e_0 = pc.epsilon_0

r_inf = 20*a #this is L
h = 0.001*a
def V(r): #potential energy
    potential = -e**2/(4*np.pi*e_0*r)
    return potential

def f(R,S,r,E,l): #Schrodinger
    dR = S/r**2
    dS = l*(l+1)*R + (2*m*r**2/hbar**2)*(V(r)-E)*R
    return np.array([dR,dS] ,float) 

#need to set R(h)=0 and S(h)=1
#calculating wavefunction for energy E
def solve(E,l):
    S = 1
    R = 0
    
    x=[]
    for r in np.arange(h,r_inf,h):
        
        k1 = h*f(R,S,r,E,l)
        k2 = h*f(R+0.5*k1[0],S+0.5*k1[1],r+0.5*h,E,l)
        k3 = h*f(R+0.5*k2[0], S+0.5*k2[1], r+0.5*h, E, l)
        k4 = h*f(R+k3[0], S+k3[1], r+h, E, l)
        R += (k1[0]+2*k2[0]+2*k3[0]+k4[0])/6
        S += (k1[1]+2*k2[1]+2*k3[1]+k4[1])/6
        x.append(R)
    return [R,x]

##q2b
#first set all the different targets we will test on
target3 = e/1000
target4 = e/10000
target5 = e/100000 
#will solve for a few different situations, first when
n=1
l=0

E1 = -15*e/n**2
E2 = -13*e/n**2
R2 = solve(E1,l)[0]
#now we use the secant method

while abs(E1-E2)>target4:
    R1 , R2, p = R2, solve(E2,l)[0], solve(E2,l)[1]
    E1,E2 = E2, E2-R2*(E2-E1)/(R2-R1)
print('E=',E2/e, 'eV with target error = e/10000, n=1, l=0')


n=2 
l=0

E1 = -15*e/n**2
E2 = -13*e/n**2
R2 = solve(E1,l)[0]

while abs(E1-E2)>target4:
    R1 , R2, p2 = R2, solve(E2,l)[0], solve(E2,l)[1]
    E1,E2 = E2, E2-R2*(E2-E1)/(R2-R1)
print('E=',E2/e, 'eV with target error = e/10000, n=2, l=0')

n=2 #changed to 1 to find the values when n=1
l=1

E1 = -15*e/n**2
E2 = -13*e/n**2
R2 = solve(E1,l)[0]

while abs(E1-E2)>target4:
    R1 , R2, p3 = R2, solve(E2,l)[0], solve(E2,l)[1]
    E1,E2 = E2, E2-R2*(E2-E1)/(R2-R1)
print('E=',E2/e, 'eV with target error = e/10000, n=2, l=1')


##2C
#create array to be used for plotting
x = np.arange(h,r_inf,h)
#normalization constant using simpsons rule
def norm_const(R):
    n = len(R)
    value = R[0]**2 + R[-1]**2
    for i in range(1,n,2): #create 2 loops to loop over even and odd indices of R
        value += 4*R[i]**2
    for i in range(2,n,2):
        value += 2*R[i]**2
    return 1/3 * h/a * value
#taking the sqrt so we can divide them by our integral values p,p2,p3
norm1 = np.sqrt(norm_const(p))
norm2 = np.sqrt(norm_const(p2))
norm3 = np.sqrt(norm_const(p3))

plt.figure()
plt.plot(x,p/norm1, color='navy')
plt.title('Solution using RK4, [n=1&l=0]')
plt.ylabel('R(r) normalized')
plt.xlabel('x (the range of r values)')

plt.figure()
plt.plot(x,p2/norm2, color='green')
plt.title('Solution using RK4, [n=2&l=0]')
plt.ylabel('R(r) normalized')
plt.xlabel('x (the range of r values)')

plt.figure()
plt.plot(x,p3/norm3, color = 'red')
plt.title('Solution using RK4, [n=2&l=1]')
plt.ylabel('R(r) normalized')
plt.xlabel('x (the range of r values)')