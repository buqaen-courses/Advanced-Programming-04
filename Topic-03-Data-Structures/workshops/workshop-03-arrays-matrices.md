# Workshop 1: Array and Matrix Operations

**Section**: 6 - Arrays and Matrices (90 min)
**Level**: Beginner to Intermediate
**Prerequisites**: Tutorial 1 (Arrays and Matrices)

---

## 🎯 Workshop Objectives

By the end of this workshop, you will:

1. **Master Array Operations**: Implement and test various array manipulation functions
2. **Build Matrix Utilities**: Create functions for matrix operations and transformations
3. **Apply Search Algorithms**: Implement efficient search and sorting algorithms
4. **Solve Real Problems**: Use arrays and matrices to solve computational problems
5. **Write Robust Code**: Include proper error handling and validation
6. **Test Your Solutions**: Create comprehensive tests for all functions

---

## 📋 Workshop Structure

1. [Setup and Environment](#setup-and-environment)
2. [Exercise 1: Array Manipulation Functions](#exercise-1-array-manipulation-functions)
3. [Exercise 2: Matrix Operations](#exercise-2-matrix-operations)
4. [Exercise 3: Search and Sort Algorithms](#exercise-3-search-and-sort-algorithms)
5. [Exercise 4: Practical Applications](#exercise-4-practical-applications)
6. [Challenge Exercises](#challenge-exercises)
7. [Solution Code](#solution-code)

---

## 🛠️ Setup and Environment

### Create Project Structure

```bash
# Create workshop directory
mkdir workshop-arrays-matrices
cd workshop-arrays-matrices

# Create Python files
touch array_utils.py matrix_utils.py test_workshop.py

# Optional: Create virtual environment
python -m venv venv
# Windows: venv\Scripts\activate
# macOS/Linux: source venv/bin/activate
```

### Import Required Modules

```python
# array_utils.py
"""
Array Utilities Workshop
A collection of functions for array operations
"""

# matrix_utils.py
"""
Matrix Utilities Workshop
A collection of functions for matrix operations
"""

# No external imports needed for this workshop
# All functionality uses built-in Python features
```

---

## 🏃 Exercise 1: Array Manipulation Functions

**Goal**: Create utility functions for common array operations

### Task 1.1: Array Statistics

Create a function that calculates various statistics for an array.

```python
def array_statistics(arr):
    """
    Calculate comprehensive statistics for an array.

    Args:
        arr: List of numbers

    Returns:
        Dictionary with statistics: count, sum, mean, median, mode, min, max, range, variance

    Examples:
        >>> stats = array_statistics([1, 2, 3, 4, 5])
        >>> print(stats['mean'], stats['median'])
        3.0 3.0
    """
    # TODO: Implement comprehensive statistics calculation
    # Handle empty arrays gracefully
    # Use appropriate formulas for variance
    pass
```

**Test your function:**
```python
# Test cases
test_arrays = [
    [1, 2, 3, 4, 5],
    [1, 1, 2, 2, 3],
    [],
    [42]
]

for i, arr in enumerate(test_arrays):
    print(f"Array {i+1}: {arr}")
    stats = array_statistics(arr)
    if stats:
        for key, value in stats.items():
            print(f"  {key}: {value}")
    else:
        print("  No statistics (empty array)")
    print()
```

### Task 1.2: Array Filtering and Transformation

Create functions to filter and transform arrays.

```python
def filter_by_condition(arr, condition_func):
    """
    Filter array elements based on a condition function.

    Args:
        arr: Input array
        condition_func: Function that takes an element and returns True/False

    Returns:
        New array with filtered elements

    Examples:
        >>> numbers = [1, 2, 3, 4, 5, 6]
        >>> filter_by_condition(numbers, lambda x: x % 2 == 0)
        [2, 4, 6]
    """
    # TODO: Implement filtering logic
    pass

def transform_array(arr, transform_func):
    """
    Transform each element in array using a transformation function.

    Args:
        arr: Input array
        transform_func: Function that takes an element and returns transformed value

    Returns:
        New array with transformed elements

    Examples:
        >>> transform_array([1, 2, 3], lambda x: x**2)
        [1, 4, 9]
    """
    # TODO: Implement transformation logic
    pass

def chain_operations(arr, operations):
    """
    Apply multiple operations to an array in sequence.

    Args:
        arr: Input array
        operations: List of functions to apply in order

    Returns:
        Array after applying all operations

    Examples:
        >>> ops = [lambda x: x*2, lambda x: x+1]
        >>> chain_operations([1, 2, 3], ops)
        [3, 5, 7]
    """
    # TODO: Implement operation chaining
    pass
```

**Test your functions:**
```python
# Test filtering
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter even numbers
evens = filter_by_condition(numbers, lambda x: x % 2 == 0)
print(f"Even numbers: {evens}")

# Filter numbers greater than 5
big_numbers = filter_by_condition(numbers, lambda x: x > 5)
print(f"Numbers > 5: {big_numbers}")

# Test transformation
original = [1, 2, 3, 4, 5]
squared = transform_array(original, lambda x: x**2)
print(f"Squared: {squared}")

# Test chaining
ops = [
    lambda x: x * 2,    # Double
    lambda x: x + 1,    # Add 1
    lambda x: x ** 0.5  # Square root
]
chained = chain_operations([1, 4, 9], ops)
print(f"Chained operations: {chained}")
```

### Task 1.3: Array Comparison and Set Operations

Create functions to compare arrays and perform set-like operations.

```python
def arrays_equal(arr1, arr2):
    """
    Check if two arrays are equal (same elements in same order).

    Args:
        arr1, arr2: Arrays to compare

    Returns:
        True if arrays are equal, False otherwise
    """
    # TODO: Implement array equality check
    pass

def array_intersection(arr1, arr2):
    """
    Find intersection of two arrays (elements common to both).

    Args:
        arr1, arr2: Input arrays

    Returns:
        Array of common elements (preserve order from first array)
    """
    # TODO: Implement intersection logic
    pass

def array_union(arr1, arr2):
    """
    Find union of two arrays (all unique elements from both).

    Args:
        arr1, arr2: Input arrays

    Returns:
        Array with all unique elements (preserve order)
    """
    # TODO: Implement union logic
    pass

def array_difference(arr1, arr2):
    """
    Find difference of arrays (elements in arr1 but not in arr2).

    Args:
        arr1, arr2: Input arrays

    Returns:
        Array of elements unique to arr1
    """
    # TODO: Implement difference logic
    pass
```

**Test your functions:**
```python
# Test arrays
a = [1, 2, 3, 4, 5]
b = [3, 4, 5, 6, 7]
c = [1, 2, 3, 4, 5]  # Same as a

print(f"Array A: {a}")
print(f"Array B: {b}")
print(f"Array C: {c}")
print()

print(f"A equals B: {arrays_equal(a, b)}")
print(f"A equals C: {arrays_equal(a, c)}")
print()

print(f"A ∩ B (intersection): {array_intersection(a, b)}")
print(f"A ∪ B (union): {array_union(a, b)}")
print(f"A - B (difference): {array_difference(a, b)}")
print(f"B - A (difference): {array_difference(b, a)}")
```

---

## 📊 Exercise 2: Matrix Operations

**Goal**: Implement essential matrix operations and utilities

### Task 2.1: Matrix Creation and Validation

Create functions to create and validate matrices.

```python
def create_matrix(rows, cols, default_value=0):
    """
    Create a matrix with specified dimensions and default value.

    Args:
        rows: Number of rows
        cols: Number of columns
        default_value: Value to fill matrix with

    Returns:
        2D list representing the matrix
    """
    # TODO: Create matrix with specified dimensions
    pass

def create_identity_matrix(n):
    """
    Create n×n identity matrix.

    Args:
        n: Size of identity matrix

    Returns:
        Identity matrix as 2D list
    """
    # TODO: Create identity matrix
    pass

def validate_matrix(matrix):
    """
    Validate that input is a proper matrix (rectangular 2D list).

    Args:
        matrix: Input to validate

    Returns:
        True if valid matrix, raises ValueError otherwise

    Raises:
        ValueError: If input is not a valid matrix
    """
    # TODO: Implement matrix validation
    pass

def get_matrix_dimensions(matrix):
    """
    Get dimensions of matrix.

    Args:
        matrix: Input matrix

    Returns:
        Tuple (rows, columns)
    """
    # TODO: Return matrix dimensions
    pass
```

**Test your functions:**
```python
# Test matrix creation
zero_matrix = create_matrix(3, 4, 0)
print("3×4 Zero matrix:")
for row in zero_matrix: print(row)
print()

identity = create_identity_matrix(3)
print("3×3 Identity matrix:")
for row in identity: print(row)
print()

# Test validation
valid_matrix = [[1, 2, 3], [4, 5, 6]]
invalid_matrix = [[1, 2], [3, 4, 5]]  # Irregular rows

print(f"Valid matrix dimensions: {get_matrix_dimensions(valid_matrix)}")
try:
    validate_matrix(valid_matrix)
    print("Valid matrix passed validation")
except ValueError as e:
    print(f"Validation error: {e}")

try:
    validate_matrix(invalid_matrix)
    print("Invalid matrix passed validation (unexpected)")
except ValueError as e:
    print(f"Invalid matrix correctly rejected: {e}")
```

### Task 2.2: Matrix Arithmetic

Implement basic matrix arithmetic operations.

```python
def add_matrices(matrix1, matrix2):
    """
    Add two matrices element-wise.

    Args:
        matrix1, matrix2: Matrices to add

    Returns:
        Result matrix

    Raises:
        ValueError: If matrices have incompatible dimensions
    """
    # TODO: Implement matrix addition
    pass

def scalar_multiply_matrix(matrix, scalar):
    """
    Multiply matrix by scalar.

    Args:
        matrix: Input matrix
        scalar: Scalar value

    Returns:
        Scaled matrix
    """
    # TODO: Implement scalar multiplication
    pass

def transpose_matrix(matrix):
    """
    Transpose a matrix (swap rows and columns).

    Args:
        matrix: Input matrix

    Returns:
        Transposed matrix
    """
    # TODO: Implement matrix transposition
    pass

def matrix_trace(matrix):
    """
    Calculate trace of square matrix (sum of diagonal elements).

    Args:
        matrix: Square matrix

    Returns:
        Trace value

    Raises:
        ValueError: If matrix is not square
    """
    # TODO: Implement matrix trace calculation
    pass
```

**Test your functions:**
```python
# Test matrices
A = [[1, 2, 3], [4, 5, 6]]
B = [[6, 5, 4], [3, 2, 1]]
C = [[1, 2], [3, 4], [5, 6]]  # Different dimensions

print("Matrix A:")
for row in A: print(row)
print("\nMatrix B:")
for row in B: print(row)
print()

# Test addition
try:
    sum_matrix = add_matrices(A, B)
    print("A + B:")
    for row in sum_matrix: print(row)
except ValueError as e:
    print(f"Addition failed: {e}")

# Test scalar multiplication
scaled = scalar_multiply_matrix(A, 2)
print("\nA × 2:")
for row in scaled: print(row)

# Test transpose
transposed = transpose_matrix(A)
print("\nTranspose of A:")
for row in transposed: print(row)

# Test trace
square_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
trace = matrix_trace(square_matrix)
print(f"\nTrace of square matrix: {trace}")
```

### Task 2.3: Matrix Search and Analysis

Create functions to search and analyze matrices.

```python
def find_in_matrix(matrix, target):
    """
    Find first occurrence of target in matrix.

    Args:
        matrix: Input matrix
        target: Value to search for

    Returns:
        Tuple (row, col) if found, None otherwise
    """
    # TODO: Implement matrix search
    pass

def find_max_in_matrix(matrix):
    """
    Find maximum value and its position in matrix.

    Args:
        matrix: Input matrix

    Returns:
        Tuple (max_value, row, col)
    """
    # TODO: Find maximum value and position
    pass

def matrix_row_sums(matrix):
    """
    Calculate sum of each row in matrix.

    Args:
        matrix: Input matrix

    Returns:
        List of row sums
    """
    # TODO: Calculate row sums
    pass

def matrix_column_sums(matrix):
    """
    Calculate sum of each column in matrix.

    Args:
        matrix: Input matrix

    Returns:
        List of column sums
    """
    # TODO: Calculate column sums
    pass

def is_symmetric_matrix(matrix):
    """
    Check if matrix is symmetric (equal to its transpose).

    Args:
        matrix: Input matrix

    Returns:
        True if symmetric, False otherwise
    """
    # TODO: Check matrix symmetry
    pass
```

**Test your functions:**
```python
# Test matrix
test_matrix = [
    [1, 8, 3],
    [4, 5, 6],
    [7, 2, 9]
]

print("Test matrix:")
for row in test_matrix: print(row)
print()

# Test search
position = find_in_matrix(test_matrix, 5)
print(f"Position of 5: {position}")

missing = find_in_matrix(test_matrix, 10)
print(f"Position of 10: {missing}")

# Test max finding
max_val, max_row, max_col = find_max_in_matrix(test_matrix)
print(f"Maximum {max_val} at position ({max_row}, {max_col})")

# Test sums
row_sums = matrix_row_sums(test_matrix)
print(f"Row sums: {row_sums}")

col_sums = matrix_column_sums(test_matrix)
print(f"Column sums: {col_sums}")

# Test symmetry
symmetric = [[1, 2, 3], [2, 4, 5], [3, 5, 6]]
asymmetric = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(f"Symmetric matrix is symmetric: {is_symmetric_matrix(symmetric)}")
print(f"Asymmetric matrix is symmetric: {is_symmetric_matrix(asymmetric)}")
```

---

## 🔍 Exercise 3: Search and Sort Algorithms

**Goal**: Implement efficient search and sort algorithms for arrays

### Task 3.1: Search Algorithms

Implement different search algorithms and compare their performance.

```python
def linear_search(arr, target):
    """
    Linear search - check each element sequentially.

    Args:
        arr: Array to search
        target: Value to find

    Returns:
        Index of target if found, -1 otherwise
    """
    # TODO: Implement linear search
    pass

def binary_search(arr, target):
    """
    Binary search - requires sorted array.

    Args:
        arr: Sorted array to search
        target: Value to find

    Returns:
        Index of target if found, -1 otherwise
    """
    # TODO: Implement binary search
    pass

def interpolation_search(arr, target):
    """
    Interpolation search - for uniformly distributed data.

    Args:
        arr: Sorted array to search
        target: Value to find

    Returns:
        Index of target if found, -1 otherwise
    """
    # TODO: Implement interpolation search
    pass

def find_all_occurrences(arr, target):
    """
    Find all occurrences of target in array.

    Args:
        arr: Array to search
        target: Value to find

    Returns:
        List of indices where target appears
    """
    # TODO: Find all occurrences
    pass
```

**Test your search functions:**
```python
import time

# Test arrays
small_array = [1, 3, 5, 7, 9, 11, 13, 15]
large_array = list(range(0, 10000, 2))  # Even numbers 0-9998

target = 500

print(f"Searching for {target} in array of size {len(large_array)}")

# Test linear search
start = time.time()
linear_result = linear_search(large_array, target)
linear_time = time.time() - start
print(f"Linear search: index {linear_result}, time: {linear_time:.6f}s")

# Test binary search
start = time.time()
binary_result = binary_search(large_array, target)
binary_time = time.time() - start
print(f"Binary search: index {binary_result}, time: {binary_time:.6f}s")

# Test with unsorted array for linear search
unsorted = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
occurrences = find_all_occurrences(unsorted, 5)
print(f"All occurrences of 5 in {unsorted}: indices {occurrences}")
```

### Task 3.2: Sort Algorithms

Implement different sorting algorithms.

```python
def bubble_sort(arr):
    """
    Bubble sort - repeatedly swap adjacent elements.

    Args:
        arr: Array to sort (modified in place)

    Returns:
        Sorted array
    """
    # TODO: Implement bubble sort
    pass

def selection_sort(arr):
    """
    Selection sort - find minimum and swap.

    Args:
        arr: Array to sort (modified in place)

    Returns:
        Sorted array
    """
    # TODO: Implement selection sort
    pass

def insertion_sort(arr):
    """
    Insertion sort - build sorted array one element at a time.

    Args:
        arr: Array to sort (modified in place)

    Returns:
        Sorted array
    """
    # TODO: Implement insertion sort
    pass

def merge_sort(arr):
    """
    Merge sort - divide and conquer algorithm.

    Args:
        arr: Array to sort

    Returns:
        New sorted array (original unchanged)
    """
    # TODO: Implement merge sort
    pass

def quick_sort(arr):
    """
    Quick sort - partition and sort recursively.

    Args:
        arr: Array to sort

    Returns:
        New sorted array (original unchanged)
    """
    # TODO: Implement quick sort
    pass
```

**Test your sort functions:**
```python
import time
import random

# Test data
small_test = [64, 34, 25, 12, 22, 11, 90]
large_test = [random.randint(0, 1000) for _ in range(1000)]

print("Testing sort algorithms on small array:")
print(f"Original: {small_test}")

# Test each algorithm
algorithms = [
    ("Bubble sort", bubble_sort),
    ("Selection sort", selection_sort),
    ("Insertion sort", insertion_sort),
    ("Merge sort", merge_sort),
    ("Quick sort", quick_sort)
]

for name, sort_func in algorithms:
    test_copy = small_test.copy()
    start = time.time()
    result = sort_func(test_copy)
    elapsed = time.time() - start
    print(f"{name}: {result}, time: {elapsed:.6f}s")

print("\nTesting on large array (1000 elements):")
for name, sort_func in algorithms:
    test_copy = large_test.copy()
    start = time.time()
    result = sort_func(test_copy)
    elapsed = time.time() - start
    print(f"{name}: {elapsed:.4f}s")
```

---

## 🌍 Exercise 4: Practical Applications

**Goal**: Apply array and matrix operations to solve real-world problems

### Task 4.1: Image Processing Basics

Create basic image processing functions using matrices.

```python
def create_image_matrix(width, height, default_color=128):
    """
    Create a simple grayscale image matrix.

    Args:
        width: Image width
        height: Image height
        default_color: Default pixel value (0-255)

    Returns:
        2D list representing image
    """
    # TODO: Create image matrix
    pass

def invert_image(image):
    """
    Invert image colors.

    Args:
        image: 2D list representing image

    Returns:
        Inverted image
    """
    # TODO: Invert pixel values
    pass

def flip_image_horizontal(image):
    """
    Flip image horizontally.

    Args:
        image: 2D list representing image

    Returns:
        Horizontally flipped image
    """
    # TODO: Flip image horizontally
    pass

def apply_threshold(image, threshold=128):
    """
    Apply threshold to create binary image.

    Args:
        image: 2D list representing image
        threshold: Threshold value

    Returns:
        Binary image (0 or 255)
    """
    # TODO: Apply thresholding
    pass

def get_pixel_region(image, x, y, width, height):
    """
    Extract region from image.

    Args:
        image: 2D list representing image
        x, y: Top-left corner coordinates
        width, height: Region dimensions

    Returns:
        Extracted region or None if invalid
    """
    # TODO: Extract image region
    pass
```

**Test your image processing functions:**
```python
# Create test image
image = create_image_matrix(5, 4, 100)
print("Original image:")
for row in image: print(row)

# Modify some pixels
image[0][0] = 255  # White pixel
image[1][1] = 0    # Black pixel
image[2][2] = 128  # Gray pixel

print("\nModified image:")
for row in image: print(row)

# Test operations
inverted = invert_image(image)
print("\nInverted image:")
for row in inverted: print(row)

flipped = flip_image_horizontal(image)
print("\nHorizontally flipped:")
for row in flipped: print(row)

binary = apply_threshold(image, 127)
print("\nBinary image (threshold 127):")
for row in binary: print(row)

# Extract region
region = get_pixel_region(image, 1, 1, 3, 2)
if region:
    print("\nExtracted region (1,1 to 3,2):")
    for row in region: print(row)
```

### Task 4.2: Data Analysis with Arrays

Create functions for basic data analysis.

```python
def calculate_moving_average(data, window_size):
    """
    Calculate moving average of data.

    Args:
        data: List of numbers
        window_size: Size of moving window

    Returns:
        List of moving averages
    """
    # TODO: Calculate moving averages
    pass

def find_peaks(data, threshold=None):
    """
    Find peaks in data (local maxima).

    Args:
        data: List of numbers
        threshold: Minimum value to consider as peak

    Returns:
        List of indices where peaks occur
    """
    # TODO: Find peaks in data
    pass

def normalize_array(data, method="minmax"):
    """
    Normalize array data.

    Args:
        data: List of numbers
        method: Normalization method ("minmax" or "zscore")

    Returns:
        Normalized data
    """
    # TODO: Normalize data
    pass

def detect_outliers(data, method="iqr", threshold=1.5):
    """
    Detect outliers in data.

    Args:
        data: List of numbers
        method: Outlier detection method ("iqr" or "zscore")
        threshold: Outlier threshold

    Returns:
        Tuple (normal_data, outliers, outlier_indices)
    """
    # TODO: Detect outliers
    pass

def correlation_coefficient(x, y):
    """
    Calculate Pearson correlation coefficient between two arrays.

    Args:
        x, y: Arrays of equal length

    Returns:
        Correlation coefficient (-1 to 1)
    """
    # TODO: Calculate correlation
    pass
```

**Test your data analysis functions:**
```python
import random

# Generate test data
data = [random.gauss(50, 10) for _ in range(20)]
data.extend([200, -10, 150])  # Add outliers

print(f"Test data ({len(data)} points): {['.1f' for x in data[:10]]}...")

# Test moving average
moving_avg = calculate_moving_average(data, 5)
print(f"Moving average (window=5): {['.1f' for x in moving_avg[:5]]}...")

# Test normalization
normalized = normalize_array(data, "minmax")
print(f"Min-max normalized: {['.2f' for x in normalized[:5]]}...")

# Test outlier detection
normal, outliers, outlier_indices = detect_outliers(data, "iqr")
print(f"Found {len(outliers)} outliers at indices: {outlier_indices}")
print(f"Outlier values: {['.1f' for x in outliers]}")

# Test correlation
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
correlation = correlation_coefficient(x, y)
print(f"Correlation between {x} and {y}: {correlation:.3f}")
```

---

## 🚀 Challenge Exercises

### Challenge 1: Matrix Multiplication Optimization

Implement and compare different matrix multiplication algorithms.

```python
def matrix_multiply_standard(A, B):
    """Standard matrix multiplication - O(n^3)"""
    # TODO: Implement standard matrix multiplication
    pass

def matrix_multiply_strassen(A, B):
    """Strassen's algorithm - O(n^2.81) for large matrices"""
    # TODO: Implement Strassen's algorithm (advanced)
    pass

def benchmark_matrix_multiplication():
    """Compare performance of different multiplication algorithms"""
    # TODO: Create benchmark comparing algorithms
    pass
```

### Challenge 2: Advanced Image Processing

Implement more sophisticated image processing operations.

```python
def apply_convolution(image, kernel):
    """Apply convolution filter to image."""
    # TODO: Implement 2D convolution
    pass

def resize_image(image, new_width, new_height):
    """Resize image using nearest neighbor interpolation."""
    # TODO: Implement image resizing
    pass

def detect_edges(image, method="sobel"):
    """Detect edges in image."""
    # TODO: Implement edge detection
    pass
```

### Challenge 3: Path Finding in Matrix

Implement path finding algorithms for matrix-based grids.

```python
def find_shortest_path(matrix, start, end):
    """Find shortest path in matrix grid using BFS."""
    # TODO: Implement BFS for grid path finding
    pass

def find_all_paths(matrix, start, end, max_length=None):
    """Find all possible paths from start to end."""
    # TODO: Implement DFS to find all paths
    pass
```

---

## ✅ Solution Code

### Exercise 1 Solutions

```python
import statistics
from collections import Counter

def array_statistics(arr):
    """Calculate comprehensive statistics for an array."""
    if not arr:
        return None

    return {
        'count': len(arr),
        'sum': sum(arr),
        'mean': statistics.mean(arr),
        'median': statistics.median(arr),
        'mode': statistics.mode(arr) if len(set(arr)) < len(arr) else None,
        'min': min(arr),
        'max': max(arr),
        'range': max(arr) - min(arr),
        'variance': statistics.variance(arr) if len(arr) > 1 else 0,
        'stdev': statistics.stdev(arr) if len(arr) > 1 else 0
    }

def filter_by_condition(arr, condition_func):
    """Filter array elements based on condition."""
    return [x for x in arr if condition_func(x)]

def transform_array(arr, transform_func):
    """Transform array elements."""
    return [transform_func(x) for x in arr]

def chain_operations(arr, operations):
    """Apply multiple operations in sequence."""
    result = arr.copy()
    for operation in operations:
        result = [operation(x) for x in result]
    return result

def arrays_equal(arr1, arr2):
    """Check if arrays are equal."""
    return arr1 == arr2

def array_intersection(arr1, arr2):
    """Find intersection preserving order from first array."""
    set2 = set(arr2)
    return [x for x in arr1 if x in set2]

def array_union(arr1, arr2):
    """Find union preserving order."""
    result = arr1.copy()
    seen = set(arr1)
    for x in arr2:
        if x not in seen:
            result.append(x)
            seen.add(x)
    return result

def array_difference(arr1, arr2):
    """Find elements in arr1 but not in arr2."""
    set2 = set(arr2)
    return [x for x in arr1 if x not in set2]
```

### Exercise 2 Solutions

```python
def create_matrix(rows, cols, default_value=0):
    """Create matrix with specified dimensions."""
    return [[default_value for _ in range(cols)] for _ in range(rows)]

def create_identity_matrix(n):
    """Create identity matrix."""
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]

def validate_matrix(matrix):
    """Validate matrix structure."""
    if not isinstance(matrix, list) or not matrix:
        raise ValueError("Matrix must be non-empty list")

    if not all(isinstance(row, list) for row in matrix):
        raise ValueError("All elements must be lists")

    row_lengths = [len(row) for row in matrix]
    if len(set(row_lengths)) != 1:
        raise ValueError("All rows must have same length")

    return True

def get_matrix_dimensions(matrix):
    """Get matrix dimensions."""
    if not matrix:
        return (0, 0)
    return (len(matrix), len(matrix[0]))

def add_matrices(matrix1, matrix2):
    """Add two matrices."""
    validate_matrix(matrix1)
    validate_matrix(matrix2)

    if get_matrix_dimensions(matrix1) != get_matrix_dimensions(matrix2):
        raise ValueError("Matrices must have same dimensions")

    rows, cols = get_matrix_dimensions(matrix1)
    return [[matrix1[i][j] + matrix2[i][j] for j in range(cols)] for i in range(rows)]

def scalar_multiply_matrix(matrix, scalar):
    """Multiply matrix by scalar."""
    validate_matrix(matrix)
    return [[x * scalar for x in row] for row in matrix]

def transpose_matrix(matrix):
    """Transpose matrix."""
    validate_matrix(matrix)
    rows, cols = get_matrix_dimensions(matrix)
    return [[matrix[j][i] for j in range(rows)] for i in range(cols)]

def matrix_trace(matrix):
    """Calculate matrix trace."""
    validate_matrix(matrix)
    rows, cols = get_matrix_dimensions(matrix)
    if rows != cols:
        raise ValueError("Matrix must be square")
    return sum(matrix[i][i] for i in range(rows))

def find_in_matrix(matrix, target):
    """Find first occurrence in matrix."""
    validate_matrix(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == target:
                return (i, j)
    return None

def find_max_in_matrix(matrix):
    """Find maximum value and position."""
    validate_matrix(matrix)
    max_val = matrix[0][0]
    max_pos = (0, 0)

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] > max_val:
                max_val = matrix[i][j]
                max_pos = (i, j)

    return max_val, max_pos[0], max_pos[1]

def matrix_row_sums(matrix):
    """Calculate row sums."""
    validate_matrix(matrix)
    return [sum(row) for row in matrix]

def matrix_column_sums(matrix):
    """Calculate column sums."""
    validate_matrix(matrix)
    rows, cols = get_matrix_dimensions(matrix)
    return [sum(matrix[i][j] for i in range(rows)) for j in range(cols)]

def is_symmetric_matrix(matrix):
    """Check if matrix is symmetric."""
    validate_matrix(matrix)
    rows, cols = get_matrix_dimensions(matrix)
    if rows != cols:
        return False

    for i in range(rows):
        for j in range(i + 1, cols):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True
```

### Exercise 3 Solutions

```python
def linear_search(arr, target):
    """Linear search implementation."""
    for i, element in enumerate(arr):
        if element == target:
            return i
    return -1

def binary_search(arr, target):
    """Binary search implementation."""
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

def interpolation_search(arr, target):
    """Interpolation search implementation."""
    low, high = 0, len(arr) - 1

    while low <= high and arr[low] <= target <= arr[high]:
        # Interpolation formula
        if arr[high] == arr[low]:
            if arr[low] == target:
                return low
            else:
                return -1

        pos = low + ((high - low) // (arr[high] - arr[low])) * (target - arr[low])

        if pos < low or pos > high:
            return -1

        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return -1

def find_all_occurrences(arr, target):
    """Find all occurrences of target."""
    return [i for i, x in enumerate(arr) if x == target]

def bubble_sort(arr):
    """Bubble sort implementation."""
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def selection_sort(arr):
    """Selection sort implementation."""
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def insertion_sort(arr):
    """Insertion sort implementation."""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def merge_sort(arr):
    """Merge sort implementation."""
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    """Helper function for merge sort."""
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

def quick_sort(arr):
    """Quick sort implementation."""
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)
```

---

## 🧪 Testing Your Solutions

Create a comprehensive test file:

```python
# test_workshop.py
import array_utils
import matrix_utils

def test_array_statistics():
    """Test array statistics function."""
    # Normal case
    stats = array_utils.array_statistics([1, 2, 3, 4, 5])
    assert stats['mean'] == 3.0
    assert stats['median'] == 3.0
    assert stats['min'] == 1
    assert stats['max'] == 5

    # Empty array
    assert array_utils.array_statistics([]) is None

    print("✓ Array statistics tests passed")

def test_matrix_operations():
    """Test matrix operations."""
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]

    # Test addition
    result = matrix_utils.add_matrices(A, B)
    expected = [[6, 8], [10, 12]]
    assert result == expected

    # Test transpose
    transposed = matrix_utils.transpose_matrix(A)
    expected_transpose = [[1, 3], [2, 4]]
    assert transposed == expected_transpose

    # Test trace
    trace = matrix_utils.matrix_trace(A)
    assert trace == 5  # 1 + 4

    print("✓ Matrix operations tests passed")

def test_search_algorithms():
    """Test search algorithms."""
    arr = [1, 3, 5, 7, 9, 11]

    # Linear search
    assert array_utils.linear_search(arr, 5) == 2
    assert array_utils.linear_search(arr, 10) == -1

    # Binary search
    assert array_utils.binary_search(arr, 5) == 2
    assert array_utils.binary_search(arr, 10) == -1

    print("✓ Search algorithms tests passed")

def test_sort_algorithms():
    """Test sorting algorithms."""
    test_arr = [64, 34, 25, 12, 22, 11, 90]
    expected = [11, 12, 22, 25, 34, 64, 90]

    # Test each algorithm
    assert array_utils.bubble_sort(test_arr.copy()) == expected
    assert array_utils.selection_sort(test_arr.copy()) == expected
    assert array_utils.insertion_sort(test_arr.copy()) == expected
    assert array_utils.merge_sort(test_arr.copy()) == expected
    assert array_utils.quick_sort(test_arr.copy()) == expected

    print("✓ Sort algorithms tests passed")

if __name__ == "__main__":
    test_array_statistics()
    test_matrix_operations()
    test_search_algorithms()
    test_sort_algorithms()
    print("🎉 All workshop tests passed!")
```

---

## 📝 Key Takeaways

1. **Arrays are Powerful**: Lists provide efficient array operations for most applications
2. **Matrix Operations**: Understand dimensions and compatibility rules for matrix operations
3. **Search Algorithms**: Choose appropriate search algorithm based on data characteristics
4. **Sort Performance**: Different sorting algorithms have different time/space complexity trade-offs
5. **Real-World Applications**: Arrays and matrices solve many computational problems
6. **Error Handling**: Always validate input dimensions and handle edge cases
7. **Performance Matters**: Consider time and space complexity when choosing algorithms

---

**Workshop Version**: 1.0
**Last Updated**: February 2026
**Estimated Completion Time**: 120 minutes