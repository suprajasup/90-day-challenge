import numpy as np
n, m, p = map(int, input().strip().split())
for i in range(0,n):
    print(np.zeros((m,p),dtype=np.int))
for i in range(0,n):
    print(np.ones((m,p),dtype=np.int))