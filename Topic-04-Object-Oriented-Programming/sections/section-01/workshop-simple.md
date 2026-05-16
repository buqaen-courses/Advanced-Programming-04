# Workshop: Persistent Library Management System (CRUD with JSON)

**Level**: Beginner  
**Prerequisites**: Basic Python (variables, lists, dictionaries, functions, file I/O)  
**Est. Time**: 90 minutes  

## 🎯 What You Will Learn

- Create simple classes (`Book`, `Member`, `Library`)
- Store data permanently using JSON files
- Implement **Create, Read, Update, Delete** (CRUD) operations for books and members
- Build a complete library system that remembers everything even after restart

---

## 📁 Setup

Create a new folder and inside it create these Python files:

```
library_crud/
├── book.py
├── member.py
├── library.py
└── main.py   (optional – for testing/interaction)
```

The program will automatically create `books.json` and `members.json` when you first run it.

---

## 📖 Exercise 1: The `Book` Class

**Goal**: A class that stores book information and can be converted to/from a dictionary (for JSON).

### Step 1.1 – Basic attributes

Create `book.py`:

```python
class Book:
    def __init__(self, title, author, year=None):
        self.title = title
        self.author = author
        self.year = year   # optional publication year

    def __repr__(self):
        year_str = f" ({self.year})" if self.year else ""
        return f"'{self.title}' by {self.author}{year_str}"
```

### Step 1.2 – Convert to dictionary and back

Add these methods inside the `Book` class:

```python
    def to_dict(self):
        """Convert Book object to a dictionary for JSON."""
        return {
            "title": self.title,
            "author": self.author,
            "year": self.year
        }

    @classmethod
    def from_dict(cls, data):
        """Create a Book object from a dictionary."""
        return cls(
            title=data["title"],
            author=data["author"],
            year=data.get("year")   # .get() returns None if 'year' missing
        )
```

### Step 1.3 – Test the Book class

Add at the bottom of `book.py`:

```python
if __name__ == "__main__":
    b1 = Book("1984", "George Orwell", 1949)
    print(b1)
    print(b1.to_dict())
    b2 = Book.from_dict(b1.to_dict())
    print(b2)
```

Run `python book.py` and verify output.

---

## 👥 Exercise 2: The `Member` Class

**Goal**: Store member information with a unique ID.

Create `member.py`:

```python
class Member:
    def __init__(self, name, member_id, email=None):
        self.name = name
        self.member_id = member_id   # e.g., "M001"
        self.email = email

    def __repr__(self):
        email_str = f" <{self.email}>" if self.email else ""
        return f"{self.name} (ID: {self.member_id}){email_str}"

    def to_dict(self):
        return {
            "name": self.name,
            "member_id": self.member_id,
            "email": self.email
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data["name"],
            member_id=data["member_id"],
            email=data.get("email")
        )
```

Test it similarly (optional).

---

## 🏛️ Exercise 3: The `Library` Class with JSON Persistence

**Goal**: Manage collections of books and members, save/load automatically to/from JSON files.

### Step 3.1 – Initialize and load/create JSON files

Create `library.py`:

```python
import json
import os
from book import Book
from member import Member

class Library:
    def __init__(self, books_file="books.json", members_file="members.json"):
        self.books_file = books_file
        self.members_file = members_file
        self.books = []      # list of Book objects
        self.members = []    # list of Member objects
        
        # Load existing data or create empty files
        self.load_data()
    
    def load_data(self):
        """Load books and members from JSON files. If files don't exist, create empty ones."""
        # Load books
        if os.path.exists(self.books_file):
            with open(self.books_file, "r") as f:
                books_data = json.load(f)
            self.books = [Book.from_dict(b) for b in books_data]
        else:
            self.books = []
            self._save_books()   # create empty file
    
        # Load members
        if os.path.exists(self.members_file):
            with open(self.members_file, "r") as f:
                members_data = json.load(f)
            self.members = [Member.from_dict(m) for m in members_data]
        else:
            self.members = []
            self._save_members()
    
    def _save_books(self):
        """Save current books list to JSON file."""
        with open(self.books_file, "w") as f:
            json.dump([b.to_dict() for b in self.books], f, indent=2)
    
    def _save_members(self):
        """Save current members list to JSON file."""
        with open(self.members_file, "w") as f:
            json.dump([m.to_dict() for m in self.members], f, indent=2)
```

### Step 3.2 – Add, list, update, delete books

Add these methods to the `Library` class:

```python
    # ---------- Book CRUD ----------
    def add_book(self, book):
        """Add a new book (if not already present by title+author)."""
        # Check for duplicate
        for b in self.books:
            if b.title.lower() == book.title.lower() and b.author.lower() == book.author.lower():
                print(f"Book '{book.title}' by {book.author} already exists.")
                return False
        self.books.append(book)
        self._save_books()
        print(f"Added: {book}")
        return True

    def list_books(self):
        """Display all books."""
        if not self.books:
            print("No books in the library.")
        else:
            print("\n--- Books ---")
            for idx, book in enumerate(self.books, 1):
                print(f"{idx}. {book}")
            print(f"Total: {len(self.books)} books\n")

    def find_book_by_title(self, title):
        """Return book object with matching title (case-insensitive)."""
        title_lower = title.lower()
        for book in self.books:
            if book.title.lower() == title_lower:
                return book
        return None

    def update_book(self, old_title, new_title=None, new_author=None, new_year=None):
        """Update a book's details. Searches by old_title."""
        book = self.find_book_by_title(old_title)
        if not book:
            print(f"Book '{old_title}' not found.")
            return False
        if new_title:
            book.title = new_title
        if new_author:
            book.author = new_author
        if new_year is not None:
            book.year = new_year
        self._save_books()
        print(f"Updated book: {book}")
        return True

    def delete_book(self, title):
        """Remove a book by title."""
        book = self.find_book_by_title(title)
        if not book:
            print(f"Book '{title}' not found.")
            return False
        self.books.remove(book)
        self._save_books()
        print(f"Deleted book: {book}")
        return True
```

