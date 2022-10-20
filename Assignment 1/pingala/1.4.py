
import numpy as np
import matplotlib.pyplot as plt
import math
import scipy

def f5(n,a,b):
   return np.dot(vec_bn(np.arange(n),a,b),np.array([1/10**i for i in range(n)]))-8/89
vec_f5=scipy.vectorize(f5)
l6=vec_f5(n,a,b)
plt.plot(n,l6,label=r'$\sum_{k=1}^{n}\frac{b_{k}}{10^k}-(\frac{8}{89})$')
plt.grid()
plt.legend()
plt.show()