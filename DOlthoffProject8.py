#Dylan Olthoff
#Project 8
# Packages imported are listed below
from scipy import pi
from scipy.integrate import quad, simps
import numpy as np
import matplotlib.pyplot as plt



def reisum(f, minlim, maxlim, N): # function gets the reimann sum
    n = 1000
    #arrays used
    x = np.linspace(minlim, maxlim, N + 1)
    y = f(x)
    X = np.linspace(minlim, maxlim, n * N + 1)
    Y = f(X)

    plt.figure(figsize=(20, 5))
    # first plot
    plt.subplot(1, 3, 1)
    plt.plot(X, Y, 'b')
    x_left = x[:-1]
    y_left = y[:-1]

    plt.plot(x_left, y_left, 'b.', markersize=10)
    plt.bar(x_left, y_left, width=(maxlim - minlim) / N, alpha=0.2, align='edge', edgecolor='b')
    plt.title('Left Riemann Sum, N = {}'.format(N))

    #second plot
    plt.subplot(1, 3, 2)
    plt.plot(X, Y, 'b')
    x_mid = (x[:-1] + x[1:]) / 2
    y_mid = f(x_mid)

    plt.plot(x_mid, y_mid, 'b.', markersize=10)
    plt.bar(x_mid, y_mid, width=(maxlim - minlim) / N, alpha=0.2, edgecolor='b')
    plt.title('Midpoint Riemann Sum, N = {}'.format(N))

    #third plot
    plt.subplot(1, 3, 3)
    plt.plot(X, Y, 'b')
    x_right = x[1:]
    y_right = y[1:]

    plt.plot(x_right, y_right, 'b.', markersize=10)
    plt.bar(x_right, y_right, width=-(maxlim - minlim) / N, alpha=0.2, align='edge', edgecolor='b')
    plt.title('Right Riemann Sum, N = {}'.format(N))

    plt.show()



def fullreisum(f, minlim, maxlim, N):  # function for left mid and right
    dx = (maxlim - minlim) / N
    x_left = np.linspace(minlim, maxlim - dx, N)
    x_midpoint = np.linspace(dx / 2, maxlim - dx / 2, N)
    x_right = np.linspace(dx, maxlim, N)

    #left
    left_riemann_sum = np.sum(f(x_left) * dx)
    print("left sum\t", left_riemann_sum)

    #mid
    midpoint_riemann_sum = np.sum(f(x_midpoint) * dx)
    print("mid sum:\t", midpoint_riemann_sum)

    #right
    right_riemann_sum = np.sum(f(x_right) * dx)
    print("Right sum:\t", right_riemann_sum)


f = lambda x: np.sin(x) + 1  # Part 1a
g = lambda x: (3 * x) + (2 * (x ** 2))  # Part 1b
h = lambda x: np.log(x)  # Part 1c1
i = lambda x: (x ** 2) - (x ** 3)  # Part 1c2

# print statements for results
print("\nriemman sum of Part 1a is:");
fullreisum(f, -pi, pi, 4)
print("correct value: ", quad(f, -pi, pi)[0])
print("\nriemman sum of Part 1b is:");
fullreisum(g, 0, 1, 1000)
print("correct value: ", quad(g, 0, 1)[0])
print("\nThe riemman sum of Part 1c1 is:");
fullreisum(h, 1, np.e, 1000)
print("correct value: ", quad(h, 1, np.e)[0])
print("\nThe riemman sum of Part 1c2 is:");
fullreisum(i, -1, 0, 1000)
print("correct value: ", quad(i, -1, 0)[0])

# graphs
reisum(f, -pi, pi, 4)
reisum(g, 0, 1, 50)
reisum(h, 1, np.e, 50)
reisum(i, -1, 0, 50)

# Part 2
# xs and ys array to store data download information
xs = np.linspace(0, 30, 31)
ys = [2.5, 2.8, 2.2, 2.7, 3, 3.16, 3.1, 3, 3.3, 3.8, 3.8, 3.9, 3.6, 3.5, 3.2, 3.1, 3.3, 3.1, 3.1, 2.9, 3.5, 3.5, 3.5,
      3.6, 3.5, 3.1, 3.2, 3.4, 3.5, 3.6, 3.3]

for i in range(len(ys)): ys[i] *= 60.0  # mbps conversion
print("\nThe integral of the data download speeds is:\t", simps(ys, xs), "megabits") # print total data amount
