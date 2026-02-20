# Homework 1: Arrays and Matrices

**Section**: 6 - Arrays and Matrices (60 min)
**Level**: Beginner to Intermediate
**Prerequisites**: Tutorial 1 (Arrays and Matrices)

---

## 🎯 Assignment Objectives

By completing this homework, you will:

1. **Work with Arrays**: Practice basic array operations and manipulations
2. **Perform Matrix Operations**: Implement essential matrix arithmetic
3. **Apply Search Algorithms**: Use linear and binary search effectively
4. **Solve Practical Problems**: Apply array/matrix concepts to real scenarios

---

## 📋 Assignment Structure

Complete 2 main tasks with practical applications:

1. [Task 1: Array Operations](#task-1-array-operations) (40 points)
2. [Task 2: Matrix Operations](#task-2-matrix-operations) (40 points)
3. [Task 3: Practical Application](#task-3-practical-application) (20 points)

---

## 🏃 Task 1: Array Operations

**Points: 40** | **Time Estimate: 25 minutes**

Create functions for common array operations in `array_ops.py`.

### 1.1 Array Statistics

```python
def array_sum(arr):
    """
    Calculate sum of all elements in array.

    Args:
        arr: List of numbers

    Returns:
        Sum of all elements

    Examples:
        >>> array_sum([1, 2, 3, 4])
        10
    """
    pass

def array_average(arr):
    """
    Calculate average of array elements.

    Args:
        arr: List of numbers

    Returns:
        Average value (float)

    Examples:
        >>> array_average([1, 2, 3, 4])
        2.5
    """
    pass

def find_max(arr):
    """
    Find maximum value in array.

    Args:
        arr: List of numbers

    Returns:
        Maximum value

    Examples:
        >>> find_max([3, 1, 4, 1, 5])
        5
    """
    pass
```

### 1.2 Array Searching

```python
def linear_search(arr, target):
    """
    Find target in array using linear search.

    Args:
        arr: Array to search
        target: Value to find

    Returns:
        Index of target or -1 if not found

    Examples:
        >>> linear_search([1, 2, 3, 4], 3)
        2
        >>> linear_search([1, 2, 3, 4], 5)
        -1
    """
    pass

def binary_search(arr, target):
    """
    Find target in sorted array using binary search.

    Args:
        arr: Sorted array to search
        target: Value to find

    Returns:
        Index of target or -1 if not found

    Examples:
        >>> binary_search([1, 2, 3, 4, 5], 3)
        2
    """
    pass
```

### 1.3 Array Transformations

```python
def reverse_array(arr):
    """
    Reverse array in place.

    Args:
        arr: Array to reverse (modified in place)

    Returns:
        Reversed array

    Examples:
        >>> arr = [1, 2, 3, 4]
        >>> reverse_array(arr)
        [4, 3, 2, 1]
    """
    pass

def rotate_left(arr, k):
    """
    Rotate array left by k positions.

    Args:
        arr: Array to rotate
        k: Number of positions to rotate

    Returns:
        Rotated array

    Examples:
        >>> rotate_left([1, 2, 3, 4, 5], 2)
        [3, 4, 5, 1, 2]
    """
    pass
```

---

## 📊 Task 2: Matrix Operations

**Points: 40** | **Time Estimate: 25 minutes**

Create functions for matrix operations in `matrix_ops.py`.

### 2.1 Basic Matrix Operations

```python
def create_matrix(rows, cols, value=0):
    """
    Create matrix with specified dimensions filled with value.

    Args:
        rows: Number of rows
        cols: Number of columns
        value: Fill value

    Returns:
        2D list representing matrix

    Examples:
        >>> create_matrix(2, 3, 5)
        [[5, 5, 5], [5, 5, 5]]
    """
    pass

def matrix_transpose(matrix):
    """
    Transpose a matrix.

    Args:
        matrix: 2D list to transpose

    Returns:
        Transposed matrix

    Examples:
        >>> matrix_transpose([[1, 2], [3, 4]])
        [[1, 3], [2, 4]]
    """
    pass

def matrix_scalar_multiply(matrix, scalar):
    """
    Multiply matrix by scalar.

    Args:
        matrix: 2D list
        scalar: Number to multiply by

    Returns:
        Scaled matrix

    Examples:
        >>> matrix_scalar_multiply([[1, 2], [3, 4]], 2)
        [[2, 4], [6, 8]]
    """
    pass
```

### 2.2 Matrix Arithmetic

```python
def matrix_add(A, B):
    """
    Add two matrices element-wise.

    Args:
        A, B: Matrices to add (same dimensions)

    Returns:
        Sum matrix

    Examples:
        >>> A = [[1, 2], [3, 4]]
        >>> B = [[5, 6], [7, 8]]
        >>> matrix_add(A, B)
        [[6, 8], [10, 12]]
    """
    pass

def matrix_multiply(A, B):
    """
    Multiply two matrices.

    Args:
        A, B: Matrices to multiply (compatible dimensions)

    Returns:
        Product matrix

    Examples:
        >>> A = [[1, 2], [3, 4]]
        >>> B = [[5, 6], [7, 8]]
        >>> matrix_multiply(A, B)
        [[19, 22], [43, 50]]
    """
    pass
```

### 2.3 Matrix Analysis

```python
def matrix_trace(matrix):
    """
    Calculate trace of square matrix (sum of diagonal).

    Args:
        matrix: Square matrix

    Returns:
        Trace value

    Examples:
        >>> matrix_trace([[1, 2], [3, 4]])
        5
    """
    pass

def find_matrix_max(matrix):
    """
    Find maximum value and position in matrix.

    Args:
        matrix: 2D list

    Returns:
        Tuple (max_value, row, col)

    Examples:
        >>> find_matrix_max([[1, 8, 3], [4, 5, 6]])
        (8, 0, 1)
    """
    pass
```

---

## 🌍 Task 3: Practical Application

**Points: 20** | **Time Estimate: 15 minutes**

Apply your functions to solve a practical problem in `image_processing.py`.

### Image Processing Basics

```python
def create_simple_image(width, height):
    """
    Create a simple grayscale image (matrix).

    Args:
        width: Image width
        height: Image height

    Returns:
        Matrix filled with random values 0-255
    """
    import random
    return [[random.randint(0, 255) for _ in range(width)] for _ in range(height)]

def invert_image(image):
    """
    Invert image colors.

    Args:
        image: 2D list representing image

    Returns:
        Inverted image matrix

    Examples:
        >>> img = [[0, 128], [255, 64]]
        >>> invert_image(img)
        [[255, 127], [0, 191]]
    """
    pass

def apply_threshold(image, threshold):
    """
    Apply threshold to create binary image.

    Args:
        image: 2D list
        threshold: Threshold value

    Returns:
        Binary image (0 or 255)

    Examples:
        >>> img = [[100, 200], [50, 150]]
        >>> apply_threshold(img, 128)
        [[0, 255], [0, 255]]
    """
    pass
```

---

## 📤 Submission Requirements

### Code Quality (20 points)
- **Documentation**: Functions have clear docstrings
- **Readability**: Code is clean and well-organized
- **Correctness**: Functions work as specified

### Functionality (60 points)
- **Array Operations**: All array functions work correctly
- **Matrix Operations**: Matrix functions handle edge cases
- **Search Algorithms**: Search functions work for various inputs

### Testing (20 points)
- **Test Cases**: Test all functions with different inputs
- **Edge Cases**: Handle empty arrays, invalid dimensions
- **Verification**: Demonstrate functions work correctly

### File Structure
```
homework-01-arrays-matrices/
├── array_ops.py         # Array operations
├── matrix_ops.py        # Matrix operations
├── image_processing.py  # Practical application
├── test_homework.py     # Tests
└── README.md           # Brief documentation
```

---

## 🧪 Testing Guidelines

Create `test_homework.py` with basic tests:

```python
# Test array operations
def test_arrays():
    from array_ops import array_sum, array_average, find_max
    from array_ops import linear_search, binary_search
    from array_ops import reverse_array, rotate_left

    # Test statistics
    arr = [1, 2, 3, 4, 5]
    assert array_sum(arr) == 15
    assert array_average(arr) == 3.0
    assert find_max(arr) == 5

    # Test search
    assert linear_search(arr, 3) == 2
    assert binary_search(sorted(arr), 3) == 2

    # Test transformations
    assert reverse_array([1, 2, 3]) == [3, 2, 1]
    assert rotate_left([1, 2, 3, 4], 1) == [2, 3, 4, 1]

    print("✓ Array tests passed")

def test_matrices():
    from matrix_ops import create_matrix, matrix_transpose
    from matrix_ops import matrix_add, matrix_scalar_multiply
    from matrix_ops import matrix_trace, find_matrix_max

    # Test creation
    mat = create_matrix(2, 3, 5)
    assert len(mat) == 2 and len(mat[0]) == 3

    # Test operations
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]

    result = matrix_add(A, B)
    assert result == [[6, 8], [10, 12]]

    scaled = matrix_scalar_multiply(A, 2)
    assert scaled == [[2, 4], [6, 8]]

    transposed = matrix_transpose(A)
    assert transposed == [[1, 3], [2, 4]]

    assert matrix_trace(A) == 5

    max_val, row, col = find_matrix_max(A)
    assert max_val == 4 and row == 1 and col == 1

    print("✓ Matrix tests passed")

def test_practical():
    from image_processing import invert_image, apply_threshold

    img = [[0, 128, 255], [64, 192, 32]]

    inverted = invert_image(img)
    assert inverted[0][0] == 255  # 255 - 0
    assert inverted[0][1] == 127  # 255 - 128

    binary = apply_threshold(img, 128)
    # Values >= 128 become 255, others become 0
    assert binary[0] == [0, 255, 255]  # [0, 128, 255] -> [0, 255, 255]
    assert binary[1] == [0, 255, 0]    # [64, 192, 32] -> [0, 255, 0]

    print("✓ Practical tests passed")

if __name__ == "__main__":
    test_arrays()
    test_matrices()
    test_practical()
    print("🎉 All homework tests passed!")
```

---

## 📊 Grading Rubric

| Criteria | Points | Excellent | Good | Satisfactory |
|----------|--------|-----------|------|--------------|
| **Array Functions** | 25 | All functions correct, handle edge cases | Most functions work | Basic functionality |
| **Matrix Functions** | 25 | All matrix operations correct | Core operations work | Basic matrix handling |
| **Search Algorithms** | 15 | Both search methods implemented | One search method works | Basic search |
| **Practical Application** | 15 | Image processing works correctly | Basic image operations | Simple image functions |
| **Code Quality** | 10 | Clean, documented code | Readable code | Basic code structure |
| **Testing** | 10 | Comprehensive tests | Good test coverage | Basic tests |

---

## 🎯 Learning Outcomes

After completing this homework, you should be able to:
- ✅ Create and manipulate arrays and matrices
- ✅ Implement basic search algorithms
- ✅ Perform matrix arithmetic operations
- ✅ Apply computational concepts to practical problems
- ✅ Write clean, testable Python functions

---

**Homework Version**: 1.0
**Last Updated**: February 2026
**Estimated Completion Time**: 60 minutes