import numpy as np
import matplotlib.pyplot as plt

# Ryan Cunningham

# Define the constants
"""""
We will be assuming the value of these constant to be:
ep = 1
sig = 1
m = 1
"""

# Define a function for the Lennard-Jones Potential
def V(r):
    return (4) * ((1 / r) ** 12 - (1 / r) ** 6)


# Define a function for acceleration
def a(r):
    return (48 * (1 / r ** 13) - 24 * (1 / r ** 7))


# Define a function for f(r, t) where f = dr/dt
def f(r, t):
    # Assign intitial positions for Particle 1 and Particle 2
    r1_x = r[0]
    r1_y = r[1]
    r2_x = r[2]
    r2_y = r[3]

    # Find the differences between the particles (dx_1 == - dx_2) so we could use this or just calculate dx_2 seperately
    dx_1 = r1_x - r2_x
    dy_1 = r1_y - r2_y
    dx_2 = r2_x - r1_x
    dy_2 = r2_y - r1_y
    r_1 = np.sqrt(dx_1 ** 2 + dy_1 ** 2)
    r_2 = np.sqrt(dx_2 ** 2 + dy_2 ** 2)

    # Calculate the accerlation in the x and y directions for Particle 1
    fx_1 = a(r_1) * dx_1 / r_1
    fy_1 = a(r_1) * dy_1 / r_1

    # Calculate the accerlation in the x and y directions for Particle 2
    fx_2 = a(r_2) * dx_2 / r_2
    fy_2 = a(r_2) * dy_2 / r_2

    return np.array([fx_1, fy_1, fx_2, fy_2])


# List of all initial conditions rs[0] = [r1x,r1y,r2x,r2y] for situation i for example
rs = [[4, 4, 5.2, 4], [4.5, 4, 5.2, 4], [2, 3, 3.5, 4.4]]

# Create empty lists to be appended to later
x1s = []
x2s = []
y1s = []
y2s = []
vx1s = []
vy1s = []
vx2s = []
vy2s = []

# For each of the initial conditions
for r in rs:
    v = [0, 0, 0, 0]

    # Create the time variable with time step (h) = 0.01 s
    h = 0.01
    time = np.arange(0, 1, h)

    # Create the list for the trajecotry points, as well as append the initial conditions
    x1_points = [r[0]]
    y1_points = [r[1]]
    x2_points = [r[2]]
    y2_points = [r[3]]
    vx_1 = [v[0]]
    vy_1 = [v[1]]
    vx_2 = [v[2]]
    vy_2 = [v[3]]

    # Verlet Algorithm has a unique first step:
    vhalf = v + h / 2 * f(r, time[0])

    # Continue with the Verlet algorithm loop
    for t in time[1:]:
        r = r + h * vhalf
        k = h * f(r, t + h)
        vth = vhalf + k / 2
        vt32h = vhalf + k
        vhalf = vt32h

        # Append the iterations to a list
        x1_points.append(r[0])
        y1_points.append(r[1])
        x2_points.append(r[2])
        y2_points.append(r[3])
        vx_1.append(vth[0])
        vy_1.append(vth[1])
        vx_2.append(vth[2])
        vy_2.append(vth[3])

    # Save each of the lists to the empty lists created above so type(xs) = list(list) etc.
    x1s.append(x1_points)
    x2s.append(x2_points)
    y1s.append(y1_points)
    y2s.append(y2_points)
    vx1s.append(vx_1)
    vy1s.append(vy_1)
    vx2s.append(vx_2)
    vy2s.append(vy_2)

# Plot the results

fig, axs = plt.subplots(3)
fig.set_figheight(100)
fig.set_figwidth(5)
axs[0].plot(x1s[0], y1s[0], ".", color="b", label="Particle 1")
axs[0].plot(x2s[0], y2s[0], ".", color="r", label="Particle 2")
axs[0].legend(loc="best")
axs[0].set_title("Trajectory for Situation i")
axs[0].set(xlabel='x position', ylabel="y position")
axs[1].plot(x1s[1], y1s[1], ".", color="b", label="Particle 1")
axs[1].plot(x2s[1], y2s[1], ".", color="r", label="Particle 2")
axs[1].legend(loc="best")
axs[1].set_title("Trajectory for Situation ii")
axs[1].set(xlabel='x position', ylabel="y position")
axs[2].plot(x1s[2], y1s[2], ".", color="b", label="Particle 1")
axs[2].plot(x2s[2], y2s[2], ".", color="r", label="Particle 2")
axs[2].legend(loc="best")
axs[2].set_title("Trajectory for Situation iii")
axs[2].set(xlabel='x position', ylabel="y position")
plt.show()


# Q1 Part c)
plt.plot(time, x1s[0], label = "Particle 1", color = "b")
plt.plot(time, x2s[0], label = "Particle 2", color = "r")
plt.legend(loc = 'best')
plt.title("X Position vs Time for Particles 1 and 2 (Situation i)")
plt.xlabel("Time / s")
plt.ylabel("x position")
print("Situation i leads to oscillatory motion for the two particles")
plt.show()