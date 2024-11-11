# In Python, an array is a data structure that can store a collection of items of the same type.
from array import *

arr = array('i',[1,2,10,3,4,5,2,6])
# Add element at last
arr.append(7)
# Find size of aeeat its return (address,size)
print(arr.buffer_info())
# remove first occurance of 2
arr.remove(2);
# delete al element
# arr.clear()
print(arr.pop(3))
print(arr)
