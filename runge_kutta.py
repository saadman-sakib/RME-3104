import matplotlib.pyplot as plt

def dy_dx(x, y):
    return y**(.5) + x

x_0, y_0 = 0, 0
points = [(x_0, y_0)]

h = .01

x, y = x_0, y_0
for i in range(1000):
    k1 = dy_dx(x, y)
    k2 = dy_dx(x+h/2, y+k1*h/2)
    k3 = dy_dx(x+h/2, y+k2*h/2)
    k4 = dy_dx(x+h, y+k3*h)
    y = y + (k1 + 2*k2 + 2*k3 + k4)*h/6
    x = x+h
    points.append((x,y))


# plot points
xs, ys = zip(*points)
plt.plot(xs, ys)
plt.show()

