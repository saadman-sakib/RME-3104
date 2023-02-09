THRESHOLD = 0.000000000000000001

def secant(function, x_0=0, x_1=1):
    f = function
    while abs(f(x_0)-f(x_1)) > THRESHOLD:
        x_0, x_1 = x_1, x_1 - f(x_1)/(f(x_0)-f(x_1)) * (x_0-x_1)
    return x_0

def f(x):
    return x**2-4

print(secant(f))