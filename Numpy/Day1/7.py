import numpy as np

arr = np.arange(1,13).reshape(3,4)

t1 = np.savetxt("test.txt",arr)

t2 = np.loadtxt("test.txt")
print(t2)

# In NumPy, `savetxt` and `loadtxt` are functions for saving and loading arrays in text format (typically CSV or other delimited text files). Let’s break down both of these functions in detail.

# ### 1. **`savetxt`**
#    - **Purpose**: Saves an array to a text file.
#    - **Format**: The array is stored as rows and columns in a text format where each element is written in a specified delimiter (default is space).
   
#    #### Syntax:
#    ```python
#    numpy.savetxt(fname, X, fmt='%.18e', delimiter=' ', newline='\n', header='', footer='', comments='#')
#    ```
#    - **`fname`**: The name of the file (or file object) to which the array will be saved. The file extension is typically `.txt` or `.csv`.
#    - **`X`**: The array you want to save.
#    - **`fmt`**: Format for the elements of the array (default is `%.18e` which means scientific notation with 18 decimal places). You can specify a custom format, e.g., `fmt='%d'` for integers or `fmt='%.2f'` for two decimal float precision.
#    - **`delimiter`**: The string separating values (default is a space). You can use a comma for CSV files, e.g., `delimiter=','`.
#    - **`newline`**: String or character to separate lines (default is `\n`).
#    - **`header`**: String that will be written at the beginning of the file.
#    - **`footer`**: String that will be written at the end of the file.
#    - **`comments`**: String that will be prefixed to the header (default is `#`). You can set it to an empty string to avoid comment lines in the file.

#    #### Example:
#    ```python
#    import numpy as np

#    # Create an array
#    arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

#    # Save the array to a text file
#    np.savetxt('my_array.txt', arr, fmt='%d', delimiter=',')
#    ```
#    - **Explanation**: This will create a file called `my_array.txt` with the following content:
#      ```
#      1,2,3
#      4,5,6
#      7,8,9
     ```

   #### Example with Header/Footer:
#    ```python
#    np.savetxt('array_with_header_footer.txt', arr, fmt='%d', delimiter=',', header='This is the header', footer='This is the footer', comments='')
#    ```
#    This will produce:
#    ```
#    This is the header
#    1,2,3
#    4,5,6
#    7,8,9
#    This is the footer
   ```

# ### 2. **`loadtxt`**
#    - **Purpose**: Loads data from a text file into a NumPy array. It assumes the data in the file is organized in rows and columns, with values separated by a delimiter (default is space).

#    #### Syntax:
#    ```python
#    numpy.loadtxt(fname, dtype=float, delimiter=' ', skiprows=0, usecols=None, unpack=False, ndmin=0, comments='#')
#    ```
#    - **`fname`**: The name of the file (or file object) from which the data will be loaded.
#    - **`dtype`**: Data type of the resulting array (default is `float`). You can change this to `int`, `str`, or any other type.
#    - **`delimiter`**: The string separating values in the file (default is space). For CSV files, you would use `delimiter=','`.
#    - **`skiprows`**: Number of lines to skip at the beginning of the file (default is `0`). Useful when there’s a header.
#    - **`usecols`**: Which columns to read from the file (default is all columns). You can pass an index or a tuple of indices.
#    - **`unpack`**: If `True`, the columns will be transposed so that you get a tuple of 1D arrays.
#    - **`ndmin`**: Specifies the minimum number of dimensions of the returned array.
#    - **`comments`**: String that indicates comments in the file (default is `#`).

#    #### Example:
#    Assume we have a file `my_array.txt` with the following content:
#    ```
#    1,2,3
#    4,5,6
#    7,8,9
#    ```

#    We can load it using:
#    ```python
#    import numpy as np

#    # Load the file into an array
#    arr = np.loadtxt('my_array.txt', delimiter=',', dtype=int)

#    print(arr)
#    ```
#    - **Output**:
#      ```python
#      [[1 2 3]
#       [4 5 6]
#       [7 8 9]]
#      ```

#    #### Example with Skipping Rows:
#    If your file has a header and you want to skip it:
#    ```python
#    arr = np.loadtxt('array_with_header_footer.txt', delimiter=',', dtype=int, skiprows=1)
#    print(arr)
#    ```
#    This will skip the first row (the header) and load the rest of the data:
#    ```python
#    [[1 2 3]
#     [4 5 6]
#     [7 8 9]]
#    ```

#    #### Example with `usecols`:
#    If you only want to load specific columns:
#    ```python
#    arr = np.loadtxt('my_array.txt', delimiter=',', usecols=(0, 2), dtype=int)
#    print(arr)
#    ```
#    This will load only the first and third columns:
#    ```python
#    [[1 3]
#     [4 6]
#     [7 9]]
#    ```

# ### Differences between `savetxt` and `loadtxt`:
# - **`savetxt`**: Used to save a NumPy array to a text file. You can control how the data is formatted and how the file is structured.
# - **`loadtxt`**: Used to load data from a text file into a NumPy array. You can specify the format of the data, handle delimiters, skip rows, and choose specific columns to read.

# ### Key Points to Remember:
# 1. **`savetxt` is for writing NumPy arrays to a text file**, while **`loadtxt` is for reading arrays from text files**.
# 2. Use **delimiters** such as commas (`delimiter=','`) for CSV files.
# 3. Use **headers/footers** with `savetxt` for more informative outputs.
# 4. Use **`skiprows`** and **`usecols`** with `loadtxt` to load specific portions of the data.

# This covers the detailed usage of `savetxt` and `loadtxt`. Let me know if you'd like to explore any specific examples further!