# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 15:42:46 2022

@author: habib
"""

##3a
import numpy as np
from numpy import random
import matplotlib.pyplot as plt

def f(x): #the function in the integral we want to evaluate
    return x**(-1/2)/(1+np.exp(x))

N=10000 #number of sample points
n=100 #will repeat the mean value method n times

#since the integral is between 0 and 1 we will use the function random() to
#get N sample points
random.seed(807)
def mvm(N): #equation for the mean value method
    rand = 0
    for i in range(N):
        rand += f(random.random())
    return rand/N

mean_vm = [] #empty array to append values we get using the mean value method
for i in range(n):
    mean_vm.append(mvm(N))

##3b
def w(x): #weights
    return x**(-1/2)

def g(x): #we set this function to be f(x)/w(x)
    return 1/(1+np.exp(x))

def p_dist(x): #probability distribution found by integrating p(x) given in
#the question from 0 to a function of some random variable and then inversing it
    return x**2

def imp_samp(N):
    important = 0
    for i in range(N):
        important += g(p_dist(random.random()))
    #we multiple this by 2 because thats the integral of w(x) from 0-1
    return 2*important/N

imp = []
for i in range(n):
    imp.append(imp_samp(N))
    
##3c
#plotting the histograms for each method
plt.figure()
plt.hist(mean_vm, 10, range=[0.8,0.88], color='red')
plt.title('Mean value method')

plt.figure()
plt.hist(imp, 10, range=[0.8,0.88], color='green')
plt.title('Importance sampling method')