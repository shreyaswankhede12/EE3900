import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import toeplitz
#If using termux
import subprocess
import shlex
#end if



n = np.arange(14)
fn=(-1/2)**n
hn1=np.pad(fn, (0,2), 'constant', constant_values=(0))
hn2=np.pad(fn, (2,0), 'constant', constant_values=(0))
h = hn1+hn2

nh=len(h)
x=np.array([1.0,2.0,3.0,4.0,2.0,1.0])
nx = len(x)

padding = np.zeros(nx-1,x.dtype)
# print(h)
a = np.array([h[0]])
f_col = np.pad(h,(0,nx-1),'constant', constant_values=(0))
f_row = np.pad(a,(0,nx-1),'constant', constant_values=(0))

H =toeplitz(f_col, f_row)

y = np.matmul(H,x)
print(y)

# print(y)
# #plots
plt.stem(range(0,nx+nh-1),y)
plt.title('Filter Output using Convolution')
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.grid()# minor
# plt.show()
# #If using termux
plt.savefig('figs/5.5 ynconv.pdf')
# # subprocess.run(shlex.split("termux-open ../figs/ynconv.pdf"))