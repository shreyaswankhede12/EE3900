import numpy as np
import matplotlib.pyplot as plt
import scipy

N = 20

def x(n):
    if n < 0 or n > 5:
        return 0
    elif n < 4:
        return n + 1
    else:
        return 6 - n

def y(n):
    if n < 0:
        return 0
    else:
        return x(n) + x(n-2) - 0.5 * y(n-1)

def delta(n):
    if n == 0:
        return 1
    else:
        return 0

def h(n):
    if n == 0:
        return 1
    elif n > 0:
        return delta(n) + delta(n-2) - 0.5*h(n-1)
    else:
        return 2*(delta(n+1) + delta(n-1) - h(n+1))

def DFT(k, inp):
    ksum = 0
    for n in range(N):
        ksum += inp(n) * np.exp(-2j * np.pi * k * n / N)
    return ksum

def Y(k):
    return DFT(k, x) * DFT(k, h)

def IDFT(n, inp):
    nsum = 0
    for k in range(N):
        nsum += inp(k) * np.exp(2j * np.pi * k * n / N)
    return nsum / N

vec_y = scipy.vectorize(y)

nvalues = np.linspace(0, N-1, N)
plt.stem(nvalues, vec_y(nvalues), markerfmt='bo', label='$y(n)$')
plt.stem(nvalues, np.real(IDFT(nvalues, Y)), linefmt='r--', markerfmt='ro', label='$y_D(n)$')
plt.title('Filter Output using DFT')
plt.ylabel('$y(n)$')
plt.xlabel('$n$')
plt.legend()
plt.grid()
plt.savefig('figs/6.3.png')
plt.show()