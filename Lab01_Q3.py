#Lab01_Q3 code
#coded using spyder from anaconda

#Authors: Augustine Tai and Habiba Zaghloul
#Shared effort in coding
#This code times the time needed for matrix multiplication using two methods
#The first method is from example 4.3 and the other uses numpy.dot
#returns two plots: matrix size vs time and matrix size cubed vs time

#import the needed libraries
import numpy as np
import matplotlib.pyplot as plt
import time #used to time the multiplication process

matrix_max = 300 #setting the max size of the matrixes, change this if you want the code to run longer
N = 2 #setting the min size of the matrixes
time1 = [] #empty array for storing the time needed for matrix multiplication

#This first loop multipliees matrix using the equation in example 4.3
for x in range(N,matrix_max+1):
    A = np.ones([x,x],float)*3. #create matrices of size N in each iteration, increasing in size each time, filled with 3's 
    B = np.ones([x,x],float)*3. #create matrices of size N in each iteration, increasing in size each time filled with 3's 
    C = np.zeros([x,x],float) #create matrices of size N in each iteration, increasing in size each time
    start_time = time.time() #times the start of the multiplication
    
    for i in range(x):#this snippit of code is from example 4.3, multiplies matrices A and B together
        for j in range(x):
            for k in range(x):
                C[i,j] += A[i,k]*B[k,j]
    
    end_time = time.time() #times the end of the multiplication
    time1.append(end_time-start_time) #subtracts end time with start time to find the time elapsed and places into the empty array created
    print(time1) #just to check whether the code is running or not

#print(time1)

##############################################################################
#np.dot method of matrix multiplication
time2 = [] #empty array for storing time elasped for the np.dot method

for y in range(N,matrix_max+1):
    A_2 = np.ones([y,y],float)*3. #create matrices of size N in each iteration, increasing in size each time, filled with 3's 
    B_2 = np.ones([y,y],float)*3. #create matrices of size N in each iteration, increasing in size each time, filled with 3's 
    C_2 = np.zeros([y,y],float) #create matrices of size N in each iteration, increasing in size each time
    start_time2 = time.time() #times the start of the multiplication
    C_2 = np.dot(A_2,B_2) #multplies matrices A and B using np.dot
    
    end_time2 = time.time() #times the end of the multiplication
    time2.append(end_time2-start_time2)  #subtracts end time with start time to find the time elapsed and places into the empty array created
    
#Plotting N vs time elapsed
plt.figure()
plt.scatter(range(N,matrix_max+1), time1, color = 'b', label = "normal method (slow)") #plots time elasped for multiplication using example 4.3 method
plt.scatter(range(N,matrix_max+1), time2, color = 'r', label = "numpy dot method") #plots time elasped for multiplication using np.dot
plt.title('Time needed for matrix multiplication vs matrix size',fontsize=16,fontweight='bold')
plt.xlabel('Matrix size (N)',fontsize=14,fontweight='bold')
plt.ylabel('Time elasped (s)',fontsize=14,fontweight='bold')
plt.grid() #visual
plt.legend() #legend for both datasets

#Plotting N vs time elapsed
N3=[] #make an empty array to store N^3
for x in range(N,matrix_max+1): 
    N3.append(x**3) #cubes N and places it in the empty array
    
#same plotting as befor except N is cubed
plt.figure()
plt.scatter(N3, time1, color = 'b', label = "normal method (slow)") 
plt.scatter(N3, time2, color = 'r', label = "numpy dot method")
plt.title('Time needed for matrix multiplication vs matrix size (cubed)',fontsize=16,fontweight='bold')
plt.xlabel('Matrix size (N^3)',fontsize=14,fontweight='bold')
plt.ylabel('Time elasped (s)',fontsize=14,fontweight='bold')
plt.grid()
plt.legend()  

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    