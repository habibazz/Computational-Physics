# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 11:30:29 2022

@author: habib
"""

import numpy as np
from scipy.io.wavfile import read, write
from numpy import empty
import matplotlib.pyplot as plt

##q2b
#read in the file
sample, data = read('GraviteaTime.wav')
#split data into 2 channels
channel_0 = data[:, 0]
channel_1 = data[:, 1]
N_Points = len(channel_0)

#find period (1/frequency)
dt = 1/sample
T = N_Points*dt
#find the angular frequency
N_points = np.arange(N_Points/2+1)*2*np.pi/T
#create an array to be used to pplot the time
t = np.arange(N_Points)*dt
#divide by frequency because period=1/f and we must account for this sampling rate


plt.figure()
plt.plot(t,channel_0, color = 'turquoise')
plt.xlabel('Time (s)')
plt.title('Channel 0')
plt.figure()
plt.plot(t,channel_1, color = 'teal')
plt.xlabel('Time (s)')
plt.title('Channel 1')

##2d
#compute fourier transform for each channel
transform_original_0 = np.fft.rfft(channel_0)
transform_original_1 = np.fft.rfft(channel_1)

transform_0 = np.fft.rfft(channel_0)
transform_1 = np.fft.rfft(channel_1)
#find the frequencies using rfftfreq
freq0 = np.fft.rfftfreq(N_Points,d=1/sample)
freq1 = np.fft.rfftfreq(N_Points,d=1/sample)
#print(freq0)
#print(freq1)
#set frequencies greater than 880 to 0

print(len(freq1))
for i in range(len(freq1)):
    if freq0[i] > 880:
        transform_0[i] = 0
    if freq1[i] > 880:
        transform_1[i] = 0

#transforming back to the time domain

channel_0_filt = np.fft.irfft(transform_0, N_Points)
channel_1_filt = np.fft.irfft(transform_1, N_Points)
#plot timeseries for both channels and the filtered channels
plt.figure()
plt.plot(t,channel_0, label = 'raw data')
plt.plot(t, channel_0_filt, label = 'filtered data', linewidth=2)
plt.legend()
plt.xlabel('time (s)')
plt.title('Channel 0 timeseries')
plt.xlim(0, 0.05)

plt.figure()
plt.plot(t,channel_1, label = 'raw data')
plt.plot(t, channel_1_filt, label = 'filtered data', linewidth=2)
plt.legend()
plt.xlabel('time (s)')
plt.title('Channel 1 timeseries')
plt.xlim(0, 0.05)
#plot the frequencies vs transformations
plt.figure()
plt.plot(abs(transform_original_0 ), label = 'raw data')
plt.plot(abs(transform_0), label = 'filtered frequencies')
plt.legend()
plt.xlabel('Frequency (Hz)')
plt.title('Amplitude for channel 0')


plt.figure()
plt.plot(abs(transform_original_1), label = 'raw data')
plt.plot(abs(transform_1), label = 'filtered frequencies')
plt.legend()
plt.xlabel('Frequency (Hz)')
plt.title('Amplitude for channel 1')


##Q2e
#print(data.shape)
data_out = np.empty(data.shape, dtype= np.int16())
# fill data_out
data_out[:,0] = channel_0_filt
data_out[:,1] = channel_1_filt

#print(channel_0_filt)



write('GraviteaTime_lpf.wav', sample, data_out)

print(abs(transform_1)-abs(transform_original_1))




