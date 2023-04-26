import math

def f(x, n):
    return ((1 - (-1)**n) / (n*math.pi))  * math.sin(n*x)


func = []

x = 0
for i in range(10000):
    val = 0
    dx = 0.001
    for j in range(1, 100):
        val += f(x, j)
    x += dx
    func.append(val)


import matplotlib.pyplot as plt
plt.plot(func)
# show grid
plt.grid(True)
plt.show()
