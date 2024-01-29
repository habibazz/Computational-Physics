import numpy as np
from time import time
import matplotlib.pyplot as plt
from scipy import constants as con

# Ryan Cunningham and Habib Zaghloul

def rel_err(x, y):
    return (x - y)/y

# Question 2: Trapezoidal and Simpson’s rules for integration

# Q2 Part b)

# Use the Trapezoid method to estimate the integral
a = 0.0
b = 1.0
N = 4
dx = (b - a) / N
fun_0 = (4 / (1 + a ** 2))
fun_1 = (4 / (1 + b ** 2))
x_count = a + dx
sum_ = 0
for i in range(N - 1):
    fun = 4 / (1 + x_count ** 2)
    sum_ = sum_ + fun
    x_count = x_count + dx

int1 = dx * (sum_ + ((fun_1 + fun_0) / 2))

# Use the Simpson method to estimate the integral

coeff = 4
x_count_S = a + dx
sum_S = 0
for i in range(N - 1):
    func = coeff * (4 / (1 + x_count_S ** 2))
    if coeff == 4:
        coeff = 2
    else:
        coeff = 4
    sum_S = sum_S + func

int2 = (dx / 3) * (fun_0 + sum_S + fun_1)

rel1 = (int1 - np.pi) / np.pi
rel2 = (int2 - np.pi) / np.pi

print("\033[1m" + "For Q2b)" + '\033[0m')
print("The true value of the integration is pi")
print("The estimation using the trapezoid method yielded a value of", int1, "with a relative error of", rel1)
print("The estimation using the Simpson method yielded a value of", int2, "with a relative error of", rel2)
print("\n")

# Q2 Part c)

a = 0.0
b = 1.0
v = 12
N = 2 ** v
dx = (b - a) / N

start = time()

fun_0 = (4 / (1 + a ** 2))
fun_1 = (4 / (1 + b ** 2))
x_count = a + dx
sum_ = 0
for i in range(N - 1):
    fun = 4 / (1 + x_count ** 2)
    sum_ = sum_ + fun
    x_count = x_count + dx

int3 = dx * (sum_ + ((fun_1 + fun_0) / 2))

end = time()
timing = end - start

rel3 = (int3 - np.pi) / np.pi

print("\033[1m" + "For Q2c)" + '\033[0m')
print("The value of v for N^v to achieve an error of 10^-9 is 12")
print("The value of the integral using this N is", int3, "with a relative value of", rel3)
print("The time taken for this calculation to be completed was", timing, "seconds")
print("\n")

# Q2 Part d)

# Use the Trapezoid method to estimate the integral, using N_1 = 16
a_3 = 0.0
b_3 = 1.0
N_1 = 16
dx_3 = (b_3 - a_3) / N_1
fun3_0 = (4 / (1 + a_3 ** 2))
fun3_1 = (4 / (1 + b_3 ** 2))
x_count_3 = a_3 + dx_3
sum_3 = 0
for i in range(N_1 - 1):
    fun = 4 / (1 + x_count_3 ** 2)
    sum_3 = sum_3 + fun
    x_count_3 = x_count_3 + dx_3

int6 = dx_3 * (sum_3 + ((fun3_1 + fun3_0) / 2))

# Now do the same but with N_2 = 32
# Use the Trapezoid method to estimate the integral
N_2 = 32
dx_4 = (b_3 - a_3) / N_2
fun3_0 = (4 / (1 + a_3 ** 2))
fun3_1 = (4 / (1 + b_3 ** 2))
x_count_4 = a_3 + dx_4
sum_4 = 0
for i in range(N_2 - 1):
    fun = 4 / (1 + x_count_4 ** 2)
    sum_4 = sum_4 + fun
    x_count_4 = x_count_4 + dx_4

int7 = dx_4 * (sum_4 + ((fun3_1 + fun3_0) / 2))

RE = rel_err(int6, np.pi)
RE2 = rel_err(int7, np.pi)

# Print the results

print("\033[1m" + "For Q2d)" + '\033[0m')
print("The value of the integral using N=16 is", int6)
print("The value of the integral using N=32 is", int7)
print("The relative error of the N_1 value is", RE)
print("The relative error of the N_2 value is", RE2)
print("When we multiply RE2 by 4 we obtain", RE2 * 4, "This is very similar to RE which is what we hoped to see")