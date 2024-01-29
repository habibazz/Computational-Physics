import numpy as np
import matplotlib.pyplot as plt

# Ryan Cunningham

# Define the constants

L = 1
J = 50
dx = 0.02
g = 9.81
n_b = 0
H = 0.01
dt = 0.01
A = 0.002
mu = 0.5
sig = 0.05

# Create the x values
x = np.arange(0, L + dx, dx)

# Create time values:
t = np.arange(0, 5, dt)

# Define empty arrays
u = np.zeros(J + 1, float)
n = np.zeros(J + 1, float)

u_new = np.zeros(J + 1, float)
n_new = np.zeros(J + 1, float)

# Define the Initial Conditions

x_avg = np.average(A * np.exp(-(x - mu) ** 2 / sig ** 2))
n = H + A * np.exp(-(x - mu) ** 2 / sig ** 2) - x_avg
n_0 = np.copy(n)
ns = []

# Write a loop that performs the FTCS scheme

for time in t:
    for j in range(J + 1):

        # When x = 0 condition
        if j == 0:
            u_new[j] = 0
            n_new[j] = n[j] - (u[j + 1] * n[j + 1] - u[j] * n[j]) * dt / dx

        # When x = L condition
        elif j == J:
            u_new[j] = 0
            n_new[j] = n[j] - (u[j] * n[j] - u[j - 1] * n[j - 1]) * dt / dx

        # Otherwise, perform the FTCS scheme
        else:
            u_new[j] = u[j] - ((u[j + 1] ** 2 - u[j - 1] ** 2) / 2 + g * (n[j + 1] - n[j - 1])) * dt / (2 * dx)
            n_new[j] = n[j] - (u[j + 1] * n[j + 1] - u[j - 1] * n[j - 1]) * dt / (2 * dx)

        if time == 1.0:
            n_1 = np.copy(n)

        if time == 4.0:
            n_4 = np.copy(n)

    # Update the variables
    u = np.copy(u_new)
    n = np.copy(n_new)

plt.plot(x, n_0, label="t = 0 s")
plt.plot(x, n_1, label="t - 1 s")
plt.plot(x, n_4, label="t = 4 s")
plt.title("Waveforms in a 1D Water Simulation using an FTCS Scheme")
plt.xlabel("x / m")
plt.ylabel("Free Surface Altitude / m")
plt.legend(loc="best")
plt.show()