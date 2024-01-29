import numpy as np
from scipy import constants as con
import numpy.linalg as la
import matplotlib.pyplot as plt
# Ryan Cunningham

# Question 3

# Q3 Part a)

# Define our function f(x)
def f(x, c):
    return 1 - np.e ** (-c * x)


# Define a function that performs the relax method
def relax_method(c):
    x_i = 1
    x_i_1 = 1 - np.e ** (-c * x_i)

    while abs(x_i_1 - x_i) > 1 * 10 ** -6:
        x_i = x_i_1
        x_i_1 = f(x_i, c)

    return x_i_1


# Perform the relax method on different values of c
c_values = np.linspace(0, 3, 300)
f_solutions = []

for num in c_values:
    f_solutions.append(relax_method(num))

# plot the results
plt.plot(c_values, f_solutions)
plt.xlabel("c")
plt.ylabel("f(x)")
plt.title("Using the Relaxation Method for f(x) = 1 - e^(-cx)")
plt.show()


# Q3 Part b)

# Edit the relax method to count the number of interations
def relax_method_2(c):
    x_i = 1
    x_i_1 = 1 - np.exp(-c * x_i)
    num = 1
    while abs(x_i_1 - x_i) > 1e-6:
        x_i = x_i_1
        x_i_1 = f(x_i, c)
        num = num + 1

    return x_i_1, num


# Define a function that perform the overrelaxation method
def overrelax_method(c, omega):
    x_i = 1
    x_i_1 = 1 - np.exp(-c * x_i)
    num = 1
    while np.abs(x_i_1 - x_i) > 1e-6:
        x_i = x_i_1
        x_i_1 = f(x_i, c) * (1 + omega) - omega * x_i
        num += 1

    return x_i_1, num


# Print the results
print("Result from using the relaxation method without overrelaxation", relax_method_2(2)[0],
      "with an number of iterations of", relax_method_2(2)[1])
print("Using overrelaxation with an omega of 0.5 gives the result", overrelax_method(2, 0.5)[0],
      "with a number of iterations of", overrelax_method(2, 0.5)[1])
print("Using overrelaxation with an omega of 0.65 gives the result", overrelax_method(2, 0.65)[0],
      "with a number of iterations of", overrelax_method(2, 0.65)[1])


# Q3 Part c)

# Define a function that acts as the Wien's Displacement Constant Equation
def wien(x):
    return 5 * np.exp(-x) + x - 5


# Define a function that performs the binary search method
def binary(fun, x_1, x_2, e):
    while abs(x_1 - x_2) > e:
        x_i = (x_1 + x_2) / 2
        if fun(x_i) * fun(x_1) > 0:

            x_1 = x_i
        else:

            x_2 = x_i

    return x_1


# Perform the binary search method to obtan an x value
x_value = binary(wien, 0.01, 100, 10 ** -6)

# Use the x value to estimate the temperature for the surface of the sun
h = con.Planck
c = con.c
wl = 502.0 * 10 ** -9
k = con.k

T = (h * c) / (wl * k * x_value)

print("The x value was found to be", x_value)
print("The estimation for the Temperature of the Surface of the Sun is", T, "K")
