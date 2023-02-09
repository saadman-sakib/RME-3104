THRESHOLD = .00000000000000001


def false_position(function, lower, upper):
    l, r, f = lower, upper, function
    m = r
    m_prev = l
    while abs(f(m)-f(m_prev)) > THRESHOLD:
        m_prev = m

        # w1, w2 = abs(1/f(l)), abs(1/f(r))
        # m = (w1*r + w2*l)/(w1 + w2)
        
        m = (abs(f(r))*l + abs(f(l))*r)/(abs(f(r)) + abs(f(l)))
        if f(m) > 0 :
            r = m
        else:
            l = m
    return l


def f(x):
    return x**2-4


print(false_position(f, 0, 5))
