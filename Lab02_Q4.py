import numpy as np
from time import time
import matplotlib.pyplot as plt
from scipy import constants as con

# Ryan Cunningham (In a group with Habib Zaghloul)

# Question 4: Exploring Roundoff Error

#Q4 Part a)

# Create a u array close to the value of 1
u = np.linspace(0.98, 1.02, 500)

# Define p
p = (1-u) ** 8

# Define q, an estimation of p
q = 1 - 8*u + 28*(u**2) - 56*(u**3) + 70*(u**4) - 56*(u**5) + 28*(u**6) - 8*(u**7) + u**8


# Plot p vs u and q vs u on the same graph
plt.scatter(u, p, s= 10, color = "r", label = "p")
plt.scatter(u, q, s = 10, label = "q")
plt.legend(loc = "best")
plt.title("p Function and the q Function against u")
plt.show()
#Q4 Part b)


# Plot the histogram of (p-q)
plt.hist(p-q, bins = 20, edgecolor = "black")
plt.title("Histogram of (p-q)")
plt.show()
# Calculate the standard deviation of (p-q)
N = len(u)
C = 10**-16
stan_dev = C * np.sqrt(N) * np.sqrt(np.mean(u)**2)
print("The true standard deviation is", np.std(p-q))
print("The standard deviation estimated using Equation 3 is", stan_dev)

# Plot (p-q) vs u
plt.scatter(u, p-q, s = 15, marker = "x")
plt.title("A Graph of (p-q) against u")
plt.xlabel("(p-q)")
plt.ylabel("u")
plt.show()
# Q4 Part c

# Define a new u array
u_2 = np.linspace(0.98, 0.984, 500)
y = np.ones(len(u_2))

# Calculate a new p and a new q using the new u array
p_2 = (1-u_2) ** 8

q_2 = 1 - 8*u_2 + 28*(u_2**2) - 56*(u_2**3) + 70*(u_2**4) - 56*(u_2**5) + 28*(u_2**6) - 8*(u_2**7) + u_2**8

pq_diff = abs(p_2-q_2)/abs(p_2)

# Plot the absolute value of (p-q) against the absolute value of p
plt.scatter(u_2, pq_diff, s = 10, marker = "x")
plt.plot(u_2, y, color = "r")
plt.title("q Function's Relative Error When Compared to p Function")
plt.xlabel("u")
plt.ylabel("Error")
plt.show()

#Q4 Part d

f = u**8/((u**4)*(u**4))
plt.scatter(u, f-1, s = 5, marker = "x")

print("Error estimated from Equation 4.5 in Textbook is", np.std(f))
plt.title("f-1 against u")
plt.xlabel("u")
plt.ylabel("f-1")
plt.show()