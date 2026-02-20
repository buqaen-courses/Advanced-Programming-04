# Homework 1: Data Manipulation with Lists and Sets

**Section**: 6 - Working with Lists and Sets (120 min)
**Level**: Beginner to Intermediate
**Prerequisites**: Tutorial 1 (Lists and Sets)

---

## 🎯 Assignment Objectives

By completing this homework, you will demonstrate your ability to:

1. **Apply List Operations**: Implement functions using add, remove, sort, filter operations
2. **Use Set Operations**: Perform union, intersection, difference operations
3. **Handle Data Processing**: Clean and transform data using Python collections
4. **Write Clean Code**: Follow best practices with proper documentation and error handling
5. **Solve Real Problems**: Apply data structures to practical scenarios

---

## 📋 Assignment Structure

This homework consists of 3 main tasks with increasing complexity:

1. [Task 1: List Manipulation Functions](#task-1-list-manipulation-functions) (40 points)
2. [Task 2: Set-Based Data Processing](#task-2-set-based-data-processing) (35 points)
3. [Task 3: Real-World Data Processing](#task-3-real-world-data-processing) (25 points)

---

## 🏃 Task 1: List Manipulation Functions

**Points: 40** | **Time Estimate: 45 minutes**

Create a module called `list_operations.py` with the following functions:

### 1.1 Data Cleaning Functions

```python
def remove_duplicates_preserve_order(items):
    """
    Remove duplicates from a list while preserving the original order.

    Args:
        items: List that may contain duplicates

    Returns:
        List with duplicates removed, order preserved

    Examples:
        >>> remove_duplicates_preserve_order([1, 2, 2, 3, 1, 4])
        [1, 2, 3, 4]
    """
    pass

def clean_text_list(texts, strip_whitespace=True, remove_empty=True):
    """
    Clean a list of text strings.

    Args:
        texts: List of strings
        strip_whitespace: Whether to strip leading/trailing whitespace
        remove_empty: Whether to remove empty strings after cleaning

    Returns:
        List of cleaned strings

    Examples:
        >>> clean_text_list(["  hello  ", "", "world", "  "])
        ["hello", "world"]
    """
    pass

def normalize_numbers(numbers, remove_negatives=False):
    """
    Normalize a list of numbers by converting to float and handling invalid values.

    Args:
        numbers: List of number-like values (strings, ints, floats)
        remove_negatives: Whether to remove negative numbers

    Returns:
        List of valid float numbers

    Examples:
        >>> normalize_numbers(["1.5", 2, "invalid", -1], remove_negatives=True)
        [1.5, 2.0]
    """
    pass
```

### 1.2 Data Transformation Functions

```python
def group_by_frequency(items):
    """
    Group items by their frequency in the list.

    Args:
        items: List of hashable items

    Returns:
        Dictionary mapping frequency to list of items with that frequency

    Examples:
        >>> group_by_frequency([1, 2, 2, 3, 3, 3])
        {1: [1], 2: [2], 3: [3]}
    """
    pass

def sliding_window_average(numbers, window_size):
    """
    Calculate sliding window averages for a list of numbers.

    Args:
        numbers: List of numbers
        window_size: Size of the sliding window

    Returns:
        List of averages for each window position

    Examples:
        >>> sliding_window_average([1, 2, 3, 4, 5], 3)
        [2.0, 3.0, 4.0]
    """
    pass

def rotate_list(items, k):
    """
    Rotate a list by k positions to the right.

    Args:
        items: List to rotate
        k: Number of positions to rotate (can be negative for left rotation)

    Returns:
        Rotated list

    Examples:
        >>> rotate_list([1, 2, 3, 4, 5], 2)
        [4, 5, 1, 2, 3]
        >>> rotate_list([1, 2, 3, 4, 5], -1)
        [2, 3, 4, 5, 1]
    """
    pass
```

### 1.3 Advanced List Operations

```python
def find_longest_increasing_subsequence(numbers):
    """
    Find the length of the longest increasing subsequence.

    Args:
        numbers: List of numbers

    Returns:
        Length of the longest increasing subsequence

    Examples:
        >>> find_longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18])
        4  # (2, 5, 7, 18) or (2, 3, 7, 101)
    """
    pass

def partition_list(items, predicate):
    """
    Partition a list into two lists based on a predicate function.

    Args:
        items: List to partition
        predicate: Function that returns True/False for each item

    Returns:
        Tuple of (true_items, false_items)

    Examples:
        >>> partition_list([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
        ([2, 4, 6], [1, 3, 5])
    """
    pass

def compress_list(items):
    """
    Compress consecutive duplicates in a list using run-length encoding.

    Args:
        items: List to compress

    Returns:
        List of tuples (value, count) for consecutive duplicates

    Examples:
        >>> compress_list([1, 1, 2, 2, 2, 3, 1, 1])
        [(1, 2), (2, 3), (3, 1), (1, 2)]
    """
    pass
```

---

## 🔸 Task 2: Set-Based Data Processing

**Points: 35** | **Time Estimate: 40 minutes**

Create a module called `set_operations.py` with the following functions:

### 2.1 Set Analysis Functions

```python
def analyze_relationships(set1, set2):
    """
    Analyze the relationship between two sets.

    Args:
        set1, set2: Sets to analyze

    Returns:
        Dictionary with analysis results:
        - 'intersection': common elements
        - 'union': all elements
        - 'difference_1_2': elements in set1 but not set2
        - 'difference_2_1': elements in set2 but not set1
        - 'symmetric_difference': elements in either set but not both
        - 'is_subset': whether set1 is subset of set2
        - 'is_superset': whether set1 is superset of set2
        - 'are_disjoint': whether sets have no common elements

    Examples:
        >>> analyze_relationships({1, 2, 3}, {2, 3, 4})
        {
            'intersection': {2, 3},
            'union': {1, 2, 3, 4},
            'difference_1_2': {1},
            'difference_2_1': {4},
            'symmetric_difference': {1, 4},
            'is_subset': False,
            'is_superset': False,
            'are_disjoint': False
        }
    """
    pass

def find_unique_elements(*lists):
    """
    Find elements that appear in exactly one of the input lists.

    Args:
        *lists: Variable number of lists

    Returns:
        Set of elements that appear in exactly one list

    Examples:
        >>> find_unique_elements([1, 2, 3], [2, 3, 4], [3, 4, 5])
        {1, 5}
    """
    pass
```

### 2.2 Data Deduplication

```python
def deduplicate_with_priority(items, key_func, priority_func):
    """
    Remove duplicates based on a key function, keeping the item with highest priority.

    Args:
        items: List of items
        key_func: Function to extract comparison key from each item
        priority_func: Function to determine priority (higher = better)

    Returns:
        List with duplicates removed, best version kept

    Examples:
        >>> data = [
        ...     {'name': 'Alice', 'score': 85},
        ...     {'name': 'Alice', 'score': 92},
        ...     {'name': 'Bob', 'score': 78}
        ... ]
        >>> deduplicate_with_priority(
        ...     data,
        ...     lambda x: x['name'],
        ...     lambda x: x['score']
        ... )
        [{'name': 'Alice', 'score': 92}, {'name': 'Bob', 'score': 78}]
    """
    pass

def remove_common_elements(main_list, *other_lists):
    """
    Remove elements from main_list that appear in any of the other lists.

    Args:
        main_list: List to filter
        *other_lists: Other lists to check against

    Returns:
        Filtered list with common elements removed

    Examples:
        >>> remove_common_elements([1, 2, 3, 4, 5], [2, 4, 6], [3, 6, 9])
        [1, 5]
    """
    pass
```

### 2.3 Set-Based Text Processing

```python
def extract_unique_words(texts):
    """
    Extract all unique words from a list of texts.

    Args:
        texts: List of strings

    Returns:
        Set of unique words (case-insensitive, punctuation removed)

    Examples:
        >>> extract_unique_words(["Hello world", "World peace", "hello universe"])
        {"hello", "world", "peace", "universe"}
    """
    pass

def find_common_words(*texts):
    """
    Find words that appear in all input texts.

    Args:
        *texts: Variable number of text strings

    Returns:
        Set of words that appear in all texts

    Examples:
        >>> find_common_words("the quick brown", "brown fox jumps", "the brown dog")
        {"brown"}
    """
    pass

def text_similarity_score(text1, text2):
    """
    Calculate similarity score between two texts based on word overlap.

    Args:
        text1, text2: Text strings to compare

    Returns:
        Float between 0 and 1 indicating similarity

    Examples:
        >>> text_similarity_score("the quick brown fox", "the brown fox jumps")
        0.75  # 3 out of 4 words overlap
    """
    pass
```

---

## 🌍 Task 3: Real-World Data Processing

**Points: 25** | **Time Estimate: 35 minutes**

Create a module called `data_processor.py` that integrates your list and set operations to solve a real-world problem.

### 3.1 Student Grade Processor

```python
class StudentGradeProcessor:
    """Process student grade data with various analysis functions."""

    def __init__(self):
        self.students = []

    def add_student(self, name, grades):
        """
        Add a student with their grades.

        Args:
            name: Student name (string)
            grades: List of numeric grades
        """
        pass

    def get_student_average(self, name):
        """
        Get average grade for a student.

        Args:
            name: Student name

        Returns:
            Average grade or None if student not found
        """
        pass

    def get_class_statistics(self):
        """
        Calculate class-wide statistics.

        Returns:
            Dictionary with class statistics:
            - total_students
            - average_grade
            - highest_grade
            - lowest_grade
            - grade_distribution (A: 90+, B: 80-89, C: 70-79, D: 60-69, F: <60)
        """
        pass

    def find_top_performers(self, n=5):
        """
        Find top n performing students by average grade.

        Args:
            n: Number of top students to return

        Returns:
            List of tuples (name, average) sorted by average descending
        """
        pass

    def identify_at_risk_students(self, threshold=70):
        """
        Identify students with average below threshold.

        Args:
            threshold: Grade threshold

        Returns:
            List of student names with averages below threshold
        """
        pass
```

### 3.2 Data Analysis Integration

```python
def process_survey_data(responses):
    """
    Process survey response data.

    Args:
        responses: List of dictionaries with survey responses
            [{"age": 25, "interests": ["python", "data"], "satisfaction": 8}, ...]

    Returns:
        Dictionary with analysis results:
        - total_responses
        - average_age
        - unique_interests (set of all mentioned interests)
        - top_interests (list of tuples: interest, count)
        - average_satisfaction
        - age_groups (dictionary with age ranges as keys)
    """
    pass

def analyze_text_corpus(texts):
    """
    Analyze a corpus of texts.

    Args:
        texts: List of text strings

    Returns:
        Dictionary with text analysis:
        - total_texts
        - unique_words
        - most_common_words (top 10)
        - average_words_per_text
        - vocabulary_richness (unique_words / total_words)
        - word_length_distribution
    """
    pass
```

---

## 📤 Submission Requirements

### Code Quality (20 points)
- **Documentation**: All functions must have proper docstrings
- **Type Hints**: Use type hints where appropriate
- **Error Handling**: Handle edge cases and invalid inputs gracefully
- **Code Style**: Follow PEP 8 style guidelines
- **Modularity**: Separate concerns into appropriate functions/classes

### Functionality (60 points)
- **Correctness**: All functions must work as specified
- **Edge Cases**: Handle empty inputs, invalid data, etc.
- **Efficiency**: Use appropriate data structures and algorithms
- **Integration**: Modules work together properly

### Testing (20 points)
- **Unit Tests**: Create comprehensive test functions
- **Edge Cases**: Test boundary conditions
- **Integration**: Test module interactions

### File Structure
```
homework-01-data-manipulation/
├── list_operations.py       # Task 1 functions
├── set_operations.py        # Task 2 functions
├── data_processor.py        # Task 3 functions
├── test_homework.py         # Your test file
└── README.md               # Brief documentation
```

---

## 🧪 Testing Guidelines

Create a `test_homework.py` file with comprehensive tests:

```python
# Example test structure
def test_list_operations():
    """Test all list operation functions."""
    # Test remove_duplicates_preserve_order
    assert remove_duplicates_preserve_order([1, 2, 2, 3, 1]) == [1, 2, 3]

    # Test clean_text_list
    result = clean_text_list(["  hello  ", "", "world"])
    assert result == ["hello", "world"]

    # Add more tests...

def test_set_operations():
    """Test all set operation functions."""
    # Test analyze_relationships
    result = analyze_relationships({1, 2, 3}, {2, 3, 4})
    assert result['intersection'] == {2, 3}
    assert result['union'] == {1, 2, 3, 4}

    # Add more tests...

def test_real_world_processing():
    """Test real-world data processing functions."""
    processor = StudentGradeProcessor()
    processor.add_student("Alice", [85, 92, 88])
    processor.add_student("Bob", [78, 82, 79])

    assert processor.get_student_average("Alice") == 88.33333333333333

    stats = processor.get_class_statistics()
    assert stats['total_students'] == 2

    # Add more tests...

if __name__ == "__main__":
    test_list_operations()
    test_set_operations()
    test_real_world_processing()
    print("All tests passed! ✅")
```

---

## 📊 Grading Rubric

| Criteria | Excellent (90-100%) | Good (80-89%) | Satisfactory (70-79%) | Needs Improvement (<70%) |
|----------|-------------------|---------------|---------------------|-------------------------|
| **Functionality** | All functions work correctly, handle edge cases | Most functions work, minor issues | Some functions work, major issues | Few functions work |
| **Code Quality** | Clean, well-documented, follows best practices | Good documentation, minor style issues | Basic documentation, style issues | Poor documentation, doesn't follow standards |
| **Testing** | Comprehensive tests cover all cases | Good test coverage, some gaps | Basic tests, missing edge cases | Minimal or no testing |
| **Problem Solving** | Creative, efficient solutions | Solid solutions, good approach | Basic solutions, works but not optimal | Incorrect or incomplete solutions |

---

## 🎯 Learning Outcomes Assessment

After completing this homework, you should be able to:
- ✅ Manipulate lists using various operations (add, remove, filter, sort)
- ✅ Use sets for efficient data processing and analysis
- ✅ Apply list and set operations to solve real-world problems
- ✅ Write clean, documented, and testable Python code
- ✅ Handle edge cases and invalid inputs gracefully

---

**Homework Version**: 1.0
**Last Updated**: February 2026
**Estimated Completion Time**: 120 minutes