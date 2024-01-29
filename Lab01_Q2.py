#Lab01_Q2 code
#coded using spyder from anaconda

#Authors: Augustine Tai and Habiba Zaghloul
#Shared effort in coding
#This code answers Q2, producing two planetary bodie's orbit (Earth or asteroid and Jupiter)
#By changing the initial conditions you can change the charactersitics of the planetary body in the code
#most of the code is exactly the same as Q1c), exceot Jupiter was added to the system

#import the needed libraries
import numpy as np
import matplotlib.pyplot as plt

#Defining given constants, initial conditions, and time step parameters:
Ms = 1 #I defined Ms in terms of 2e30kg (2*10**30kg) as 1 unit, as Jupiter's mass uses units of sun masses
#otherwise i need a smaller dt to capture the elliptical shape
G = 39.5 #gravitational constant (G) with units (AU**3)(Ms**-1)(yr**-2)
Mj = 1e-3  #1e-3 is Jupiter's original mass, change this to 1 for 1000x its size

#initial conditions for Earth:  #1 major change in this code is that i set initial conidtions earlier, not directly inserting them at this point so i can play around with the initial conditions
x_einit = 1 #3.3 for asteroid #AU 
y_einit = 0 #AU
vx_einit = 0 #AU/year
vy_einit = 6.18 #AU/year #3.46 for asteroid

#initial conditions for Jupiteer
x_jinit = 5.2 #AU
y_jinit = 0 #AU
vx_jinit = 0 #AU/year
vy_jinit = 2.63 #AU/year

time = 10 #20 for asteroid, change this to set the duration of the orbit according to the question
dt = 0.0001 #time step size
t = np.arange(0,time,dt) #used when graphing later
num=len(t) #used for how long the loop should go on for
#print(num)

#make empty arrays for storage during loop for integration (for Earth)
x_e = np.empty(num) #x-position
y_e = np.empty(num) #y-position
r_e = np.empty(num) #radial length
vx_e = np.empty(num) #x-velocity
vy_e = np.empty(num) #y-velocity

#make empty arrays for storage during loop for integration (for Jupiter)
x_j = np.empty(num) #x-position
y_j = np.empty(num) #y-position
r_j = np.empty(num) #radial length
vx_j = np.empty(num) #x-velocity
vy_j = np.empty(num) #y-velocity
r_ej = np.empty(num) #radial distance between Earth/asteroid and jupiter

#Placing initial conditions into empty array + integration loop using the Euler-Cromer method
#Earth's initial conditions
x_e[0] = x_einit
y_e[0] = y_einit
r_e[0] = np.sqrt((x_einit)**2+(y_einit)**2)
vx_e[0] = vx_einit
vy_e[0] = vy_einit

#Jupiter's initial conditions, place this into the empty arrays created above
x_j[0] = x_jinit
y_j[0] = y_jinit
r_j[0] = np.sqrt((x_jinit)**2+(y_jinit)**2)
vx_j[0] = vx_jinit
vy_j[0] = vy_jinit
r_ej[0] = np.sqrt((x_jinit-x_einit)**2+(y_jinit-y_einit)**2) #radial distance between Earth/asteroid and Jupiter

for i in range(num-1):#using a loop updates the new positional values of the planet to be used in the next iteration of the loop
    #separated radial length, velocity components, and positions for clarity, still the same loop
    r_e[i+1] = np.sqrt(x_e[i]**2+y_e[i]**2) #radial distance between Earth/asteroid and Sun
    r_j[i+1] = np.sqrt(x_j[i]**2+y_j[i]**2) #radial distance between Jupiter and Sun
    r_ej[i+1] = np.sqrt((x_j[i]-x_e[i])**2+(y_j[i]-y_e[i])**2) #added this to calculate the radial distance between Earth/asteroid and Jupiter
    
    vx_e[i+1] = vx_e[i]-(((G*Ms*x_e[i])/(r_e[i])**3)*dt - ((G*Mj*x_e[i])/(r_ej[i])**3)*dt) #-((G*Mj*x_e[i])/(r_ej[i])**3)*dt) is Jupiter's affect on Earth/asteroid
    vy_e[i+1] = vy_e[i]-(((G*Ms*y_e[i])/(r_e[i])**3)*dt - ((G*Mj*y_e[i])/(r_ej[i])**3)*dt) #-((G*Mj*y_e[i])/(r_ej[i])**3)*dt) is Jupiter's affect on Earth/asteroid
    vx_j[i+1] = vx_j[i]-((G*Ms*x_j[i]*dt)/(r_j[i])**3)
    vy_j[i+1] = vy_j[i]-((G*Ms*y_j[i]*dt)/(r_j[i])**3)
    
    x_e[i+1] = x_e[i]+vx_e[i+1]*dt
    y_e[i+1] = y_e[i]+vy_e[i+1]*dt
    x_j[i+1] = x_j[i]+vx_j[i+1]*dt
    y_j[i+1] = y_j[i]+vy_j[i+1]*dt
         
