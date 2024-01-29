import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import random

# Ryan Cunningham

# Question 2

def volume(dim, N):
    count = 0
    for i in range(N):

        # Generate an array of length 10, values [-1,1]
        r = 2 * np.random.rand(dim) - 1

        # Check if expected value of the array is inside the sphere, if so add one to the count
        if np.sqrt(np.sum(r ** 2)) < 1:
            count += 1

    return count * 2 ** dim / N

random.seed(123456)
# We want a tenth dimension sphere
d = 10

# Number of points
N = 1000000

# Volume array, to be appended to later
V = []

# For a better result, complete the estimation 10 times
for i in range(10):
    V = np.append(V, volume(d, N))


# Print Result
print('The average volume V of the hyper-sphere is:', np.average(V))
