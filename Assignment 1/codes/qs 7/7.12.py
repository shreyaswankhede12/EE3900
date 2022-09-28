import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 2, 1], dtype=float)
x = np.pad(x, (0,2), 'constant', constant_values=(0))
X = np.fft.fft(x)

plt.stem(np.real(X))
plt.xlabel('$k$')
plt.ylabel('$X(k)$')
plt.title('FFT after zero padding $\mathbf{x}$')
plt.grid()
plt.savefig('Assignment 1/figs/7.12.png')
plt.show()