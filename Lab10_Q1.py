import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import random

# Ryan Cunningham

def nextmove(x, y):
    """ randomly choose a direction
    0 = up, 1 = down, 2 = left, 3 = right"""
    direction =  random.randrange(0,4)

    if direction == 0:  # move up
        y += 1
    elif direction == 1:  # move down
        y -= 1
    elif direction == 2:  # move right
        x += 1
    elif direction == 3:  # move left
        x -= 1
    else:
        print("error: direction isn't 0-3")

    return x, y


# YOU NEED TO FINISH IT!

plt.ion()

random.seed(12345)
Lp = 101  # size of domain
Nt = 5000  # number of time steps

centre_point = (Lp - 1) // 2  # middle point of domain
xp = centre_point
yp = centre_point

# Empty arrays, to be appended to later
i_s = []
j_s = []

# Loop to perform the Brownian Motion
for i in range(Nt):
    xpp, ypp = nextmove(xp, yp)

    # Make sure the particle is within bounds
    while xpp <= 0 or xpp >= Lp - 1 or ypp <= 0 or ypp >= Lp - 1:
        xpp, ypp = nextmove(xp, yp)

    xp = xpp
    yp = ypp

    # Append the position of the particle to the lists
    i_s.append(xp)
    j_s.append(yp)

# Plot the results

# Plot i vs j
fig = plt.figure(figsize=(10, 10))  # Create window
plt.scatter(i_s, j_s, s=15, marker="x", color="r", label="Particle Position")
plt.scatter(centre_point, centre_point, marker="x", color="b", s=500, label="Centre Point")
plt.title("i vs j")
plt.xlabel("x position")
plt.ylabel("y position")
plt.legend(loc="best")
plt.ioff()
plt.show()

# Create an arbitrary time array
t = np.arange(0, len(i_s))

# Plot i vs time
fig = plt.figure(figsize=(10, 10)) # Create window
plt.scatter(t, i_s, s = 20, marker = "x", color = "r", label = "Particle Position")
plt.scatter(centre_point, centre_point, marker = "x", color = "b", s = 500, label = "Centre Point")
plt.title("i vs time")
plt.xlabel("time / t")
plt.ylabel("x position")
plt.legend(loc = "best")
plt.show()

# Plot j vs time
fig = plt.figure(figsize=(10, 10)) # Create window
plt.scatter(t, j_s, s = 20, marker = "x", color = "r", label = "Particle Position")
plt.scatter(centre_point, centre_point, marker = "x", color = "b", s = 500, label = "Centre Point")
plt.title("j vs time")
plt.xlabel("time / t")
plt.ylabel("y position")
plt.legend(loc = "best")
plt.show()

# Q1 Part b) Ex 10.13

plt.ion()
random.seed(123)
Lp = 101  # size of domain
N = 1000  # number of particles
# array to represent whether each gridpoint has an anchored particle
anchored = np.zeros((Lp, Lp), dtype=int)
# list to represent x and y positions of anchored points
anchored_points = [[], []]

centre_point = (Lp - 1) // 2  # middle point of domain

stop = False

for j in range(N):

    anchor = False

    xp = centre_point
    yp = centre_point
    i = 0  # counter to keep track of animation of moving particle

    # See if anchor has reached centre
    anchor_copy = np.copy(anchored_points)

    while (centre_point in anchor_copy[0]):
        index = list(anchor_copy[0]).index(centre_point)

        if anchor_copy[1][index] == centre_point:
            stop = True

        anchor_copy[0][index] = 0
        anchor_copy[1][index] = 0
    # Stop if it has
    if stop == True:
        break

    # Perform the Brownian Motion while a particle is not anchored
    while anchor == False:
        # Make sure the particle is within bounds
        if xp == 0 or xp == Lp - 1 or yp == 0 or yp == Lp - 1:

            anchored[int(xp), int(yp)] = 1
            anchored_points[0].append(xp)
            anchored_points[1].append(yp)

            anchor = True
        # If the particle encounters an anchored particle, it must become anchored too
        elif np.any(anchored[int(xp - 1):int(xp + 2), int(yp - 1):int(yp + 2)] == 1):

            # Check if particle is adjacent to an anchored particle

            anchored[int(xp), int(yp)] = 1
            anchored_points[0].append(xp)
            anchored_points[1].append(yp)

            anchor = True
        # Otherwise, Brownian Motion continues
        else:
            # while loop
            i += 1
            xp, yp = nextmove(xp, yp)

# Plot the anchored particles
fig = plt.figure(figsize=(10, 10))
plt.scatter(anchored_points[0], anchored_points[1], color="r", label="Anchored Particles")
plt.scatter(centre_point, centre_point, marker="x", color="b", s=500, label="Centre Point")
plt.title("DLA using Brownian Motion")
plt.xlabel("y position")
plt.ylabel("x position")
plt.legend(loc="best")
plt.ioff()
plt.show()
