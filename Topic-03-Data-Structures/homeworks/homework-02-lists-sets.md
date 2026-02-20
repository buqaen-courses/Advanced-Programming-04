# Homework 2: Lists and Sets Operations

**Section**: 7 - Lists and Sets (60 min)
**Level**: Beginner to Intermediate
**Prerequisites**: Tutorial 2 (Lists and Sets)

---

## 🎯 Assignment Objectives

By completing this homework, you will:

1. **Master List Operations**: Use add, remove, filter, and sort operations
2. **Work with Sets**: Perform union, intersection, difference operations
3. **Apply List Comprehensions**: Write concise list transformations
4. **Choose Data Structures**: Understand when to use lists vs sets

---

## 📋 Assignment Structure

Complete 2 main tasks with practical applications:

1. [Task 1: List Operations](#task-1-list-operations) (40 points)
2. [Task 2: Set Operations](#task-2-set-operations) (40 points)
3. [Task 3: Practical Application](#task-3-practical-application) (20 points)

---

## 🏃 Task 1: List Operations

**Points: 40** | **Time Estimate: 25 minutes**

Create functions for list operations in `list_ops.py`.

### 1.1 List Manipulation

```python
def remove_duplicates(items):
    """
    Remove duplicates from list while preserving order.

    Args:
        items: List that may contain duplicates

    Returns:
        List with duplicates removed

    Examples:
        >>> remove_duplicates([1, 2, 2, 3, 1, 4])
        [1, 2, 3, 4]
    """
    pass

def filter_even_numbers(numbers):
    """
    Filter list to keep only even numbers.

    Args:
        numbers: List of integers

    Returns:
        List containing only even numbers

    Examples:
        >>> filter_even_numbers([1, 2, 3, 4, 5, 6])
        [2, 4, 6]
    """
    pass

def sort_descending(items):
    """
    Sort list in descending order.

    Args:
        items: List to sort

    Returns:
        New sorted list (original unchanged)

    Examples:
        >>> sort_descending([3, 1, 4, 1, 5])
        [5, 4, 3, 1, 1]
    """
    pass
```

### 1.2 List Comprehensions

```python
def square_numbers(numbers):
    """
    Create list of squares using list comprehension.

    Args:
        numbers: List of numbers

    Returns:
        List of squared values

    Examples:
        >>> square_numbers([1, 2, 3, 4])
        [1, 4, 9, 16]
    """
    pass

def filter_long_words(words, min_length):
    """
    Filter words longer than min_length using comprehension.

    Args:
        words: List of strings
        min_length: Minimum word length

    Returns:
        List of words meeting length criteria

    Examples:
        >>> filter_long_words(["cat", "elephant", "dog", "hippopotamus"], 4)
        ["elephant", "hippopotamus"]
    """
    pass

def create_number_pairs(numbers1, numbers2):
    """
    Create pairs from two lists using comprehension.

    Args:
        numbers1, numbers2: Lists of numbers

    Returns:
        List of tuples (x, y) where x from first list, y from second

    Examples:
        >>> create_number_pairs([1, 2], [3, 4])
        [(1, 3), (1, 4), (2, 3), (2, 4)]
    """
    pass
```

### 1.3 List Analysis

```python
def find_longest_word(words):
    """
    Find longest word in list.

    Args:
        words: List of strings

    Returns:
        Longest word (first one if ties)

    Examples:
        >>> find_longest_word(["cat", "elephant", "dog"])
        "elephant"
    """
    pass

def count_occurrences(items, target):
    """
    Count how many times target appears in list.

    Args:
        items: List to search
        target: Item to count

    Returns:
        Count of target in list

    Examples:
        >>> count_occurrences([1, 2, 2, 3, 2], 2)
        3
    """
    pass
```

---

## 🔸 Task 2: Set Operations

**Points: 40** | **Time Estimate: 25 minutes**

Create functions for set operations in `set_ops.py`.

### 2.1 Basic Set Operations

```python
def create_set_from_list(items):
    """
    Create set from list to remove duplicates.

    Args:
        items: List that may contain duplicates

    Returns:
        Set with unique items

    Examples:
        >>> create_set_from_list([1, 2, 2, 3, 1])
        {1, 2, 3}
    """
    pass

def set_intersection(set1, set2):
    """
    Find intersection of two sets.

    Args:
        set1, set2: Sets to intersect

    Returns:
        Set containing elements in both sets

    Examples:
        >>> set_intersection({1, 2, 3}, {2, 3, 4})
        {2, 3}
    """
    pass

def set_union(set1, set2):
    """
    Find union of two sets.

    Args:
        set1, set2: Sets to union

    Returns:
        Set containing elements from both sets

    Examples:
        >>> set_union({1, 2, 3}, {3, 4, 5})
        {1, 2, 3, 4, 5}
    """
    pass
```

### 2.2 Set Analysis

```python
def set_difference(set1, set2):
    """
    Find elements in set1 but not in set2.

    Args:
        set1, set2: Sets for difference

    Returns:
        Set of elements unique to set1

    Examples:
        >>> set_difference({1, 2, 3, 4}, {2, 4, 6})
        {1, 3}
    """
    pass

def is_subset(set1, set2):
    """
    Check if set1 is subset of set2.

    Args:
        set1, set2: Sets to check

    Returns:
        True if set1 ⊆ set2, False otherwise

    Examples:
        >>> is_subset({1, 2}, {1, 2, 3})
        True
        >>> is_subset({1, 4}, {1, 2, 3})
        False
    """
    pass

def unique_elements(*lists):
    """
    Find elements that appear in exactly one list.

    Args:
        *lists: Variable number of lists

    Returns:
        Set of elements in exactly one list

    Examples:
        >>> unique_elements([1, 2, 3], [2, 3, 4], [3, 4, 5])
        {1, 5}
    """
    pass
```

### 2.3 Practical Set Operations

```python
def common_elements(*lists):
    """
    Find elements common to all lists.

    Args:
        *lists: Variable number of lists

    Returns:
        Set of elements in all lists

    Examples:
        >>> common_elements([1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6])
        {3, 4}
    """
    pass

def merge_unique(*lists):
    """
    Merge lists keeping only unique elements.

    Args:
        *lists: Variable number of lists

    Returns:
        Set with all unique elements from all lists

    Examples:
        >>> merge_unique([1, 2, 2], [2, 3, 3], [3, 4])
        {1, 2, 3, 4}
    """
    pass
```

---

## 🌍 Task 3: Practical Application

**Points: 20** | **Time Estimate: 15 minutes**

Apply your functions to solve practical problems in `text_analysis.py`.

### Text Analysis

```python
def extract_unique_words(text):
    """
    Extract unique words from text.

    Args:
        text: String of text

    Returns:
        Set of unique words (lowercase, no punctuation)

    Examples:
        >>> extract_unique_words("Hello world, hello universe!")
        {"hello", "world", "universe"}
    """
    pass

def word_frequency(text):
    """
    Count word frequencies in text.

    Args:
        text: String of text

    Returns:
        Dictionary of word frequencies

    Examples:
        >>> word_frequency("cat dog cat bird")
        {"cat": 2, "dog": 1, "bird": 1}
    """
    pass

def find_common_words(text1, text2):
    """
    Find words common to both texts.

    Args:
        text1, text2: Text strings

    Returns:
        Set of words in both texts

    Examples:
        >>> find_common_words("the cat sat", "cat on mat")
        {"cat"}
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
- **List Operations**: All list functions work correctly
- **Set Operations**: Set functions handle various inputs
- **Comprehensions**: List comprehensions used appropriately

### Testing (20 points)
- **Test Cases**: Test all functions with different inputs
- **Edge Cases**: Handle empty lists, duplicate items
- **Verification**: Demonstrate functions work correctly

### File Structure
```
homework-02-lists-sets/
├── list_ops.py          # List operations
├── set_ops.py           # Set operations
├── text_analysis.py     # Practical application
├── test_homework.py     # Tests
└── README.md           # Brief documentation
```

---

## 🧪 Testing Guidelines

Create `test_homework.py` with basic tests:

```python
# Test list operations
def test_lists():
    from list_ops import remove_duplicates, filter_even_numbers, sort_descending
    from list_ops import square_numbers, filter_long_words, find_longest_word

    # Test manipulation
    assert remove_duplicates([1, 2, 2, 3, 1]) == [1, 2, 3]
    assert filter_even_numbers([1, 2, 3, 4, 5, 6]) == [2, 4, 6]
    assert sort_descending([3, 1, 4, 1, 5]) == [5, 4, 3, 1, 1]

    # Test comprehensions
    assert square_numbers([1, 2, 3]) == [1, 4, 9]
    assert filter_long_words(["cat", "elephant", "dog"], 4) == ["elephant"]
    assert find_longest_word(["cat", "elephant", "dog"]) == "elephant"

    print("✓ List tests passed")

def test_sets():
    from set_ops import create_set_from_list, set_intersection, set_union
    from set_ops import set_difference, unique_elements, common_elements

    # Test basic operations
    s1 = create_set_from_list([1, 2, 2, 3, 1])
    assert s1 == {1, 2, 3}

    assert set_intersection({1, 2, 3}, {2, 3, 4}) == {2, 3}
    assert set_union({1, 2, 3}, {3, 4, 5}) == {1, 2, 3, 4, 5}
    assert set_difference({1, 2, 3, 4}, {2, 4, 6}) == {1, 3}

    # Test advanced operations
    unique = unique_elements([1, 2, 3], [2, 3, 4], [3, 4, 5])
    assert unique == {1, 5}

    common = common_elements([1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6])
    assert common == {3, 4}

    print("✓ Set tests passed")

def test_practical():
    from text_analysis import extract_unique_words, word_frequency, find_common_words

    # Test word extraction
    words = extract_unique_words("Hello world, hello universe!")
    assert words == {"hello", "world", "universe"}

    # Test frequency counting
    freq = word_frequency("cat dog cat bird")
    assert freq == {"cat": 2, "dog": 1, "bird": 1}

    # Test common words
    common = find_common_words("the cat sat", "cat on mat")
    assert common == {"cat"}

    print("✓ Practical tests passed")

if __name__ == "__main__":
    test_lists()
    test_sets()
    test_practical()
    print("🎉 All homework tests passed!")
```

---

## 📊 Grading Rubric

| Criteria | Points | Excellent | Good | Satisfactory |
|----------|--------|-----------|------|--------------|
| **List Functions** | 25 | All functions correct, use comprehensions | Most functions work | Basic functionality |
| **Set Functions** | 25 | All set operations correct | Core operations work | Basic set handling |
| **Comprehensions** | 15 | Effective use of list comprehensions | Some comprehensions used | Basic list operations |
| **Practical Application** | 15 | Text analysis works correctly | Basic text operations | Simple text functions |
| **Code Quality** | 10 | Clean, documented code | Readable code | Basic code structure |
| **Testing** | 10 | Comprehensive tests | Good test coverage | Basic tests |

---

## 🎯 Learning Outcomes

After completing this homework, you should be able to:
- ✅ Manipulate lists using various operations
- ✅ Perform set operations effectively
- ✅ Use list comprehensions for concise code
- ✅ Choose appropriate data structures for tasks
- ✅ Apply list and set concepts to text processing

---

**Homework Version**: 1.0
**Last Updated**: February 2026
**Estimated Completion Time**: 60 minutes