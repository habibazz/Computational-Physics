import numpy as np
from time import time
import matplotlib.pyplot as plt
from scipy import constants as con

# Ryan Cunningham and Habiba Zaghloul

# Question 1: Standard Deviation Calculations

# Import the data needed for this question
data = np.loadtxt('cdata.txt')


# Q1 Part b)

# Define a function that acts as Equation 1
def sd_1(x):
    mean = np.mean(x)
    n = len(x)
    count = 0
    for i in range(len(x - 1)):
        diff = (x[i] - mean) ** 2
        count = count + diff

    sig = np.sqrt((1 / (n - 1)) * count)
    return sig


# Define a function that acts as Equation 2
def sd_2(x):
    mean = np.mean(x)
    n = len(x)
    count = 0

    for i in range(len(x - 1)):
        diff = x[i] ** 2
        count = count + diff

    sig = np.sqrt((1 / (n - 1)) * (count - n * (mean) ** 2))
    return sig


# Define a function that calculates the relative error between two values
def rel_err(x, y):
    return (x - y) / y


rel_err_1 = rel_err(x=sd_1(data), y=np.std(data, ddof=1))
rel_err_2 = rel_err(sd_2(data), np.std(data, ddof=1))

# Print the results
print("\033[1m" + "For Q1b)" + '\033[0m')
print("The standard deviation calculated using Equation 1 yields", sd_1(data))
print("The standard deviation calculated using Equation 2 yields", sd_2(data))
print("The standard deviation calculated using the correct method yields", np.std(data))
print("\n")

print("The Relative Error between Equation 1 and the correct standard deviation is", rel_err_1)
print("The Relative Error between Equation 2 and the correct standard deviation is", rel_err_2)
print("\n")
#Q1 Part c)

# Create the two sequences, one with a much higher mean
seq1 = np.random.normal(0.0, 1.0, 2000)
seq2 = np.random.normal(10**7, 1.0, 2000)


# Print the results using the functions defined in Part c)
print("\033[1m"  "For Q1c)" + '\033[0m')
print("\033[1m" + "For Sequence 1" + '\033[0m')
print("The standard deviation calculated using Equation 1 yields", sd_1(seq1))
print("The standard deviation calculated using Equation 2 yields", sd_1(seq1))
print("The standard deviation calculated using the correct method yields", np.std(seq1))
print("\n")

print("The Relative Error between Equation 1 and the correct standard deviation is", rel_err(sd_1(seq1), np.std(seq1, ddof = 1)))
print("The Relative Error between Equation 2 and the correct standard deviation is", rel_err(sd_2(seq1), np.std(seq1, ddof = 1)))

print("\n")
print("\n")

print("\033[1m" + "For Sequence 2" + '\033[0m')
print("The standard deviation calculated using Equation 1 yields", sd_1(seq2))
print("The standard deviation calculated using Equation 2 yields", sd_2(seq2))
print("The standard deviation calculated using the correct method yeilds", np.std(seq2, ddof = 1))
print("\n")

print("The Relative Error between Equation 1 and the correct standard deviation is", rel_err(sd_1(seq2), np.std(seq2, ddof = 1)))
print("The Relative Error between Equation 2 and the correct standard deviation is", rel_err(sd_2(seq2), np.std(seq2, ddof = 1)))

#Q1 Part d

#Work around for the Equation 2

# There was no error encountered when using Equation 2.