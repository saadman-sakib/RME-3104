THRESHOLD = .00000000000000001


def false_position(function, lower, upper):
    l, r, f = lower, upper, function
    m = 0
    while abs(f(l)-0) > THRESHOLD:
        w1, w2 = abs(1/f(l)), abs(1/f(r))
        m = (w1*l + w2*r)/(w1 + w2)
        if f(m)*f(r) > 0 :
            r = m
        else:
            l = m
    return l


def f(x):
    return x**2-4


print(false_position(f, 0, 5))
