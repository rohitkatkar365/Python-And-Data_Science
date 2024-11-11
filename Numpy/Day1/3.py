# Different Ways of cretion of array

import numpy as np

arr = np.array([1,2,3,4,5])
print(arr)

arr1 = np.zeros((2,2))
print(arr1)

arr2 = np.ones((2,2))
print(arr2)

arr3 = np.arange(10)
print(arr3)

arr4 = np.linspace(1,5,5)
print(arr4)

arr5 = np.eye(3)
print(arr5)

arr6 = np.random.rand(3,2)
print(arr6)