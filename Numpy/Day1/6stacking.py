import numpy as np

arr1 = np.arange(6).reshape(3,2)
arr2 = np.arange(6,12).reshape(3,2)

# print(arr1)
# print(arr2)

arr3 = np.vstack((arr1,arr2))
print(arr3)

arr4 = np.hstack((arr1,arr2))
print(arr4)

arr5 = np.arange(20).reshape(2,10)
arr6 = np.vsplit(arr5,2)
print(arr6)

arr7 = np.arange(12).reshape(3,4)

b = arr7 > 6
print(b)

arr7[b] = -1
print(arr7)