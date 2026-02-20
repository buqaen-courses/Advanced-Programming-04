# Workshop 3: Advanced Data Processing and Error Handling

**Section**: 8 - Dictionaries and Advanced Python Features (90 min)
**Level**: Intermediate to Advanced
**Prerequisites**: Tutorial 3 (Dictionaries and Advanced Python Features)

---

## 🎯 Workshop Objectives

By the end of this workshop, you will:

1. **Master Dictionary Operations**: Create, manipulate, and analyze complex nested dictionaries
2. **Handle JSON Data**: Parse, validate, and transform JSON data structures
3. **Use Advanced Python Features**: Implement match statements, error handling, and comprehensions
4. **Build Robust Applications**: Create reliable code with proper error handling and validation
5. **Process API Data**: Fetch and process data from web APIs with comprehensive error handling

---

## 📋 Workshop Structure

1. [Setup and Environment](#setup-and-environment)
2. [Exercise 1: Advanced Dictionary Operations](#exercise-1-advanced-dictionary-operations)
3. [Exercise 2: JSON Processing and Validation](#exercise-2-json-processing-and-validation)
4. [Exercise 3: Match Statements and Pattern Matching](#exercise-3-match-statements-and-pattern-matching)
5. [Exercise 4: Error Handling and Exception Management](#exercise-4-error-handling-and-exception-management)
6. [Exercise 5: API Integration with Error Handling](#exercise-5-api-integration-with-error-handling)
7. [Challenge Exercises](#challenge-exercises)
8. [Solution Code](#solution-code)

---

## 🛠️ Setup and Environment

### Create Project Structure

```bash
# Create workshop directory
mkdir workshop-advanced-data
cd workshop-advanced-data

# Create Python files
touch dict_utils.py json_utils.py api_utils.py test_workshop.py

# Optional: Create virtual environment
python -m venv venv
# Windows: venv\Scripts\activate
# macOS/Linux: source venv/bin/activate

# Install requests if needed
pip install requests
```

### Import Required Modules

```python
# dict_utils.py
"""
Advanced Dictionary Operations
Functions for complex dictionary manipulations
"""

# json_utils.py
"""
JSON Processing and Validation
Robust JSON handling with error management
"""

# api_utils.py
"""
API Integration with Error Handling
Safe API calls with comprehensive error management
"""

import json
import requests
from typing import Dict, List, Any, Optional, Union
```

---

## 🏃 Exercise 1: Advanced Dictionary Operations

**Goal**: Master complex dictionary manipulations and nested data structures

### Task 1.1: Deep Dictionary Operations

Create functions for deep dictionary operations.

```python
def deep_get(data: Dict[str, Any], keys: List[str], default=None) -> Any:
    """
    Safely access deeply nested dictionary values.

    Args:
        data: Dictionary to search
        keys: List of keys to traverse
        default: Default value if path doesn't exist

    Returns:
        Value at nested path or default

    Examples:
        >>> data = {"user": {"profile": {"name": "Alice"}}}
        >>> deep_get(data, ["user", "profile", "name"])
        "Alice"
        >>> deep_get(data, ["user", "settings", "theme"], "light")
        "light"
    """
    # TODO: Implement deep dictionary access
    pass

def deep_set(data: Dict[str, Any], keys: List[str], value: Any) -> None:
    """
    Set value in deeply nested dictionary, creating intermediate dicts if needed.

    Args:
        data: Dictionary to modify
        keys: List of keys for path
        value: Value to set

    Examples:
        >>> data = {}
        >>> deep_set(data, ["user", "profile", "name"], "Alice")
        >>> data
        {"user": {"profile": {"name": "Alice"}}}
    """
    # TODO: Implement deep dictionary setting
    pass

def flatten_dict(data: Dict[str, Any], prefix: str = "", separator: str = ".") -> Dict[str, str]:
    """
    Flatten nested dictionary into single level with dotted keys.

    Args:
        data: Nested dictionary
        prefix: Current key prefix
        separator: Key separator

    Returns:
        Flattened dictionary

    Examples:
        >>> data = {"user": {"name": "Alice", "age": 25}}
        >>> flatten_dict(data)
        {"user.name": "Alice", "user.age": "25"}
    """
    # TODO: Implement dictionary flattening
    pass
```

**Test your functions:**
```python
# Test deep operations
data = {"user": {"profile": {"name": "Alice", "settings": {"theme": "dark"}}}}

# Test deep_get
name = deep_get(data, ["user", "profile", "name"])
print(f"Name: {name}")

theme = deep_get(data, ["user", "profile", "settings", "theme"])
print(f"Theme: {theme}")

missing = deep_get(data, ["user", "account", "email"], "not found")
print(f"Missing value: {missing}")

# Test deep_set
deep_set(data, ["user", "profile", "age"], 25)
deep_set(data, ["user", "account", "email"], "alice@example.com")

print("Updated data:")
print(data)

# Test flatten
flat = flatten_dict(data)
print("Flattened:")
for key, value in flat.items():
    print(f"  {key}: {value}")
```

### Task 1.2: Dictionary Merging and Diffing

Create functions for advanced dictionary operations.

```python
def merge_dicts(*dicts: Dict[str, Any], strategy: str = "overwrite") -> Dict[str, Any]:
    """
    Merge multiple dictionaries with different strategies.

    Args:
        *dicts: Dictionaries to merge
        strategy: Merge strategy ("overwrite", "deep", "list")

    Returns:
        Merged dictionary

    Examples:
        >>> merge_dicts({"a": 1}, {"a": 2, "b": 3}, strategy="overwrite")
        {"a": 2, "b": 3}
    """
    # TODO: Implement dictionary merging with strategies
    pass

def dict_diff(dict1: Dict[str, Any], dict2: Dict[str, Any]) -> Dict[str, List[Any]]:
    """
    Find differences between two dictionaries.

    Args:
        dict1, dict2: Dictionaries to compare

    Returns:
        Dictionary with differences:
        - "added": Keys in dict2 but not dict1
        - "removed": Keys in dict1 but not dict2
        - "changed": Keys with different values
        - "unchanged": Keys with same values

    Examples:
        >>> d1 = {"a": 1, "b": 2}
        >>> d2 = {"a": 1, "c": 3}
        >>> dict_diff(d1, d2)
        {"added": ["c"], "removed": ["b"], "changed": [], "unchanged": ["a"]}
    """
    # TODO: Implement dictionary diffing
    pass

def group_by_multiple_keys(items: List[Dict[str, Any]], keys: List[str]) -> Dict[str, List[Dict[str, Any]]]:
    """
    Group list of dictionaries by multiple keys.

    Args:
        items: List of dictionaries
        keys: Keys to group by

    Returns:
        Nested dictionary grouped by keys

    Examples:
        >>> data = [
        ...     {"city": "NYC", "type": "A", "value": 1},
        ...     {"city": "NYC", "type": "B", "value": 2},
        ...     {"city": "LA", "type": "A", "value": 3}
        ... ]
        >>> group_by_multiple_keys(data, ["city", "type"])
        {
            "NYC": {"A": [{"city": "NYC", "type": "A", "value": 1}],
                    "B": [{"city": "NYC", "type": "B", "value": 2}]},
            "LA": {"A": [{"city": "LA", "type": "A", "value": 3}]}
        }
    """
    # TODO: Implement multi-key grouping
    pass
```

**Test your functions:**
```python
# Test merging
dict1 = {"user": {"name": "Alice", "age": 25}}
dict2 = {"user": {"age": 26, "city": "NYC"}, "settings": {"theme": "dark"}}

merged = merge_dicts(dict1, dict2, strategy="overwrite")
print("Merged dictionaries:")
print(merged)

# Test diffing
d1 = {"a": 1, "b": 2, "c": {"x": 1}}
d2 = {"a": 1, "b": 3, "d": 4, "c": {"x": 1}}

diff = dict_diff(d1, d2)
print("Dictionary differences:")
for key, values in diff.items():
    print(f"  {key}: {values}")

# Test grouping
data = [
    {"city": "NYC", "category": "A", "sales": 100},
    {"city": "NYC", "category": "B", "sales": 200},
    {"city": "LA", "category": "A", "sales": 150},
    {"city": "LA", "category": "A", "sales": 75}
]

grouped = group_by_multiple_keys(data, ["city", "category"])
print("Grouped data:")
import json
print(json.dumps(grouped, indent=2))
```

---

## 🔸 Exercise 2: JSON Processing and Validation

**Goal**: Build robust JSON processing with validation and error handling

### Task 2.1: JSON Schema Validation

Create JSON validation and processing functions.

```python
def validate_json_schema(data: Any, schema: Dict[str, Any]) -> List[str]:
    """
    Validate JSON data against a simple schema.

    Args:
        data: Data to validate
        schema: Schema definition with field types and requirements

    Returns:
        List of validation errors (empty if valid)

    Schema format:
    {
        "type": "object",  # or "array"
        "required": ["name", "age"],
        "properties": {
            "name": {"type": "string", "min_length": 1},
            "age": {"type": "number", "min": 0, "max": 150}
        }
    }
    """
    # TODO: Implement JSON schema validation
    pass

def safe_json_loads(json_str: str) -> tuple:
    """
    Safely parse JSON string with detailed error information.

    Args:
        json_str: JSON string to parse

    Returns:
        Tuple of (success: bool, data: Any, error: str)
    """
    # TODO: Implement safe JSON parsing
    pass

def json_to_dict_table(json_data: Any) -> List[Dict[str, Any]]:
    """
    Convert JSON data to tabular format for analysis.

    Args:
        json_data: JSON data (object or array)

    Returns:
        List of dictionaries representing table rows

    Examples:
        >>> data = {"users": [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 30}]}
        >>> json_to_dict_table(data)
        [{"path": "users[0].name", "value": "Alice", "type": "string"},
         {"path": "users[0].age", "value": 25, "type": "number"},
         ...]
    """
    # TODO: Convert JSON to tabular format
    pass
```

**Test your functions:**
```python
# Test validation
schema = {
    "type": "object",
    "required": ["name", "age"],
    "properties": {
        "name": {"type": "string", "min_length": 1},
        "age": {"type": "number", "min": 0, "max": 150}
    }
}

# Valid data
valid_data = {"name": "Alice", "age": 25, "city": "NYC"}
errors = validate_json_schema(valid_data, schema)
print(f"Valid data errors: {errors}")

# Invalid data
invalid_data = {"name": "", "age": 200}
errors = validate_json_schema(invalid_data, schema)
print(f"Invalid data errors: {errors}")

# Test safe parsing
test_cases = [
    '{"name": "Alice", "age": 25}',
    '{"name": "Bob", "age": }',  # Invalid JSON
    'not json at all'
]

for i, json_str in enumerate(test_cases):
    success, data, error = safe_json_loads(json_str)
    print(f"Test {i+1}: {'✓' if success else '✗'} - {error}")
    if success:
        print(f"  Data: {data}")
```

### Task 2.2: JSON Transformations

Create functions for JSON data transformations.

```python
def json_normalize(data: Any, separator: str = ".") -> Dict[str, Any]:
    """
    Normalize nested JSON into flat structure.

    Args:
        data: JSON data to normalize
        separator: Key separator for nested paths

    Returns:
        Flattened dictionary

    Examples:
        >>> data = {"user": {"name": "Alice", "profile": {"age": 25}}}
        >>> json_normalize(data)
        {"user.name": "Alice", "user.profile.age": 25}
    """
    # TODO: Implement JSON normalization
    pass

def json_filter_by_path(data: Any, path_pattern: str) -> Any:
    """
    Filter JSON data by path patterns.

    Args:
        data: JSON data
        path_pattern: Path pattern to match (supports wildcards)

    Returns:
        Filtered data matching the pattern

    Examples:
        >>> data = {"users": [{"name": "Alice"}, {"name": "Bob"}]}
        >>> json_filter_by_path(data, "users[*].name")
        ["Alice", "Bob"]
    """
    # TODO: Implement JSON path filtering
    pass

def json_transform(data: Any, transformations: Dict[str, callable]) -> Any:
    """
    Transform JSON data using function mappings.

    Args:
        data: JSON data to transform
        transformations: Dict mapping paths to transformation functions

    Returns:
        Transformed data

    Examples:
        >>> data = {"users": [{"age": 25}, {"age": 30}]}
        >>> transformations = {"users[*].age": lambda x: x + 1}
        >>> json_transform(data, transformations)
        {"users": [{"age": 26}, {"age": 31}]}
    """
    # TODO: Implement JSON transformations
    pass
```

**Test your functions:**
```python
# Test normalization
nested_data = {
    "company": {
        "name": "Tech Corp",
        "departments": [
            {"name": "Engineering", "employees": 50},
            {"name": "Sales", "employees": 30}
        ]
    }
}

normalized = json_normalize(nested_data)
print("Normalized JSON:")
for key, value in normalized.items():
    print(f"  {key}: {value}")

# Test filtering
data = {
    "users": [
        {"name": "Alice", "age": 25, "active": True},
        {"name": "Bob", "age": 30, "active": False},
        {"name": "Charlie", "age": 35, "active": True}
    ]
}

# Simple filtering example (without complex path patterns)
active_users = [user for user in data["users"] if user["active"]]
print(f"Active users: {[u['name'] for u in active_users]}")

# Test transformations
transformations = {
    "users": lambda users: [dict(user, age=user["age"] + 1) for user in users]
}

transformed = json_transform(data, transformations)
print("Transformed data (ages + 1):")
print(transformed)
```

---

## 🎯 Exercise 3: Match Statements and Pattern Matching

**Goal**: Master Python's match statement for advanced pattern matching

### Task 3.1: Basic Match Patterns

Create functions using match statements for different scenarios.

```python
def classify_data(data: Any) -> str:
    """
    Classify data type using match statement.

    Args:
        data: Data to classify

    Returns:
        Classification string

    Examples:
        >>> classify_data({"type": "user", "name": "Alice"})
        "User data: Alice"
        >>> classify_data([1, 2, 3])
        "List with 3 items"
    """
    # TODO: Implement classification using match
    pass

def process_config(config: Dict[str, Any]) -> Dict[str, Any]:
    """
    Process configuration using pattern matching.

    Args:
        config: Configuration dictionary

    Returns:
        Processed configuration with defaults applied

    Examples:
        >>> config = {"database": {"type": "postgres", "host": "localhost"}}
        >>> process_config(config)
        {"database": {"type": "postgres", "host": "localhost", "port": 5432}}
    """
    # TODO: Process config using match patterns
    pass

def validate_api_request(request: Dict[str, Any]) -> tuple[bool, str]:
    """
    Validate API request using pattern matching.

    Args:
        request: API request data

    Returns:
        Tuple of (is_valid: bool, error_message: str)

    Examples:
        >>> req = {"method": "GET", "path": "/users", "params": {"id": "123"}}
        >>> validate_api_request(req)
        (True, "")
    """
    # TODO: Validate request using match patterns
    pass
```

**Test your functions:**
```python
# Test classification
test_data = [
    {"type": "user", "name": "Alice", "role": "admin"},
    {"type": "product", "name": "Widget", "price": 29.99},
    [1, 2, 3, 4, 5],
    "simple string",
    42,
    None
]

for data in test_data:
    classification = classify_data(data)
    print(f"{type(data).__name__}: {classification}")

# Test config processing
configs = [
    {"database": {"type": "postgres", "host": "localhost"}},
    {"database": {"type": "mysql", "port": 3306}},
    {"cache": {"type": "redis", "host": "cache.example.com"}}
]

for config in configs:
    processed = process_config(config)
    print(f"Processed config: {processed}")

# Test API validation
requests = [
    {"method": "GET", "path": "/users", "params": {"limit": "10"}},
    {"method": "POST", "path": "/users", "body": {"name": "Alice"}},
    {"method": "INVALID", "path": "/users"},
    {"path": "/users"}  # Missing method
]

for req in requests:
    valid, error = validate_api_request(req)
    status = "✓" if valid else "✗"
    print(f"{status} {req} - {error}")
```

### Task 3.2: Advanced Match Patterns

Create more complex pattern matching functions.

```python
def parse_command(command: str) -> Dict[str, Any]:
    """
    Parse command string using pattern matching.

    Args:
        command: Command string to parse

    Returns:
        Parsed command dictionary

    Examples:
        >>> parse_command("CREATE USER alice admin")
        {"action": "create", "type": "user", "name": "alice", "role": "admin"}
    """
    # TODO: Parse command using match patterns
    pass

def analyze_http_response(response: Dict[str, Any]) -> str:
    """
    Analyze HTTP response using pattern matching.

    Args:
        response: HTTP response data

    Returns:
        Analysis string

    Examples:
        >>> resp = {"status": 200, "data": {"users": 5}}
        >>> analyze_http_response(resp)
        "Success: Retrieved 5 users"
    """
    # TODO: Analyze response using match patterns
    pass

def categorize_error(error: Exception) -> str:
    """
    Categorize exception using pattern matching.

    Args:
        error: Exception object

    Returns:
        Error category

    Examples:
        >>> categorize_error(ValueError("Invalid input"))
        "Validation error"
    """
    # TODO: Categorize error using match patterns
    pass
```

**Test your functions:**
```python
# Test command parsing
commands = [
    "CREATE USER alice admin",
    "DELETE USER bob",
    "UPDATE PRODUCT widget price 29.99",
    "LIST USERS",
    "INVALID COMMAND"
]

for cmd in commands:
    try:
        parsed = parse_command(cmd)
        print(f"Parsed '{cmd}': {parsed}")
    except Exception as e:
        print(f"Failed to parse '{cmd}': {e}")

# Test HTTP response analysis
responses = [
    {"status": 200, "data": {"users": 5, "total": 100}},
    {"status": 404, "error": "Not found"},
    {"status": 500, "error": "Internal server error"},
    {"status": 201, "data": {"id": 123}}
]

for resp in responses:
    analysis = analyze_http_response(resp)
    print(f"Response analysis: {analysis}")

# Test error categorization
errors = [
    ValueError("Invalid input"),
    KeyError("missing_key"),
    ConnectionError("Network failed"),
    FileNotFoundError("File not found"),
    RuntimeError("Unexpected error")
]

for error in errors:
    category = categorize_error(error)
    print(f"{type(error).__name__}: {category}")
```

---

## ⚠️ Exercise 4: Error Handling and Exception Management

**Goal**: Implement comprehensive error handling and custom exceptions

### Task 4.1: Custom Exceptions

Create custom exception classes and error handling.

```python
class DataProcessingError(Exception):
    """Base exception for data processing errors."""
    pass

class ValidationError(DataProcessingError):
    """Exception for data validation failures."""
    def __init__(self, field: str, value: Any, message: str = None):
        self.field = field
        self.value = value
        self.message = message or f"Validation failed for field '{field}' with value '{value}'"
        super().__init__(self.message)

class APIError(DataProcessingError):
    """Exception for API-related errors."""
    def __init__(self, message: str, status_code: int = None, response_data: Any = None):
        self.status_code = status_code
        self.response_data = response_data
        super().__init__(message)

class ConfigurationError(DataProcessingError):
    """Exception for configuration-related errors."""
    pass

def validate_user_data(user_data: Dict[str, Any]) -> None:
    """
    Validate user data and raise appropriate exceptions.

    Args:
        user_data: User data dictionary

    Raises:
        ValidationError: If validation fails
    """
    # TODO: Implement validation with custom exceptions
    pass

def safe_api_call(url: str, **kwargs) -> Dict[str, Any]:
    """
    Make safe API call with comprehensive error handling.

    Args:
        url: API endpoint URL
        **kwargs: Additional parameters for requests

    Returns:
        API response data

    Raises:
        APIError: If API call fails
    """
    # TODO: Implement safe API call with error handling
    pass
```

**Test your functions:**
```python
# Test validation
test_users = [
    {"name": "Alice", "email": "alice@example.com", "age": 25},
    {"name": "", "email": "bob@example.com", "age": 30},  # Invalid name
    {"name": "Charlie", "email": "invalid-email", "age": 35},  # Invalid email
    {"name": "Diana", "email": "diana@example.com", "age": -5}  # Invalid age
]

for user in test_users:
    try:
        validate_user_data(user)
        print(f"✓ User {user['name']} is valid")
    except ValidationError as e:
        print(f"✗ Validation failed for {user['name']}: {e}")
    except Exception as e:
        print(f"✗ Unexpected error for {user['name']}: {e}")

# Test API calls (simulated)
def mock_api_call(url, **kwargs):
    """Mock API call for testing."""
    if "fail" in url:
        raise APIError("API call failed", 500)
    return {"status": "success", "data": {"message": "Mock response"}}

# Test safe API call
urls = ["https://api.example.com/success", "https://api.example.com/fail"]

for url in urls:
    try:
        result = mock_api_call(url)
        print(f"✓ API call to {url} succeeded: {result}")
    except APIError as e:
        print(f"✗ API call to {url} failed: {e}")
```

### Task 4.2: Context Managers and Resource Management

Create context managers for resource management.

```python
from contextlib import contextmanager
import time

@contextmanager
def timer(operation_name: str):
    """
    Context manager for timing operations.

    Args:
        operation_name: Name of the operation being timed

    Yields:
        None

    Examples:
        >>> with timer("data processing"):
        ...     # Some operation
        ...     pass
        Processing time for data processing: 0.0012 seconds
    """
    # TODO: Implement timer context manager
    pass

@contextmanager
def safe_file_operation(filename: str, mode: str = "r"):
    """
    Context manager for safe file operations.

    Args:
        filename: File to operate on
        mode: File mode

    Yields:
        File object

    Examples:
        >>> with safe_file_operation("data.txt", "w") as f:
        ...     f.write("Hello, World!")
    """
    # TODO: Implement file operation context manager
    pass

@contextmanager
def database_connection(config: Dict[str, Any]):
    """
    Context manager for database connections.

    Args:
        config: Database configuration

    Yields:
        Database connection object
    """
    # TODO: Implement database connection context manager
    pass

def process_data_with_timing(data: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Process data with timing and error handling.

    Args:
        data: Data to process

    Returns:
        Processing results
    """
    # TODO: Use context managers for timing and resource management
    pass
```

**Test your functions:**
```python
# Test timer context manager
with timer("simple calculation"):
    result = sum(range(100000))
    print(f"Sum: {result}")

# Test file operations
try:
    with safe_file_operation("test_output.txt", "w") as f:
        f.write("Hello from context manager!\n")
        f.write("This file operation is safe.\n")

    with safe_file_operation("test_output.txt", "r") as f:
        content = f.read()
        print("File content:")
        print(content)

except Exception as e:
    print(f"File operation failed: {e}")

# Test data processing with timing
test_data = [
    {"name": "Alice", "scores": [85, 92, 88]},
    {"name": "Bob", "scores": [78, 82, 79]},
    {"name": "Charlie", "scores": [92, 88, 95]}
]

try:
    results = process_data_with_timing(test_data)
    print(f"Processing results: {results}")
except Exception as e:
    print(f"Data processing failed: {e}")
```

---

## 🌐 Exercise 5: API Integration with Error Handling

**Goal**: Build robust API clients with comprehensive error handling

### Task 5.1: Advanced API Client

Create an advanced API client with retry logic and error handling.

```python
import requests
from typing import Dict, List, Any, Optional
import time
import json

class AdvancedAPIClient:
    """Advanced API client with comprehensive error handling and features."""

    def __init__(self, base_url: str, api_key: Optional[str] = None,
                 timeout: int = 10, max_retries: int = 3):
        """
        Initialize advanced API client.

        Args:
            base_url: Base API URL
            api_key: Optional API key for authentication
            timeout: Request timeout
            max_retries: Maximum number of retries
        """
        # TODO: Initialize client attributes
        pass

    def _make_request(self, method: str, endpoint: str,
                     params: Optional[Dict[str, Any]] = None,
                     data: Optional[Dict[str, Any]] = None,
                     json_data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Make HTTP request with retry logic and error handling.

        Args:
            method: HTTP method
            endpoint: API endpoint
            params: Query parameters
            data: Form data
            json_data: JSON data

        Returns:
            Response data

        Raises:
            APIError: If request fails after retries
        """
        # TODO: Implement request with retry logic
        pass

    def get(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Make GET request."""
        return self._make_request("GET", endpoint, params=params)

    def post(self, endpoint: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Make POST request."""
        return self._make_request("POST", endpoint, data=data)

    def put(self, endpoint: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Make PUT request."""
        return self._make_request("PUT", endpoint, data=data)

    def delete(self, endpoint: str) -> Dict[str, Any]:
        """Make DELETE request."""
        return self._make_request("DELETE", endpoint)

    def get_with_cache(self, endpoint: str, params: Optional[Dict[str, Any]] = None,
                      cache_ttl: int = 300) -> Dict[str, Any]:
        """
        Make GET request with caching.

        Args:
            endpoint: API endpoint
            params: Query parameters
            cache_ttl: Cache time-to-live in seconds

        Returns:
            Cached or fresh response data
        """
        # TODO: Implement caching mechanism
        pass
```

**Test your API client:**
```python
# Note: This example uses httpbin.org for testing
# In real scenarios, replace with actual API endpoints

client = AdvancedAPIClient("https://httpbin.org")

# Test basic requests
try:
    # GET request
    response = client.get("/get", params={"test": "value"})
    print(f"GET response: {response['args']}")

    # POST request
    response = client.post("/post", data={"key": "value"})
    print(f"POST response: {response['json']}")

except APIError as e:
    print(f"API request failed: {e}")

# Test caching (simulated)
try:
    # First request
    print("First cached request:")
    response1 = client.get_with_cache("/get", params={"cached": "true"})

    # Second request (should use cache)
    print("Second cached request:")
    response2 = client.get_with_cache("/get", params={"cached": "true"})

    print("Caching test completed")

except APIError as e:
    print(f"Cached request failed: {e}")
```

### Task 5.2: Data Processing Pipeline

Create a complete data processing pipeline with error handling.

```python
def fetch_process_store_data(api_client: AdvancedAPIClient,
                           endpoint: str, storage_file: str) -> Dict[str, Any]:
    """
    Complete data processing pipeline: fetch → process → store.

    Args:
        api_client: API client instance
        endpoint: API endpoint to fetch from
        storage_file: File to store processed data

    Returns:
        Processing statistics

    Raises:
        DataProcessingError: If pipeline fails
    """
    # TODO: Implement complete data processing pipeline
    pass

def validate_and_transform_data(raw_data: Dict[str, Any],
                              validation_schema: Dict[str, Any],
                              transformations: Dict[str, callable]) -> Dict[str, Any]:
    """
    Validate and transform API response data.

    Args:
        raw_data: Raw data from API
        validation_schema: Schema for validation
        transformations: Transformation functions

    Returns:
        Validated and transformed data

    Raises:
        ValidationError: If validation fails
        DataProcessingError: If transformation fails
    """
    # TODO: Implement validation and transformation
    pass

def create_data_report(processed_data: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Create comprehensive report from processed data.

    Args:
        processed_data: List of processed data items

    Returns:
        Report with statistics and insights
    """
    # TODO: Generate data analysis report
    pass
```

**Test your pipeline:**
```python
# Test data processing pipeline (using mock data)
mock_client = AdvancedAPIClient("https://httpbin.org")

# Mock data for testing
test_data = {
    "users": [
        {"id": 1, "name": "Alice", "email": "alice@example.com", "active": True},
        {"id": 2, "name": "Bob", "email": "bob@example.com", "active": False},
        {"id": 3, "name": "Charlie", "email": "charlie@example.com", "active": True}
    ]
}

validation_schema = {
    "type": "object",
    "required": ["users"],
    "properties": {
        "users": {
            "type": "array",
            "items": {
                "type": "object",
                "required": ["id", "name", "email"],
                "properties": {
                    "id": {"type": "number"},
                    "name": {"type": "string"},
                    "email": {"type": "string"},
                    "active": {"type": "boolean"}
                }
            }
        }
    }
}

transformations = {
    "users": lambda users: [dict(user, status="active" if user["active"] else "inactive")
                           for user in users]
}

try:
    # Test validation and transformation
    validated_data = validate_and_transform_data(
        test_data, validation_schema, transformations
    )
    print("Validated and transformed data:")
    print(json.dumps(validated_data, indent=2))

    # Test reporting
    report = create_data_report(validated_data["users"])
    print("
Data report:")
    print(json.dumps(report, indent=2))

except (ValidationError, DataProcessingError) as e:
    print(f"Data processing failed: {e}")
```

---

## 🚀 Challenge Exercises

### Challenge 1: Advanced JSON Schema Validator

Create a comprehensive JSON schema validator.

```python
def validate_complex_schema(data: Any, schema: Dict[str, Any]) -> List[str]:
    """
    Validate data against complex JSON schema with nested validation.

    Supports:
    - Object and array validation
    - Type checking
    - Required fields
    - Value constraints (min, max, pattern, etc.)
    - Nested schema validation
    """
    # TODO: Implement comprehensive schema validator
    pass
```

### Challenge 2: Match Statement Parser

Create a domain-specific language parser using match statements.

```python
def parse_dsl_query(query: str) -> Dict[str, Any]:
    """
    Parse domain-specific query language using match statements.

    Supports queries like:
    - "FIND users WHERE age > 25 AND city = 'NYC'"
    - "COUNT products BY category"
    - "AVG sales GROUP BY month"
    """
    # TODO: Implement DSL parser with match statements
    pass
```

### Challenge 3: Fault-Tolerant API Client

Build an API client that handles various failure scenarios.

```python
class FaultTolerantAPIClient(AdvancedAPIClient):
    """
    API client with advanced fault tolerance features:
    - Circuit breaker pattern
    - Fallback responses
    - Request deduplication
    - Response compression
    """
    # TODO: Implement fault-tolerant API client
    pass
```

---

## ✅ Solution Code

### Exercise 1 Solutions

```python
from typing import Dict, List, Any

def deep_get(data: Dict[str, Any], keys: List[str], default=None) -> Any:
    """Safely access deeply nested dictionary values."""
    try:
        for key in keys:
            data = data[key]
        return data
    except (KeyError, TypeError):
        return default

def deep_set(data: Dict[str, Any], keys: List[str], value: Any) -> None:
    """Set value in deeply nested dictionary."""
    for key in keys[:-1]:
        if key not in data:
            data[key] = {}
        data = data[key]
    data[keys[-1]] = value

def flatten_dict(data: Dict[str, Any], prefix: str = "", separator: str = ".") -> Dict[str, str]:
    """Flatten nested dictionary."""
    flattened = {}
    for key, value in data.items():
        new_key = f"{prefix}{separator}{key}" if prefix else key
        if isinstance(value, dict):
            flattened.update(flatten_dict(value, new_key, separator))
        else:
            flattened[new_key] = str(value)
    return flattened

def merge_dicts(*dicts: Dict[str, Any], strategy: str = "overwrite") -> Dict[str, Any]:
    """Merge multiple dictionaries."""
    result = {}
    for d in dicts:
        if strategy == "overwrite":
            result.update(d)
        # Add other strategies as needed
    return result

def dict_diff(dict1: Dict[str, Any], dict2: Dict[str, Any]) -> Dict[str, List[Any]]:
    """Find differences between dictionaries."""
    keys1, keys2 = set(dict1.keys()), set(dict2.keys())

    return {
        "added": list(keys2 - keys1),
        "removed": list(keys1 - keys2),
        "changed": [k for k in keys1 & keys2 if dict1[k] != dict2[k]],
        "unchanged": [k for k in keys1 & keys2 if dict1[k] == dict2[k]]
    }
```

### Exercise 2 Solutions

```python
import json
from typing import Any, List, Dict

def validate_json_schema(data: Any, schema: Dict[str, Any]) -> List[str]:
    """Validate JSON data against schema."""
    errors = []

    def validate_value(value: Any, schema_part: Dict[str, Any], path: str = "") -> None:
        if "type" in schema_part:
            expected_type = schema_part["type"]
            if expected_type == "string" and not isinstance(value, str):
                errors.append(f"{path}: Expected string, got {type(value).__name__}")
            elif expected_type == "number" and not isinstance(value, (int, float)):
                errors.append(f"{path}: Expected number, got {type(value).__name__}")

        # Add more validation rules as needed

    if isinstance(schema.get("type"), str) and schema["type"] == "object":
        if not isinstance(data, dict):
            errors.append("Root: Expected object")
            return errors

        required = schema.get("required", [])
        for req in required:
            if req not in data:
                errors.append(f"Root: Missing required field '{req}'")

        properties = schema.get("properties", {})
        for key, prop_schema in properties.items():
            if key in data:
                validate_value(data[key], prop_schema, f"Root.{key}")

    return errors

def safe_json_loads(json_str: str) -> tuple:
    """Safely parse JSON string."""
    try:
        data = json.loads(json_str)
        return True, data, ""
    except json.JSONDecodeError as e:
        return False, None, f"JSON decode error: {e}"
    except Exception as e:
        return False, None, f"Unexpected error: {e}"
```

### Exercise 3 Solutions

```python
from typing import Any, Dict

def classify_data(data: Any) -> str:
    """Classify data using match statement."""
    match data:
        case {"type": "user", "name": name}:
            return f"User data: {name}"
        case {"type": "product", "name": name, "price": price}:
            return f"Product: {name} (${price})"
        case [first, *rest] if isinstance(first, (int, float)):
            return f"Numeric list with {len(data)} elements"
        case str() as s if len(s) > 10:
            return f"Long string ({len(s)} chars)"
        case list() as lst:
            return f"List with {len(lst)} items"
        case dict() as d:
            return f"Dictionary with {len(d)} keys"
        case _:
            return f"Other data type: {type(data).__name__}"

def process_config(config: Dict[str, Any]) -> Dict[str, Any]:
    """Process configuration."""
    match config:
        case {"database": {"type": "postgres"} as db}:
            db.setdefault("port", 5432)
        case {"database": {"type": "mysql"} as db}:
            db.setdefault("port", 3306)
        case {"cache": {"type": "redis"} as cache}:
            cache.setdefault("port", 6379)

    return config
```

### Exercise 4 Solutions

```python
from contextlib import contextmanager
import time

class DataProcessingError(Exception):
    """Base exception for data processing."""
    pass

class ValidationError(DataProcessingError):
    """Validation error."""
    pass

class APIError(DataProcessingError):
    """API error."""
    def __init__(self, message: str, status_code: int = None):
        self.status_code = status_code
        super().__init__(message)

@contextmanager
def timer(operation_name: str):
    """Timer context manager."""
    start_time = time.time()
    try:
        yield
    finally:
        elapsed = time.time() - start_time
        print(f"Processing time for {operation_name}: {elapsed:.4f} seconds")

@contextmanager
def safe_file_operation(filename: str, mode: str = "r"):
    """Safe file operations."""
    file = None
    try:
        file = open(filename, mode)
        yield file
    except IOError as e:
        raise DataProcessingError(f"File operation failed: {e}")
    finally:
        if file:
            file.close()
```

---

## 📝 Key Takeaways

1. **Dictionary Operations**: Master nested access, merging, and transformations
2. **JSON Processing**: Handle parsing, validation, and transformation safely
3. **Match Statements**: Use pattern matching for clean, readable code
4. **Error Handling**: Implement comprehensive exception handling and custom exceptions
5. **API Integration**: Build robust clients with retry logic and caching
6. **Context Managers**: Use context managers for resource management
7. **Validation**: Always validate input data and handle edge cases
8. **Testing**: Write comprehensive tests for all error scenarios

---

**Workshop Version**: 1.0
**Last Updated**: February 2026
**Estimated Completion Time**: 120 minutes