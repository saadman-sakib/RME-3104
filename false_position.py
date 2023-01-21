def bisect(function, lower, upper):
    l, r, f = lower, upper, function
    m = 0
    while abs(f(l)-0) > .00000000000000000001:
        w1, w2 = abs(1/f(l)), abs(1/f(r))
        m = (w1*l + w2*r)/(w1 + w2)
        if f(m) > 0 :
            r = m
        else:
            l = m
    return l
    

def f(x):
    return x**2-4


print(bisect(f, 0, 5))