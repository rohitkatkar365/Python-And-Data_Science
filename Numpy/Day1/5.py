import numpy as np

arr1 = np.array([[6,7,8],
                 [1,2,3],
                 [9,3,2]])


for row in arr1:
    print(row)

for cell in arr1.flat:
    print(cell)