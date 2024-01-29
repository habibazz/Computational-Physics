#Lab03_Q2 code
#coded using spyder from anaconda
#Authors: Augustine Tai and Habiba Zaghloul

#This code answers Q2:
#a) fractional error for periods (N=8,16)
#b) output plots: weighted values vs sample points position and integrand vs sample point position
#c) finds period and percentage error wne N=200
#d) finds initial displacement xc, where velocity = c, at x = 0


import numpy as np
import matplotlib.pyplot as plt
from gaussxw import gaussxwab
from gaussxw import gaussxw
from scipy import constants


###############################################################################

#fractional error for Q2 a)

#Define values and constants
kspring = 12 #N/m
mass = 1 #kg
N1 = 8 #sample points
N2 = 16 #sample points
c = 3e8 #m/s - speed of light
x_0 = 0.01 #initial displacement
a = 0 #m lower limit
b = 0.01 #m upper limit same as x_0

#define finctions:

def f(x,x_0,kspring,mass):#defines the expression (equation 6) we will be trying to integrate
    return 1/(c*((0.5*kspring*((x_0**2)-(x**2))*(2*mass*(c**2)+0.5*kspring*((x_0**2)-(x**2))))/((mass*c**2)+0.5*kspring*((x_0**2)-(x**2)))** 2)** 0.5)

#define a function that uses Gaussian quadrature to calculate the integral
def Gauss(N,a,b,x_0,ksping,mass): #takes N,a,b,x_0,ksping, and mass to calculate the integral
    xp,wp = gaussxwab(N,a,b) #This part of the code comes from Example 5.2 from text book
    s = 0#create space to sum values
    weighted= []
    for i in range(N):
        s += wp[i]*f(xp[i],x_0,kspring,mass) #sums the individuak units of the integral
        weighted.append(4*wp[i]*f(xp[i],x_0,kspring,mass)) #this will calculate weighted values used in part b)
    period = 4*s #calcualtes the period
    return period,f(xp,x_0,kspring,mass),xp, weighted #returns the calculated period, integrand, sample points, and the weighted values

def Gauss2(N,a,b,x_0,ksping,mass): #just an alternate method to check if I'm doing it correctly, not labelled since i don't use it
    x,w = gaussxw(N)
    s = 0
    xp = 0.5*(b-a)*x + 0.5*(b+a)
    wp = 0.5*(b-a)*w
    weighted= []
    for i in range(N):
        s += wp[i]*f(xp[i],x_0,kspring,mass)
        weighted.append(4*wp[i]*f(xp[i],x_0,kspring,mass))
    period = 4/s
    return period,f(xp,x_0,kspring,mass),xp, weighted

#separate the values returned by the Gauss function, so they may be called individually
period8, intergrand8, sample_points8, weighted_values8= Gauss(N1,a,b,x_0,kspring,mass)
period16, intergrand16, sample_points16, weighted_values16= Gauss(N2,a,b,x_0,kspring,mass)

#calculates the classical limit given by the lab handout
classicalLimit = 2*np.pi*np.sqrt(mass/kspring)
print("Classical limit:",classicalLimit)

#function frac_error() calculates the fractional error when called + given calculated period and the classical limit
def frac_error(period,classicalLimit):
    return abs(period-classicalLimit)/(classicalLimit)

#prints the period calculated for N=8 and 16
print("N=8 period:",period8)
print("N=16 period:",period16)
#print((weighted_values8))

#prints the fractional error
fractionalError_8 = frac_error(period8,classicalLimit)
print("Fractional error when N = 8:",fractionalError_8)

fractionalError_16 = frac_error(period16,classicalLimit)
print("Fractional error when N = 16:",fractionalError_16)

########################################################################
#plots for Q2 b)

#This part mostly uses code from a, just calling the proper values from Gauss() function to plot them

