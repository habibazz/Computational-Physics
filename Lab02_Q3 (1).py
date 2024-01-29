# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 09:54:07 2022

@author: Habib Zaghloul (in group with Ryan Cunningham)
"""
import numpy as np
import scipy.constants as c

#Q3b

#Assign values to the constants that will be used in this equation

h = c.Planck
c_light = c.speed_of_light
k_boltzmann = 1.380649*10**(-23)

#Define the function W that we will integrate over
def W(x):
    return (x**3)/(np.e**x-1)
#Using simpsons rule so we assign a and b to the integral limits and N to the 
#number of slices we want
N=800
a=0.0001
b=700
#let hh be the width of every slice
hh=(b-a)/N
#use 2 for loops, one for even values and one for odd to add the areas since 
#we have 3 points every 2 slices, a, a+h and a+2h
s = W(a) + W(b)
for i in range(1,N,2):
    s += 4*W(a+i*hh)

for k in range(2,N,2):
    s += 2*W(a+k*hh)
#printing the value of the integral
print(hh*s/3)
    


#Q3c

#Calculate the constant C_1 found in part a

C_1 = (2*np.pi*k_boltzmann**4)/(c_light**2*h**3)

#Multiply C_1 by the value of the integral to get the stefan boltzmanns constant
stefan = C_1*6.503708322854249

print(stefan, 'is our calculated stefan boltzmann constant')
print(c.Stefan_Boltzmann, 'is the true Stefan Boltzmann constant')

#calculating the relative error
re = (stefan-c.Stefan_Boltzmann)/c.Stefan_Boltzmann
print(re, 'is the relative error')

