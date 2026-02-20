# Homework 3: Dictionaries and Advanced Python

**Section**: 8 - Dictionaries and Advanced Python Features (60 min)
**Level**: Intermediate to Advanced
**Prerequisites**: Tutorial 3 (Dictionaries and Advanced Python Features)

---

## 🎯 Assignment Objectives

By completing this homework, you will:

1. **Master Dictionary Operations**: Create and manipulate dictionaries
2. **Handle JSON Data**: Parse and create JSON structures
3. **Use Match Statements**: Apply pattern matching in Python
4. **Implement Error Handling**: Use try/except for robust code
5. **Apply Advanced Features**: Use modern Python capabilities

---

## 📋 Assignment Structure

Complete 2 main tasks with practical applications:

1. [Task 1: Dictionary Operations](#task-1-dictionary-operations) (40 points)
2. [Task 2: Advanced Python Features](#task-2-advanced-python-features) (40 points)
3. [Task 3: Practical Application](#task-3-practical-application) (20 points)

---

## 🏃 Task 1: Dictionary Operations

**Points: 40** | **Time Estimate: 25 minutes**

Create functions for dictionary operations in `dict_ops.py`.

### 1.1 Basic Dictionary Operations

```python
def create_person_dict(name, age, city):
    """
    Create dictionary representing a person.

    Args:
        name: Person's name
        age: Person's age
        city: Person's city

    Returns:
        Dictionary with person information

    Examples:
        >>> create_person_dict("Alice", 25, "NYC")
        {"name": "Alice", "age": 25, "city": "NYC"}
    """
    pass

def update_person_info(person_dict, **updates):
    """
    Update person dictionary with new information.

    Args:
        person_dict: Existing person dictionary
        **updates: Key-value pairs to update

    Returns:
        Updated dictionary

    Examples:
        >>> person = {"name": "Alice", "age": 25}
        >>> update_person_info(person, age=26, city="Boston")
        {"name": "Alice", "age": 26, "city": "Boston"}
    """
    pass

def get_person_info(person_dict, key, default="Unknown"):
    """
    Safely get information from person dictionary.

    Args:
        person_dict: Person dictionary
        key: Key to retrieve
        default: Default value if key not found

    Returns:
        Value for key or default

    Examples:
        >>> person = {"name": "Alice", "age": 25}
        >>> get_person_info(person, "age")
        25
        >>> get_person_info(person, "city", "Unknown")
        "Unknown"
    """
    pass
```

### 1.2 Dictionary Analysis

```python
def count_keys(dictionary):
    """
    Count total number of keys in dictionary.

    Args:
        dictionary: Dictionary to analyze

    Returns:
        Number of keys

    Examples:
        >>> count_keys({"a": 1, "b": 2, "c": 3})
        3
    """
    pass

def find_max_value(dictionary):
    """
    Find key with maximum value in dictionary.

    Args:
        dictionary: Dictionary with numeric values

    Returns:
        Key with maximum value

    Examples:
        >>> find_max_value({"a": 10, "b": 20, "c": 15})
        "b"
    """
    pass

def merge_dictionaries(dict1, dict2):
    """
    Merge two dictionaries (dict2 overrides dict1).

    Args:
        dict1, dict2: Dictionaries to merge

    Returns:
        Merged dictionary

    Examples:
        >>> merge_dictionaries({"a": 1, "b": 2}, {"b": 3, "c": 4})
        {"a": 1, "b": 3, "c": 4}
    """
    pass
```

### 1.3 Dictionary Transformations

```python
def invert_dictionary(dictionary):
    """
    Invert dictionary (swap keys and values).

    Args:
        dictionary: Dictionary to invert

    Returns:
        Inverted dictionary

    Examples:
        >>> invert_dictionary({"a": 1, "b": 2})
        {1: "a", 2: "b"}
    """
    pass

def filter_by_value(dictionary, threshold):
    """
    Filter dictionary to keep items above threshold.

    Args:
        dictionary: Dictionary with numeric values
        threshold: Minimum value to keep

    Returns:
        Filtered dictionary

    Examples:
        >>> filter_by_value({"a": 10, "b": 5, "c": 15}, 10)
        {"a": 10, "c": 15}
    """
    pass
```

---

## 🚀 Task 2: Advanced Python Features

**Points: 40** | **Time Estimate: 25 minutes**

Create functions using advanced Python features in `advanced_ops.py`.

### 2.1 Match Statements

```python
def classify_number(num):
    """
    Classify number using match statement.

    Args:
        num: Number to classify

    Returns:
        Classification string

    Examples:
        >>> classify_number(5)
        "Positive"
        >>> classify_number(0)
        "Zero"
        >>> classify_number(-3)
        "Negative"
    """
    pass

def process_data(data):
    """
    Process different data types using match.

    Args:
        data: Data to process

    Returns:
        Processing result

    Examples:
        >>> process_data([1, 2, 3])
        "List with 3 items"
        >>> process_data({"name": "Alice", "age": 25})
        "Person: Alice"
    """
    pass
```

### 2.2 Error Handling

```python
def safe_divide(a, b):
    """
    Divide a by b with error handling.

    Args:
        a, b: Numbers to divide

    Returns:
        Division result or None if error

    Examples:
        >>> safe_divide(10, 2)
        5.0
        >>> safe_divide(10, 0)
        None
    """
    pass

def parse_number(text):
    """
    Parse string to number with error handling.

    Args:
        text: String to parse

    Returns:
        Parsed number or None if invalid

    Examples:
        >>> parse_number("123")
        123
        >>> parse_number("abc")
        None
    """
    pass

def read_file_safely(filename):
    """
    Read file content with error handling.

    Args:
        filename: File to read

    Returns:
        File content or None if error

    Examples:
        >>> read_file_safely("existing_file.txt")
        "file content..."
        >>> read_file_safely("nonexistent.txt")
        None
    """
    pass
```

### 2.3 List Comprehensions and Advanced Features

```python
def square_even_numbers(numbers):
    """
    Square even numbers using comprehension.

    Args:
        numbers: List of numbers

    Returns:
        List of squared even numbers

    Examples:
        >>> square_even_numbers([1, 2, 3, 4, 5])
        [4, 16]
    """
    pass

def create_pairs(list1, list2):
    """
    Create all pairs from two lists using comprehension.

    Args:
        list1, list2: Lists to pair

    Returns:
        List of tuples

    Examples:
        >>> create_pairs([1, 2], [3, 4])
        [(1, 3), (1, 4), (2, 3), (2, 4)]
    """
    pass

def flatten_matrix(matrix):
    """
    Flatten 2D matrix to 1D list using comprehension.

    Args:
        matrix: 2D list

    Returns:
        Flattened 1D list

    Examples:
        >>> flatten_matrix([[1, 2], [3, 4]])
        [1, 2, 3, 4]
    """
    pass
```

---

## 🌍 Task 3: Practical Application

**Points: 20** | **Time Estimate: 15 minutes**

Apply your functions to practical problems in `data_processor.py`.

### Data Processing

```python
def process_student_records(records):
    """
    Process student records and return statistics.

    Args:
        records: List of student dictionaries

    Returns:
        Dictionary with statistics

    Examples:
        >>> records = [
        ...     {"name": "Alice", "grade": 85},
        ...     {"name": "Bob", "grade": 92}
        ... ]
        >>> process_student_records(records)
        {"count": 2, "average": 88.5, "highest": 92}
    """
    pass

def validate_user_input(user_data):
    """
    Validate user input data with error handling.

    Args:
        user_data: Dictionary with user input

    Returns:
        Tuple (is_valid: bool, errors: list)

    Examples:
        >>> validate_user_input({"name": "Alice", "age": "25"})
        (True, [])
        >>> validate_user_input({"name": "", "age": "abc"})
        (False, ["Name cannot be empty", "Age must be number"])
    """
    pass

def format_data_for_display(data):
    """
    Format data for display using advanced features.

    Args:
        data: Dictionary or list to format

    Returns:
        Formatted string

    Examples:
        >>> format_data_for_display({"name": "Alice", "scores": [85, 92]})
        "Alice: Average score 88.5"
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
- **Dictionary Operations**: All dict functions work correctly
- **Match Statements**: Pattern matching used appropriately
- **Error Handling**: Try/except blocks handle errors properly

### Testing (20 points)
- **Test Cases**: Test all functions with different inputs
- **Edge Cases**: Handle invalid inputs, missing keys
- **Verification**: Demonstrate functions work correctly

### File Structure
```
homework-03-dictionaries-advanced/
├── dict_ops.py          # Dictionary operations
├── advanced_ops.py      # Advanced Python features
├── data_processor.py    # Practical application
├── test_homework.py     # Tests
└── README.md           # Brief documentation
```

---

## 🧪 Testing Guidelines

Create `test_homework.py` with basic tests:

```python
# Test dictionary operations
def test_dictionaries():
    from dict_ops import create_person_dict, update_person_info, get_person_info
    from dict_ops import count_keys, find_max_value, merge_dictionaries

    # Test basic operations
    person = create_person_dict("Alice", 25, "NYC")
    assert person["name"] == "Alice"
    assert person["age"] == 25

    updated = update_person_info(person, age=26, city="Boston")
    assert updated["age"] == 26
    assert updated["city"] == "Boston"

    assert get_person_info(person, "age") == 26
    assert get_person_info(person, "country", "USA") == "USA"

    # Test analysis
    assert count_keys({"a": 1, "b": 2, "c": 3}) == 3
    assert find_max_value({"a": 10, "b": 20, "c": 15}) == "b"

    merged = merge_dictionaries({"a": 1, "b": 2}, {"b": 3, "c": 4})
    assert merged == {"a": 1, "b": 3, "c": 4}

    print("✓ Dictionary tests passed")

def test_advanced():
    from advanced_ops import classify_number, process_data, safe_divide
    from advanced_ops import parse_number, square_even_numbers

    # Test match statements
    assert classify_number(5) == "Positive"
    assert classify_number(0) == "Zero"
    assert classify_number(-3) == "Negative"

    assert process_data([1, 2, 3]) == "List with 3 items"
    assert process_data({"name": "Alice"}) == "Person: Alice"

    # Test error handling
    assert safe_divide(10, 2) == 5.0
    assert safe_divide(10, 0) is None

    assert parse_number("123") == 123
    assert parse_number("abc") is None

    # Test comprehensions
    assert square_even_numbers([1, 2, 3, 4]) == [4, 16]
    assert flatten_matrix([[1, 2], [3, 4]]) == [1, 2, 3, 4]

    print("✓ Advanced tests passed")

def test_practical():
    from data_processor import process_student_records, validate_user_input

    # Test student processing
    records = [
        {"name": "Alice", "grade": 85},
        {"name": "Bob", "grade": 92}
    ]
    stats = process_student_records(records)
    assert stats["count"] == 2
    assert stats["average"] == 88.5
    assert stats["highest"] == 92

    # Test validation
    valid, errors = validate_user_input({"name": "Alice", "age": "25"})
    assert valid == True
    assert errors == []

    invalid, errors = validate_user_input({"name": "", "age": "abc"})
    assert invalid == False
    assert len(errors) > 0

    print("✓ Practical tests passed")

if __name__ == "__main__":
    test_dictionaries()
    test_advanced()
    test_practical()
    print("🎉 All homework tests passed!")
```

---

## 📊 Grading Rubric

| Criteria | Points | Excellent | Good | Satisfactory |
|----------|--------|-----------|------|--------------|
| **Dictionary Functions** | 25 | All dict operations correct | Most functions work | Basic functionality |
| **Match Statements** | 15 | Effective pattern matching | Basic match usage | Simple cases |
| **Error Handling** | 15 | Robust try/except blocks | Good error handling | Basic error catching |
| **Practical Application** | 15 | Data processing works correctly | Basic validation | Simple processing |
| **Code Quality** | 15 | Clean, documented code | Readable code | Basic code structure |
| **Testing** | 15 | Comprehensive tests | Good test coverage | Basic tests |

---

## 🎯 Learning Outcomes

After completing this homework, you should be able to:
- ✅ Create and manipulate dictionaries effectively
- ✅ Use match statements for pattern matching
- ✅ Implement proper error handling with try/except
- ✅ Apply advanced Python features in practical code
- ✅ Process and validate data robustly

---

**Homework Version**: 1.0
**Last Updated**: February 2026
**Estimated Completion Time**: 60 minutes