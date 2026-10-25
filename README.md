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

- np.random.rand(row,col): We get randome decimal matrix in shape of the given row and column
- np.random.randint(start, end, size = (row, col) / (num)): Here we get numbers between start (inclusive) and end (exclusive) and the size can be matrix if given 2 values and 1 value will make it a vector of that size.
- np.random.randn(row, col): This is used for normal distribution in bell curve where values lie in between -3 and +3. row and col are used for making it a matrix. If 1 value is given then it will be a vector.

## Attributes of Array
- shape: This is used for getting the shape of the array. Which if 1D is `(n,)` or if 2D is `(row, col)`
- ndim: This is used for getting the dimension of the array.
- size: This is used for getting the size which means the number of elements in the array.
- dtype: This is used for getting data type of the array.

## Indexing
- 1D Array
```py
# here idx can be from 0 to n - 1.
arr[idx]
```
- 2D Array
```py
# Here idx will give us that whole row
arr[idx]

# Here we will get the element at particular row and column
arr[row, col]
```
*Note*: Negative indexing is also allowed where it starts from -1.

## Slicing
- 1D Array
```py
arr[:] # For the entire
arr[start:stop] # Will slice from start to stop - 1 position
arr[start: stop: step] # Here step will give you elements that comes at that distance
```
- 2D array
```py
# Here too the default is 0 for start and end is whole length - 1
arr[rowStart:rowStop, colStart:colStop]
```

## Boolean indexing
- 1D array
```py
arr > 5 # Will give an array of boolean where is element is greater than 5 then its true
arr[arr > 5] # Will give us an array of all elements in the array which are greater than 5
```
- 2D array
```py
arr > 5 # Will give a 2D array of boolean where every element which is greater than 5 then its true else its false
arr[arr > 5] # Will give us a 1D array of all elements in the array which are greater than 5
```

## Reshape an Array
- We can reshape an array into our desired shape by mention the row and colum.
```py
# If the shape is possible then only we will get the reshaped array
np.arange(1,31).reshape(6, 5)
```

## Flattening an array
- We can flatten a 2D array into a 1D using `flatten()`