#Plots x-coords vs y-coords plot
plt.figure()
plt.plot(x_e,y_e,label='Earth')
plt.plot(x_j,y_j,label='Jupiter')

#use these plt.xlim and plt.ylim to zoom in on the asteroid/Earth
plt.title('2D Orbital position of Earth and Jupiter\nfor 10 Earth years',fontsize=16,fontweight='bold') #change title for each part of the question
plt.xlabel('x-position (AU)',fontsize=14,fontweight='bold')
plt.ylabel('y-position (AU)',fontsize=14,fontweight='bold')
plt.grid() #grid for visual effect
plt.legend(bbox_to_anchor=(1,1),prop={'size':14}) #need legend to show which orbital path is which planets

##########################################################################################
    
#This part of the code deals with a 1000x sized Jupiter

Mj = 1  #1e-3 is Jupiter's original mass, change this to 1 for 1000x its size

#initial conditions for Earth (change values for the astroid)
x_einit = 1 #3.3 for asteroid #AU 
y_einit = 0 #AU
vx_einit = 0 #AU/year
vy_einit = 6.18 #AU/year #3.46 for asteroid

#initial conditions for Jupiteer
x_jinit = 5.2 #AU
y_jinit = 0 #AU
vx_jinit = 0 #AU/year
vy_jinit = 2.63 #AU/year

time = 3 #3 years 
dt = 0.0001 #time step size
t = np.arange(0,time,dt) #used when graphing later
num=len(t) #used for how long the loop should go on for
#print(num)

#make empty arrays for storage during loop for integration (for Earth)
x_e = np.empty(num) #x-position
y_e = np.empty(num) #y-position
r_e = np.empty(num) #radial length
vx_e = np.empty(num) #x-velocity
vy_e = np.empty(num) #y-velocity

#make empty arrays for storage during loop for integration (for Jupiter)
x_j = np.empty(num) #x-position
y_j = np.empty(num) #y-position
r_j = np.empty(num) #radial length
vx_j = np.empty(num) #x-velocity
vy_j = np.empty(num) #y-velocity
r_ej = np.empty(num) #radial distance between Earth/asteroid and jupiter

#Placing initial conditions into empty array + integration loop using the Euler-Cromer method
#Earth's initial conditions
x_e[0] = x_einit
y_e[0] = y_einit
r_e[0] = np.sqrt((x_einit)**2+(y_einit)**2)
vx_e[0] = vx_einit
vy_e[0] = vy_einit

#Jupiter's initial conditions, place this into the empty arrays created above
x_j[0] = x_jinit
y_j[0] = y_jinit
r_j[0] = np.sqrt((x_jinit)**2+(y_jinit)**2)
vx_j[0] = vx_jinit
vy_j[0] = vy_jinit
r_ej[0] = np.sqrt((x_jinit-x_einit)**2+(y_jinit-y_einit)**2) #radial distance between Earth/asteroid and Jupiter

for i in range(num-1):#using a loop updates the new positional values of the planet to be used in the next iteration of the loop
    #separated radial length, velocity components, and positions for clarity, still the same loop
    r_e[i+1] = np.sqrt(x_e[i]**2+y_e[i]**2) #radial distance between Earth/asteroid and Sun
    r_j[i+1] = np.sqrt(x_j[i]**2+y_j[i]**2) #radial distance between Jupiter and Sun
    r_ej[i+1] = np.sqrt((x_j[i]-x_e[i])**2+(y_j[i]-y_e[i])**2) #added this to calculate the radial distance between Earth/asteroid and Jupiter
    
    vx_e[i+1] = vx_e[i]-(((G*Ms*x_e[i])/(r_e[i])**3)*dt - ((G*Mj*x_e[i])/(r_ej[i])**3)*dt) #-((G*Mj*x_e[i])/(r_ej[i])**3)*dt) is Jupiter's affect on Earth/asteroid
    vy_e[i+1] = vy_e[i]-(((G*Ms*y_e[i])/(r_e[i])**3)*dt - ((G*Mj*y_e[i])/(r_ej[i])**3)*dt) #-((G*Mj*y_e[i])/(r_ej[i])**3)*dt) is Jupiter's affect on Earth/asteroid
    vx_j[i+1] = vx_j[i]-((G*Ms*x_j[i]*dt)/(r_j[i])**3)
    vy_j[i+1] = vy_j[i]-((G*Ms*y_j[i]*dt)/(r_j[i])**3)
    
    x_e[i+1] = x_e[i]+vx_e[i+1]*dt
    y_e[i+1] = y_e[i]+vy_e[i+1]*dt
    x_j[i+1] = x_j[i]+vx_j[i+1]*dt
    y_j[i+1] = y_j[i]+vy_j[i+1]*dt
         
