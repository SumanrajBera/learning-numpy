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
- np.fliplr(arr): This flips the array from left to right

*Note*: NumPy automatically scales operations **(mathematical, logical, or structural )** across arrays; it performs scalar broadcasting for single values `(e.g., np.array([10, 20]) + 5 results in [15, 25])` and element-wise multiplication when combining multiple arrays of matching shapes `(e.g., np.array([10, 20]) * np.array([4, 3]) results in [40, 60])`

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

## Operations, Broadcasting, and Aggregation

### Arithmetic Operations

NumPy supports element-wise arithmetic operations between arrays of compatible shapes.

```python
import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([21, 32, 40, 50])

print(a + b)   # [22 34 43 54]
print(a * b)   # [ 21  64 120 200]
print(a - b)   # [-20 -30 -37 -46]
print(a / b)   # Normal division
print(b // a)  # Floor division
```

| Operator | Description |
|---|---|
| `+` | Adds corresponding elements |
| `-` | Subtracts corresponding elements |
| `*` | Multiplies corresponding elements |
| `/` | Performs true division |
| `//` | Performs floor division |

**Note:** These operations are element-wise, not matrix multiplication. Use `@` for matrix multiplication.

### Broadcasting

Broadcasting allows NumPy to perform operations on arrays of different but compatible shapes without manually repeating their elements.

#### Scalar Broadcasting

A scalar operates on every element of an array.

```python
arr = np.array([10, 20, 30, 40])

print(arr * 2)  # [20 40 60 80]
print(arr + 2)  # [12 22 32 42]
```

#### Broadcasting with 2D Arrays

```python
arr2D = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80]
])

# Broadcasting across columns
print(arr2D * np.array([5, 5, 5, 5]))

# Different multiplier for each row
print(arr2D * np.array([[5], [2]]))

# Scalar broadcasting
print(arr2D * 2)
```

**Output:**

```python
# First operation
[[ 50 100 150 200]
 [250 300 350 400]]

# Second operation
[[ 50 100 150 200]
 [100 120 140 160]]

# Third operation
[[ 20  40  60  80]
 [100 120 140 160]]
```

#### Broadcasting Rules

Compare array shapes from right to left. Two dimensions are compatible if:

- They are equal.
- One of them is `1`.
- One shape has no dimension at that position, in which case it is treated as `1`.

Examples:

- `(2, 4)` and `(4,)` → Compatible.
- `(2, 4)` and `(2, 1)` → Compatible.
- `(2, 4)` and `(3,)` → Incompatible.

### Aggregate Functions

Aggregate functions summarize array values using operations such as sum, minimum, maximum, mean, variance, and standard deviation.

```python
stat1D = np.array([1, 5, 16, 2, 20, 15])

print(np.sum(stat1D))   # 59
print(np.max(stat1D))   # 20
print(np.min(stat1D))   # 1
print(np.mean(stat1D))  # 9.8333...
print(np.std(stat1D))   # Standard deviation
print(np.var(stat1D))   # Variance
```

| Function | Description |
|---|---|
| `np.sum()` | Calculates the sum |
| `np.max()` | Returns the maximum value |
| `np.min()` | Returns the minimum value |
| `np.mean()` | Calculates the arithmetic mean |
| `np.std()` | Calculates standard deviation |
| `np.var()` | Calculates variance |
| `np.trace()` | Calculates sum across diagonal from left to right |

**Statistics note:** `np.std()` and `np.var()` use `ddof=0` by default, which calculates population standard deviation and population variance. Use `ddof=1` for sample estimates.

### Aggregation Along Axes in 2D Arrays

The `axis` parameter determines which dimension is reduced during aggregation.

```python
stat2D = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
```

#### `axis=0` — Column-wise Aggregation

Aggregates values down the rows, producing one result per column.

```python
print(np.sum(stat2D, axis=0))
# [5 7 9]
```

Calculation:

- Column 1: `1 + 4 = 5`
- Column 2: `2 + 5 = 7`
- Column 3: `3 + 6 = 9`

#### `axis=1` — Row-wise Aggregation

Aggregates values across the columns, producing one result per row.

```python
print(np.sum(stat2D, axis=1))
# [6 15]
```

Calculation:

- Row 1: `1 + 2 + 3 = 6`
- Row 2: `4 + 5 + 6 = 15`

## Fancy Indexing, Conditional Selection, Sorting, and Stacking

### Fancy Indexing

Fancy indexing allows us to select multiple elements from an array by passing a list or an array of indices.

#### Fancy Indexing in a 1D Array

```python
import numpy as np

arr = np.arange(1, 20)
print(arr)
# [ 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19]

print(arr[[1, 5, 8]])
# [2 6 9]
```

**Explanation:**
- NumPy uses zero-based indexing.
- `arr[[1, 5, 8]]` selects elements at indices `1`, `5`, and `8`.
- We get a new array containing the selected elements.

