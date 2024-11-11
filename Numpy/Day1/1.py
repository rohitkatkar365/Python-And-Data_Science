import numpy as np
import time
import sys

# Less Memory
li = range(1000)
print(sys.getsizeof(5)*len(li))

arr = np.arange(1000)
print(arr.size*arr.itemsize)

# Faster
import time

l1 = list(range(1000000)) 
l2 = list(range(1000000))  

# Timing list comprehension
start = time.time()
res1 = [x + y for x, y in zip(l1, l2)]
print("Python List Comprehension Took", (time.time() - start) * 1000, "ms")

# Timing list concatenation
start = time.time()
# Sum
res2 = l1 + l2
print("Python List Concatenation Took", (time.time() - start) * 1000, "ms")

# Convinent
print(arr.dtype)
