#import the needed libraries
import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import rfft
from numpy import loadtxt
from matplotlib.pyplot import contourf, xlabel, ylabel, title, colorbar
#these imports came from the lab handout


###############################################################################
#This part of the code is from the lab handout + plots SLP contour plot for all waves
SLP = loadtxt('SLP.txt')
Longitude = loadtxt('lon.txt')
Times = loadtxt('times.txt')

plt.figure()
plt.contourf(Longitude, Times, SLP)
plt.xlabel('longitude(degrees)',fontsize=14,fontweight='bold')
plt.ylabel('days since Jan. 1 2015',fontsize=14,fontweight='bold')
plt.title('SLP anomaly (hPa)',fontsize=16,fontweight='bold')
plt.colorbar()
#####################################################################
#these are prints that i used to check the dimensions they are reasonable"

#print(SLP.shape)
#(120, 144) this is its dimensions
#print(len(SLP))

#print(len(Times))
#120 in length

##############################################################
# This part deals with Lab 5 Q3 a)

#take the fft of SLP data using np.fft.rfft to get coefficeints note that 
SLP_rfft = np.fft.rfft(SLP)
print(SLP_rfft.shape)
print(len(SLP_rfft[0])) #checking dimensions/lengths

storage_SLP = np.zeros(SLP_rfft.shape,dtype = "complex_") #need to set this array as complex or the imaginary parts will be gone later on
#print(storage_SLP.shape) #checking dimensions

for i in range(len(SLP_rfft)): #use For loop to loop through the rows in SLP_rfft
    storage_SLP[i][3] = SLP_rfft[i][3] #place the values into np.zeros storage when j==3 into the storage
    #because we used np.zeros as the storage array, all wavenumber values are set to 0 (other than m=3)
    #also note that in this part if we didn't set storage_SLP array to dtype = "complex_", the imaginary parts would be discarded
    #we need the imaginary parts when we reverse-FFT the storage_SLP


#inverse/reverse FFT our storage storage_SLP using np.fft.irfft to get component of SLP corresponding to Fourier wavenumber m = 3
SLP_3 = (np.fft.irfft(storage_SLP))

#plots the contour plots for m = 3
plt.figure()
plt.contourf(Longitude, Times, SLP_3)
plt.xlabel('longitude(degrees)',fontsize=14,fontweight='bold')
plt.ylabel('days since Jan. 1 2015',fontsize=14,fontweight='bold')
plt.title('SLP anomaly (hPa), m = 3',fontsize=16,fontweight='bold')
plt.colorbar()


#############################################################################
#This following code does the same thing as above, except we changed m = 3 to m = 5

#take the fft of SLP data using np.fft.rfft
SLP_rfft = np.fft.rfft(SLP)
print(SLP_rfft.shape)
print(len(SLP_rfft[0])) #checking dimensions/lengths

storage_SLP = np.zeros(SLP_rfft.shape,dtype = "complex_")
#print(storage_SLP.shape)

for i in range(len(SLP_rfft)): #use For loop to loop through the rows in SLP_rfft
    storage_SLP[i][5] = SLP_rfft[i][5] #place the values into np.zeros storage when j==5 into the storage
    #because we used np.zeros as the storage array, all wavenumber values are set to 0 (other than m=3)
    #also note that in this part if we didn't set storage_SLP array to dtype = "complex_", the imaginary parts would be discarded
    #we need the imaginary parts when we reverse-FFT the storage_SLP = 5
SLP_5 = (np.fft.irfft(storage_SLP))

#plots the contour plots for m = 5
plt.figure()
plt.contourf(Longitude, Times, SLP_5)
plt.xlabel('longitude(degrees)',fontsize=14,fontweight='bold')
plt.ylabel('days since Jan. 1 2015',fontsize=14,fontweight='bold')
plt.title('SLP anomaly (hPa), m = 5',fontsize=16,fontweight='bold')
plt.colorbar()




