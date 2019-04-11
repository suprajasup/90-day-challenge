import numpy as np 
n, m, p = map(int, input("enter values for n, m and p").strip().split())
arr = np.array(input("enter array elements").strip().split(), int)
for i in range(1, n + m):
    arr = np.vstack((arr, np.array(input().strip().split(), int)))
print(arr