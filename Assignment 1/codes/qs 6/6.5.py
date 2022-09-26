import numpy as np
import matplotlib.pyplot as plt
from scipy import vectorize, linalg

N = 20

def x(n):
    if n < 0 or n > 5:
        return 0
    elif n < 4:
        return n + 1
    else:
        return 6 - n

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

def y(n):
    if n < 0:
        return 0
    else:
        return x(n) + x(n-2) - 0.5 * y(n-1)

vec_y = vectorize(y, otypes=[float])
x_vec = vectorize(x, otypes=[float])
h_vec = vectorize(h, otypes=[float])

n_values = np.arange(N)
x_arr = x_vec(n_values)
h_arr = h_vec(n_values)

W = linalg.dft(N)
X = np.dot(W, x_arr)
H = np.dot(W, h_arr)
Y = X * H
y = np.dot(np.linalg.inv(W), Y)

# DFT
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

plt.stem(n_values, np.real(IDFT(n_values, Y)), markerfmt='go', label='$y_D(n)$')
plt.stem(n_values, np.real(y), markerfmt='ro', label='$y_M(n)$')
plt.title('Filter Output using DFT Matrix')
plt.ylabel('$y(n)$')
plt.xlabel('$n$')
plt.grid()
plt.legend()
plt.savefig('figs/6.5.png')
plt.show()