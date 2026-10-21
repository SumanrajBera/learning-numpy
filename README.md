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