# The nditer function in NumPy is an efficient and flexible tool to iterate over multi-dimensional arrays.

# syntax :

# numpy.nditer(op, flags=None, op_flags=None, op_dtypes=None, order='K', casting='unsafe', buffersize=0)

# op: The array (or arrays) you want to iterate over.
# flags: Controls the behavior of the iteration (discussed below).
# op_flags: Flags that determine how each operand (array) is read or written.
# op_dtypes: Used to specify the dtype of the array operands.
# order: The iteration order—either 'C' (row-major), 'F' (column-major), or 'K' (preserve existing order).
# casting: Controls data type casting (default is 'unsafe').
# buffersize: Controls the internal buffer size used during iteration.

import numpy as np 

arr = np.array([[1, 2, 3], [4, 5, 6]])

# op

# it = np.nditer(arr)
# for i in it:
    # print(i)

# flag
# it = np.nditer(arr,flags=['c_index']);
# for i in it:
#     print(f"C-index:{it.index},Value : {i}")

# op_flag
# it = np.nditer(arr,op_flags=["readwrite"])
# for i in it:
#     i[...] = i*2
# print(arr)

# 
# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])

# # Iterate over two arrays simultaneously
# for x, y in np.nditer([a, b]):
#     print(f'{x} + {y} = {x + y}')




