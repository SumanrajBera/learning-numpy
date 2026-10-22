# Numpy

## Arrays
- Numpy arrays essentially come in two types: vectors and matrices. Vectors are strictly 1-d arrays and matrices are 2-d (but a matrix can still have only one row or one column).

### Vector
```py
import numpy as np
li = [1,2,3,4]
arr = np.array(li)
print(arr.dtype) # Will print int

# It also convert into unicode if the strings are mixed with Numbers and if float is mixed int then it converts into float
```
*Note*: numpy.array() converts a heterogeneous list into a NumPy array using a common data type when possible.

### Matrix
- The process is similar but we need to create a list of lists
```py
import numpy as np
matLi = [[1,2,3],[0,10,7]]
matrix = np.array(matLi)
```

## Built-in Methods
- np.zeros(): This method is used to make vector or matrix of zeros
```py
import numpy as np
# For 1D array with n zeros
np.zeros(10)
# For 2D array [row, col]
np.zeros([10,5])
```
- np.ones(): This is same as zeros but for ones
- np.full(): This is similar to zeros and ones but for any other number
```py
import numpy as np
# For 1D array with n numbers
np.zeros(10, 7)
# For 2D array [row, col] of n
np.zeros([10,5], 7)
```
- np.arange(start, stop): Here we give start and stop values to create an 1D array. By default start is 0.
- np.linspace(start, stop, count): Here we get start and stop both inclusive and count is the number of elements we want which is evenly spaced. By default count is 50.
- np.eye(n): This gives us an identity matrix of n*n.

*Note*: Numpy broadcasts scalar addition example if we do `np.array([10,20]) + 5` then the result will be `[15,25]`. 
*Note*: Numpy performs element-wise multiplication with multiple arrays example if we do `np.array([10,20]) * np.array([4, 3])` then the result will be `[40, 60]`.