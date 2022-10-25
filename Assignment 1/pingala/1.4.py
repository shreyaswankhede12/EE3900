
import numpy as np
import matplotlib.pyplot as plt
import scipy
 

roots = np.polynomial.polynomial.polyroots((-1,-1,1))
a = roots[0]
b = roots[1]

def a_k(k):
    if k >=1:
        return (a**k - b**k)/(a - b)
    else :
        return 0
def b_k(k):
    if k >=2:
        return a_k(k-1) + a_k(k+1)
    elif k == 1:
        return 1.0
    else :
        return 0
def sum_a(n):
    sum = 0
    for i in range(n):
        sum += a_k(i+1)
    return sum

def powersum_a(n):
    return np.dot(np.array([a_k(i) for i in range(1,n+1)]),np.array([1/10**i for i in range(1,n+1)]))

def powersum_b(n):
    return np.dot(np.array([b_k(i) for i in range(1,n+1)]),np.array([1/10**i for i in range(1,n+1)]))

def powersum_roots(n):
    if n >=1 :
        return a**n + b**n
    else :
        return 0
vec_a_k = scipy.vectorize(a_k)

vec_sum = scipy.vectorize(sum_a)

n = np.arange(10)
#1.1
plt.figure(1)

plt.stem(n,vec_sum(n),markerfmt = 'bo')

plt.stem(n,vec_a_k(n+2) - 1,linefmt = 'r--',markerfmt = 'ro')
plt.legend(["$\sum_{k=1}^{n}a_k$","$a_{n+2} - 1$"])
plt.grid()
plt.savefig("figs/1_1.png")
#plt.show()

#1.2
vec_powersum_a = scipy.vectorize(powersum_a)
plt.figure(2)

plt.stem(n,vec_powersum_a(n))

plt.plot(n,np.ones(10)*10/89,color = 'g')
plt.legend(["$y = 10/89$","$\sum_{k=1}^{\infty}a_k/10^k$"])
plt.grid()
plt.savefig("figs/1.2.png")
#plt.show()

#1.3

vec_b_k = scipy.vectorize(b_k)

vec_powersum_roots = scipy.vectorize(powersum_roots)

plt.figure(3)

plt.stem(n,vec_powersum_roots(n),markerfmt = 'ro')

plt.stem(n,vec_b_k(n),linefmt = 'r--',markerfmt = 'bo')

plt.legend(["$b_n$",r"$\alpha^n + \beta^n$"])
plt.grid()
plt.savefig("figs/1.3.png")
plt.show()

#1.4

vec_powersum_b = scipy.vectorize(powersum_b)
plt.figure(4)

plt.stem(n,vec_powersum_b(n))

plt.plot(n,np.ones(10)*8/89,color = 'g')
plt.legend(["$y = 8/89$","$\sum_{k=1}^{\infty}b_k/10^k$"])
plt.grid()
plt.savefig("figs/1.4.png")
plt.show()