### Step 3.3 – Member CRUD (similar pattern)

Add these methods:

```python
    # ---------- Member CRUD ----------
    def add_member(self, member):
        """Add a new member (unique member_id)."""
        for m in self.members:
            if m.member_id == member.member_id:
                print(f"Member ID {member.member_id} already exists.")
                return False
        self.members.append(member)
        self._save_members()
        print(f"Added: {member}")
        return True

    def list_members(self):
        """Display all members."""
        if not self.members:
            print("No members in the library.")
        else:
            print("\n--- Members ---")
            for idx, member in enumerate(self.members, 1):
                print(f"{idx}. {member}")
            print(f"Total: {len(self.members)} members\n")

    def find_member_by_id(self, member_id):
        """Return member object with given ID."""
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

    def update_member(self, member_id, new_name=None, new_email=None):
        """Update member details."""
        member = self.find_member_by_id(member_id)
        if not member:
            print(f"Member ID {member_id} not found.")
            return False
        if new_name:
            member.name = new_name
        if new_email is not None:
            member.email = new_email
        self._save_members()
        print(f"Updated member: {member}")
        return True

    def delete_member(self, member_id):
        """Remove a member by ID."""
        member = self.find_member_by_id(member_id)
        if not member:
            print(f"Member ID {member_id} not found.")
            return False
        self.members.remove(member)
        self._save_members()
        print(f"Deleted member: {member}")
        return True
```

---

## 🚀 Exercise 4: Putting It All Together – Interactive Menu

Create `main.py` to test the system with a simple console menu.

```python
from library import Library
from book import Book
from member import Member

def main():
    lib = Library()
    
    while True:
        print("\n" + "="*40)
        print("LIBRARY MANAGEMENT SYSTEM")
        print("="*40)
        print("1. List all books")
        print("2. Add a book")
        print("3. Update a book")
        print("4. Delete a book")
        print("5. List all members")
        print("6. Add a member")
        print("7. Update a member")
        print("8. Delete a member")
        print("0. Exit")
        
        choice = input("\nEnter your choice: ").strip()
        
        if choice == "1":
            lib.list_books()
        
        elif choice == "2":
            title = input("Title: ").strip()
            author = input("Author: ").strip()
            year_str = input("Year (optional, press Enter to skip): ").strip()
            year = int(year_str) if year_str.isdigit() else None
            book = Book(title, author, year)
            lib.add_book(book)
        
        elif choice == "3":
            old_title = input("Enter current title of the book to update: ").strip()
            new_title = input("New title (Enter to keep): ").strip() or None
            new_author = input("New author (Enter to keep): ").strip() or None
            year_str = input("New year (Enter to keep): ").strip()
            new_year = int(year_str) if year_str.isdigit() else None
            lib.update_book(old_title, new_title, new_author, new_year)
        
        elif choice == "4":
            title = input("Enter title of book to delete: ").strip()
            lib.delete_book(title)
        
        elif choice == "5":
            lib.list_members()
        
        elif choice == "6":
            name = input("Name: ").strip()
            member_id = input("Member ID (e.g., M001): ").strip()
            email = input("Email (optional): ").strip() or None
            member = Member(name, member_id, email)
            lib.add_member(member)
        
        elif choice == "7":
            member_id = input("Enter Member ID to update: ").strip()
            new_name = input("New name (Enter to keep): ").strip() or None
            new_email = input("New email (Enter to keep): ").strip() or None
            lib.update_member(member_id, new_name, new_email)
        
        elif choice == "8":
            member_id = input("Enter Member ID to delete: ").strip()
            lib.delete_member(member_id)
        
        elif choice == "0":
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```

Run `python main.py` and test adding, listing, updating, and deleting books and members. Close and restart – your data will persist in `books.json` and `members.json`.

---

## ✅ What You Have Built

- **Persistent storage** using JSON – no database needed
- **CRUD operations** for books and members
- **Object-oriented design** with three cooperating classes
- **Automatic file handling** – empty files created if missing
- **Simple console interface** for real interaction

---

## 🔧 Challenge Exercises (Optional)

1. **Search books by author** – add a method to list all books by a given author.
2. **Prevent duplicate member IDs** – already done, but improve error message.
3. **Add a `status` field to books** – e.g., "Good", "Damaged", "Lost".
4. **Export library to CSV** – write a method that saves books and members to CSV files.
5. **Add a simple borrowing feature** – if you want to extend later, add a `borrow_book(member_id, book_title)` that checks both exist and updates a new field `borrowed_by` in Book.

---

## 📚 Full Code List (Summary)

- `book.py` – Book class with `to_dict/from_dict`
- `member.py` – Member class with `to_dict/from_dict`
- `library.py` – Library class with JSON load/save and CRUD methods
- `main.py` – Interactive menu

All files are provided above. You can copy them directly into your project folder and run `python main.py`.

---

**Workshop Version**: 2.0 (CRUD with JSON persistence)  
**Last Updated**: March 2026  
**Estimated Completion Time**: 90 minutes