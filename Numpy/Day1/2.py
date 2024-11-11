import numpy as np

arr = np.array([1,2,3])
arr2 = np.ones((3,2))

print(arr.size)
print(arr)

# return shape of array
print(arr.shape)

# Return sum of array element
print(arr.sum())
# Return sum of each row 
print("Sum of:-",arr2.sum(axis=1))

# Return Max number
print(arr.max())

# Return min number
print(arr.min())

# Return mean
print(arr.mean())

# Return type of arrray
print(arr.dtype)

# Copy one array to another
arr1 = arr.copy()
print(arr1)

# Return dimension of array
print(arr.ndim)

# return square root of each element of array
print(np.sqrt(arr))

# return standard deviation
print(arr.std())

arr3 = np.arange(3)
arr4 = np.arange(3)

print(arr3 + arr4)
print(arr3 * arr4)
print(arr3.dot(arr4))
# print(arr3 / arr4)

# reshpe array 
arr5 = arr2.reshape(6,1)
print(arr5)

# Flatten array
arr6 = arr4.ravel()
print(arr6)

