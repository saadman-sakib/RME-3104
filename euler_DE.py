import matplotlib.pyplot as plt
import math

def dy_dx(x, y):
    return math.sqrt(abs(1-y**2))

def d_dy_dx(x, y):
    return -y


x_0, y_0 = 0, 0
dy_0 = 1

points = [(x_0, y_0)]

dx = .01

x, y, y_d = x_0, y_0, dy_0
for i in range(00):
    x = x + dx
    y = y + dy_dx(x, y)*dx
    points.append((x,y))


# plot points
xs, ys = zip(*points)
plt.plot(xs, ys)
plt.show()

