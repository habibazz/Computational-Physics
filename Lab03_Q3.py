#Lab03_Q2 code
#coded using spyder from anaconda
#Authors: Augustine Tai and Habiba Zaghloul

#import the needed librariees
import numpy as np
import matplotlib.pyplot as plt
from gaussxw import gaussxwab
from gaussxw import gaussxw
import math

#define hermite function, takes in x-values (range -4 to 4 for part a) and the energy levels (n)
def Hermite(x,n):
    if n==0 :#make condition for n = 0, polynomial = 1
        return 1
    elif n == 1:
        return 2*x #make condition for n = 1, polynomial = 2x
    else: #for all other values of n follow the expression below equation (9)
        for i in range(2,n+1):
                return 2*x*Hermite(x,n-1) - 2*(n-1)*Hermite(x,n-2)

#define a wavefunction which obtains the probability amplitude (psi) for each energy level
def Wave(x,n):#give x and the energy level for the function to compute
    wave=[] #set empty space for storage
    for i in range(len(x)): #loops the range of values (-4,4)
        a = (1/(np.sqrt(2**n*math.factorial(n)*np.sqrt(np.pi)))) #separated the equation into 2 parts (a and b) as i the equation is quite long
        b = np.exp(-x[i]**2/2) #separate the equation to avoid mistakes in the formula (happened alot)
        wave.append(a*b*Hermite(x[i],n)) #calculate the values and place into list
    return wave #outputs the values when function is called

x = np.linspace(-4,4, 100) #set the range of x-values , i chose the number of points in the range to = 100 
#by increasing the value of 100 to be larger generates more points + makes graph look smoother


#call the functions for different calus of n (0-3)
wave0 = (Wave(x,0))
wave1 = (Wave(x,1))
wave2 = (Wave(x,2))
wave3 = (Wave(x,3))

#plot the graph for Q3 a
plt.figure()
#plots all 4 energy levels
plt.scatter(x,wave0,label='n=0')
plt.scatter(x,wave1,label='n=1')
plt.scatter(x,wave2,label='n=2')
plt.scatter(x,wave3,label='n=3')
plt.title('Harmonic oscillator wavefunctions',fontsize = 16,fontweight='bold')
plt.xlabel('Position (x)',fontsize = 14,fontweight='bold')
plt.ylabel('Probability amplitude (psi)',fontsize = 14,fontweight='bold')
plt.grid()
plt.legend()

#####################################################################
#this part deals with Q3 b: plots the wave function for n=30 from a range of x-value (-10,10)
#For some reason it takes a while for the function to run (less than 2 minutes though)
#I suspect my hermite polynomial is quite inefficient for larger values of n
"""

#create the range of values for x, i chose number of points within range to be = 100
x2 = np.linspace(-10,10, 1000) 
#use the Wave() function defined before to obtaine the wave function for Q3 b
wave30 = (Wave(x2,30))

#plots the wave function for Q3 b
plt.figure()
plt.plot(x2, wave30, label = 'n=30')
plt.title('Harmonic oscillator wavefunction for n=3',fontsize = 16,fontweight='bold')
plt.xlabel('Position (x)',fontsize = 14,fontweight='bold')
plt.ylabel('Probability amplitude (psi)',fontsize = 14,fontweight='bold')
plt.grid()
plt.legend()
"""
#########################################################################
#From here on everything is for Q3 c, i further separate it based on waht it is calculation as this part is quite long

N = 100 #here the questions
a = -np.pi / 2        
b = np.pi / 2         

#create a modified Wave() function because we don't have a range of x values anymore
def Wave2(x,n):#we only change how we use/call for x, because of the change of variables
    wave2=[]#empty space for storage
    a = (1/(np.sqrt(2**n*math.factorial(n)*np.sqrt(np.pi)))) #here x use to be: x[i], we no longer have a list of values (range) so we use just x
    b = np.exp(-(x**2)/2)
    wave2 = a*b*Hermite(x,n) #caclualtes wavefunction
    return wave2 #returns the calculated values (used in integration - Gaussain quad)

