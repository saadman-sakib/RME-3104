import matplotlib.pyplot as plt

def dy_dx(x, y):
    return y + x

x_0, y_0 = 0, 0


points = [(x_0, y_0)]

dx = .01

x, y = x_0, y_0
for i in range(1000):
    x = x+dx
    y = y+dy_dx(x,y)*dx
    points.append((x,y))


# plot points
xs, ys = zip(*points)
plt.plot(xs, ys)
plt.show()

