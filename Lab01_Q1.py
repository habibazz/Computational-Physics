#Lab01_Q1 code
#coded using spyder from anaconda

#Authors: Augustine Tai and Habiba Zaghloul
#Augustine Tai note: Just for transparency, I took classical mechanics and created something similar to this before 
#Shared effort in coding
#This code answers Q1 and outputs Mercury's x vs y position plots, x and y velocity vs time plot, angular momentum magnitude vs time plot, and Mercury;s orbit using general relativity
#when i say eq i am referting to the equations in the lab handout

#import the needed libraries
import numpy as np
import matplotlib.pyplot as plt

#Defining given constants, initial conditions, and time step parameters:
    
#Constants
Ms = 1 #I defined Ms in terms of 2e30kg (2*10**30kg) as 1 unit, 
#otherwise i need a smaller dt to capture the elliptical shape
G = 39.5 #gravitational constant (G) with units (AU**3)(Ms**-1)(yr**-2)


#Time step arrays and step paramters
time = 1 #1 yearr duration
dt = 0.0001 #time step size

t = np.arange(0,time,dt) #used when graphing later
num=len(t) #used when graphing later for range() to determine how many loops are needed
#print(num) # checks whethern the number of steps are correct

#make empty arrays for storage during loop
x = np.empty(num) #x-position
y = np.empty(num) #y-position
r = np.empty(num) #radial length
vx = np.empty(num) #x-velocity
vy = np.empty(num) #y-velocity
L = np.empty(num) #angular momentum used in part c)

#Placing initial conditions into empty array directly + integration loop using the Euler-Cromer method
x[0] = 0.47 #AU
y[0] = 0 #AU
r[0] = np.sqrt((x[0])**2+(y[0])**2) # calulate first radial length based on initial conditions
vx[0] = 0 #AU/year
vy[0] = 8.17 #AU/year
L[0] = (x[0]*vy[0]-y[0]*vx[0]) #This isn't exactly momentum but rather the magnitude of the momentum
#Mass of Mercury is not given, but since mass is constant we can still see whether the angular momentum is conserved from its magnitude

for i in range(num-1):#using a loop updates the new positional values, radial length, and velocities of the planet to be used in the next iteration of the loop
    r[i+1] = np.sqrt(x[i]**2+y[i]**2) #caculates radial distance
    vx[i+1] = vx[i]-(((G*Ms*x[i])/(r[i])**3)*dt) #based on eq(6)
    vy[i+1] = vy[i]-(((G*Ms*y[i])/(r[i])**3)*dt)
    x[i+1] = x[i]+(vx[i+1]*dt)
    y[i+1] = y[i]+(vy[i+1]*dt)
    
    L[i+1] = (x[i+1]*vy[i+1]-y[i+1]*vx[i+1]) #calculates angular momentum based on current velocity and position, mass of planet is unknown so it isn't multiplied
    
#Each iteration of the loop stores the value in the empty arrays created in the beginning
# explanation of L: x and y components are multiplied by their opposite velocity components ie. cross product
# This works because they are orthogonal to each other, explained in the write-up

#plots x-velocity vs time plot
plt.figure()
plt.plot(t,vx)
plt.title('x-velocity vs time plot of Mercury',fontsize=16,fontweight='bold') #fontsize makes font larger and fontweight bolds the words for clarity
plt.xlabel('t (years)',fontsize=14,fontweight='bold')
plt.ylabel('x-velocity (AU/year)',fontsize=14,fontweight='bold')
plt.grid() #places grids on the plot nothing special

#plots y-velocity vs time plot #basically the same code as above
plt.figure()
plt.plot(t,vy)
plt.title('y-velocity vs time plotof Mercury',fontsize=16,fontweight='bold')
plt.xlabel('t (years)',fontsize=14,fontweight='bold')
plt.ylabel('y-velocity (AU/year)',fontsize=13,fontweight='bold')
plt.grid()

#plots x-coords vs y-coords plot
plt.figure()
plt.plot(x,y)
plt.title('2D Orbital position of Mercury (x and y position)',fontsize=16,fontweight='bold')
plt.xlabel('x-position (AU)',fontsize=14,fontweight='bold')
plt.ylabel('y-position (AU)',fontsize=14,fontweight='bold')
plt.grid()

#plots Angular momentum vs time
plt.figure()
plt.plot(t, L,linewidth=3)
plt.title('Angular Momentum (magnitude) vs. Time',fontsize=16,fontweight='bold')
plt.xlabel('Time(yr)',fontsize=14,fontweight='bold')
plt.ylabel('Angular momentum \nmagnitude (AU^2/year)',fontsize=14,fontweight='bold')
plt.grid()
plt.ylim(-2, 5)
plt.axhline(y=0, color='black',linestyle='-',linewidth=1)

##############################################################################
#This part of the code uses the general relativity form given in eq (7) from the handout
#most of the code is exactly the same except during the loop eq (7) is used/added
 
#Add a new constant (alpha)
alpha = 0.01 #AU**2
Mp=1 #mass of the planet is unknwon, this value is used as a place holder
#but since the mass of the planet remains constant the resulting graph should still be similar bu multiplied by some scalar factor
#Similar to why equation(6) does not include the mass of the planet eventhough Mp is present in equation(5)

#Create separate new arrays for the new loop
x_new = np.zeros(num)
y_new = np.zeros(num)
r_new = np.zeros(num)
vx_new = np.zeros(num)
vy_new = np.zeros(num)

#Placing initial conditions into new empty array (same as before)
x_new[0] = 0.47 #AU
y_new[0] = 0 #AU
r_new[0] = np.sqrt((x[0])**2+(y[0])**2)
vx_new[0] = 0 #AU/year
vy_new[0] = 8.17 #AU/year

#New integration loop using the Euler-Cromer method
for i in range(num-1):
    r_new[i+1] = np.sqrt(x_new[i]**2 + y_new[i]**2)
    vx_new[i+1] = vx_new[i]-(((G*Ms*Mp)/(r_new[i]**3))*(1+alpha/r_new[i]**2)*x_new[i]*dt) #eq(7) is introduced here
    vy_new[i+1] = vy_new[i]-(((G*Ms*Mp)/(r_new[i]**3))*(1+alpha/r_new[i]**2)*y_new[i]*dt) #eq(7) is introduced here
    x_new[i+1] = x_new[i]+vx_new[i+1]*dt
    y_new[i+1] = y_new[i]+vy_new[i+1]*dt

#Plots x-velocity vs time plot
plt.figure()
plt.plot(t,vx_new)
plt.title('x-velocity vs time plot of Mercury',fontsize=14,fontweight='bold')
plt.xlabel('t (years)',fontsize=12,fontweight='bold')
plt.ylabel('x-velocity (AU/year)',fontsize=12,fontweight='bold')
plt.grid()

#Plots y-velocity vs time plot
plt.figure()
plt.plot(t,vy_new)
plt.title('y-velocity vs time plotof Mercury',fontsize=14,fontweight='bold')
plt.xlabel('t (years)',fontsize=12,fontweight='bold')
plt.ylabel('y-velocity (AU/year)',fontsize=12,fontweight='bold')
plt.grid()

#Plots x-coords vs y-coords plot
plt.figure()
plt.plot(x_new,y_new)
plt.title('2D Orbital position of Mercury using \norbital relativity (x and y position)',fontsize=14,fontweight='bold')
plt.xlabel('x-position (AU)',fontsize=12,fontweight='bold')
plt.ylabel('y-position (AU)',fontsize=12,fontweight='bold')
plt.grid()





