# Tutorial 1: Arrays and Matrices in Python

**Section**: 6 - Arrays and Matrices (90 min)
**Level**: Beginner to Intermediate
**Prerequisites**: Basic Python knowledge (variables, loops, functions)

---

## 📋 Learning Objectives

By the end of this tutorial, you will be able to:

1. **Understand Array Concepts**: Work with one-dimensional and multi-dimensional arrays
2. **Perform Array Operations**: Add, multiply, and transform arrays and matrices
3. **Implement Matrix Operations**: Matrix multiplication, transposition, and other linear algebra operations
4. **Apply Search Algorithms**: Search and sort elements in arrays and matrices
5. **Solve Real Problems**: Use arrays and matrices to solve practical computational problems
6. **Optimize Performance**: Choose appropriate data structures and algorithms for array operations

---

## 📚 Table of Contents

1. [Array Fundamentals](#array-fundamentals)
2. [Multi-dimensional Arrays (Matrices)](#multi-dimensional-arrays-matrices)
3. [Array Operations](#array-operations)
4. [Matrix Operations](#matrix-operations)
5. [Searching and Sorting](#searching-and-sorting)
6. [Common Algorithms](#common-algorithms)
7. [Performance Considerations](#performance-considerations)
8. [Best Practices](#best-practices)

---

## 🔸 Array Fundamentals

Arrays are ordered collections of elements that can be accessed by index. In Python, we typically use lists to represent arrays, though for high-performance numerical computing, you'd use libraries like NumPy.

### Creating Arrays

```python
# One-dimensional arrays using lists
empty_array = []
numbers = [1, 2, 3, 4, 5]
strings = ["apple", "banana", "cherry"]
mixed = [1, "hello", 3.14, True]

# Using list comprehensions
squares = [x**2 for x in range(10)]  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
evens = [x for x in range(20) if x % 2 == 0]  # [0, 2, 4, ..., 18]

# Creating arrays with repeated values
zeros = [0] * 10  # [0, 0, 0, ..., 0]
ones = [1] * 5    # [1, 1, 1, 1, 1]

# Converting other types to arrays
from_string = list("hello")  # ['h', 'e', 'l', 'l', 'o']
from_range = list(range(5))   # [0, 1, 2, 3, 4]
```

### Array Indexing and Slicing

```python
numbers = [10, 20, 30, 40, 50, 60, 70]

# Basic indexing (zero-based)
first = numbers[0]    # 10
last = numbers[-1]    # 70
third = numbers[2]    # 30

# Slicing [start:end:step]
first_three = numbers[0:3]    # [10, 20, 30]
middle = numbers[2:5]         # [30, 40, 50]
every_other = numbers[::2]    # [10, 30, 50, 70]
reversed_arr = numbers[::-1]  # [70, 60, 50, 40, 30, 20, 10]

# Advanced slicing
# Get last 3 elements
last_three = numbers[-3:]     # [50, 60, 70]
# Skip first and last
middle_only = numbers[1:-1]   # [20, 30, 40, 50, 60]
```

### Array Modification

```python
numbers = [1, 2, 3, 4, 5]

# Modifying elements
numbers[0] = 10        # [10, 2, 3, 4, 5]
numbers[-1] = 50       # [10, 2, 3, 4, 50]

# Inserting elements
numbers.insert(1, 15)  # [10, 15, 2, 3, 4, 50]
numbers.insert(0, 5)   # [5, 10, 15, 2, 3, 4, 50]

# Appending elements
numbers.append(60)     # [5, 10, 15, 2, 3, 4, 50, 60]

# Extending with another array
numbers.extend([70, 80])  # [5, 10, 15, 2, 3, 4, 50, 60, 70, 80]

# Removing elements
numbers.remove(15)     # Remove first occurrence of 15
popped = numbers.pop() # Remove and return last element (80)
popped_index = numbers.pop(2)  # Remove and return element at index 2
```

---

## 📊 Multi-dimensional Arrays (Matrices)

Matrices are two-dimensional arrays. In Python, we represent them as lists of lists.

### Creating Matrices

```python
# Creating a 3x3 matrix
matrix_3x3 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Identity matrix 3x3
identity_3x3 = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
]

# Zero matrix 2x4
zero_2x4 = [
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

# Using nested list comprehensions
# Create a 4x4 matrix with values 0-15
matrix_4x4 = [[i*4 + j for j in range(4)] for i in range(4)]
# [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]

# Diagonal matrix
diagonal = [[1 if i == j else 0 for j in range(5)] for i in range(5)]
```

### Matrix Indexing and Slicing

```python
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

# Accessing elements [row][column]
element_00 = matrix[0][0]  # 1
element_12 = matrix[1][2]  # 7
element_22 = matrix[2][2]  # 11

# Getting matrix dimensions
rows = len(matrix)        # 3
cols = len(matrix[0])     # 4

# Accessing entire rows
first_row = matrix[0]     # [1, 2, 3, 4]
last_row = matrix[-1]     # [9, 10, 11, 12]

# Accessing columns (using list comprehension)
first_column = [row[0] for row in matrix]  # [1, 5, 9]
second_column = [row[1] for row in matrix] # [2, 6, 10]

# Matrix slicing
# Get submatrix (first 2 rows, first 3 columns)
submatrix = [row[:3] for row in matrix[:2]]
# [[1, 2, 3], [5, 6, 7]]

# Get diagonal elements
diagonal = [matrix[i][i] for i in range(min(rows, cols))]  # [1, 6, 11]
```

### Matrix Properties

```python
def get_matrix_dimensions(matrix):
    """Return (rows, columns) of matrix."""
    if not matrix:
        return (0, 0)
    rows = len(matrix)
    cols = len(matrix[0]) if matrix else 0
    return (rows, cols)

def is_square_matrix(matrix):
    """Check if matrix is square (rows == columns)."""
    rows, cols = get_matrix_dimensions(matrix)
    return rows == cols and rows > 0

def is_diagonal_matrix(matrix):
    """Check if matrix is diagonal (non-zero only on diagonal)."""
    if not is_square_matrix(matrix):
        return False

    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if i != j and matrix[i][j] != 0:
                return False
    return True

# Test functions
test_matrix = [[1, 0, 0], [0, 2, 0], [0, 0, 3]]
print(f"Dimensions: {get_matrix_dimensions(test_matrix)}")  # (3, 3)
print(f"Is square: {is_square_matrix(test_matrix)}")        # True
print(f"Is diagonal: {is_diagonal_matrix(test_matrix)}")    # True
```

---

## 🔧 Array Operations

### Element-wise Operations

```python
def add_arrays(arr1, arr2):
    """Add two arrays element-wise."""
    if len(arr1) != len(arr2):
        raise ValueError("Arrays must have same length")
    return [a + b for a, b in zip(arr1, arr2)]

def multiply_arrays(arr1, arr2):
    """Multiply two arrays element-wise."""
    if len(arr1) != len(arr2):
        raise ValueError("Arrays must have same length")
    return [a * b for a, b in zip(arr1, arr2)]

def scalar_multiply(arr, scalar):
    """Multiply array by scalar."""
    return [x * scalar for x in arr]

def array_sum(arr):
    """Calculate sum of array elements."""
    return sum(arr)

def array_mean(arr):
    """Calculate mean of array elements."""
    if not arr:
        return 0
    return sum(arr) / len(arr)

# Usage examples
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]

print(f"Array a: {a}")
print(f"Array b: {b}")
print(f"Sum: {add_arrays(a, b)}")        # [6, 8, 10, 12]
print(f"Product: {multiply_arrays(a, b)}") # [5, 12, 21, 32]
print(f"Scalar multiply (×3): {scalar_multiply(a, 3)}")  # [3, 6, 9, 12]
print(f"Sum of a: {array_sum(a)}")       # 10
print(f"Mean of a: {array_mean(a)}")     # 2.5
```

### Array Transformations

```python
def reverse_array(arr):
    """Reverse an array in place."""
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

def rotate_left(arr, k):
    """Rotate array left by k positions."""
    n = len(arr)
    k = k % n  # Handle k > n
    return arr[k:] + arr[:k]

def rotate_right(arr, k):
    """Rotate array right by k positions."""
    n = len(arr)
    k = k % n
    return arr[-k:] + arr[:-k]

def find_max_min(arr):
    """Find maximum and minimum values with their indices."""
    if not arr:
        return None, None, None, None

    max_val = max(arr)
    min_val = min(arr)
    max_idx = arr.index(max_val)
    min_idx = arr.index(min_val)

    return max_val, max_idx, min_val, min_idx

# Usage examples
test_arr = [1, 5, 3, 9, 2, 7]

print(f"Original: {test_arr}")
print(f"Reversed: {reverse_array(test_arr.copy())}")
print(f"Rotate left by 2: {rotate_left(test_arr, 2)}")
print(f"Rotate right by 2: {rotate_right(test_arr, 2)}")

max_val, max_idx, min_val, min_idx = find_max_min(test_arr)
print(f"Max: {max_val} at index {max_idx}")
print(f"Min: {min_val} at index {min_idx}")
```

---

## 📐 Matrix Operations

### Matrix Addition and Subtraction

```python
def add_matrices(matrix1, matrix2):
    """Add two matrices element-wise."""
    if get_matrix_dimensions(matrix1) != get_matrix_dimensions(matrix2):
        raise ValueError("Matrices must have same dimensions")

    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result

def subtract_matrices(matrix1, matrix2):
    """Subtract matrix2 from matrix1 element-wise."""
    if get_matrix_dimensions(matrix1) != get_matrix_dimensions(matrix2):
        raise ValueError("Matrices must have same dimensions")

    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] - matrix2[i][j])
        result.append(row)
    return result

# Usage
A = [[1, 2, 3], [4, 5, 6]]
B = [[6, 5, 4], [3, 2, 1]]

print("Matrix A:")
for row in A: print(row)
print("\nMatrix B:")
for row in B: print(row)

C = add_matrices(A, B)
print("\nA + B:")
for row in C: print(row)

D = subtract_matrices(A, B)
print("\nA - B:")
for row in D: print(row)
```

### Matrix Transposition

```python
def transpose_matrix(matrix):
    """Transpose a matrix (swap rows and columns)."""
    if not matrix:
        return []

    rows, cols = get_matrix_dimensions(matrix)
    result = []

    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        result.append(new_row)

    return result

def transpose_matrix_compact(matrix):
    """Transpose matrix using list comprehension."""
    if not matrix:
        return []
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

# Usage
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Original matrix:")
for row in matrix: print(row)

transposed = transpose_matrix(matrix)
print("\nTransposed:")
for row in transposed: print(row)

# Verify: transpose of transpose should equal original
double_transposed = transpose_matrix(transposed)
print("\nDouble transposed (should equal original):")
for row in double_transposed: print(row)
```

### Matrix Multiplication

```python
def multiply_matrices(matrix1, matrix2):
    """Multiply two matrices using standard matrix multiplication."""
    rows1, cols1 = get_matrix_dimensions(matrix1)
    rows2, cols2 = get_matrix_dimensions(matrix2)

    if cols1 != rows2:
        raise ValueError("Cannot multiply: columns of first matrix must equal rows of second")

    result = []
    for i in range(rows1):
        result_row = []
        for j in range(cols2):
            # Calculate dot product of row i from matrix1 and column j from matrix2
            sum_val = 0
            for k in range(cols1):
                sum_val += matrix1[i][k] * matrix2[k][j]
            result_row.append(sum_val)
        result.append(result_row)

    return result

def scalar_multiply_matrix(matrix, scalar):
    """Multiply matrix by scalar."""
    return [[element * scalar for element in row] for row in matrix]

# Usage examples
A = [[1, 2], [3, 4]]  # 2x2
B = [[5, 6], [7, 8]]  # 2x2

print("Matrix A:")
for row in A: print(row)
print("\nMatrix B:")
for row in B: print(row)

C = multiply_matrices(A, B)
print("\nA × B:")
for row in C: print(row)

# Scalar multiplication
D = scalar_multiply_matrix(A, 3)
print("\nA × 3:")
for row in D: print(row)
```

### Matrix-Vector Operations

```python
def multiply_matrix_vector(matrix, vector):
    """Multiply matrix by vector."""
    rows, cols = get_matrix_dimensions(matrix)
    if len(vector) != cols:
        raise ValueError("Vector length must equal matrix columns")

    result = []
    for i in range(rows):
        sum_val = 0
        for j in range(cols):
            sum_val += matrix[i][j] * vector[j]
        result.append(sum_val)
    return result

def create_identity_matrix(n):
    """Create n×n identity matrix."""
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]

def create_zero_matrix(rows, cols):
    """Create zero matrix with specified dimensions."""
    return [[0 for _ in range(cols)] for _ in range(rows)]

# Usage
matrix = [[1, 2, 3], [4, 5, 6]]
vector = [2, 1, 3]

print(f"Matrix: {matrix}")
print(f"Vector: {vector}")

result = multiply_matrix_vector(matrix, vector)
print(f"Matrix × Vector: {result}")  # [13, 31]

identity = create_identity_matrix(3)
print(f"\n3×3 Identity matrix:")
for row in identity: print(row)
```

---

## 🔍 Searching and Sorting

### Linear Search in Arrays

```python
def linear_search(arr, target):
    """Find target in array using linear search."""
    for i, element in enumerate(arr):
        if element == target:
            return i
    return -1

def linear_search_all(arr, target):
    """Find all occurrences of target in array."""
    indices = []
    for i, element in enumerate(arr):
        if element == target:
            indices.append(i)
    return indices

# Usage
arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
target = 5

index = linear_search(arr, target)
print(f"First occurrence of {target}: index {index}")

all_indices = linear_search_all(arr, target)
print(f"All occurrences of {target}: indices {all_indices}")
```

### Binary Search (requires sorted array)

```python
def binary_search(arr, target):
    """Find target in sorted array using binary search."""
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

def binary_search_recursive(arr, target, left=0, right=None):
    """Recursive binary search."""
    if right is None:
        right = len(arr) - 1

    if left > right:
        return -1

    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)

# Usage
sorted_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(f"Sorted array: {sorted_arr}")
print(f"Binary search for 7: index {binary_search(sorted_arr, 7)}")
print(f"Binary search for 11: index {binary_search(sorted_arr, 11)}")
print(f"Recursive binary search for 4: index {binary_search_recursive(sorted_arr, 4)}")
```

### Matrix Search

```python
def search_matrix(matrix, target):
    """Search for target in matrix (assuming row-wise sorted)."""
    if not matrix or not matrix[0]:
        return False

    rows, cols = get_matrix_dimensions(matrix)

    # Start from top-right corner
    row, col = 0, cols - 1

    while row < rows and col >= 0:
        if matrix[row][col] == target:
            return (row, col)
        elif matrix[row][col] < target:
            row += 1  # Move down
        else:
            col -= 1  # Move left

    return None

def find_max_in_matrix(matrix):
    """Find maximum value and its position in matrix."""
    if not matrix or not matrix[0]:
        return None, None, None

    max_val = matrix[0][0]
    max_row, max_col = 0, 0

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] > max_val:
                max_val = matrix[i][j]
                max_row, max_col = i, j

    return max_val, max_row, max_col

# Usage
matrix = [
    [1, 4, 7, 11],
    [2, 5, 8, 12],
    [3, 6, 9, 16]
]

print("Matrix:")
for row in matrix: print(row)

position = search_matrix(matrix, 8)
print(f"Position of 8: {position}")  # (1, 2)

max_val, max_row, max_col = find_max_in_matrix(matrix)
print(f"Maximum value {max_val} at position ({max_row}, {max_col})")
```

### Sorting Arrays and Matrices

```python
def bubble_sort(arr):
    """Sort array using bubble sort."""
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def selection_sort(arr):
    """Sort array using selection sort."""
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def sort_matrix_rows(matrix):
    """Sort each row of matrix."""
    return [sorted(row) for row in matrix]

def sort_matrix_columns(matrix):
    """Sort each column of matrix."""
    if not matrix:
        return []

    transposed = transpose_matrix(matrix)
    sorted_transposed = [sorted(col) for col in transposed]
    return transpose_matrix(sorted_transposed)

# Usage
arr = [64, 34, 25, 12, 22, 11, 90]
print(f"Original array: {arr}")
print(f"Bubble sort: {bubble_sort(arr.copy())}")
print(f"Selection sort: {selection_sort(arr.copy())}")

matrix = [
    [3, 1, 4],
    [1, 5, 9],
    [2, 6, 5]
]

print(f"\nOriginal matrix:")
for row in matrix: print(row)

print(f"\nRows sorted:")
sorted_rows = sort_matrix_rows(matrix)
for row in sorted_rows: print(row)

print(f"\nColumns sorted:")
sorted_cols = sort_matrix_columns(matrix)
for row in sorted_cols: print(row)
```

---

## 🧮 Common Algorithms

### Array Rotation and Reversal

```python
def rotate_array_left(arr, k):
    """Rotate array left by k positions efficiently."""
    n = len(arr)
    k = k % n
    return arr[k:] + arr[:k]

def rotate_array_right(arr, k):
    """Rotate array right by k positions efficiently."""
    n = len(arr)
    k = k % n
    return arr[-k:] + arr[:-k]

def reverse_array_in_place(arr):
    """Reverse array in place."""
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

def rotate_array_in_place(arr, k):
    """Rotate array in place using reversal algorithm."""
    n = len(arr)
    k = k % n

    # Reverse entire array
    reverse_array_in_place(arr)
    # Reverse first k elements
    reverse_array_in_place(arr[:k])
    # Reverse remaining elements
    reverse_array_in_place(arr[k:])
    return arr
```

### Matrix Algorithms

```python
def matrix_trace(matrix):
    """Calculate trace of square matrix (sum of diagonal elements)."""
    if not is_square_matrix(matrix):
        raise ValueError("Matrix must be square")

    return sum(matrix[i][i] for i in range(len(matrix)))

def matrix_determinant_2x2(matrix):
    """Calculate determinant of 2x2 matrix."""
    if get_matrix_dimensions(matrix) != (2, 2):
        raise ValueError("Matrix must be 2x2")

    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

def extract_diagonal(matrix):
    """Extract main diagonal of matrix."""
    n = min(get_matrix_dimensions(matrix))
    return [matrix[i][i] for i in range(n)]

def extract_anti_diagonal(matrix):
    """Extract anti-diagonal of matrix."""
    rows, cols = get_matrix_dimensions(matrix)
    n = min(rows, cols)
    return [matrix[i][n-1-i] for i in range(n)]

def is_symmetric_matrix(matrix):
    """Check if matrix is symmetric."""
    if not is_square_matrix(matrix):
        return False

    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True
```

### Image Processing Basics (using matrices)

```python
def create_image_matrix(width, height, default_value=0):
    """Create a simple image matrix representation."""
    return [[default_value for _ in range(width)] for _ in range(height)]

def get_pixel(image, x, y):
    """Get pixel value at position (x, y)."""
    if 0 <= y < len(image) and 0 <= x < len(image[0]):
        return image[y][x]
    return None

def set_pixel(image, x, y, value):
    """Set pixel value at position (x, y)."""
    if 0 <= y < len(image) and 0 <= x < len(image[0]):
        image[y][x] = value

def invert_image(image):
    """Invert image colors (assuming 0-255 range)."""
    return [[255 - pixel for pixel in row] for row in image]

def flip_image_horizontal(image):
    """Flip image horizontally."""
    return [row[::-1] for row in image]

def flip_image_vertical(image):
    """Flip image vertically."""
    return image[::-1]

# Usage
image = create_image_matrix(5, 3, 128)  # 5x3 image with gray pixels
print("Original image:")
for row in image: print(row)

# Set some pixels
set_pixel(image, 0, 0, 255)  # White pixel
set_pixel(image, 2, 1, 0)    # Black pixel

print("\nAfter setting pixels:")
for row in image: print(row)

print("\nInverted image:")
inverted = invert_image(image)
for row in inverted: print(row)
```

---

## ⚡ Performance Considerations

### Time Complexity Analysis

```python
# Different operations have different time complexities:

# Array operations
arr = [1, 2, 3, 4, 5]

arr[0]        # O(1) - Direct access
arr.append(6) # O(1) - Append to end
arr.insert(0, 0)  # O(n) - Insert at beginning
arr.remove(3)     # O(n) - Search and remove
3 in arr          # O(n) - Linear search

# Matrix operations
matrix = [[1, 2], [3, 4]]

# Element access: O(1)
element = matrix[0][1]

# Matrix addition: O(rows × cols)
# Matrix multiplication: O(rows1 × cols2 × cols1)

# Search algorithms
# Linear search: O(n)
# Binary search: O(log n) - requires sorted array
```

### Space Complexity

```python
# Array operations
original = [1, 2, 3, 4, 5]
copy_arr = original.copy()  # O(n) space

# Matrix operations
matrix = [[1, 2], [3, 4]]
transposed = transpose_matrix(matrix)  # O(rows × cols) space

# In-place operations (better space complexity)
def reverse_in_place(arr):
    # O(1) extra space
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
```

### Choosing the Right Approach

```python
# Example: Finding maximum in array
def find_max_loop(arr):
    """O(n) time, O(1) space"""
    if not arr:
        return None
    max_val = arr[0]
    for num in arr[1:]:
        if num > max_val:
            max_val = num
    return max_val

def find_max_builtin(arr):
    """O(n) time, O(1) space - same complexity, more readable"""
    return max(arr) if arr else None

# For large datasets, consider memory usage
def process_large_matrix_efficiently(matrix):
    """Process matrix without creating full copy"""
    rows, cols = get_matrix_dimensions(matrix)

    # Instead of creating new matrix, process element by element
    total = 0
    for i in range(rows):
        for j in range(cols):
            # Process each element without storing intermediate results
            total += matrix[i][j] * 2

    return total
```

---

## 🎯 Best Practices

### Code Organization

```python
class ArrayUtils:
    """Utility class for array operations."""

    @staticmethod
    def validate_array(arr, allow_empty=True):
        """Validate array input."""
        if not isinstance(arr, list):
            raise TypeError("Input must be a list")
        if not allow_empty and not arr:
            raise ValueError("Array cannot be empty")
        return True

    @staticmethod
    def validate_matrix(matrix):
        """Validate matrix input."""
        if not isinstance(matrix, list) or not matrix:
            raise TypeError("Matrix must be non-empty list of lists")

        row_length = len(matrix[0])
        for row in matrix:
            if not isinstance(row, list) or len(row) != row_length:
                raise ValueError("All rows must have same length")
        return True

class MatrixUtils:
    """Utility class for matrix operations."""

    @staticmethod
    def print_matrix(matrix, label="Matrix"):
        """Print matrix in readable format."""
        print(f"{label}:")
        for row in matrix:
            print(f"  {row}")
        print()

    @staticmethod
    def create_random_matrix(rows, cols, min_val=0, max_val=10):
        """Create matrix with random values."""
        import random
        return [[random.randint(min_val, max_val) for _ in range(cols)]
                for _ in range(rows)]
```

### Error Handling

```python
def safe_matrix_multiply(matrix1, matrix2):
    """Safely multiply matrices with comprehensive error handling."""
    try:
        # Validate inputs
        MatrixUtils.validate_matrix(matrix1)
        MatrixUtils.validate_matrix(matrix2)

        rows1, cols1 = get_matrix_dimensions(matrix1)
        rows2, cols2 = get_matrix_dimensions(matrix2)

        # Check dimensions
        if cols1 != rows2:
            raise ValueError(
                f"Cannot multiply: {cols1} columns ≠ {rows2} rows"
            )

        # Perform multiplication
        result = multiply_matrices(matrix1, matrix2)
        return result

    except (TypeError, ValueError) as e:
        print(f"Matrix multiplication error: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None
```

### Documentation and Testing

```python
def comprehensive_test():
    """Test all array and matrix functions."""

    # Test array operations
    a = [1, 2, 3]
    b = [4, 5, 6]

    # Test addition
    result = add_arrays(a, b)
    assert result == [5, 7, 9], f"Expected [5, 7, 9], got {result}"

    # Test matrix operations
    m1 = [[1, 2], [3, 4]]
    m2 = [[5, 6], [7, 8]]

    product = multiply_matrices(m1, m2)
    expected = [[19, 22], [43, 50]]
    assert product == expected, f"Expected {expected}, got {product}"

    # Test search functions
    arr = [1, 3, 5, 7, 9]
    assert binary_search(arr, 5) == 2, "Binary search failed"
    assert binary_search(arr, 4) == -1, "Binary search should return -1 for missing element"

    print("All tests passed! ✅")

# Run tests
if __name__ == "__main__":
    comprehensive_test()
```

---

## 🎯 Key Takeaways

1. **Arrays are Lists**: Use Python lists to represent one-dimensional arrays
2. **Matrices are Lists of Lists**: Two-dimensional arrays are represented as nested lists
3. **Performance Matters**: Choose algorithms based on time and space complexity
4. **Validation is Key**: Always validate input dimensions and types
5. **In-place Operations**: Modify arrays in place when possible to save memory
6. **Search Algorithms**: Use binary search for sorted arrays, linear search otherwise
7. **Matrix Operations**: Understand matrix multiplication rules and dimensions

---

## 🔗 Further Reading

- [Python Lists and Arrays](https://docs.python.org/3/tutorial/datastructures.html)
- [Matrix Operations](https://en.wikipedia.org/wiki/Matrix_(mathematics))
- [Algorithm Complexity](https://en.wikipedia.org/wiki/Time_complexity)
- [NumPy Documentation](https://numpy.org/doc/) (for advanced numerical computing)

---

## 📝 Practice Exercises

1. **Array Operations**: Implement functions to find duplicates, remove duplicates, and find unique elements
2. **Matrix Creation**: Create functions to generate special matrices (identity, diagonal, triangular)
3. **Matrix Transformations**: Implement matrix rotation (90, 180, 270 degrees)
4. **Search Algorithms**: Implement different search algorithms and compare their performance
5. **Sorting Algorithms**: Implement and compare different sorting algorithms for arrays
6. **Image Processing**: Create functions for basic image manipulations using matrix operations

---

**Tutorial Version**: 1.0
**Last Updated**: February 2026
**Estimated Reading Time**: 75 minutes