THRESHOLD = .000000000000001

def d_dx(function, x):
    h = 0.000000001
    f = function
    return (f(x+h)-f(x))/h

def newton_raphson(function, x_0=0):
    f = function
    x = x_0
    h = 0.00001
    while abs(f(x)-0) > THRESHOLD:
        x = x - f(x)/(d_dx(f, x) + h)
    return x

def f(x):
    return x**2-4

print(newton_raphson(f))