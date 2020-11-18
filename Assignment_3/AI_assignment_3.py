import math
import numpy as np
import matplotlib.pyplot as plt


(x,y) = (0,0)     # this is just only for calculate the minors
(x1,y1) = (1,2)   #point P
(x2,y2) = (3,-4)  #point Q
(x3,y3) = (5,-6)  #point R

h = np.linspace(1, 21, 1000)

M = [[x**2 + y**2, x, y, 1], [x1**2 + y1**2, x1, y1, 1], [x2**2 + y2**2, x2, y2, 1], [x3**2 + y3**2, x3, y3, 1]]

def mnr(M,i,j):
    return [row[:j] + row[j+1:] for row in (M[:i]+M[i+1:])]

M11 = np.linalg.det(mnr(M,0,0))
M12 = np.linalg.det(mnr(M,0,1))
M13 = np.linalg.det(mnr(M,0,2))
M14 = np.linalg.det(mnr(M,0,3))

g = round(-M12/(2*M11),3)
f = round(M13/(2*M11), 3)
c = round(-M14/M11, 3)
r = np.sqrt((-g-x1)**2 + (-f-y1)**2)

k1 = -f + np.sqrt((100 - (h+g)**2)) 
k2 = -f - np.sqrt((100 - (h+g)**2)) 
fig, ax = plt.subplots()
ax.set_aspect(1)

print("centre of this circle is (x0,y0) = ", (-g,-f))
print("constant c = ", c)
print("radius of circle : ",r)

plt.annotate("P(1,2)", (x1,y1))
plt.annotate("Q(3,-4)", (x2,y2))
plt.annotate("R(5,-6)", (x3,y3))
plt.annotate("C(11,2)", (-g,-f))
plt.plot(x1,y1,'o')
plt.plot(x2,y2,'o')
plt.plot(x3,y3,'o')
plt.plot(-g,-f,'o')
plt.plot(h,k1,'y',label='x^T x - 2 (11  2)x + 25 = 0')
plt.plot(h,k2,'y')

plt.xlim(-g-r-2,-g+r+2)
plt.ylim(-f-r-4,-f+r+4)
plt.legend(loc='upper right')

plt.show()
