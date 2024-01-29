# Habiba Zaghloul

# Question 1
from numpy import empty, copy


# The following will be useful for partial pivoting
# from numpy import empty, copy

# this function was given to us and is going to be used throughout the rest of this question
def GaussElim(A_in, v_in):
    """Implement Gaussian Elimination. This should be non-destructive for input
    arrays, so we will copy A and v to
    temporary variables
    IN:
    A_in, the matrix to pivot and triangularize
    v_in, the RHS vector
    OUT:
    x, the vector solution of A_in x = v_in """
    # copy A and v to temporary variables using copy command
    A = copy(A_in)
    v = copy(v_in)
    N = len(v)

    for m in range(N):
        # Divide by the diagonal element
        div = A[m, m]
        A[m, :] /= div
        v[m] /= div

        # Now subtract from the lower rows
        for i in range(m + 1, N):
            mult = A[i, m]
            A[i, :] -= mult * A[m, :]
            v[i] -= mult * v[m]

    # Backsubstitution
    # create an array of the same type as the input array
    x = empty(N, dtype=v.dtype)
    for m in range(N - 1, -1, -1):
        x[m] = v[m]
        for i in range(m + 1, N):
            x[m] -= A[m, i] * x[i]
    return x


import numpy as np
import matplotlib.pyplot as plt

# defining the matrix A to check if we get the same answer using gausselim and partialpivot
A = np.array([[2, 1, 4, 1],
              [3, 4, -1, -1],
              [1, -4, 1, 5],
              [2, -2, 1, 3]], float)
v = np.array([-4, 3, 9, 7], float)
n = len(v)


# setting S=A so we can change S how we like and keep A if we need it for a different part of the question

def PartialPivot(A_in, v_in):
    """ In this function, code the partial pivot (see Newman p. 222) """
    S = copy(A_in)
    N = len(v_in)
    for i in range(N):
        for k in range(i, N):  # looping through every elemnt in each row and column
            if abs(S[k][i]) > abs(S[i][i]):  # checking to see which value is furthest away from 0
                S[i, :], S[k, :] = copy(S[k, :]), copy(S[i, :])  # switching the rows of the matrix
                v_in[i], v_in[k] = v_in[k], v_in[i]  # switching the corresponding values of the vector v

    for m in range(N):
        # Divide by the diagonal element
        div = S[m][m]
        S[m, :] /= div
        v_in[m] /= div

        # Now subtract from the lower rows
        for i in range(m + 1, N):
            mult = S[i, m]
            S[i, :] -= mult * S[m, :]
            v_in[i] -= mult * v_in[m]

    # Backsubstitution
    # create an array of the same type as the input array
    x = empty(N, dtype=v.dtype)
    for m in range(N - 1, -1, -1):
        x[m] = v_in[m]
        for i in range(m + 1, N):
            x[m] -= S[m, i] * x[i]
    return x


# checking if both methods yield the same answer
gauss_x = GaussElim(A, v)
partial_x = PartialPivot(A, v)
print('The vector we get using gaussian elimination is', gauss_x, 'and what we get when we do partial pivoting is',
      partial_x)
# the vectors are identical
##Q1b
from numpy.random import rand
import time
from numpy.linalg import solve

# set N and create a random vector and matrix using rand
N_b = 300

# empty arrays to be used in forloop
e_gauss = []
e_piv = []
e_lu = []
t_gauss = []
t_piv = []
t_lu = []

# create a for loop that creates a random matrix and vector with dimensions (NxN) and N, respectively
for i in range(5, N_b):
    v_b = rand(i) * 5  # multiply both the vector and matrix by 5 because rand generates
    A_b = rand(i, i) * 5  # nubers from 0 to 1 and we dont want numbers too close to 0 to avoid errors

    t1 = time.time()  # start timing how long it takes to find vector x using this method
    x_gauss = (GaussElim(A_b, v_b))  # finding x
    gaussend = time.time()  # stopping the timer
    t_gauss.append(gaussend - t1)  # taking the difference to see how long it took
    vsol_gauss = np.dot(A_b, x_gauss)  # testing to see if the true value matches what we got
    e_gauss.append(np.mean(abs(v_b - vsol_gauss)))  # checking for errors by taking mean of abs value of difference

    t2 = time.time()
    x_piv = PartialPivot(A_b, v_b)
    pivend = time.time()
    t_piv.append(pivend - t2)
    vsol_piv = np.dot(A_b, x_piv)
    e_piv.append(np.mean(abs(v_b - vsol_piv)))

    t3 = time.time()
    x_lu = (solve(A_b, v_b))
    luend = time.time()
    t_lu.append(luend - t3)
    vsol_lu = np.dot(A_b, x_lu)
    e_lu.append(np.mean(abs(v_b - vsol_lu)))

print(max(t_gauss), 'is the max time to find our answer using gaussian elimination')
print(max(t_piv), ' is the max time it took using partial pivoting')
print(max(t_lu), 'is the max time it took using LU decomposition')

nn = np.arange(5, N_b)

plt.figure()

plt.plot(nn, t_gauss, label='Gaussian time', color='black')
plt.plot(nn, t_piv, label='Partial Pivoting time', color='red')
plt.plot(nn, t_lu, label='LU decomposition time', color='green')
plt.xlabel('Number of matrix N, (NxN)')
plt.ylabel('Time (seconds)')
plt.legend()
plt.title('Time taken to find x using 3 methods')
plt.loglog()
plt.grid()
plt.show()

plt.figure()

plt.plot(nn, e_gauss, label='Gaussian errors', color='black')
plt.plot(nn, e_piv, label='Partial Pivoting errors', color='red')
plt.plot(nn, e_lu, label='LU decomposition errors', color='green')
plt.xlabel('Number of matrix N, (NxN)')
plt.ylabel('Error')
plt.legend()
plt.title('Errors from each method')
plt.loglog()
plt.show()