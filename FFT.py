import matplotlib.pyplot as plt
import math
import numpy as np

def omega(N):
    return math.e**(-2j*math.pi/N)


def omega_inv(N):
    return math.e**(2j*math.pi/N)


def nround(x, n):
    return round(x.real, n) + round(x.imag, n)*1j



def fft(x):
    n = len(x)
    if n == 1:
        return x
    else:
        X_even = fft(x[0::2])
        X_odd = fft(x[1::2])
        y = [0]*n
        for k in range(n//2):
            y[k] = X_even[k] + (omega(n)**k) * X_odd[k]  
            y[k+n//2] = X_even[k] - (omega(n)**k) * X_odd[k]
        return y


def ifft(X):
    n = len(X)
    if n == 1:
        return X
    else:
        x_even = ifft(X[0::2])
        x_odd = ifft(X[1::2])
        y = [0]*n
        for k in range(n//2):
            y[k] = ( x_even[k] + (omega_inv(n)**k) * x_odd[k] )
            y[k+n//2] = ( x_even[k] - (omega_inv(n)**k) * x_odd[k] )
        return y



def f(x):
    return math.sin(100*x) + math.sin(200*x) + math.sin(300*x)


N = 2**12

y = [f(x) for x in np.linspace(0, 3, N)]

Y = [nround(_, 10) for _ in fft(y)]
y2 = [nround(_, 10)/N for _ in ifft(Y)]


plt.subplot(2, 2, 1)
plt.plot(np.linspace(0, .3/10, N//10), y[0:N//10])
plt.title('Original Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')

# space between subplots
plt.subplots_adjust(wspace=.5)

plt.subplot(2, 2, 2)
plt.plot(np.linspace(0, 999, 1000), [abs(_) for _ in Y[0:1000]])
plt.title('Fourier Coefficients')
plt.xlabel('Frequency')
plt.ylabel('Amplitude')

plt.subplots_adjust(hspace=.5)

plt.subplot(2, 2, 3)
plt.plot(np.linspace(0, .3/10, N//10), y2[0:N//10])
plt.title('Reconstructed Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')


plt.show()
