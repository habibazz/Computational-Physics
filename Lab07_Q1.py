#Lab07_Q1 code
#coded using spyder from anaconda
#Authors: Augustine Tai + Habiba Zaghloul

#This code answers Lab7 Q1:
#a) plots the trajectory of the object using the adaptive step and normal step method
#b) outputs the time elapsed for both methods (adaptive and normal)
#c) outputs a plot of the adaptive step size vs time 

############################################################################

#import needed modules
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import time

#############################################################################

#This section was taken from the Newman_8-8.py file

def rhs(r):
    """ The right-hand-side of the equations
    INPUT:
    r = [x, vx, y, vy] are floats (not arrays)
    note: no explicit dependence on time
    OUTPUT:
    1x2 numpy array, rhs[0] is for x, rhs[1] is for vx, etc"""
    M = 10.
    L = 2.

    x = r[0]
    vx = r[1]
    y = r[2]
    vy = r[3]

    r2 = x**2 + y**2
    Fx, Fy = - M * np.array([x, y], float) / (r2 * np.sqrt(r2 + .25*L**2))
    return np.array([vx, Fx, vy, Fy], float)

# This next part adapted from Newman's odesim.py 
a = 0.0
b = 10.0
N = 10000  # let's leave it at that for now
h = (b-a)/N

tpoints = np.arange(a, b, h)
xpoints = []
vxpoints = []  # the future dx/dt
ypoints = []
vypoints = []  # the future dy/dt

#########################################################################

#Here is a modified RK4 function, original was from Newman_8-8.py file
#modifications is explained later

# below: ordering is x, dx/dt, y, dy/dt
r = np.array([1., 0., 0., 1.], float)
tpoints = np.arange(a, b, h)

def RK4mod(r,h):
    #removed loop explnantion below
    xpoints.append(r[0])
    vxpoints.append(r[1])
    ypoints.append(r[2])
    vypoints.append(r[3])
    k1 = h*rhs(r)  # all the k's are vectors
    k2 = h*rhs(r + 0.5*k1)  # note: no explicit dependence on time of the RHSs
    k3 = h*rhs(r + 0.5*k2)
    k4 = h*rhs(r + k3)
    values = r+(k1 + 2*k2 + 2*k3 + k4)/6 
    #here i changed it so that the RK4 section will produce values at each time step
    #originally this would just a loop through the values and append the values into storage for plotting
    #the original did store the values at each point and instead adds the next value to the previous value directly
    #i needed the values at each timestep so i had to modify it
    return (values)

#############################################################################

#Adaptive step integration into the RK4 method:

#Set some constants and storage for the adaptive method:
r0 = np.array([1., 0., 0., 1.], float) #set our initial condition
delta = 1e-6 #delta value according to lab handout

#time values:
time_storage = [] #storage for time values, used in plotting
time_storage = [0] #set initial value of time to 0 seconds
time_func = 0 #set our initial time in our adaptive step size loop to 0, ie we start at t=0 seconds
t_end = 10 #set our end time, which is 10 seconds

#step values:
hstep_value=[] #create storage for the adaptice step sizes
h = 0.01 #our starting step size accroding to lab handout 
hstep_value=[h] #set initial adaptive step size to h (above)

#storage for our x and y values for trajectory plot
xpoints2=[] #x coordinates
ypoints2=[] #y-coordinates