#### Fancy Indexing in a 2D Array

```python
arr2D = np.arange(1, 13).reshape(3, 4)

print(arr2D)
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]

print(arr2D[1, 2])
# 7

print(arr2D[[0, 2, 2], [1, 3, 2]])
# [ 2 12 11]
```

**Explanation:**

- `arr2D[1, 2]` selects the element at row `1`, column `2`.
- `arr2D[[0, 2, 2], [1, 3, 2]]` selects corresponding row and column pairs.

| Row index | Column index | Selected element |
|---:|---:|---:|
| 0 | 1 | 2 |
| 2 | 3 | 12 |
| 2 | 2 | 11 |

**Important:** The two index lists work together element by element, rather than selecting every combination of rows and columns.

---

### Conditional Selection

Conditional selection allows us to filter array elements based on a condition.

```python
arr = np.random.randint(1, 20, 5)

print(arr)
print(arr[arr > 5])
```

**Explanation:**

- `np.random.randint(1, 20, 5)` generates five random integers from `1` to `19`.
- `arr > 5` creates a Boolean array containing `True` or `False`.
- `arr[arr > 5]` returns only the elements that satisfy the condition.

For example, if `arr = [3, 8, 12, 4, 17]`, the result is:

```python
arr > 5
# [False  True  True False  True]

arr[arr > 5]
# [ 8 12 17]
```

#### Using `np.where()` to Get Indices

```python
print(np.where(arr > 5))
```

`np.where(condition)` returns the indices where the condition is `True`.

For the example above:

```python
np.where(arr > 5)
# (array([1, 2, 4]),)
```

**Note:** For a 1D array, the result is a tuple containing an array of indices.

#### Using `np.where()` to Replace Values

```python
print(np.where(arr > 5, arr, 0))
```

Syntax:

```python
np.where(condition, value_if_true, value_if_false)
```

- If the condition is `True`, use the corresponding element from `arr`.
- If the condition is `False`, use `0`.

Example:

```python
arr = np.array([3, 8, 12, 4, 17])

np.where(arr > 5, arr, 0)
# [ 0  8 12  0 17]
```

---

### Sorting

NumPy provides functions to sort elements and find their sorted positions.

#### `np.sort()`

Returns a sorted copy of an array in ascending order by default.

```python
arr = np.random.randint(30, 60, 5)

print(arr)
print(np.sort(arr))
```

Example:

```python
arr = np.array([45, 32, 57, 41, 36])

np.sort(arr)
# [32 36 41 45 57]
```

**Important:** `np.sort(arr)` does not modify the original array.

#### `np.argsort()`

Returns the indices that would arrange an array in sorted order.

```python
arr = np.array([45, 32, 57, 41, 36])

print(np.argsort(arr))
# [1 4 3 0 2]
```

The sorted order is obtained by visiting indices `1`, `4`, `3`, `0`, and `2`.

```python
arr[np.argsort(arr)]
# [32 36 41 45 57]
```

**Difference:**

- `np.sort(arr)` returns the sorted values.
- `np.argsort(arr)` returns the indices corresponding to the sorted order.

#### Sorting a 2D Array

```python
arr2D = np.array([
    [3, 1, 2],
    [9, 7, 8]
])

print(np.sort(arr2D))
# [[1 2 3]
#  [7 8 9]]
```

By default, NumPy sorts each row independently along the last axis.

To sort each column instead:

```python
np.sort(arr2D, axis=0)
```

- `axis=0`: sort down each column.
- `axis=1`: sort across each row.

---

### Concatenation and Stacking

Concatenation and stacking combine multiple arrays into a larger array.

#### `np.concat()`

Concatenates arrays along an existing axis.

```python
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7])

result = np.concat([a, b])

print(result)
# [1 2 3 4 5 6 7]
```

For 1D arrays, concatenation joins their elements into one longer array.

For multidimensional arrays, the arrays must have matching dimensions along every axis except the axis being concatenated.

#### `np.vstack()`

Stacks arrays vertically, adding rows.

```python
A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

B = np.array([
    [7, 8, 9],
    [10, 11, 12]
])

print(np.vstack([B, A]))
# [[ 7  8  9]
#  [10 11 12]
#  [ 1  2  3]
#  [ 4  5  6]]
```

**Explanation:**
- The rows of `B` appear first, followed by the rows of `A`.
- Both arrays must have the same number of columns.

#### `np.hstack()`

Stacks arrays horizontally, adding columns when working with 2D arrays.

```python
print(np.hstack([A, B]))
# [[ 1  2  3  7  8  9]
#  [ 4  5  6 10 11 12]]
```

**Explanation:**
- The columns of `B` are added to the right of `A`.
- Both arrays must have the same number of rows.
