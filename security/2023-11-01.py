import numpy as np
from numpy.linalg import inv

a = np.matrix([[1,2,3,4], [2,3,1,2], [1,1,1,-1], [1,0,-2,-6]])

np.set_printoptions(floatmode="fixed")

for i in range(0, 4):
    for j in range(0, 4):
        print('% 4s ' % (a[i][j]), end=" ")
    print()