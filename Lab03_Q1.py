#Lab03_Q1 code
#coded using spyder from anaconda
#Authors: Augustine Tai and Habiba Zaghloul

#This code answers Q2:
#a) Calculates the derivative using forward + central method, central method used later on
#b) Output plots: plots the error vs stepsize of the forward method  (loglog plot)
#c) Output plots: plots the error vs stepsize of the forward methodand central method  (loglog plot)

#import neeeded functions
import numpy as np
import matplotlib.pyplot as plt

####################################################################
#This part mostly deals with Q2 a) 
#finds the derivatives of both central + forward method


#define the function we wish to take the derivative of
def f(x):
    return np.exp(-x**2)

# Define function to perfrom forward diff derivative
def forwarddiff(f,x,h):
	return ((f(x+h)-f(x))/h)

# Define function to perfrom central diff derivative
def centraldiff(f,x,h):
	return ((f(x+0.5*h)-f(x-0.5*h))/h)

#create a range of values for h for the derivatives. Range of values = 1e-16 to 1e0, increasing by a factor of 10 each time
hRange = [10**i for i in range(-16,1)]

#performs and prints the derivative for the forward method
forward_val  = list(forwarddiff(f,0.5,10**i) for i in range(-16,1)) 
print(list(forwarddiff(f,0.5,10**i) for i in range(-16,1)))

#performs and prints the derivative for the central method
central_val = list(centraldiff(f,0.5,10**i) for i in range(-16,1))
print(list(centraldiff(f,0.5,10**i) for i in range(-16,1)))

####################################################################
#This part mostly deals with Q2 b): calculates the error between the calculated derivatives and its actual value 
#in this part only the forward method's error is plotted 

#calculates the true value of the derivative at 0.5, expression was done manually
true_val = -2*(0.5)*np.exp(-0.5**2)


#calculates the error between the calculated derivatives (forward + central) and the true value 
forward_error=[] #creates storage to store errors
central_error=[] #creates storage to store errors
for i in range(len(hRange)):
    forward_error.append(abs(forward_val[i] - true_val))
    central_error.append(abs(central_val[i] - true_val))
    
#prints the errors of each method
print(forward_error)
print(central_error)

#just printting to see if values are correct
print(hRange)
print(len(hRange))

#plots error vs stepsize for the forward diff method
plt.figure()
plt.loglog(hRange,forward_error,'s',markersize = 12,label = 'Forward difference method')
plt.axvline(1e-8,linestyle='--',color = 'r',label = 'h = 1e-8')#marks the 1e-8 for easy analysis
plt.xlabel('Step size (h)',fontsize = 14,fontweight='bold')
plt.ylabel('Error',fontsize = 14,fontweight='bold')
plt.title('Error vs Stepsize for the forward \ndifference method',fontsize = 16,fontweight='bold')
plt.grid()
#plt.tight_layout()

####################################################################
#This part mostly deals with Q2 c): continues from part b and plots central method's error on the same plot as the forward method
    
    
    
#plots error vs stepsize for the forward diff and central method
plt.figure()
plt.loglog(hRange,forward_error,'s',markersize = 12,label = 'Forward difference method')
plt.loglog(hRange,central_error,'o',markersize = 10,label = 'Central difference method')
plt.axvline(1e-8,linestyle='--',color = 'r',label = 'h = 1e-8')
plt.xlabel('Step size (h)',fontsize = 14,fontweight='bold')
plt.ylabel('Error',fontsize = 14,fontweight='bold')
plt.title('Error vs Stepsize for the forward \nand central difference method',fontsize = 16,fontweight='bold')
plt.grid()
plt.legend()
#plt.tight_layout()