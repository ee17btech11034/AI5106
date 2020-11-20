import math
import numpy as np
import csv
import matplotlib.pyplot as plt 
from sympy import *

(x1,y1) = (1,2)   #point P
(x2,y2) = (3,-4)  #point Q
(x3,y3) = (5,-6)  #point R

P = np.array([x1,y1])
Q = np.array([x2,y2])
R = np.array([x3,y3])

x = np.linspace(1, 21, 1000)

# making augmented matrix
M =[[2*x1, 2*y1, -1, (np.linalg.norm(P))**2], [2*x2, 2*y2, -1, (np.linalg.norm(Q))**2], [2*x3, 2*y3, -1, (np.linalg.norm(R))**2]]
M1 = Matrix(M)
M_rred = M1.rref() 

g = -1*M_rred[0][3] 
f = -1*M_rred[0][7]
k = M_rred[0][11]

k1 = 2 + np.sqrt((100 - (x-11)**2)) 
k2 = 2 - np.sqrt((100 - (x-11)**2)) 
fig, ax = plt.subplots()
ax.set_aspect(1)

print("Centre of Circle: ",(-g,-f))

plt.annotate("P(1,2)", (x1,y1))
plt.annotate("Q(3,-4)", (x2,y2))
plt.annotate("R(5,-6)", (x3,y3))
plt.annotate("C(11,2)", (11,2))
plt.plot(x1,y1,'o')
plt.plot(x2,y2,'o')
plt.plot(x3,y3,'o')
plt.plot(11,2,'o')
plt.plot(x,k1,'y',label='x^T x - 2 (11  2)x + 25 = 0')
plt.plot(x,k2,'y')

plt.xlim(-1,23)
plt.ylim(-10,15)
plt.legend(loc='upper right')

plt.show()
