import numpy as np

arr = np.array([6,7,8])

# Accessing
# print(arr[0])
# print(arr[-1])
# Slicing
# print(arr[1:3])


arr1 = np.array([[6,7,8],
                 [1,2,3],
                 [9,3,2]])

# print(arr1[0][1])
# print(arr1[0,1])

# print(arr1)

print(arr1[0:2,2])
print(arr1[-1,0:2])
print(arr1[0:3,1:3])

