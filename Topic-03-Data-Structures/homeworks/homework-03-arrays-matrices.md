# Homework 3: Arrays and Matrices Operations

**Section**: 8 - Arrays and Matrices (120 min)
**Level**: Intermediate
**Prerequisites**: Tutorial 3 (Arrays and Matrices)

---

## 🎯 Assignment Objectives

By completing this homework, you will demonstrate your ability to:

1. **Master Array Operations**: Implement efficient array manipulation algorithms
2. **Perform Matrix Operations**: Build matrix arithmetic and transformation functions
3. **Apply Search Algorithms**: Implement and optimize search algorithms for arrays and matrices
4. **Solve Computational Problems**: Use arrays and matrices to solve real-world problems
5. **Optimize Performance**: Choose appropriate algorithms based on time/space complexity
6. **Write Robust Code**: Handle edge cases and implement proper error handling

---

## 📋 Assignment Structure

This homework consists of 3 main tasks:

1. [Task 1: Array Operations & Algorithms](#task-1-array-operations--algorithms) (40 points)
2. [Task 2: Matrix Operations](#task-2-matrix-operations) (35 points)
3. [Task 3: Practical Applications](#task-3-practical-applications) (25 points)

---

## 🏃 Task 1: Array Operations & Algorithms

**Points: 40** | **Time Estimate: 45 minutes**

Create a module called `array_operations.py` with the following functionality:

### 1.1 Array Manipulation Functions

```python
from typing import List, Any, Optional, Tuple

def find_kth_largest(arr: List[int], k: int) -> int:
    """
    Find the kth largest element in an array.

    Args:
        arr: Array of integers
        k: Position (1-based) to find

    Returns:
        Kth largest element

    Examples:
        >>> find_kth_largest([3, 2, 1, 5, 6, 4], 2)
        5
    """
    pass

def remove_duplicates_in_place(arr: List[int]) -> int:
    """
    Remove duplicates from sorted array in place.

    Args:
        arr: Sorted array with possible duplicates

    Returns:
        Length of array after removing duplicates

    Examples:
        >>> arr = [1, 1, 2, 2, 3, 3]
        >>> length = remove_duplicates_in_place(arr)
        >>> arr[:length]
        [1, 2, 3]
    """
    pass

def rotate_array(arr: List[int], k: int) -> List[int]:
    """
    Rotate array to the right by k steps.

    Args:
        arr: Array to rotate
        k: Number of steps to rotate

    Returns:
        Rotated array

    Examples:
        >>> rotate_array([1, 2, 3, 4, 5, 6, 7], 3)
        [5, 6, 7, 1, 2, 3, 4]
    """
    pass

def max_subarray_sum(arr: List[int]) -> int:
    """
    Find maximum subarray sum using Kadane's algorithm.

    Args:
        arr: Array of integers (can contain negative numbers)

    Returns:
        Maximum subarray sum

    Examples:
        >>> max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4])
        6  # (4, -1, 2, 1)
    """
    pass
```

### 1.2 Search and Sort Algorithms

```python
def binary_search_first_occurrence(arr: List[int], target: int) -> int:
    """
    Find first occurrence of target in sorted array.

    Args:
        arr: Sorted array
        target: Value to search for

    Returns:
        Index of first occurrence or -1 if not found

    Examples:
        >>> binary_search_first_occurrence([1, 2, 2, 2, 3], 2)
        1
    """
    pass

def binary_search_last_occurrence(arr: List[int], target: int) -> int:
    """
    Find last occurrence of target in sorted array.

    Args:
        arr: Sorted array
        target: Value to search for

    Returns:
        Index of last occurrence or -1 if not found

    Examples:
        >>> binary_search_last_occurrence([1, 2, 2, 2, 3], 2)
        3
    """
    pass

def merge_sorted_arrays(arr1: List[int], arr2: List[int]) -> List[int]:
    """
    Merge two sorted arrays into one sorted array.

    Args:
        arr1, arr2: Sorted arrays to merge

    Returns:
        Merged sorted array

    Examples:
        >>> merge_sorted_arrays([1, 3, 5], [2, 4, 6])
        [1, 2, 3, 4, 5, 6]
    """
    pass

def quicksort(arr: List[int]) -> List[int]:
    """
    Sort array using quicksort algorithm.

    Args:
        arr: Array to sort

    Returns:
        Sorted array (new list, original unchanged)

    Examples:
        >>> quicksort([3, 1, 4, 1, 5, 9, 2, 6])
        [1, 1, 2, 3, 4, 5, 6, 9]
    """
    pass

def count_inversions(arr: List[int]) -> int:
    """
    Count inversions in array using merge sort.

    Args:
        arr: Array to analyze

    Returns:
        Number of inversions (pairs where i < j but arr[i] > arr[j])

    Examples:
        >>> count_inversions([2, 4, 1, 3, 5])
        3  # (2,1), (4,1), (4,3)
    """
    pass
```

### 1.3 Array Analysis Functions

```python
def find_majority_element(arr: List[int]) -> int:
    """
    Find majority element (appears more than n/2 times).

    Args:
        arr: Array of integers

    Returns:
        Majority element or -1 if none exists

    Examples:
        >>> find_majority_element([2, 2, 1, 1, 1, 2, 2])
        2
        >>> find_majority_element([1, 2, 3])
        -1
    """
    pass

def find_missing_number(arr: List[int], n: int) -> int:
    """
    Find missing number in array containing 1 to n.

    Args:
        arr: Array containing numbers from 1 to n with one missing
        n: Maximum number (array should contain 1 to n except one)

    Returns:
        Missing number

    Examples:
        >>> find_missing_number([1, 2, 4, 5], 5)
        3
    """
    pass

def find_duplicate_number(arr: List[int]) -> int:
    """
    Find duplicate number in array containing 1 to n with one duplicate.

    Args:
        arr: Array containing numbers from 1 to n with one duplicate

    Returns:
        Duplicate number

    Examples:
        >>> find_duplicate_number([1, 3, 4, 2, 2])
        2
    """
    pass

def product_except_self(arr: List[int]) -> List[int]:
    """
    Calculate product of all elements except self.

    Args:
        arr: Array of integers

    Returns:
        Array where result[i] = product of all elements except arr[i]

    Examples:
        >>> product_except_self([1, 2, 3, 4])
        [24, 12, 8, 6]
    """
    pass
```

---

## 📊 Task 2: Matrix Operations

**Points: 35** | **Time Estimate: 40 minutes**

Create a module called `matrix_operations.py` with matrix functionality:

### 2.1 Basic Matrix Operations

```python
from typing import List, Tuple

def matrix_addition(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
    """
    Add two matrices element-wise.

    Args:
        A, B: Matrices to add

    Returns:
        Result matrix

    Raises:
        ValueError: If matrices have incompatible dimensions
    """
    pass

def matrix_multiplication(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
    """
    Multiply two matrices.

    Args:
        A, B: Matrices to multiply

    Returns:
        Result matrix

    Raises:
        ValueError: If matrices have incompatible dimensions
    """
    pass

def matrix_transpose(A: List[List[int]]) -> List[List[int]]:
    """
    Transpose a matrix.

    Args:
        A: Matrix to transpose

    Returns:
        Transposed matrix
    """
    pass

def matrix_scalar_multiply(A: List[List[int]], scalar: int) -> List[List[int]]:
    """
    Multiply matrix by scalar.

    Args:
        A: Input matrix
        scalar: Scalar value

    Returns:
        Scaled matrix
    """
    pass
```

### 2.2 Matrix Properties and Analysis

```python
def is_square_matrix(A: List[List[int]]) -> bool:
    """
    Check if matrix is square.

    Args:
        A: Matrix to check

    Returns:
        True if square, False otherwise
    """
    pass

def matrix_trace(A: List[List[int]]) -> int:
    """
    Calculate trace of square matrix.

    Args:
        A: Square matrix

    Returns:
        Trace (sum of diagonal elements)

    Raises:
        ValueError: If matrix is not square
    """
    pass

def matrix_determinant(A: List[List[int]]) -> int:
    """
    Calculate determinant of 2x2 or 3x3 matrix.

    Args:
        A: Square matrix (2x2 or 3x3)

    Returns:
        Determinant value

    Raises:
        ValueError: If matrix is not 2x2 or 3x3
    """
    pass

def is_symmetric_matrix(A: List[List[int]]) -> bool:
    """
    Check if matrix is symmetric.

    Args:
        A: Matrix to check

    Returns:
        True if symmetric, False otherwise
    """
    pass

def matrix_rank(A: List[List[int]]) -> int:
    """
    Calculate rank of matrix using Gaussian elimination.

    Args:
        A: Input matrix

    Returns:
        Rank of matrix
    """
    pass
```

### 2.3 Matrix Transformations

```python
def rotate_matrix_90_clockwise(A: List[List[int]]) -> List[List[int]]:
    """
    Rotate matrix 90 degrees clockwise.

    Args:
        A: Square matrix to rotate

    Returns:
        Rotated matrix

    Raises:
        ValueError: If matrix is not square
    """
    pass

def rotate_matrix_180(A: List[List[int]]) -> List[List[int]]:
    """
    Rotate matrix 180 degrees.

    Args:
        A: Matrix to rotate

    Returns:
        Rotated matrix
    """
    pass

def flip_matrix_horizontal(A: List[List[int]]) -> List[List[int]]:
    """
    Flip matrix horizontally (left-right).

    Args:
        A: Matrix to flip

    Returns:
        Flipped matrix
    """
    pass

def matrix_power(A: List[List[int]], n: int) -> List[List[int]]:
    """
    Calculate matrix power A^n.

    Args:
        A: Square matrix
        n: Power (positive integer)

    Returns:
        A raised to power n

    Raises:
        ValueError: If matrix is not square or n < 0
    """
    pass
```

### 2.4 Matrix Search and Analysis

```python
def search_matrix(A: List[List[int]], target: int) -> Tuple[int, int]:
    """
    Search for target in matrix (assuming row-wise sorted).

    Args:
        A: Matrix to search
        target: Value to find

    Returns:
        Tuple (row, col) if found, (-1, -1) otherwise
    """
    pass

def find_saddle_points(A: List[List[int]]) -> List[Tuple[int, int]]:
    """
    Find saddle points in matrix (min in row, max in column).

    Args:
        A: Matrix to analyze

    Returns:
        List of tuples (row, col) of saddle points
    """
    pass

def matrix_local_maxima(A: List[List[int]]) -> List[Tuple[int, int]]:
    """
    Find local maxima in matrix (greater than all neighbors).

    Args:
        A: Matrix to analyze

    Returns:
        List of tuples (row, col) of local maxima
    """
    pass

def extract_diagonal(A: List[List[int]]) -> List[int]:
    """
    Extract main diagonal of matrix.

    Args:
        A: Square matrix

    Returns:
        List of diagonal elements
    """
    pass

def extract_anti_diagonal(A: List[List[int]]) -> List[int]:
    """
    Extract anti-diagonal of matrix.

    Args:
        A: Square matrix

    Returns:
        List of anti-diagonal elements
    """
    pass
```

---

## 🌍 Task 3: Practical Applications

**Points: 25** | **Time Estimate: 35 minutes**

Create a module called `array_applications.py` with practical applications:

### 3.1 Image Processing Basics

```python
def create_image_matrix(width: int, height: int, default_value: int = 128) -> List[List[int]]:
    """
    Create a simple grayscale image matrix.

    Args:
        width: Image width
        height: Image height
        default_value: Default pixel value (0-255)

    Returns:
        2D list representing image
    """
    pass

def invert_image(image: List[List[int]]) -> List[List[int]]:
    """
    Invert image colors.

    Args:
        image: 2D list representing image

    Returns:
        Inverted image
    """
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
    pass

def calculate_image_histogram(image: List[List[int]]) -> List[int]:
    """
    Calculate histogram of image pixel values.

    Args:
        image: 2D list representing image

    Returns:
        List of 256 values representing pixel count for each intensity
    """
    pass

def resize_image_nearest_neighbor(image: List[List[int]],
                                new_width: int, new_height: int) -> List[List[int]]:
    """
    Resize image using nearest neighbor interpolation.

    Args:
        image: Input image
        new_width: New width
        new_height: New height

    Returns:
        Resized image
    """
    pass
```

### 3.2 Path Finding

```python
def find_path_in_grid(grid: List[List[int]], start: Tuple[int, int],
                     end: Tuple[int, int]) -> List[Tuple[int, int]]:
    """
    Find path from start to end in grid using BFS.

    Args:
        grid: 2D grid (0 = empty, 1 = wall)
        start: Starting position (row, col)
        end: Ending position (row, col)

    Returns:
        List of positions representing path, empty list if no path
    """
    pass

def count_islands(grid: List[List[int]]) -> int:
    """
    Count number of islands in grid (connected components of 1s).

    Args:
        grid: 2D grid (0 = water, 1 = land)

    Returns:
        Number of islands
    """
    pass

def flood_fill(grid: List[List[int]], start: Tuple[int, int],
              new_color: int) -> List[List[int]]:
    """
    Perform flood fill operation on grid.

    Args:
        grid: 2D grid
        start: Starting position
        new_color: New color value

    Returns:
        Grid after flood fill
    """
    pass
```

### 3.3 Data Analysis

```python
def moving_average(data: List[float], window_size: int) -> List[float]:
    """
    Calculate moving average of data.

    Args:
        data: List of numbers
        window_size: Size of moving window

    Returns:
        List of moving averages
    """
    pass

def detect_peaks(data: List[float], threshold: float = 0) -> List[int]:
    """
    Detect peaks in 1D data.

    Args:
        data: List of numbers
        threshold: Minimum value to consider as peak

    Returns:
        List of indices where peaks occur
    """
    pass

def correlation_matrix(data_matrix: List[List[float]]) -> List[List[float]]:
    """
    Calculate correlation matrix for multiple data series.

    Args:
        data_matrix: Matrix where each row is a data series

    Returns:
        Correlation matrix
    """
    pass

def principal_component_analysis(data_matrix: List[List[float]],
                               num_components: int = 2) -> Tuple[List[List[float]], List[float]]:
    """
    Perform basic PCA on data matrix.

    Args:
        data_matrix: Data matrix (rows = samples, cols = features)
        num_components: Number of principal components to return

    Returns:
        Tuple of (transformed_data, explained_variance)
    """
    pass
```

---

## 📤 Submission Requirements

### Code Quality (25 points)
- **Algorithm Implementation**: Correct, efficient algorithms
- **Documentation**: Complete docstrings with examples
- **Error Handling**: Proper validation and error messages
- **Type Hints**: Use type hints throughout
- **Code Style**: Follow PEP 8 conventions

### Functionality (50 points)
- **Array Algorithms**: Correct implementation of search/sort algorithms
- **Matrix Operations**: Proper matrix arithmetic and transformations
- **Edge Cases**: Handle empty arrays, invalid dimensions, etc.
- **Performance**: Use efficient algorithms (avoid O(n²) when O(n) possible)

### Testing & Applications (25 points)
- **Comprehensive Tests**: Test all functions with various inputs
- **Practical Applications**: Working image processing and data analysis
- **Integration**: Combine array and matrix operations effectively

### File Structure
```
homework-03-arrays-matrices/
├── array_operations.py     # Task 1 - Array algorithms
├── matrix_operations.py    # Task 2 - Matrix operations
├── array_applications.py   # Task 3 - Practical applications
├── test_homework.py        # Comprehensive tests
└── README.md              # Documentation
```

---

## 🧪 Testing Guidelines

Create comprehensive tests:

```python
def test_array_operations():
    """Test array operation functions."""
    # Test kth largest
    arr = [3, 2, 1, 5, 6, 4]
    assert find_kth_largest(arr, 2) == 5

    # Test duplicate removal
    arr = [1, 1, 2, 2, 3, 3]
    length = remove_duplicates_in_place(arr)
    assert arr[:length] == [1, 2, 3]

    # Test rotation
    result = rotate_array([1, 2, 3, 4, 5, 6, 7], 3)
    assert result == [5, 6, 7, 1, 2, 3, 4]

    # Test max subarray
    assert max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

def test_matrix_operations():
    """Test matrix operation functions."""
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]

    # Test addition
    result = matrix_addition(A, B)
    expected = [[6, 8], [10, 12]]
    assert result == expected

    # Test multiplication
    result = matrix_multiplication(A, B)
    expected = [[19, 22], [43, 50]]
    assert result == expected

    # Test transpose
    result = matrix_transpose(A)
    expected = [[1, 3], [2, 4]]
    assert result == expected

    # Test properties
    assert is_square_matrix(A) == True
    assert matrix_trace(A) == 5

def test_practical_applications():
    """Test practical application functions."""
    # Test image operations
    image = create_image_matrix(3, 3, 100)
    inverted = invert_image(image)
    assert inverted[0][0] == 155  # 255 - 100

    # Test path finding
    grid = [
        [0, 1, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    path = find_path_in_grid(grid, (0, 0), (2, 2))
    assert len(path) > 0  # Should find a path

if __name__ == "__main__":
    test_array_operations()
    test_matrix_operations()
    test_practical_applications()
    print("All tests passed! ✅")
```

---

## 📊 Grading Rubric

| Criteria | Excellent (90-100%) | Good (80-89%) | Satisfactory (70-79%) | Needs Improvement (<70%) |
|----------|-------------------|---------------|---------------------|-------------------------|
| **Algorithm Correctness** | All algorithms work correctly, handle edge cases | Most algorithms correct, minor issues | Some algorithms work, major issues | Few algorithms work |
| **Efficiency** | Optimal algorithms chosen, good time/space complexity | Good algorithms, reasonable complexity | Basic algorithms, acceptable complexity | Inefficient algorithms, poor complexity |
| **Matrix Operations** | Complete matrix arithmetic, proper error handling | Good matrix operations, some error handling | Basic operations, minimal error handling | Poor matrix operations, no error handling |
| **Code Quality** | Clean, well-documented, modular, type hints | Good structure, some documentation | Basic structure, minimal docs | Poor structure, undocumented |
| **Practical Applications** | Working image processing, path finding, data analysis | Good applications, some features working | Basic applications, limited functionality | Minimal applications, not working |

---

## 🎯 Learning Outcomes Assessment

After completing this homework, you should be able to:
- ✅ Implement efficient array search and sort algorithms
- ✅ Perform matrix arithmetic and transformations
- ✅ Apply arrays and matrices to solve computational problems
- ✅ Analyze algorithm time and space complexity
- ✅ Handle edge cases and implement proper error handling
- ✅ Use arrays and matrices for image processing and data analysis

---

**Homework Version**: 1.0
**Last Updated**: February 2026
**Estimated Completion Time**: 120 minutes