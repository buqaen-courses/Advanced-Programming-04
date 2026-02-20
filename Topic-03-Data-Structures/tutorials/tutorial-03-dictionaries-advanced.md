# Tutorial 3: Dictionaries and Advanced Python Features

**Section**: 8 - Dictionaries and Advanced Python Features (90 min)
**Level**: Intermediate to Advanced
**Prerequisites**: Tutorial 2 (Lists and Sets), basic Python knowledge

---

## 📋 Learning Objectives

By the end of this tutorial, you will be able to:

1. **Master Dictionary Operations**: Create, access, modify, and manipulate dictionaries
2. **Work with JSON Data**: Parse, create, and manipulate JSON structures
3. **Handle Advanced Python Features**: Use match statements, error handling, and advanced comprehensions
4. **Make HTTP Requests**: Use the requests library to interact with web APIs
5. **Process API Responses**: Extract and transform data from real API endpoints
6. **Implement Robust Error Handling**: Handle network errors, exceptions, and malformed data

---

## 📚 Table of Contents

1. [Dictionary Fundamentals](#dictionary-fundamentals)
2. [Advanced Dictionary Operations](#advanced-dictionary-operations)
3. [JSON Handling](#json-handling)
4. [Match Statements (Python 3.10+)](#match-statements-python-310)
5. [Error Handling with Try/Except](#error-handling-with-tryexcept)
6. [HTTP Requests and API Integration](#http-requests-and-api-integration)
7. [Advanced List Comprehensions](#advanced-list-comprehensions)
8. [Best Practices and Common Patterns](#best-practices-and-common-patterns)

---

## 📚 Dictionary Fundamentals

Dictionaries are Python's mapping type that store key-value pairs. They are unordered, mutable, and extremely efficient for lookups.

### Creating Dictionaries

```python
# Empty dictionary
empty_dict = {}

# Dictionary with initial values
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# Using dict() constructor
from_list = dict([("a", 1), ("b", 2)])  # {"a": 1, "b": 2}
from_kwargs = dict(name="Bob", age=30)  # {"name": "Bob", "age": 30}

# Dictionary comprehensions
squares = {x: x**2 for x in range(5)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

### Accessing Dictionary Values

```python
person = {"name": "Alice", "age": 25, "city": "New York"}

# Direct access (raises KeyError if key doesn't exist)
name = person["name"]  # "Alice"

# Safe access with get()
age = person.get("age")        # 25
country = person.get("country", "Unknown")  # "Unknown"

# Check if key exists
has_city = "city" in person    # True
has_country = "country" in person  # False

# Get all keys, values, or items
keys = list(person.keys())     # ["name", "age", "city"]
values = list(person.values()) # ["Alice", 25, "New York"]
items = list(person.items())   # [("name", "Alice"), ("age", 25), ("city", "New York")]
```

### Modifying Dictionaries

```python
person = {"name": "Alice", "age": 25}

# Add or update values
person["city"] = "Boston"      # Add new key-value pair
person["age"] = 26            # Update existing value

# Update with another dictionary
person.update({"email": "alice@example.com", "age": 27})

# Remove items
removed_city = person.pop("city")  # Remove and return value
removed_item = person.popitem()    # Remove and return last item (random in older Python)

# Clear all items
person.clear()  # Empty dictionary
```

---

## 🔧 Advanced Dictionary Operations

### Nested Dictionaries

```python
# Creating nested dictionaries
company = {
    "name": "Tech Corp",
    "departments": {
        "engineering": {
            "employees": ["Alice", "Bob", "Charlie"],
            "budget": 500000
        },
        "sales": {
            "employees": ["Diana", "Eve"],
            "budget": 300000
        }
    }
}

# Accessing nested values
eng_employees = company["departments"]["engineering"]["employees"]
print(eng_employees)  # ['Alice', 'Bob', 'Charlie']

# Safe access with get() for nested dictionaries
def safe_get_nested(data, keys, default=None):
    """Safely access nested dictionary values."""
    for key in keys:
        if isinstance(data, dict) and key in data:
            data = data[key]
        else:
            return default
    return data

budget = safe_get_nested(company, ["departments", "engineering", "budget"])
print(budget)  # 500000

missing = safe_get_nested(company, ["departments", "hr", "budget"], "Not found")
print(missing)  # "Not found"
```

### Dictionary Merging and Updating

```python
# Using update() method
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 20, "c": 30}

dict1.update(dict2)
print(dict1)  # {'a': 1, 'b': 20, 'c': 30}

# Dictionary unpacking (Python 3.5+)
dict3 = {**dict1, **{"d": 40, "b": 100}}
print(dict3)  # {'a': 1, 'b': 100, 'c': 30, 'd': 40}

# Merging nested dictionaries
from collections import ChainMap
nested1 = {"user": {"name": "Alice", "age": 25}}
nested2 = {"user": {"email": "alice@example.com", "city": "NYC"}}

# ChainMap for non-destructive merging
merged = dict(ChainMap(nested2, nested1))
print(merged)
# {'user': {'email': 'alice@example.com', 'city': 'NYC'}}
# Note: ChainMap takes the first dict's values for conflicting keys
```

### Advanced Dictionary Techniques

```python
# defaultdict for automatic key creation
from collections import defaultdict

# Automatic list creation
word_counts = defaultdict(int)
words = ["apple", "banana", "apple", "cherry"]

for word in words:
    word_counts[word] += 1

print(dict(word_counts))  # {'apple': 2, 'banana': 1, 'cherry': 1}

# OrderedDict for maintaining insertion order
from collections import OrderedDict

# Before Python 3.7, OrderedDict was needed to maintain order
ordered = OrderedDict()
ordered["first"] = 1
ordered["second"] = 2
ordered["third"] = 3

print(list(ordered.keys()))  # ['first', 'second', 'third']

# Counter for counting hashable objects
from collections import Counter

colors = ["red", "blue", "red", "green", "blue", "red"]
color_counts = Counter(colors)
print(color_counts)  # Counter({'red': 3, 'blue': 2, 'green': 1})

# Most common elements
print(color_counts.most_common(2))  # [('red', 3), ('blue', 2)]
```

---

## 🔸 JSON Handling

JSON (JavaScript Object Notation) is a lightweight data interchange format that maps directly to Python dictionaries and lists.

### JSON Data Types

```python
# JSON supports these data types:
# - Objects: {"key": "value"} → Python dict
# - Arrays: [1, 2, 3] → Python list
# - Strings: "hello" → Python str
# - Numbers: 42, 3.14 → Python int/float
# - Booleans: true/false → Python bool
# - null: null → Python None

# Example JSON structure
json_example = {
    "name": "John Doe",
    "age": 30,
    "is_student": False,
    "courses": ["Python", "JavaScript", "SQL"],
    "address": {
        "street": "123 Main St",
        "city": "Anytown",
        "country": "USA"
    },
    "metadata": None
}
```

### Python JSON Module

```python
import json

# Encoding (Python to JSON)
data = {
    "name": "Alice",
    "age": 25,
    "courses": ["Math", "Physics"]
}

# Convert to JSON string
json_string = json.dumps(data)
print(json_string)
# Output: {"name": "Alice", "age": 25, "courses": ["Math", "Physics"]}

# Pretty printing
pretty_json = json.dumps(data, indent=2)
print(pretty_json)
# Output:
# {
#   "name": "Alice",
#   "age": 25,
#   "courses": ["Math", "Physics"]
# }

# Decoding (JSON to Python)
json_data = '{"name": "Bob", "age": 30, "active": true}'
python_data = json.loads(json_data)
print(python_data)  # {'name': 'Bob', 'age': 30, 'active': True}
print(type(python_data))  # <class 'dict'>
```

### File Operations with JSON

```python
# Writing JSON to file
data = {"users": [{"name": "Alice"}, {"name": "Bob"}]}

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

# Reading JSON from file
with open('data.json', 'r', encoding='utf-8') as f:
    loaded_data = json.load(f)

print(loaded_data)
# Output: {'users': [{'name': 'Alice'}, {'name': 'Bob'}]}
```

### Handling Special Cases

```python
# Custom objects (don't work by default)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("Charlie", 35)

# This will fail:
# json.dumps(person)  # TypeError

# Solution: Convert to dict first
person_dict = {"name": person.name, "age": person.age}
json_str = json.dumps(person_dict)
print(json_str)  # {"name": "Charlie", "age": 35}

# Handling datetime objects
import datetime

data_with_date = {
    "event": "Conference",
    "date": datetime.datetime(2024, 2, 15, 10, 30)
}

# Custom encoder for datetime
def custom_encoder(obj):
    if isinstance(obj, datetime.datetime):
        return obj.isoformat()
    raise TypeError(f"Object of type {type(obj)} is not JSON serializable")

json_str = json.dumps(data_with_date, default=custom_encoder)
print(json_str)  # {"event": "Conference", "date": "2024-02-15T10:30:00"}
```

---

## 🎯 Match Statements (Python 3.10+)

The `match` statement provides pattern matching capabilities, similar to switch statements in other languages but much more powerful.

### Basic Match Statement

```python
def describe_number(n):
    """Describe a number using pattern matching."""
    match n:
        case 0:
            return "zero"
        case 1:
            return "one"
        case 2:
            return "two"
        case _:
            return "other"

print(describe_number(1))  # "one"
print(describe_number(5))  # "other"
```

### Pattern Matching with Data Structures

```python
def process_data(data):
    """Process different types of data using pattern matching."""
    match data:
        case {"type": "user", "name": name, "age": age}:
            return f"User {name} is {age} years old"
        case {"type": "product", "name": name, "price": price}:
            return f"Product {name} costs ${price}"
        case ["item1", "item2", *rest]:
            return f"List with {len(rest) + 2} items"
        case []:
            return "Empty list"
        case _:
            return f"Unknown data type: {type(data)}"

# Test different patterns
print(process_data({"type": "user", "name": "Alice", "age": 25}))
# "User Alice is 25 years old"

print(process_data(["a", "b", "c", "d"]))
# "List with 4 items"

print(process_data([]))
# "Empty list"
```

### Advanced Pattern Matching

```python
def analyze_api_response(response):
    """Analyze API response using pattern matching."""
    match response:
        case {"status": "success", "data": data}:
            return f"Success: {data}"
        case {"status": "error", "message": msg, "code": code}:
            return f"Error {code}: {msg}"
        case {"status": "success", "data": [], "pagination": {"total": 0}}:
            return "No results found"
        case {"results": results, "count": count} if count > 10:
            return f"Large result set with {count} items"
        case _:
            return "Unknown response format"

# Test responses
responses = [
    {"status": "success", "data": {"users": 5}},
    {"status": "error", "message": "Not found", "code": 404},
    {"results": [1, 2, 3], "count": 15}
]

for response in responses:
    print(analyze_api_response(response))
```

### Guards and Conditions

```python
def categorize_age(age):
    """Categorize age using pattern matching with guards."""
    match age:
        case n if n < 0:
            return "Invalid age"
        case n if 0 <= n < 13:
            return "Child"
        case n if 13 <= n < 20:
            return "Teenager"
        case n if 20 <= n < 65:
            return "Adult"
        case n if n >= 65:
            return "Senior"
        case _:
            return "Unknown"

print(categorize_age(25))   # "Adult"
print(categorize_age(70))   # "Senior"
print(categorize_age(-5))   # "Invalid age"
```

---

## ⚠️ Error Handling with Try/Except

Proper error handling is crucial for robust Python programs. The `try/except` statement allows you to handle exceptions gracefully.

### Basic Try/Except

```python
# Basic error handling
try:
    result = 10 / 0
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Handling multiple exception types
try:
    number = int("not_a_number")
except ValueError as e:
    print(f"Value error: {e}")
except TypeError as e:
    print(f"Type error: {e}")

# Catch-all exception handler
try:
    risky_operation()
except Exception as e:
    print(f"An error occurred: {e}")
```

### Advanced Error Handling

```python
# Multiple exception types in one except clause
try:
    # Some risky operations
    data = json.loads(malformed_json)
    result = data["missing_key"]
except (ValueError, KeyError) as e:
    print(f"Data processing error: {e}")

# Using else and finally
def safe_file_operation(filename):
    """Safely read from a file with proper error handling."""
    file = None
    try:
        file = open(filename, 'r')
        content = file.read()
        return content
    except FileNotFoundError:
        print(f"File {filename} not found")
        return None
    except PermissionError:
        print(f"No permission to read {filename}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None
    else:
        print("File read successfully")
    finally:
        if file:
            file.close()
            print("File closed")

result = safe_file_operation("example.txt")
```

### Custom Exceptions

```python
# Creating custom exceptions
class DataProcessingError(Exception):
    """Custom exception for data processing errors."""
    pass

class ValidationError(DataProcessingError):
    """Exception for validation failures."""
    pass

class APIError(DataProcessingError):
    """Exception for API-related errors."""
    def __init__(self, message, status_code=None):
        super().__init__(message)
        self.status_code = status_code

def validate_user_data(user_data):
    """Validate user data and raise appropriate exceptions."""
    if not isinstance(user_data, dict):
        raise ValidationError("User data must be a dictionary")

    required_fields = ["name", "email"]
    for field in required_fields:
        if field not in user_data:
            raise ValidationError(f"Missing required field: {field}")

    if "@" not in user_data.get("email", ""):
        raise ValidationError("Invalid email format")

    return True

# Using custom exceptions
try:
    validate_user_data({"name": "Alice", "email": "invalid-email"})
except ValidationError as e:
    print(f"Validation failed: {e}")
except DataProcessingError as e:
    print(f"Data processing error: {e}")
```

### Context Managers and Error Handling

```python
# Using context managers for resource management
from contextlib import contextmanager

@contextmanager
def safe_database_connection(db_config):
    """Context manager for database connections."""
    connection = None
    try:
        connection = create_connection(db_config)
        yield connection
    except DatabaseError as e:
        print(f"Database error: {e}")
        raise
    finally:
        if connection:
            connection.close()

# Using the context manager
try:
    with safe_database_connection(db_config) as conn:
        result = conn.execute("SELECT * FROM users")
        print("Query executed successfully")
except DatabaseError:
    print("Failed to execute query")
```

---

## 🌐 HTTP Requests and API Integration

The `requests` library is the most popular HTTP library for Python, providing a simple interface for making HTTP requests.

### Basic HTTP Requests

```python
import requests

# GET request
response = requests.get("https://jsonplaceholder.typicode.com/users/1")

print(f"Status Code: {response.status_code}")
print(f"Content Type: {response.headers['content-type']}")

if response.status_code == 200:
    user_data = response.json()
    print(f"User: {user_data['name']}")
else:
    print(f"Request failed: {response.status_code}")

# POST request
new_user = {"name": "John Doe", "email": "john@example.com"}
response = requests.post(
    "https://jsonplaceholder.typicode.com/users",
    json=new_user
)

if response.status_code == 201:
    created_user = response.json()
    print(f"Created user with ID: {created_user['id']}")
```

### Advanced Request Features

```python
# Request with parameters
params = {"key": "value", "another": "param"}
response = requests.get("https://httpbin.org/get", params=params)
print(f"URL: {response.url}")
# Output: https://httpbin.org/get?key=value&another=param

# Request with headers
headers = {
    "User-Agent": "My Python App",
    "Accept": "application/json",
    "Authorization": "Bearer your_token_here"
}

response = requests.get("https://api.example.com/data", headers=headers)

# Request with timeout
try:
    response = requests.get("https://httpbin.org/delay/5", timeout=3)
except requests.Timeout:
    print("Request timed out")

# Session for connection reuse
with requests.Session() as session:
    session.headers.update({"User-Agent": "My App"})
    session.auth = ("username", "password")

    # Multiple requests with the same session
    response1 = session.get("https://api.example.com/endpoint1")
    response2 = session.get("https://api.example.com/endpoint2")
```

### API Integration Example

```python
def fetch_user_data(user_id):
    """Fetch user data from a REST API with comprehensive error handling."""
    base_url = "https://jsonplaceholder.typicode.com"
    endpoint = f"/users/{user_id}"

    try:
        response = requests.get(f"{base_url}{endpoint}", timeout=10)
        response.raise_for_status()  # Raise exception for bad status codes

        user_data = response.json()

        # Validate response structure
        required_fields = ["id", "name", "email"]
        for field in required_fields:
            if field not in user_data:
                raise ValueError(f"Missing required field: {field}")

        return user_data

    except requests.Timeout:
        print("Request timed out")
        return None
    except requests.ConnectionError:
        print("Connection error")
        return None
    except requests.HTTPError as e:
        print(f"HTTP error: {e.response.status_code}")
        return None
    except ValueError as e:
        print(f"Data validation error: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

# Usage
user = fetch_user_data(1)
if user:
    print(f"Fetched user: {user['name']} ({user['email']})")
else:
    print("Failed to fetch user data")
```

---

## ⚡ Advanced List Comprehensions

While basic list comprehensions were covered in Tutorial 2, here are more advanced patterns and techniques.

### Nested Comprehensions

```python
# Matrix creation and manipulation
matrix = [[i*3 + j for j in range(3)] for i in range(3)]
print("3x3 matrix:")
for row in matrix: print(row)

# Transpose matrix
transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print("\nTransposed:")
for row in transposed: print(row)

# Flatten nested lists
nested = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
flattened = [item for sublist in nested for item in sublist]
print(f"\nFlattened: {flattened}")  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### Dictionary and Set Comprehensions

```python
# Dictionary comprehensions with conditions
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares_dict = {x: x**2 for x in numbers if x % 2 == 0}
print(f"Even squares: {squares_dict}")  # {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}

# Set comprehensions
words = ["hello", "world", "python", "programming"]
word_lengths = {len(word) for word in words}
print(f"Unique word lengths: {word_lengths}")  # {5, 6, 11}

# Complex dictionary comprehension
students = [
    {"name": "Alice", "grades": [85, 92, 88]},
    {"name": "Bob", "grades": [78, 82, 79]},
    {"name": "Charlie", "grades": [92, 88, 95]}
]

# Create dictionary of student names to average grades
student_averages = {
    student["name"]: sum(student["grades"]) / len(student["grades"])
    for student in students
    if sum(student["grades"]) / len(student["grades"]) >= 80
}
print(f"Top students: {student_averages}")
```

### Generator Expressions

```python
# Memory-efficient for large datasets
large_numbers = range(1000000)

# List comprehension (creates entire list in memory)
squares_list = [x**2 for x in large_numbers[:10]]  # Creates list

# Generator expression (lazy evaluation)
squares_gen = (x**2 for x in large_numbers)  # Creates generator

print(f"Generator type: {type(squares_gen)}")

# Use generator for memory-efficient processing
total = sum(squares_gen)  # Only computes when needed
print(f"Sum of squares: {total}")

# Generator with conditions
even_squares = (x**2 for x in large_numbers if x % 2 == 0)
first_five_even_squares = []
for i, square in enumerate(even_squares):
    if i >= 5:
        break
    first_five_even_squares.append(square)

print(f"First 5 even squares: {first_five_even_squares}")
```

---

## 🎯 Best Practices and Common Patterns

### Dictionary Best Practices

```python
# Use dict.get() for safe access
config = {"debug": True, "timeout": 30}

debug_mode = config.get("debug", False)  # Safe, returns False if key missing
timeout = config.get("timeout", 10)      # Safe, returns 10 if key missing

# Use dict.setdefault() for default values
counters = {}
for item in ["a", "b", "a", "c", "b", "a"]:
    counters[item] = counters.setdefault(item, 0) + 1

print(counters)  # {'a': 3, 'b': 2, 'c': 1}

# Use collections.defaultdict for automatic key creation
from collections import defaultdict

word_count = defaultdict(int)
text = "the quick brown fox jumps over the lazy dog"
for word in text.split():
    word_count[word] += 1

print(dict(word_count))
```

### Error Handling Patterns

```python
# EAFP (Easier to Ask for Forgiveness than Permission)
def safe_divide(a, b):
    """Divide a by b, returning None if division by zero."""
    try:
        return a / b
    except ZeroDivisionError:
        return None

# LBYL (Look Before You Leap) - less Pythonic but sometimes necessary
def safe_divide_l byl(a, b):
    """Divide a by b using LBYL approach."""
    if b == 0:
        return None
    return a / b

# Handling multiple operations with context managers
class DatabaseManager:
    def __init__(self):
        self.connection = None

    def __enter__(self):
        self.connection = create_database_connection()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            self.connection.close()

# Usage
try:
    with DatabaseManager() as db:
        db.execute_query("SELECT * FROM users")
        db.execute_query("UPDATE users SET active = 1")
except DatabaseError as e:
    print(f"Database operation failed: {e}")
```

### API Integration Best Practices

```python
import time
import requests
from functools import wraps

def retry_on_failure(max_retries=3, delay=1):
    """Decorator to retry API calls on failure."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except (requests.RequestException, ValueError) as e:
                    last_exception = e
                    if attempt < max_retries - 1:
                        time.sleep(delay * (2 ** attempt))  # Exponential backoff
                        continue
            raise last_exception
        return wrapper
    return decorator

@retry_on_failure(max_retries=3, delay=1)
def fetch_user_with_retry(user_id):
    """Fetch user data with automatic retries."""
    response = requests.get(f"https://api.example.com/users/{user_id}", timeout=10)
    response.raise_for_status()
    return response.json()

# Usage
try:
    user = fetch_user_with_retry(123)
    print(f"Fetched user: {user['name']}")
except Exception as e:
    print(f"Failed to fetch user after retries: {e}")
```

---

## 🎯 Key Takeaways

1. **Dictionaries** are powerful key-value data structures optimized for fast lookups
2. **JSON** maps directly to Python dictionaries and is essential for data interchange
3. **Match statements** provide advanced pattern matching capabilities (Python 3.10+)
4. **Try/Except blocks** are crucial for robust error handling and graceful failure recovery
5. **HTTP requests** with the requests library enable API integration
6. **Advanced comprehensions** provide concise and efficient data transformations
7. **Custom exceptions** help create more meaningful error messages
8. **Context managers** ensure proper resource cleanup

---

## 🔗 Further Reading

- [Python Dictionary Documentation](https://docs.python.org/3/library/stdtypes.html#dict)
- [JSON Official Specification](https://www.json.org/json-en.html)
- [requests Library Documentation](https://requests.readthedocs.io/)
- [Python Match Statements](https://peps.python.org/pep-0622/)
- [Exception Handling Best Practices](https://docs.python.org/3/tutorial/errors.html)

---

## 📝 Practice Exercises

1. **Dictionary Operations**: Create a nested dictionary representing a file system and implement functions to add, remove, and traverse directories
2. **JSON Processing**: Build a JSON configuration file parser that validates structure and provides defaults for missing values
3. **Match Statements**: Implement a command-line argument parser using match statements
4. **Error Handling**: Create a robust file processing function that handles all possible file-related errors
5. **API Integration**: Build a weather API client that caches responses and handles various error conditions
6. **Advanced Comprehensions**: Use nested comprehensions to process complex nested data structures

---

**Tutorial Version**: 1.0
**Last Updated**: February 2026
**Estimated Reading Time**: 75 minutes