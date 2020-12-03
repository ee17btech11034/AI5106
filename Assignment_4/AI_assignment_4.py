import math
import numpy as np
import matplotlib.pyplot as plt 
from numpy import linalg as LA

C = np.array([3,4])
n = np.array([5,12])
x = np.linspace(-6,8,50)

r = abs(((np.dot(n,C)) -1)/(np.linalg.norm(n)))

def circ_gen(C,r):
	len = 50
	theta = np.linspace(0,2*np.pi,len)
	x_circ = np.zeros((2,len))
	x_circ[0,:] = r*np.cos(theta)
	x_circ[1,:] = r*np.sin(theta)
	x_circ = (x_circ.T + C).T
	return x_circ

##Generating the circle
x_circ= circ_gen(C,r)
y = (1 - 5*x)/12

plt.plot(3,4,'-o')
plt.plot(x_circ[0,:],x_circ[1,:],label='$circle$')
plt.plot(x, y, label='5x + 12y = 1')
plt.annotate("C(3,4)", (3, 4))
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

plt.show()
