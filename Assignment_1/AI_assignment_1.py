import math
import numpy as np

# given points are P(x1,y1) and Q(x2,y2)
(x1,y1) = (-2,4)
(x2,y2) = (3,-5)

l1 = [x1,y1]
l2 = [x2,y2]

P = np.array(l1)
Q = np.array(l2)
Z = P - Q
# distance between P and Q is d.
d = np.linalg.norm(Z)
print("Dinstance between points P and Q is: ",d)