def adaptive_method(r0,h,time_func):
    #Use while to continue the loop from 0s until 10 seconds
    while time_func < 10:
        r_initial_estimate = RK4mod(r0,h) #we take only t+h (small) step, we take one additional small step below to reach t+2h
        r_initial_estimate1 = RK4mod(r_initial_estimate,h)# use our previous value to take another small step to reach t +2h
        
        r2_2hstepsize = RK4mod(r0,2*h) #we calculate t+2h by taking one big step (we took two small steps above)
        
        #calculate the error and rho
        error_x = (1/30)*(r_initial_estimate1[0]-r2_2hstepsize[0]) #calculate the error in x-component
        error_y = (1/30)*(r_initial_estimate1[2]-r2_2hstepsize[2]) #calculate the error in y-component
        #note that the index number 2 corresponds to y-component
        rho = (h*delta)/(np.sqrt(error_x**2+error_y**2)) #calculate rho, equation (4)
        
        if rho >= 1: #when we reach our desired accuracy we keep results and move on to the next t+2h calculations 
        #we update our time by adding to our time_func by adding 2*h steps
        #we also make our steps size bigger so we don't waste time/step sizes, making the calculation quicker
            time_func = time_func + 2*h #adds the step we took to our time for plotting (advance our time)
            time_storage.append(time_func) #store our time values for plotting
            r0 = r_initial_estimate1 #update our positions
            h = h*rho**(1/4) #here we adjust our step sizes based on rho
            hstep_value.append(h) #store our adpative step sizes for plotting
            xpoints2.append(r_initial_estimate1[0]) #outputs our x-coordinates for plotting
            ypoints2.append(r_initial_estimate1[2]) #outputs our y-coordinates for plotting
        
        else: #if we did not reach our desired accuracy we go through the loop again 
            h = h*rho**(1/4) 
            #we alter our step size so it gets smaller and hopefully we reach our desired accuracy next time
            # and satsify our rho > 1 conditions
            
####################################################################
#used time.time() to time how long it takes for the adaptive method to run
#calls the functionso that the values can be used for plotting later

time_start = time.time() #time starting time
adaptive_method(r0,h,time_func)
end_time = time.time() #time the ending time
time_elapsed = end_time-time_start #calculate time elapsed

print('time elasped for adaptive step:',time_elapsed) #prints the elapsed time

###############################################################################

#here the same R4 method from Newman is performed for timing and plotting purposes
a = 0.0
b = 10.0
N = 10000  #we adjust value so that our h is 0.001 according to lab handout
h = (b-a)/N
#print(h)

"""directly taken from Newman 8-8.py code:"""

r = np.array([1., 0., 0., 1.], float)
timestart1 = time.time() #time starting time
for t in tpoints:
    xpoints.append(r[0])
    vxpoints.append(r[1])
    ypoints.append(r[2])
    vypoints.append(r[3])
    k1 = h*rhs(r)  # all the k's are vectors
    k2 = h*rhs(r + 0.5*k1)  # note: no explicit dependence on time of the RHSs
    k3 = h*rhs(r + 0.5*k2)
    k4 = h*rhs(r + k3)
    r += (k1 + 2*k2 + 2*k3 + k4)/6
timeend1 = time.time() #time ending time
time_elapsed1 = timeend1-timestart1 #calculate time elapsed
print('time elasped for normal:',time_elapsed1) #prints the elapsed time

##############################################################################

#plotting the trajectory plots from both the adaptive method and normal RK4 method

plt.figure()
plt.scatter(xpoints, ypoints,label='regular step') #plots our normal RK4 method
plt.plot(xpoints2,ypoints2,'.',color='tab:orange',label='adaptive step') #plots our adaptive method
plt.xlabel('x-coordinates',fontsize=14,fontweight='bold')
plt.ylabel('y-coordinates',fontsize=14,fontweight='bold')
plt.title('Trajectory of a ball bearing \naround a space rod',fontsize=16,fontweight='bold')
plt.legend(fontsize = 12,bbox_to_anchor=(1,1))
plt.axis('equal') #make axis equal from Newman_8-8.py
plt.grid()


#############################################################################

#plotting the adpative stepsize vs time plots

plt.figure()
plt.plot(time_storage,hstep_value) #take values from the storage we defined before for the adaptive step size method
plt.xlabel('time (s)',fontsize=14,fontweight='bold')
plt.ylabel('adaptive step size (s)',fontsize=14,fontweight='bold')
plt.title('Adaptive step size vs time plot',fontsize=16,fontweight='bold')
plt.grid()


print(len(time_storage))






