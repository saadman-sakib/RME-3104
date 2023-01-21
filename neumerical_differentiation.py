def d_dx(function, x):
    h = 0.000000001
    f = function
    return (f(x+h)-f(x))/h

def f(x):
    return x**2

print(d_dx(f, 10))