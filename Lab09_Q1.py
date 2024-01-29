# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 11:50:07 2022

@author: habib
"""

import numpy as np
from numpy import eye, diag, matmul, conj
import matplotlib.pyplot as plt

##Q1a+b+c

#defining constants
L = 10**(-8) #m
m = 9.109*10**(-31) #kg
sigma = L/25
kappa = 500/L
x0 = L/5
P = 1024
tau = 10**(-18) #s
N = 3000
T = np.arange(tau, (N+1)*tau, tau)
x = np.linspace(-L/2,L/2,P)
hbar = 1.05457182*10**(-34) #m**2 kg/s
a=L/P
#initial condition for wave function
x=x[1:-1] #dont include first and last state
phi = np.exp(-((x-x0)**2)/(4*sigma**2) + 1j*kappa*x)


#defining a function to calculate the normalization constant to normalize the 
#initial wave function
def Norm(phi):
    phi0 = np.sqrt(np.sum(np.conj(phi)*phi*a))
    return phi0

#actual normalization constant
phi0 = Norm(phi)
#normalized wave function
phi = phi*phi0

#calculating the hamiltonian
def H(V):
    A = -hbar**2/(2*m*a**2)
    B = V-2*A
    D = diag(B, k=0) #setting values to the diagonal (k=0)
    sup = A*eye(1022, k=1) #super diagonal (k=1)
    sub = A*eye(1022, k=-1) #sub diagonal (k=-1)
    H_D = D+sup+sub
    
    return H_D

#calculating the potential V at the walls
def V(x):
    pot = np.zeros(1022)
    return pot


phi_0 = []
phi_ = np.zeros((len(T)+1, len(phi)))
V = V(x)
H = H(V)
#Define L and R to solve the system of linear equations
L = eye(1022) + 1j*tau/(2*hbar)*H
R = eye(1022) - 1j*tau/(2*hbar)*H

#energy and expectation that we need for plots in part b and c
#define expectation value for the particles position x
def exp(x, phi):
    #using the formula in the lab handout
    ex = np.sum(conj(phi)*x*phi*a)
    return ex

#define energy
def energy(phi, H):
    e1 = matmul(H,phi)
    e = np.sum(conj(phi)*e1*a)
    return e


#initial wave
phi_[0] = phi
#array for the expected positions of particles
xp = []
#array for the energies
en = []
index=1
for t in T:
    v = matmul(R,phi) #multiplying matrices
    
    phi= np.linalg.solve(L,v)  #solving the linear equation to get the wavefunction
   
    phi_[index] = phi #setting new values to the wave function
    index += 1
    
    phi_0.append(Norm(phi)) #adding all the normalization constants to an array
    
    xp.append(exp(x,phi)) #calculate expected positions at each time iteration
    en.append(energy(phi,H)) #calculate the energy to show later that its conserved

t4= int(len(T)/4)
t2 = int(len(T)/2)
t3 = int(3*len(T)/4)
t= int(len(T))

plt.figure()
plt.plot(x, phi_[0], label = 't=0', color = 'red')
plt.title('Wavefunction at t=0')
plt.legend()
plt.ylabel('wavefunction')
plt.xlabel('x')

plt.figure()
plt.plot(x,phi_[t4], label = 't=T/4', color = 'green')
plt.title('Wavefunction at t=T/4')
plt.legend()
plt.ylabel('wavefunction')
plt.xlabel('x')

plt.figure()
plt.plot(x,phi_[t2], label = 't=T/2', color = 'purple')
plt.title('Wavefunction at t=T/2')
plt.legend()
plt.ylabel('wavefunction')
plt.xlabel('x')

plt.figure()
plt.plot(x,phi_[t3], label = 't=3T/4', color = 'yellow') 
plt.title('Wavefunction at t=3T/4')
plt.legend()
plt.ylabel('wavefunction')
plt.xlabel('x')

plt.figure()
plt.plot(x,phi_[t], label = 't=T', color = 'black')
plt.legend()
plt.title('Wavefunction at t=T')
plt.ylabel('wavefunction')
plt.xlabel('x')

plt.figure()
plt.plot(T,xp, color = 'navy')
plt.plot(T[0],xp[0], 'o', color = 'red', label = 't=0')
plt.plot(T[t4],xp[t4], 'o', color = 'green', label = 't=T/4')
plt.plot(T[t2],xp[t2], 'o', label = 't=T/2', color = 'purple')
plt.plot(T[t3],xp[t3], 'o', label = 't=3T/4', color = 'yellow')
plt.title('Expected position of particle vs. Time')
plt.xlabel('Time (s)')
plt.ylabel('<X>')
plt.legend()

plt.figure()
plt.plot(T,phi_0, color='black')
plt.title('Normalization constant N(t)')
plt.xlabel('Time (s)')
plt.ylabel('Normalization constant')

plt.figure()
plt.plot(T,en)
plt.title('Energy')
