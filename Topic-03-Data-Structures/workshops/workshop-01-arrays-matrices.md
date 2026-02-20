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
2. [Exercise 1: Array Operations & Algorithms](#exercise-1-array-operations--algorithms)
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
touch array_operations.py matrix_operations.py test_workshop.py

# Optional: Create virtual environment
python -m venv venv
# Windows: venv\Scripts\activate
# macOS/Linux: source venv/bin/activate
```

### Import Required Modules

```python
# array_operations.py
"""
Array Operations Workshop
A collection of functions for array algorithms
"""

# matrix_operations.py
"""
Matrix Operations Workshop
A collection of functions for matrix operations
"""

# No external imports needed for this workshop
# All functionality uses built-in Python features
```

---

## 🏃 Exercise 1: Array Operations & Algorithms

**Goal**: Create utility functions for common array operations

### Task 1.1: Array Statistics

Create a function that calculates various statistics for an array.

```python
from typing import List
import statistics

def array_statistics(arr: List[float]) -> dict:
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
def filter_by_condition(arr: List[int], condition_func) -> List[int]:
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

def transform_array(arr: List[int], transform_func) -> List[int]:
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

def chain_operations(arr: List[int], operations: List[callable]) -> List[int]:
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

---

## 📊 Exercise 2: Matrix Operations

**Goal**: Implement essential matrix operations and utilities

### Task 2.1: Basic Matrix Operations

Create functions for basic matrix operations.

```python
def create_matrix(rows: int, cols: int, default_value: int = 0) -> List[List[int]]:
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

def validate_matrix(matrix: List[List[int]]) -> bool:
    """
    Validate that input is a proper matrix (rectangular 2D list).

    Args:
        matrix: Input to validate

    Returns:
        True if valid matrix, raises ValueError otherwise
    """
    # TODO: Implement matrix validation
    pass

def add_matrices(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
    """
    Add two matrices element-wise.

    Args:
        A, B: Matrices to add

    Returns:
        Result matrix

    Raises:
        ValueError: If matrices have incompatible dimensions
    """
    # TODO: Implement matrix addition
    pass

def transpose_matrix(A: List[List[int]]) -> List[List[int]]:
    """
    Transpose a matrix (swap rows and columns).

    Args:
        A: Matrix to transpose

    Returns:
        Transposed matrix
    """
    # TODO: Implement matrix transposition
    pass
```

**Test your functions:**
```python
# Test matrix creation
zero_matrix = create_matrix(3, 4, 0)
print("3×4 Zero matrix:")
for row in zero_matrix: print(row)
print()

# Test validation
valid_matrix = [[1, 2, 3], [4, 5, 6]]
invalid_matrix = [[1, 2], [3, 4, 5]]  # Irregular rows

print(f"Valid matrix validation: {validate_matrix(valid_matrix)}")
try:
    validate_matrix(invalid_matrix)
    print("Invalid matrix passed validation (unexpected)")
except ValueError as e:
    print(f"Invalid matrix correctly rejected: {e}")

# Test addition
A = [[1, 2, 3], [4, 5, 6]]
B = [[6, 5, 4], [3, 2, 1]]

try:
    sum_matrix = add_matrices(A, B)
    print("\nA + B:")
    for row in sum_matrix: print(row)
except ValueError as e:
    print(f"Addition failed: {e}")

# Test transpose
transposed = transpose_matrix(A)
print("\nTranspose of A:")
for row in transposed: print(row)
```

---

## 🔍 Exercise 3: Search and Sort Algorithms

**Goal**: Implement efficient search and sort algorithms for arrays

### Task 3.1: Search Algorithms

Implement different search algorithms and compare their performance.

```python
def linear_search(arr: List[int], target: int) -> int:
    """
    Linear search - check each element sequentially.

    Args:
        arr: Array to search
        target: Value to search for

    Returns:
        Index of target if found, -1 otherwise
    """
    # TODO: Implement linear search
    pass

def binary_search(arr: List[int], target: int) -> int:
    """
    Binary search - requires sorted array.

    Args:
        arr: Sorted array to search
        target: Value to search for

    Returns:
        Index of target if found, -1 otherwise
    """
    # TODO: Implement binary search
    pass

def find_all_occurrences(arr: List[int], target: int) -> List[int]:
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
def bubble_sort(arr: List[int]) -> None:
    """
    Sort array using bubble sort (in-place).

    Args:
        arr: Array to sort (modified in place)
    """
    # TODO: Implement bubble sort
    pass

def selection_sort(arr: List[int]) -> None:
    """
    Sort array using selection sort (in-place).

    Args:
        arr: Array to sort (modified in place)
    """
    # TODO: Implement selection sort
    pass

def insertion_sort(arr: List[int]) -> None:
    """
    Sort array using insertion sort (in-place).

    Args:
        arr: Array to sort (modified in place)
    """
    # TODO: Implement insertion sort
    pass
```

**Test your sort functions:**
```python
import random

# Test data
small_test = [64, 34, 25, 12, 22, 11, 90]
large_test = [random.randint(0, 1000) for _ in range(1000)]

print("Testing sort algorithms on small array:")
print(f"Original: {small_test}")

algorithms = [
    ("Bubble sort", bubble_sort),
    ("Selection sort", selection_sort),
    ("Insertion sort", insertion_sort)
]

for name, sort_func in algorithms:
    test_copy = small_test.copy()
    sort_func(test_copy)
    print(f"{name}: {test_copy}")

print("\nTesting on large array (1000 elements):")
for name, sort_func in algorithms:
    test_copy = large_test.copy()
    start = time.time()
    sort_func(test_copy)
    elapsed = time.time() - start
    print(f"{name}: {elapsed:.4f}s")
```

---

## 🌍 Exercise 4: Practical Applications

**Goal**: Apply array and matrix operations to solve real-world problems

### Task 4.1: Simple Image Processing

Create basic image processing functions using matrices.

```python
def create_image(width: int, height: int, default_value: int = 128) -> List[List[int]]:
    """
    Create a simple grayscale image matrix.

    Args:
        width: Image width
        height: Image height
        default_value: Default pixel value (0-255)

    Returns:
        2D list representing image
    """
    # TODO: Create image matrix
    pass

def invert_image(image: List[List[int]]) -> List[List[int]]:
    """
    Invert image colors.

    Args:
        image: 2D list representing image

    Returns:
        Inverted image
    """
    # TODO: Invert pixel values
    pass

def apply_threshold(image: List[List[int]], threshold: int) -> List[List[int]]:
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
```

**Test your image processing functions:**
```python
# Create test image
image = create_image(3, 3, 100)
print("Original image:")
for row in image: print(row)

# Modify some pixels to simulate an image
image[0][0] = 255  # White pixel
image[1][1] = 0    # Black pixel
image[2][2] = 128  # Gray pixel

print("\nModified image:")
for row in image: print(row)

# Test operations
inverted = invert_image(image)
print("\nInverted image:")
for row in inverted: print(row)

binary = apply_threshold(image, 127)
print("\nBinary image (threshold 127):")
for row in binary: print(row)
```

---

## 🚀 Challenge Exercises

### Challenge 1: Matrix Multiplication

Implement matrix multiplication from scratch.

```python
def multiply_matrices(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
    """
    Multiply two matrices using standard matrix multiplication.

    Args:
        A, B: Matrices to multiply

    Returns:
        Result matrix

    Raises:
        ValueError: If matrices have incompatible dimensions
    """
    # TODO: Implement matrix multiplication
    pass
```

### Challenge 2: Advanced Search

Implement more advanced search algorithms.

```python
def interpolation_search(arr: List[int], target: int) -> int:
    """
    Interpolation search for uniformly distributed data.

    Args:
        arr: Sorted array to search
        target: Value to find

    Returns:
        Index of target if found, -1 otherwise
    """
    # TODO: Implement interpolation search
    pass
```

---

## ✅ Solution Code

### Exercise 1 Solutions

```python
import statistics
from typing import List

def array_statistics(arr: List[float]) -> dict:
    """Calculate comprehensive statistics for an array."""
    if not arr:
        return {}

    return {
        'count': len(arr),
        'sum': sum(arr),
        'mean': statistics.mean(arr),
        'median': statistics.median(arr),
        'mode': statistics.mode(arr) if len(set(arr)) > 1 else arr[0],
        'min': min(arr),
        'max': max(arr),
        'range': max(arr) - min(arr),
        'variance': statistics.variance(arr) if len(arr) > 1 else 0,
        'stdev': statistics.stdev(arr) if len(arr) > 1 else 0
    }

def filter_by_condition(arr: List[int], condition_func) -> List[int]:
    """Filter array elements based on condition."""
    return [x for x in arr if condition_func(x)]

def transform_array(arr: List[int], transform_func) -> List[int]:
    """Transform array elements."""
    return [transform_func(x) for x in arr]

def chain_operations(arr: List[int], operations: List[callable]) -> List[int]:
    """Apply multiple operations in sequence."""
    result = arr.copy()
    for operation in operations:
        result = [operation(x) for x in result]
    return result
```

### Exercise 2 Solutions

```python
from typing import List

def create_matrix(rows: int, cols: int, default_value: int = 0) -> List[List[int]]:
    """Create matrix with specified dimensions."""
    return [[default_value for _ in range(cols)] for _ in range(rows)]

def validate_matrix(matrix: List[List[int]]) -> bool:
    """Validate matrix structure."""
    if not matrix or not matrix[0]:
        raise ValueError("Matrix cannot be empty")

    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise ValueError("All rows must have same length")
    return True

def add_matrices(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
    """Add two matrices."""
    validate_matrix(A)
    validate_matrix(B)

    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise ValueError("Matrices must have same dimensions")

    rows, cols = len(A), len(A[0])
    return [[A[i][j] + B[i][j] for j in range(cols)] for i in range(rows)]

def transpose_matrix(A: List[List[int]]) -> List[List[int]]:
    """Transpose matrix."""
    validate_matrix(A)
    rows, cols = len(A), len(A[0])
    return [[A[j][i] for j in range(rows)] for i in range(cols)]
```

### Exercise 3 Solutions

```python
from typing import List

def linear_search(arr: List[int], target: int) -> int:
    """Linear search implementation."""
    for i, element in enumerate(arr):
        if element == target:
            return i
    return -1

def binary_search(arr: List[int], target: int) -> int:
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

def find_all_occurrences(arr: List[int], target: int) -> List[int]:
    """Find all occurrences of target."""
    return [i for i, x in enumerate(arr) if x == target]

def bubble_sort(arr: List[int]) -> None:
    """Bubble sort implementation."""
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def selection_sort(arr: List[int]) -> None:
    """Selection sort implementation."""
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def insertion_sort(arr: List[int]) -> None:
    """Insertion sort implementation."""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
```

### Exercise 4 Solutions

```python
from typing import List

def create_image(width: int, height: int, default_value: int = 128) -> List[List[int]]:
    """Create a simple grayscale image matrix."""
    return [[default_value for _ in range(width)] for _ in range(height)]

def invert_image(image: List[List[int]]) -> List[List[int]]:
    """Invert image colors (assuming 0-255 range)."""
    return [[255 - pixel for pixel in row] for row in image]

def apply_threshold(image: List[List[int]], threshold: int) -> List[List[int]]:
    """Apply threshold to create binary image."""
    return [[255 if pixel >= threshold else 0 for pixel in row] for row in image]
```

---

## 🧪 Testing Your Solutions

Create a comprehensive test file:

```python
# test_workshop.py
import array_operations
import matrix_operations

def test_array_operations():
    """Test array operation functions."""
    # Test array statistics
    stats = array_operations.array_statistics([1, 2, 3, 4, 5])
    assert stats['mean'] == 3.0
    assert stats['count'] == 5

    # Test filtering
    numbers = [1, 2, 3, 4, 5, 6]
    evens = array_operations.filter_by_condition(numbers, lambda x: x % 2 == 0)
    assert evens == [2, 4, 6]

    # Test transformation
    squared = array_operations.transform_array([1, 2, 3], lambda x: x**2)
    assert squared == [1, 4, 9]

    print("✓ Array operations tests passed")

def test_matrix_operations():
    """Test matrix operation functions."""
    # Test matrix creation
    matrix = matrix_operations.create_matrix(2, 3, 5)
    assert len(matrix) == 2 and len(matrix[0]) == 3
    assert all(all(cell == 5 for cell in row) for row in matrix)

    # Test matrix addition
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
    result = matrix_operations.add_matrices(A, B)
    expected = [[6, 8], [10, 12]]
    assert result == expected

    # Test transpose
    transposed = matrix_operations.transpose_matrix(A)
    expected_transpose = [[1, 3], [2, 4]]
    assert transposed == expected_transpose

    print("✓ Matrix operations tests passed")

def test_search_algorithms():
    """Test search algorithms."""
    arr = [1, 3, 5, 7, 9]

    # Test linear search
    assert array_operations.linear_search(arr, 5) == 2
    assert array_operations.linear_search(arr, 10) == -1

    # Test binary search
    assert array_operations.binary_search(arr, 5) == 2
    assert array_operations.binary_search(arr, 10) == -1

    print("✓ Search algorithms tests passed")

def test_sort_algorithms():
    """Test sorting algorithms."""
    test_arr = [64, 34, 25, 12, 22, 11, 90]
    expected = [11, 12, 22, 25, 34, 64, 90]

    # Test each algorithm
    for arr in [test_arr.copy() for _ in range(3)]:
        array_operations.bubble_sort(arr)
        assert arr == expected

    for arr in [test_arr.copy() for _ in range(3)]:
        array_operations.selection_sort(arr)
        assert arr == expected

    for arr in [test_arr.copy() for _ in range(3)]:
        array_operations.insertion_sort(arr)
        assert arr == expected

    print("✓ Sort algorithms tests passed")

if __name__ == "__main__":
    test_array_operations()
    test_matrix_operations()
    test_search_algorithms()
    test_sort_algorithms()
    print("🎉 All workshop tests passed!")
```

---

## 📝 Key Takeaways

1. **Arrays are Lists**: Use Python lists to represent one-dimensional arrays
2. **Matrices are Lists of Lists**: Two-dimensional arrays are represented as nested lists
3. **Performance Matters**: Choose algorithms based on time and space complexity
4. **Validation is Key**: Always validate input dimensions and types
5. **In-place Operations**: Modify arrays in place when possible to save memory
6. **Search Algorithms**: Use binary search for sorted arrays, linear search otherwise
7. **Matrix Operations**: Understand matrix multiplication rules and dimensions

---

**Workshop Version**: 1.0
**Last Updated**: February 2026
**Estimated Completion Time**: 120 minutes