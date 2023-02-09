THRESHOLD = .00000000000000001

def bisect(function, lower, upper):
    l, r, f = lower, upper, function
    m = l
    m_prev = r
    while abs(f(m)-f(m_prev)) > THRESHOLD:
        m_prev = m
        m = (l+r)/2
        if f(m)*f(r) > 0 :
            r = m
        else:
            l = m
    return l


def f(x):
    return x**2-4


print(bisect(f, 0, 5))