#Plots x-coords vs y-coords plot
plt.figure()
plt.plot(x_e,y_e,label='Earth')
plt.plot(x_j,y_j,label='Jupiter')

#use these plt.xlim and plt.ylim to zoom in on the asteroid/Earth
#plt.xlim(-1.1,1.1) 
#plt.ylim(-1.1,1.1)
plt.title('2D Orbital position of Earth and \nJupiter (1000x size) for three years',fontsize=16,fontweight='bold') #change title for each part of the question
plt.xlabel('x-position (AU)',fontsize=14,fontweight='bold')
plt.ylabel('y-position (AU)',fontsize=14,fontweight='bold')
plt.grid() #grid for visual effect
plt.legend(bbox_to_anchor=(1,1),prop={'size':14}) #need legend to show which orbital path is which planets
    
#Plots x-coords vs y-coords plot (zoomed in)
plt.figure()
plt.plot(x_e,y_e,label='Earth')
plt.plot(x_j,y_j,label='Jupiter')
plt.xlim(-1.1,1.1) 
plt.ylim(-1.1,1.1)
plt.title('2D Orbital position of Earth with a  \n1000x sized Jupiter for three years',fontsize=16,fontweight='bold') #change title for each part of the question
plt.xlabel('x-position (AU)',fontsize=14,fontweight='bold')
plt.ylabel('y-position (AU)',fontsize=14,fontweight='bold')
plt.grid() #grid for visual effect
plt.legend(bbox_to_anchor=(1,1),prop={'size':14}) #need legend to show which orbital path is which planets
    
##########################################################################################
    
#This part of the code deals with a 1000x sized Jupiter for a longer time (20 years)

Mj = 1  #1e-3 is Jupiter's original mass, change this to 1 for 1000x its size

#initial conditions for Earth (change values for the astroid)
x_einit = 1 #3.3 for asteroid #AU 
y_einit = 0 #AU
vx_einit = 0 #AU/year
vy_einit = 6.18 #AU/year #3.46 for asteroid

#initial conditions for Jupiteer
x_jinit = 5.2 #AU
y_jinit = 0 #AU
vx_jinit = 0 #AU/year
vy_jinit = 2.63 #AU/year

time = 10 #10 years 
dt = 0.0001 #time step size
t = np.arange(0,time,dt) #used when graphing later
num=len(t) #used for how long the loop should go on for
#print(num)

#make empty arrays for storage during loop for integration (for Earth)
x_e = np.empty(num) #x-position
y_e = np.empty(num) #y-position
r_e = np.empty(num) #radial length
vx_e = np.empty(num) #x-velocity
vy_e = np.empty(num) #y-velocity

#make empty arrays for storage during loop for integration (for Jupiter)
x_j = np.empty(num) #x-position
y_j = np.empty(num) #y-position
r_j = np.empty(num) #radial length
vx_j = np.empty(num) #x-velocity
vy_j = np.empty(num) #y-velocity
r_ej = np.empty(num) #radial distance between Earth/asteroid and jupiter

#Placing initial conditions into empty array + integration loop using the Euler-Cromer method
#Earth's initial conditions
x_e[0] = x_einit
y_e[0] = y_einit
r_e[0] = np.sqrt((x_einit)**2+(y_einit)**2)
vx_e[0] = vx_einit
vy_e[0] = vy_einit

#Jupiter's initial conditions, place this into the empty arrays created above
x_j[0] = x_jinit
y_j[0] = y_jinit
r_j[0] = np.sqrt((x_jinit)**2+(y_jinit)**2)
vx_j[0] = vx_jinit
vy_j[0] = vy_jinit
r_ej[0] = np.sqrt((x_jinit-x_einit)**2+(y_jinit-y_einit)**2) #radial distance between Earth/asteroid and Jupiter