#define a function that uses Gaussian quadrature to integrate the wave function (this code comes from eaxample 5.2 from textbook)
def Gauss(f,N,a,b,n): #this code is lifted from my code for Lab3 Q2 where i use the same method
    xp,wp = gaussxwab(N,a,b) 
    s = 0#create space to sum values
    for i in range(N):
        s += wp[i]*f(xp[i],n) #sums the individual units of the integral
    return s #return the final value of the integral


#define a function that calculates <x^2> (position)
def Pos(z,n): #here the change of variables z used in 5.8 from textbook
    position = ((np.tan(z)**2)*abs(((Wave2(np.tan(z),n))**2)/(np.cos(z)**2))) #change of variables: f(x)dx = f(tan(z))/cos^2(z)
    return position #outputs the calcualted <x^2> values


#outpute the <x^2> values for n = 0-15
x2 = [] #empty storage for the following loop
for n in range(0,16): #loops through vlaues n = 0-15
    x2.append(Gauss(Pos, N, a,b,n))
print("<x^2> value:",x2) #prints the <x^2> values

#########################################################################
#This part is also for Q3 c: deals with <p^2> and Energy

#define the function that takes the derivative of the wave function
def Derivative(x,n):#takes values x,n similar to Wave() function
    a = (1/(np.sqrt(2**n*math.factorial(n)*np.sqrt(np.pi)))) #separate into two parts like before
    b = np.exp(-(x**2)/2)
    if n > 0: #we have to make a condition because a problem with n=0 because of n-1 which would return a negative number.
        derivative = a*b*(-x*Hermite(x,n)+2*n*Hermite(x,n-1))#calculates the derivative normally using equation 11 
    else :
        derivative = a*b*(-x*Hermite(x,n))#here i omitted the Hermite(x,n-1), because n-1 would be negative number and i don't think a negative n value for the Hermite polynomial is valid
    #As a result, i set the (2*n*Hermite(x,n-1)) to 0 for n = 0 to avoid this error
    return derivative #returns the derivative 

#define a function that calcualtes the momentum <p^2>
def Mom(z,n):#takes value z (from the change of variables) and n to calulcate <p^2>
    momentum = abs((Derivative(np.tan(z), n))**2/(np.cos(z)**2)) #used change of vairables, same method in Pos() function
    return momentum #

#loops the values of <p^2> through n = 0-15 and sappends them for storage
p2 = [] #empty storage
for n in range(0,16):
    p2.append(Gauss(Mom, N, a,b,n))
print("<p^2> value:",p2) #prints <p^2> values

energy = [] #storage
for n in range(0,16): #loops thorugh n = 0-15 values for <x^2> and <p^2> to calcualte Energy
    energy.append(0.5*(x2[n]+p2[n])) #uses equation 14 to calculate energy
print("energy:",energy) #print the energy for n=0-15

############################################################################

#create a function to calculate the uncertainty when given <x^2> or <p^2> values
def Uncertainty(value):#root mean square of the values
    uncertainty=[]#storage
    for i in range(0,16):#loops through n=0-15
        uncertainty.append(np.sqrt(value[i])) #calcualtes uncertainty by taking the square root of <x^2> or <p^2> values
    return uncertainty

x2uncer = Uncertainty(x2)#store the uncertainty for <x^2> 
p2uncer = Uncertainty(p2)#store the uncertainty for <p^2> 

#prints the uncertainty values
print("uncertainty of <x^2>:",x2uncer)
print("uncertainty of <p^2>:",p2uncer)
#print(len(energy))

#Optional: plots <x^2> vs <p^2> to visualize relationship
plt.figure()
plt.scatter(x2uncer,p2uncer)
plt.plot(0.7071067811865476,0.7071067811865475,'ro') 
plt.xlabel('<x2> uncertainty',fontsize = 14,fontweight='bold')
plt.ylabel('<p2> uncertainty',fontsize = 14,fontweight='bold')
plt.title('Uncertainties in <x2> vs <p2>',fontsize = 14,fontweight='bold')
plt.grid()

########################################################################










