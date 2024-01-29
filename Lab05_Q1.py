#Lab05_Q1 code
#coded using spyder from anaconda
#Authors: Augustine Tai and Habiba Zaghloul

#This code answers Q1:
#a) plots the position vs time plot for x0 = 1, xc, 10xc
#b) plots the FFT plot for all 3 schenarios + compare with results from lab03


#import the needed libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy import constants
from numpy.fft import rfft
from gaussxw import gaussxw, gaussxwab
###################################################################
#this part deals with Q1 a) position vs time plots

#define constants 
k = 12 #N/m
m = 1 #kg
c = constants.c #m/s
v_initial = 0 #m/s


time = np.linspace(0,150,1048576)
print(time[1])
print(len(time)) # this is the number of samples
#made it so that the number of samples the FFT will have to go throug = 1048576 which is 2^20 samples
#announcement said to make the number of samples = a power of 2

def spring_function(x_init,v_init,k,m):
    #create storage to store values
    u_1 = np.zeros(len(time)) #u1 is equal to position (x)
    u_2 = np.zeros(len(time)) #u2 is velicty (v)
    #put initial condition as 1st value in the storage
    u_1[0] = x_init
    u_2[0] = v_init
    dt = time[1]
    #Use Fro loop to calculate position and velocity values
    for i in range(len(time)-1):
        u_2[i+1] = u_2[i] + (-k/m)*u_1[i]*(1-(u_2[i]**2/c**2))*dt
        u_1[i+1] = u_1[i] + u_2[i+1]*dt
    return u_1,u_2 #return position + velocity when called

#caclculate xc from lab03
xc = np.sqrt(c**2/k)
#print(xc)

#position + velocity when x0 = 1
x_1_initial = 1 #set initial position to 1
coordinate1, velocity1 = spring_function(x_1_initial,v_initial,k,m)#separate position + velocity values calculated using spring_function() 

#same process for the 2 other initial positions:

#position + velocity when x0 = xc
x_xc_initial = xc
coordinate2, velocity2 = spring_function(x_xc_initial,0,k,m)

#position + velocity when x0 = 10xc
x_10xc_initial = 10*xc
coordinate3, velocity3 = spring_function(x_10xc_initial,0,k,m)

print(xc)

#plot using subplot to plot all three position vs time plots in the same image

fig, (ax1, ax2, ax3) = plt.subplots(3)
fig.suptitle('Position vs time plot for three schenarios',fontsize=16,fontweight='bold')

ax1.set_title('x0 = 1m',fontsize=14,fontweight='bold')
ax1.plot(time,coordinate1)

ax2.set_title('x0 = xc',fontsize=14,fontweight='bold')
ax2.plot(time,coordinate2)

ax3.set_title('x0 = 10xc',fontsize=14,fontweight='bold')
ax3.plot(time,coordinate3)

fig.tight_layout()
ax2.set_ylabel('Position (m)',fontsize=14,fontweight='bold')
ax3.set_xlabel('Time (s)',fontsize=14,fontweight='bold')
ax1.grid()
ax2.grid()
ax3.grid()


#plot the position vs time plot for the three scehnarios:
#position vs time plot when x = 1

plt.figure()
plt.plot(time,coordinate1)
plt.title('Position vs time plot for x0 = 0',fontsize=16,fontweight='bold')
plt.xlabel('Time (s)',fontsize=14,fontweight='bold')
plt.ylabel('Position (m)',fontsize=14,fontweight='bold')
plt.grid()

#position vs time plot when x = xc
plt.figure()
plt.plot(time,coordinate2)
plt.title('Position vs time plot for x0 = xc',fontsize=16,fontweight='bold')
plt.xlabel('Time (s)',fontsize=14,fontweight='bold')
plt.ylabel('Position (m)',fontsize=14,fontweight='bold')
plt.grid()