for i in range(num-1):#using a loop updates the new positional values of the planet to be used in the next iteration of the loop
    #separated radial length, velocity components, and positions for clarity, still the same loop
    r_e[i+1] = np.sqrt(x_e[i]**2+y_e[i]**2) #radial distance between Earth/asteroid and Sun
    r_j[i+1] = np.sqrt(x_j[i]**2+y_j[i]**2) #radial distance between Jupiter and Sun
    r_ej[i+1] = np.sqrt((x_j[i]-x_e[i])**2+(y_j[i]-y_e[i])**2) #added this to calculate the radial distance between Earth/asteroid and Jupiter
    
    vx_e[i+1] = vx_e[i]-(((G*Ms*x_e[i])/(r_e[i])**3)*dt - ((G*Mj*x_e[i])/(r_ej[i])**3)*dt) #-((G*Mj*x_e[i])/(r_ej[i])**3)*dt) is Jupiter's affect on Earth/asteroid
    vy_e[i+1] = vy_e[i]-(((G*Ms*y_e[i])/(r_e[i])**3)*dt - ((G*Mj*y_e[i])/(r_ej[i])**3)*dt) #-((G*Mj*y_e[i])/(r_ej[i])**3)*dt) is Jupiter's affect on Earth/asteroid
    vx_j[i+1] = vx_j[i]-((G*Ms*x_j[i]*dt)/(r_j[i])**3)
    vy_j[i+1] = vy_j[i]-((G*Ms*y_j[i]*dt)/(r_j[i])**3)
    
    x_e[i+1] = x_e[i]+vx_e[i+1]*dt
    y_e[i+1] = y_e[i]+vy_e[i+1]*dt
    x_j[i+1] = x_j[i]+vx_j[i+1]*dt
    y_j[i+1] = y_j[i]+vy_j[i+1]*dt
         
#Plots x-coords vs y-coords plot
plt.figure()
plt.plot(x_e,y_e,label='Earth')
plt.plot(x_j,y_j,label='Jupiter')

#use these plt.xlim and plt.ylim to zoom in on the asteroid/Earth
#plt.xlim(-1.1,1.1) 
#plt.ylim(-1.1,1.1)
plt.title('2D Orbital position of Earth and \nJupiter (1000x size) for 10 years',fontsize=16,fontweight='bold') #change title for each part of the question
plt.xlabel('x-position (AU)',fontsize=14,fontweight='bold')
plt.ylabel('y-position (AU)',fontsize=14,fontweight='bold')
plt.grid() #grid for visual effect
plt.legend(bbox_to_anchor=(1,1),prop={'size':14}) #need legend to show which orbital path is which planets
    
#Plots x-coords vs y-coords plot (zoomed in)
plt.figure()
plt.plot(x_e,y_e,label='Earth')
plt.plot(x_j,y_j,label='Jupiter')
plt.xlim(-1.1,1.1) 
plt.ylim(-1.1,1.1)
plt.title('2D Orbital position of Earth with a  \n1000x sized Jupiter for 10 years',fontsize=16,fontweight='bold') #change title for each part of the question
plt.xlabel('x-position (AU)',fontsize=14,fontweight='bold')
plt.ylabel('y-position (AU)',fontsize=14,fontweight='bold')
plt.grid() #grid for visual effect
plt.legend(bbox_to_anchor=(1,1),prop={'size':14}) #need legend to show which orbital path is which planets
    
###############################################################################

#This part of the code deals with a normal sized Jupiter but with an asteroid

Mj = 1e-3  #1e-3 is Jupiter's original mass

#initial conditions for Asteroid
x_einit = 3.3 #AU 
y_einit = 0 #AU
vx_einit = 0 #AU/year
vy_einit = 3.46 #AU/year 

#initial conditions for Jupiteer
x_jinit = 5.2 #AU
y_jinit = 0 #AU
vx_jinit = 0 #AU/year
vy_jinit = 2.63 #AU/year

time = 20 #20 years for asteroid
dt = 0.0001 #time step size
t = np.arange(0,time,dt) #used when graphing later
num=len(t) #used for how long the loop should go on for
#print(num)

#make empty arrays for storage during loop for integration (for Earth)
x_e = np.empty(num) #x-position
y_e = np.empty(num) #y-position
r_e = np.empty(num) #radial length
vx_e = np.empty(num) #x-velocity
vy_e = np.empty(num) #y-velocity