#plots the integrands(4/gk) vs position of sampling points
plt.figure()
plt.scatter(sample_points8, intergrand8*4, label="Approximation with N = 8")#integrands are multiplied by 4 because of 4/g_k
plt.scatter(sample_points16, intergrand16*4, label="Approximation with N = 16")
plt.xlabel('Sampling point positions (x_k)',fontsize = 14,fontweight='bold')
plt.ylabel('Integrands (4/gk)',fontsize = 14,fontweight='bold')
plt.title('Integrand vs Sampling point for\n N=8 and N=16',fontsize = 16,fontweight='bold')
plt.grid()
plt.legend()
#print(intergrand)

#plots the weighted values (4wk/gk) vs position of sampling points
plt.figure()
plt.scatter(sample_points8,weighted_values8 , label="Approximation with N = 8")
plt.scatter(sample_points16, weighted_values16, label="Approximation with N = 16")
plt.xlabel('Sampling points positions (x_k)',fontsize = 14,fontweight='bold')
plt.ylabel('Weighted values (4wk/gk)',fontsize = 14,fontweight='bold')
plt.title('Weighted values vs Sampling point for\n N=8 and N=16',fontsize = 16,fontweight='bold')


plt.grid()
plt.legend()

#########################################################################
#plots for Q2 c)

#uses the same code except N=200

N200 = 200 #200 sample points

#separates the values returned by Gauss() for N=200
period200, intergrand200, sample_points200, weighted_values8= Gauss(N200,a,b,x_0,kspring,mass)
#print(period200)

#this function calcualtes percentage error as described in pseudocode
def percentage_error(period,classicalLimit):#similar to fractional error except it is multilplied by 100 for percentage
    return (abs(period-classicalLimit)/(classicalLimit))*100

#print(period8)
#print(period16)
#print((weighted_values8))

#prints percentage error
PercentageError_200 = percentage_error(period200,classicalLimit)
print("Percentage error when N = 200:",PercentageError_200,"%")

#########################################################################
#Calculation for Q2 d) find initial displacement xc, where velocity = c, at x = 0

c = constants.c #calls for c from scipy constants - makes sure we have the correct value
#print(c)

#calculates and prints initial displacement xc, where velocity = c, at x = 0
xc = np.sqrt(c**2/kspring)
print("initial displacement where velocity = c, at x = 0:",xc)

################################################################
#Outputs plot for Q2 e) period vs intial position (x_0) plot 

x0 = np.linspace(1, 10*xc, N200) #creates a range of x_0 values from 1 to 10*xc, with 200 sample points
b=x0
#print(b)

#define a modified Gauss() function which loops through the values of x_0
def Gauss3(N,a,ksping,mass):
    period = [] #create space for storing the periods
    for j in np.linspace(1, 10*xc, 200): #loops through x_0 values
        x,w = gaussxw(N) #same stuff as Gauss(), calculates period using Gaussian qudrature integral method
        s = 0
        xp = 0.5*(j-a)*x + 0.5*(j+a)
        wp = 0.5*(j-a)*w
        for i in range(N):
            s += wp[i]*f(xp[i],j,kspring,mass)
        period.append(4*s)#store calculated period is list/array
    return period #outputs the calculated periods

#extract periods from the function Gauss3() (mostly for naming conventions sake)
period = (Gauss3(N200,a,kspring,mass))
#print(period)

#plot the calcualted periods vs initial displacement
plt.figure()
plt.scatter(x0,period, label = 'Calculated Periods') 
plt.plot(x0, 4*x0/c, label = 'Relativistic Limit',color='tab:orange',linewidth='3')#plots the relativistic limit/prediction
plt.xlabel('x0 (m)',fontsize = 14,fontweight='bold')
plt.ylabel('Period',fontsize = 14,fontweight='bold')
plt.title('Period vs x0 plot',fontsize = 14,fontweight='bold')
axis = (2*np.pi*np.sqrt(mass/kspring)) #plots the classical limit/prediction (constant line)
plt.axhline(y=axis,linestyle='--',color = 'tab:red',label='Classical limit',linewidth='3')
plt.legend()
plt.grid()