#position vs time plot when x = 10xc
plt.figure()
plt.plot(time,coordinate3)
plt.title('Position vs time plot for x0 = 10xc',fontsize=16,fontweight='bold')
plt.xlabel('Time (s)',fontsize=14,fontweight='bold')
plt.ylabel('Position (m)',fontsize=14,fontweight='bold')
plt.grid()

#############################################################################
#this part finds the scaled amplitudes + plots the FFT + compare with Lab03 results

#obtains the FFT values of the three schenarios and scale the amplitudes of the FFT
#divides the FFT values by the max value of that particular FFT (for that initial condition)
FFT_x1 = abs(np.fft.rfft(coordinate1))/max(abs(np.fft.rfft(coordinate1)))
FFT_xc = abs(np.fft.rfft(coordinate2))/max(abs(np.fft.rfft(coordinate2)))
FFT_10xc = abs(np.fft.rfft(coordinate3))/max(abs(np.fft.rfft(coordinate3)))

#plots the scaled FFT and the results from lab 3 
plt.figure()
plt.plot(FFT_x1,label ='x0 = 1m')
plt.plot(FFT_xc,label ='x0 = xc')
plt.plot(FFT_10xc,label ='x0 = 10xc')
plt.xlim(0,150)
plt.title('FFT plot for all three values of x0',fontsize=16,fontweight='bold')
plt.xlabel('Angular frequency (f)',fontsize=14,fontweight='bold')
plt.ylabel('Scaled FFT amplitude\n (magnitude)',fontsize=14,fontweight='bold')

#these values are from lab03
plt.axvline(82.70257566438434,linestyle = '--',color = "b",label = 'Lab3 1m')
plt.axvline(70.40438814262373,linestyle = '--',color = "orange",label = 'Lab3 xc')
plt.axvline(12.859683770962501,linestyle = '--',color = "green",label = 'Lab3 10 xc')

plt.legend()
plt.grid()

###########################################################################

#code from Lab3 that calculates the expected period

#Define values and constants
kspring = 12 #N/m
mass = 1 #kg
N1 = 8 #sample points
N2 = 10000 #sample points
c = 3e8 #m/s - speed of light
xc = np.sqrt(c**2/kspring)
x_0 = 1 #initial displacement
a = 0 #m lower limit
b = x_0 #m upper limit same as x_0

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
    period = 4*s #calcualtes the period
    return period #returns the calculated period, integrand, sample points, and the weighted values


""" *******************important*********************
#to convert our period we need to first to divide 1 by the period: 1/T
#Next we need to multiply/scale up our calculated frequencies by 150 so that it agrees with the x-axis of the fft
#we multiply by 150 as it is our (number_of_samples*timestep)

#I got this info from pg 10 in https://faraday.physics.utoronto.ca/PVB/Harrison/FourierTransform.pdf
#To get the period from the location of the peak on the FFT: 
#we know that period = (2*pi)/(angular freqency)
#from the above source angular frequncy = ((location_of_the_peak)*((2pi)/(number_of_samples*timestep))
#therefore period = (2*pi)/((location_of_the_peak)*((2pi)/(number_of_samples*timestep))
#which simplifies to period = (number_of_samples*timestep)/(location_of_the_peak)
#which also means (location_of_the_peak) = (number_of_samples*timestep)/period
"""

#using: (location_of_the_peak) = (number_of_samples*timestep)/period we plot vertical lines at these points
period = (Gauss(N2,a,b,1,kspring,mass))
print("lab 3 period: x0 = 1:",period)
print("lab 3 frequency: x0 = 1:",150/period)
period = (Gauss(N2,a,xc,xc,kspring,mass))
print("lab 3 period: x0 = xc:",period)
print("lab 3 frequency: x0 = xc:",150/period)
period = (Gauss(N2,a,10*xc,10*xc,kspring,mass))
print("lab 3 period: x0 = 10xc:",period)
print("lab 3 frequency: x0 = 10xc:",150/period)

print(np.argmax(FFT_10xc))