#make empty arrays for storage during loop for integration (for Jupiter)
x_j = np.empty(num) #x-position
y_j = np.empty(num) #y-position
r_j = np.empty(num) #radial length
vx_j = np.empty(num) #x-velocity
vy_j = np.empty(num) #y-velocity
r_ej = np.empty(num) #radial distance between Earth/asteroid and jupiter

#Placing initial conditions into empty array + integration loop using the Euler-Cromer method
#Earth's initial conditions
x_e[0] = x_einit
y_e[0] = y_einit
r_e[0] = np.sqrt((x_einit)**2+(y_einit)**2)
vx_e[0] = vx_einit
vy_e[0] = vy_einit

#Jupiter's initial conditions, place this into the empty arrays created above
x_j[0] = x_jinit
y_j[0] = y_jinit
r_j[0] = np.sqrt((x_jinit)**2+(y_jinit)**2)
vx_j[0] = vx_jinit
vy_j[0] = vy_jinit
r_ej[0] = np.sqrt((x_jinit-x_einit)**2+(y_jinit-y_einit)**2) #radial distance between Earth/asteroid and Jupiter

for i in range(num-1):#using a loop updates the new positional values of the planet to be used in the next iteration of the loop
    #separated radial length, velocity components, and positions for clarity, still the same loop
    r_e[i+1] = np.sqrt(x_e[i]**2+y_e[i]**2) #radial distance between Earth/asteroid and Sun
    r_j[i+1] = np.sqrt(x_j[i]**2+y_j[i]**2) #radial distance between Jupiter and Sun
    r_ej[i+1] = np.sqrt((x_j[i]-x_e[i])**2+(y_j[i]-y_e[i])**2) #added this to calculate the radial distance between Earth/asteroid and Jupiter
    
    vx_e[i+1] = vx_e[i]-(((G*Ms*x_e[i])/(r_e[i])**3)*dt - ((G*Mj*x_e[i])/(r_ej[i])**3)*dt) #-((G*Mj*x_e[i])/(r_ej[i])**3)*dt) is Jupiter's affect on Earth/asteroid
    vy_e[i+1] = vy_e[i]-(((G*Ms*y_e[i])/(r_e[i])**3)*dt - ((G*Mj*y_e[i])/(r_ej[i])**3)*dt) #-((G*Mj*y_e[i])/(r_ej[i])**3)*dt) is Jupiter's affect on Earth/asteroid
    vx_j[i+1] = vx_j[i]-((G*Ms*x_j[i]*dt)/(r_j[i])**3)
    vy_j[i+1] = vy_j[i]-((G*Ms*y_j[i]*dt)/(r_j[i])**3)
    
    x_e[i+1] = x_e[i]+vx_e[i+1]*dt
    y_e[i+1] = y_e[i]+vy_e[i+1]*dt
    x_j[i+1] = x_j[i]+vx_j[i+1]*dt
    y_j[i+1] = y_j[i]+vy_j[i+1]*dt
         
#Plots x-coords vs y-coords plot
plt.figure()
plt.plot(x_e,y_e,label='Earth')
plt.plot(x_j,y_j,label='Jupiter')

#use these plt.xlim and plt.ylim to zoom in on the asteroid/Earth
plt.title('2D Orbital position of an asteroid \nand Jupiter for 20 years',fontsize=16,fontweight='bold') #change title for each part of the question
plt.xlabel('x-position (AU)',fontsize=14,fontweight='bold')
plt.ylabel('y-position (AU)',fontsize=14,fontweight='bold')
plt.grid() #grid for visual effect
plt.legend(bbox_to_anchor=(1,1),prop={'size':14}) #need legend to show which orbital path is which planets
    
#Plots x-coords vs y-coords plot zoomed in
plt.figure()
plt.plot(x_e,y_e,label='Earth')
plt.plot(x_j,y_j,label='Jupiter')

#use these plt.xlim and plt.ylim to zoom in on the asteroid/Earth
plt.title('2D Orbital position of an asteroid \n(zoomed in) for 20 years',fontsize=16,fontweight='bold') #change title for each part of the question
plt.xlabel('x-position (AU)',fontsize=14,fontweight='bold')
plt.ylabel('y-position (AU)',fontsize=14,fontweight='bold')
plt.xlim(-3.5,3.5) 
plt.ylim(-3.5,3.5)
plt.grid() #grid for visual effect
plt.legend(bbox_to_anchor=(1,1),prop={'size':14}) #need legend to show which orbital path is which planets