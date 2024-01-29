import numpy as np
from scipy import constants as con
import numpy.linalg as la
import matplotlib.pyplot as plt

# Ryan Cunningham
# Question 2

# Q2 Part b)

pi = np.pi
L = 5 * 10 ** -10
a = 10 * con.e
M = 9.1 * 10 ** -31
h_bar = 1.05 * 10 ** -34


# Define the H_mn function
def H_mn(m, n):
    pi = np.pi
    L = 5 * 10 ** -10
    a = 10 * con.e
    M = 9.1 * 10 ** -31
    h_bar = 1.05 * 10 ** -34

    if m == n:
        H = a / 2 + (pi ** 2 * h_bar ** 2 * m ** 2) / (2 * M * L ** 2)

    elif (m % 2 == 0 and n % 2 == 0) or (m % 2 == 1 and n % 2 == 1):
        H = 0
    else:
        H = - (8 * a * m * n) / (pi ** 2 * (m ** 2 - n ** 2) ** 2)

    return H


# Q2 Part c)

# Define a function to create the H matrix
def H_matrix(m_max, n_max):
    H_mat = np.zeros((m_max, n_max))

    for m in range(1, m_max + 1):
        for n in range(1, n_max + 1):
            H_mat[m - 1, n - 1] = H_mn(m, n)

    return H_mat


# Create the H matrix with size 10x10
H = H_matrix(10, 10)

# Find the eigenvalues of the 10x10 matrix
w, v = la.eig(H)
order = np.argsort(w)
eigen_values = w[order] / (con.e)
print("The Eigenvalues for mmax = nmax = 10 are", eigen_values)

# Q2 Part d)

# Create the H matrix with size 100x100
H_2 = H_matrix(100,100)

# Find the eigenvalues for the 100x100 matrix
w, v = la.eig(H_2)
order = np.argsort(w)
eigen_values_2 = w[order] / (con.e)
print("The First Ten Eigenvalues for mmax = nmax = 100 are", eigen_values_2[:10])

# Q2 Part e)

# Define the psi matrix
def psi(x, eig_vec, mmax):
    p = 0.0
    for i in range(mmax):
        p += eig_vec[i]*np.sin(i*np.pi*x/L)
    return p

def psi_sq(x, eig_vec, mmax):
    p = np.abs(psi(x, eig_vec, mmax))**2
    return p



# Define a function that performs the Simpson's integration method
def simpson_method(f, a, b, eig_vec, mmax):
    h = (b - a)/mmax
    k = 0.0
    x = a + h
    for i in range(1, int(mmax/2) + 1):
        k += 4 * f(x, eig_vec, mmax)
        x += 2 * h

    x = a + 2 * h
    for i in range(1, int(mmax/2)):
        k += 2 * f(x, eig_vec, mmax)
        x += 2 * h
    S = (h/3) * (f(a, eig_vec, mmax) + f(b, eig_vec, mmax) + k)
    return S


mmax = nmax = 100
eigs = eigen_values_2

# Find the eigenvectors for the first three energy states
eig_vec_1 = v[:, order[0]]
eig_vec_2 = v[:, order[1]]
eig_vec_3 = v[:, order[2]]



# Calculate the wave function for the first three energy states
x_values = np.linspace(0, L, mmax)

psi_0= psi(x_values, eig_vec_1, mmax)
a_0 = simpson_method(psi_sq, 0, L, eig_vec_1, mmax)

psi_1= psi(x_values, eig_vec_2, mmax)
a_1 = simpson_method(psi_sq, 0, L, eig_vec_2, mmax)

psi_2= psi(x_values, eig_vec_3, mmax)
a_2 = simpson_method(psi_sq, 0, L, eig_vec_3, mmax)


# plot the wave functions
plt.plot(x_values, psi_0**2/a_0, label = "Ground State")
plt.plot(x_values, psi_1**2/a_1, label = "First Excited State")
plt.plot(x_values, psi_2**2/a_2, label = "Second Excited State")
plt.legend(bbox_to_anchor=(1.5, 1.0))
plt.xlabel("x")
plt.ylabel("\u03a8(x)")
plt.title("Wave Function for the First 3 States against x")
plt.show()