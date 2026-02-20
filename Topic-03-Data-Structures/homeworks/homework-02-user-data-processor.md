# Homework 2: User Data Processor with JSON & APIs

**Section**: 7 - JSON Handling & API Integration (120 min)
**Level**: Intermediate
**Prerequisites**: Tutorial 2 (JSON & API Integration)

---

## 🎯 Assignment Objectives

By completing this homework, you will demonstrate your ability to:

1. **Master JSON Processing**: Parse, create, and manipulate JSON data structures
2. **Work with APIs**: Make HTTP requests and handle responses from web APIs
3. **Process Real Data**: Extract and transform data from API responses
4. **Implement Error Handling**: Handle network errors, invalid data, and edge cases
5. **Build Reusable Components**: Create modular API client and data processor classes
6. **Apply Data Structures**: Use dictionaries, lists effectively for data manipulation

---

## 📋 Assignment Structure

This homework consists of 3 main tasks:

1. [Task 1: JSON Data Processor](#task-1-json-data-processor) (40 points)
2. [Task 2: API Integration](#task-2-api-integration) (35 points)
3. [Task 3: Complete User Data System](#task-3-complete-user-data-system) (25 points)

---

## 🏃 Task 1: JSON Data Processor

**Points: 40** | **Time Estimate: 45 minutes**

Create a module called `json_processor.py` with the following functionality:

### 1.1 JSON File Operations

```python
import json
from typing import Dict, List, Any, Optional
from pathlib import Path

class JSONDataProcessor:
    """Process JSON data with file operations and transformations."""

    def __init__(self, data_dir: str = "data"):
        """
        Initialize processor with data directory.

        Args:
            data_dir: Directory to store/load JSON files
        """
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(exist_ok=True)

    def load_json_file(self, filename: str) -> Optional[Dict[str, Any]]:
        """
        Load JSON data from file with error handling.

        Args:
            filename: Name of JSON file (without .json extension)

        Returns:
            Loaded data or None if error
        """
        pass

    def save_json_file(self, data: Dict[str, Any], filename: str, indent: int = 2) -> bool:
        """
        Save data to JSON file with error handling.

        Args:
            data: Data to save
            filename: Name of JSON file (without .json extension)
            indent: JSON indentation level

        Returns:
            True if successful, False otherwise
        """
        pass

    def validate_json_structure(self, data: Any, schema: Dict[str, Any]) -> bool:
        """
        Validate JSON data against a simple schema.

        Args:
            data: Data to validate
            schema: Schema definition with required fields and types

        Returns:
            True if valid, False otherwise

        Schema format:
        {
            "required_fields": ["name", "age"],
            "field_types": {"name": str, "age": int}
        }
        """
        pass
```

### 1.2 Data Transformation Functions

```python
def flatten_nested_dict(data: Dict[str, Any], prefix: str = "") -> Dict[str, Any]:
    """
    Flatten a nested dictionary into a single-level dictionary.

    Args:
        data: Nested dictionary
        prefix: Prefix for flattened keys

    Returns:
        Flattened dictionary

    Examples:
        >>> flatten_nested_dict({"user": {"name": "Alice", "age": 25}})
        {"user.name": "Alice", "user.age": 25}
    """
    pass

def unflatten_dict(data: Dict[str, Any], separator: str = ".") -> Dict[str, Any]:
    """
    Convert flattened dictionary back to nested structure.

    Args:
        data: Flattened dictionary
        separator: Key separator

    Returns:
        Nested dictionary

    Examples:
        >>> unflatten_dict({"user.name": "Alice", "user.age": 25})
        {"user": {"name": "Alice", "age": 25}}
    """
    pass

def merge_json_objects(*objects: Dict[str, Any]) -> Dict[str, Any]:
    """
    Merge multiple JSON objects with conflict resolution.

    Args:
        *objects: Variable number of dictionaries to merge

    Returns:
        Merged dictionary (later objects override earlier ones)

    Examples:
        >>> merge_json_objects({"a": 1, "b": 2}, {"b": 3, "c": 4})
        {"a": 1, "b": 3, "c": 4}
    """
    pass

def filter_json_data(data: List[Dict[str, Any]], filters: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    Filter JSON data based on criteria.

    Args:
        data: List of dictionaries
        filters: Filter criteria dictionary

    Returns:
        Filtered list

    Examples:
        >>> data = [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 30}]
        >>> filter_json_data(data, {"age_min": 26})
        [{"name": "Bob", "age": 30}]
    """
    pass
```

### 1.3 JSON Data Analysis

```python
def analyze_json_structure(data: Any) -> Dict[str, Any]:
    """
    Analyze the structure and content of JSON data.

    Args:
        data: JSON data to analyze

    Returns:
        Analysis dictionary with:
        - data_type: Type of root element
        - depth: Maximum nesting depth
        - total_keys: Total number of keys (for dicts)
        - total_elements: Total number of elements (for lists)
        - field_types: Types of values for each field
    """
    pass

def extract_json_paths(data: Any, current_path: str = "") -> List[str]:
    """
    Extract all possible JSON paths in the data structure.

    Args:
        data: JSON data
        current_path: Current path prefix

    Returns:
        List of all paths in the structure

    Examples:
        >>> data = {"user": {"name": "Alice", "scores": [85, 92]}}
        >>> extract_json_paths(data)
        ["user", "user.name", "user.scores", "user.scores[0]", "user.scores[1]"]
    """
    pass

def compare_json_objects(obj1: Any, obj2: Any) -> Dict[str, Any]:
    """
    Compare two JSON objects and identify differences.

    Args:
        obj1, obj2: Objects to compare

    Returns:
        Comparison result with:
        - are_equal: Boolean
        - differences: List of differences found
        - obj1_only: Keys/paths only in obj1
        - obj2_only: Keys/paths only in obj2
    """
    pass
```

---

## 🌐 Task 2: API Integration

**Points: 35** | **Time Estimate: 40 minutes**

Create a module called `api_client.py` with API integration functionality:

### 2.1 Base API Client

```python
import requests
from typing import Dict, List, Any, Optional
import time

class APIClient:
    """Base API client with common functionality."""

    def __init__(self, base_url: str, timeout: int = 10, retries: int = 3):
        """
        Initialize API client.

        Args:
            base_url: Base URL for API
            timeout: Request timeout in seconds
            retries: Number of retries for failed requests
        """
        self.base_url = base_url.rstrip('/')
        self.timeout = timeout
        self.retries = retries
        self.session = requests.Session()

    def _make_request(self, method: str, endpoint: str,
                     params: Optional[Dict[str, Any]] = None,
                     data: Optional[Dict[str, Any]] = None,
                     json_data: Optional[Dict[str, Any]] = None) -> Optional[Dict[str, Any]]:
        """
        Make HTTP request with error handling and retries.

        Args:
            method: HTTP method (GET, POST, etc.)
            endpoint: API endpoint
            params: Query parameters
            data: Form data
            json_data: JSON data

        Returns:
            Response JSON data or None if error
        """
        pass

    def get(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Optional[Dict[str, Any]]:
        """Make GET request."""
        pass

    def post(self, endpoint: str, data: Optional[Dict[str, Any]] = None) -> Optional[Dict[str, Any]]:
        """Make POST request."""
        pass

    def close(self):
        """Close the session."""
        self.session.close()
```

### 2.2 RandomUser API Client

```python
class RandomUserAPIClient(APIClient):
    """Client for randomuser.me API."""

    def __init__(self):
        super().__init__("https://randomuser.me/api")

    def get_random_users(self, count: int = 1,
                        gender: Optional[str] = None,
                        nationality: Optional[str] = None) -> Optional[List[Dict[str, Any]]]:
        """
        Get random user data.

        Args:
            count: Number of users to fetch (max 5000)
            gender: Filter by gender ("male", "female")
            nationality: Filter by nationality (ISO country code)

        Returns:
            List of user data or None if error
        """
        pass

    def get_user_by_seed(self, seed: str) -> Optional[Dict[str, Any]]:
        """
        Get a specific user by seed (deterministic results).

        Args:
            seed: Seed string for reproducible results

        Returns:
            User data or None if error
        """
        pass

    def search_users(self, query: Dict[str, Any]) -> Optional[List[Dict[str, Any]]]:
        """
        Search users with complex criteria.

        Args:
            query: Search criteria dictionary

        Returns:
            List of matching users or None if error
        """
        pass
```

### 2.3 Data Caching

```python
import json
from pathlib import Path
from datetime import datetime, timedelta

class CachedAPIClient(APIClient):
    """API client with response caching."""

    def __init__(self, base_url: str, cache_dir: str = ".cache", cache_ttl: int = 300):
        """
        Initialize cached API client.

        Args:
            base_url: Base URL for API
            cache_dir: Cache directory
            cache_ttl: Cache time-to-live in seconds
        """
        super().__init__(base_url)
        self.cache_dir = Path(cache_dir)
        self.cache_ttl = cache_ttl
        self.cache_dir.mkdir(exist_ok=True)

    def _get_cache_key(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> str:
        """Generate cache key for request."""
        pass

    def _is_cache_valid(self, cache_file: Path) -> bool:
        """Check if cache file is still valid."""
        pass

    def _load_from_cache(self, cache_key: str) -> Optional[Dict[str, Any]]:
        """Load data from cache."""
        pass

    def _save_to_cache(self, cache_key: str, data: Dict[str, Any]):
        """Save data to cache."""
        pass

    def get_cached(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Optional[Dict[str, Any]]:
        """Make GET request with caching."""
        pass
```

---

## 🏗️ Task 3: Complete User Data System

**Points: 25** | **Time Estimate: 35 minutes**

Create a complete user data processing system that integrates all components.

### 3.1 User Data Manager

```python
class UserDataManager:
    """Complete user data management system."""

    def __init__(self, api_client=None, data_processor=None):
        """
        Initialize user data manager.

        Args:
            api_client: API client instance
            data_processor: JSON processor instance
        """
        self.api_client = api_client or RandomUserAPIClient()
        self.data_processor = data_processor or JSONDataProcessor()
        self.users_cache = []

    def fetch_users(self, count: int = 10, **filters) -> List[Dict[str, Any]]:
        """
        Fetch users from API with caching.

        Args:
            count: Number of users to fetch
            **filters: Additional filters (gender, nationality, etc.)

        Returns:
            List of processed user data
        """
        pass

    def process_user_data(self, raw_users: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Process raw API user data into clean format.

        Args:
            raw_users: Raw user data from API

        Returns:
            Processed user data with standardized fields
        """
        pass

    def save_users_to_file(self, users: List[Dict[str, Any]], filename: str) -> bool:
        """
        Save processed users to JSON file.

        Args:
            users: User data to save
            filename: Output filename

        Returns:
            True if successful
        """
        pass

    def load_users_from_file(self, filename: str) -> Optional[List[Dict[str, Any]]]:
        """
        Load users from JSON file.

        Args:
            filename: Input filename

        Returns:
            Loaded user data or None if error
        """
        pass

    def search_users(self, criteria: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Search users in cache by criteria.

        Args:
            criteria: Search criteria

        Returns:
            Matching users
        """
        pass

    def generate_user_report(self, users: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Generate comprehensive report from user data.

        Args:
            users: User data to analyze

        Returns:
            Report with statistics and insights
        """
        pass
```

### 3.2 User Data Analysis

```python
def analyze_user_demographics(users: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Analyze user demographics.

    Args:
        users: List of user data

    Returns:
        Demographics analysis with:
        - age_distribution
        - gender_distribution
        - country_distribution
        - average_age
        - age_groups
    """
    pass

def find_similar_users(users: List[Dict[str, Any]], target_user: Dict[str, Any],
                      similarity_criteria: List[str]) -> List[Dict[str, Any]]:
    """
    Find users similar to target user.

    Args:
        users: All users to search
        target_user: User to compare against
        similarity_criteria: Fields to use for similarity

    Returns:
        List of similar users sorted by similarity score
    """
    pass

def export_user_data(users: List[Dict[str, Any]], format_type: str = "json",
                    filename: str = "users") -> bool:
    """
    Export user data in different formats.

    Args:
        format_type: Export format ("json", "csv")
        filename: Base filename (without extension)

    Returns:
        True if successful
    """
    pass
```

---

## 📤 Submission Requirements

### Code Quality (25 points)
- **Modular Design**: Separate concerns into appropriate classes/modules
- **Error Handling**: Comprehensive error handling for all operations
- **Documentation**: Complete docstrings and comments
- **Type Safety**: Use type hints throughout
- **Resource Management**: Proper session/file handling

### Functionality (50 points)
- **API Integration**: Correctly fetch and process API data
- **Data Processing**: Properly transform and validate JSON data
- **Caching**: Implement effective caching mechanism
- **Search/Filter**: Efficient data querying and filtering

### Testing & Integration (25 points)
- **Unit Tests**: Test individual functions and methods
- **Integration Tests**: Test complete workflows
- **API Error Handling**: Test network failures and invalid responses
- **Data Validation**: Test with various data formats and edge cases

### File Structure
```
homework-02-user-data-processor/
├── json_processor.py        # Task 1 - JSON processing
├── api_client.py           # Task 2 - API integration
├── user_data_manager.py    # Task 3 - Complete system
├── test_homework.py        # Comprehensive tests
└── README.md              # Documentation
```

---

## 🧪 Testing Guidelines

Create comprehensive tests covering:

```python
def test_json_processing():
    """Test JSON processor functionality."""
    processor = JSONDataProcessor()

    # Test file operations
    test_data = {"name": "Alice", "age": 25}
    assert processor.save_json_file(test_data, "test_user")

    loaded = processor.load_json_file("test_user")
    assert loaded == test_data

    # Test validation
    schema = {"required_fields": ["name"], "field_types": {"name": str}}
    assert processor.validate_json_structure(test_data, schema)

    # Test transformations
    nested = {"user": {"info": {"name": "Bob"}}}
    flattened = flatten_nested_dict(nested)
    assert flattened["user.info.name"] == "Bob"

def test_api_integration():
    """Test API client functionality."""
    client = RandomUserAPIClient()

    # Test user fetching
    users = client.get_random_users(2)
    assert users is not None
    assert len(users) == 2

    # Test data structure
    user = users[0]
    assert "name" in user
    assert "email" in user

def test_complete_system():
    """Test integrated user data system."""
    manager = UserDataManager()

    # Test data fetching and processing
    users = manager.fetch_users(3)
    assert len(users) == 3

    # Test file operations
    assert manager.save_users_to_file(users, "test_users")
    loaded = manager.load_users_from_file("test_users")
    assert loaded == users

    # Test analysis
    report = manager.generate_user_report(users)
    assert "total_users" in report
    assert "average_age" in report

if __name__ == "__main__":
    test_json_processing()
    test_api_integration()
    test_complete_system()
    print("All tests passed! ✅")
```

---

## 📊 Grading Rubric

| Criteria | Excellent (90-100%) | Good (80-89%) | Satisfactory (70-79%) | Needs Improvement (<70%) |
|----------|-------------------|---------------|---------------------|-------------------------|
| **API Integration** | Robust error handling, proper authentication, efficient caching | Good error handling, basic caching | Basic API calls, minimal error handling | Poor API integration, no error handling |
| **Data Processing** | Complex transformations, validation, efficient algorithms | Good transformations, basic validation | Basic processing, some validation | Minimal processing, no validation |
| **Code Quality** | Clean, modular, well-documented, type hints | Good structure, some documentation | Basic structure, minimal docs | Poor structure, undocumented |
| **Testing** | Comprehensive tests, edge cases covered, integration tests | Good test coverage, some edge cases | Basic tests, missing edge cases | Minimal testing, no edge cases |

---

## 🎯 Learning Outcomes Assessment

After completing this homework, you should be able to:
- ✅ Parse and generate JSON data with proper error handling
- ✅ Make HTTP requests to REST APIs with authentication and caching
- ✅ Process and transform complex nested data structures
- ✅ Build modular, reusable components for data processing
- ✅ Handle network errors, invalid data, and edge cases gracefully
- ✅ Apply dictionaries and lists effectively for real-world data manipulation

---

**Homework Version**: 1.0
**Last Updated**: February 2026
**Estimated Completion Time**: 120 minutes