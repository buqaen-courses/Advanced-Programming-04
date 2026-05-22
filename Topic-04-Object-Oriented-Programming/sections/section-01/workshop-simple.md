# Workshop: Persistent Library Management System (CRUD with JSON) – Step‑by‑Step

**Level**: Beginner  
**Prerequisites**: Basic Python (variables, lists, dictionaries, functions, file I/O)  
**Est. Time**: 90 minutes

## 🎯 What You Will Learn

- Create simple classes (`Book`, `Member`, `Library`)  
- Store data permanently using JSON files  
- Implement **Create, Read, Update, Delete** (CRUD) operations for books and members  
- Build a complete library system that remembers everything even after restart  

---

## 📁 Step 0 – Folder Setup

Create a new folder on your computer and inside it create **empty** Python files:

```
library_crud/
├── book.py
├── member.py
├── library.py
└── main.py
```

All code you write will go into these files.  
The program will later create `books.json` and `members.json` automatically.

---

## 📖 Step 1 – Build the `Book` Class

**Goal**: A class that stores book information and can be converted to/from a dictionary (for JSON).

### 1.1 Basic attributes and `__repr__`

Open `book.py` and type:

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

**Explanation**:  
- `__init__` stores title, author, and an optional year.  
- `__repr__` gives a friendly representation when we print a book.

### 1.2 Add dictionary conversion methods

Add these two methods inside the `Book` class (after `__repr__`):

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

**Explanation**:  
- `to_dict` turns a `Book` into a plain dictionary so JSON can save it.  
- `from_dict` is a **class method** that rebuilds a `Book` from a dictionary (used when loading from JSON).

### 1.3 Test the `Book` class

At the bottom of `book.py`, add:

```python
if __name__ == "__main__":
    b1 = Book("1984", "George Orwell", 1949)
    print(b1)
    print(b1.to_dict())
    b2 = Book.from_dict(b1.to_dict())
    print(b2)
```

Now **run** the file:

```bash
python book.py
```

**Expected output**:  
```
'1984' by George Orwell (1949)
{'title': '1984', 'author': 'George Orwell', 'year': 1949}
'1984' by George Orwell (1949)
```

✅ **Test passed** – your `Book` class works.

---

## 👥 Step 2 – Build the `Member` Class

**Goal**: Store member information with a unique ID.

Open `member.py` and type the complete class:

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

**Explanation**: Same pattern as `Book` – `to_dict` / `from_dict` allow JSON storage.

### Test `Member` (optional)

If you want, add a similar test block at the bottom of `member.py`:

```python
if __name__ == "__main__":
    m1 = Member("Alice", "M001", "alice@example.com")
    print(m1)
    print(m1.to_dict())
    m2 = Member.from_dict(m1.to_dict())
    print(m2)
```

Run `python member.py` to verify.

---

## 🏛️ Step 3 – Start the `Library` Class with JSON Persistence

**Goal**: Manage collections of books and members, save/load automatically to/from JSON files.

### 3.1 Initialization and file loading

Open `library.py`. First, import the required modules and the two classes:

```python
import json
import os
from book import Book
from member import Member
```

Now define the `Library` class with `__init__` and the load/save helpers:

```python
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

**Explanation**:  
- When you create a `Library` object, it automatically loads any existing JSON files (or creates empty ones).  
- `_save_books` and `_save_members` write the current lists to disk. They are called after every change.

### 3.2 Test that files are created

Create a temporary test at the bottom of `library.py`:

```python
if __name__ == "__main__":
    lib = Library()
    print("Books loaded:", lib.books)
    print("Members loaded:", lib.members)
```

Run `python library.py`. You should see empty lists, and two new files `books.json` and `members.json` appear in your folder. Open them – they contain `[]` (empty list).  
✅ **Persistence setup works**.

---

## 📚 Step 4 – Add Book CRUD Operations (one by one)

Now we will add methods to the `Library` class. After each method, you will test it with a small piece of code.

### 4.1 Add a book – `add_book`

Inside `Library` class, add this method:

```python
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
```

**What it does**:  
- Prevents duplicate books (same title and author, case‑insensitive).  
- Adds the book to the `self.books` list and immediately saves to JSON.

**Test it** – replace the test block in `library.py` with:

```python
if __name__ == "__main__":
    lib = Library()
    b = Book("The Hobbit", "J.R.R. Tolkien", 1937)
    lib.add_book(b)
    lib.list_books()   # we haven't written list_books yet – we'll do that next
```

But `list_books` is missing. Let's add it now.

### 4.2 List all books – `list_books`

Add this method to `Library`:

```python
    def list_books(self):
        """Display all books."""
        if not self.books:
            print("No books in the library.")
        else:
            print("\n--- Books ---")
            for idx, book in enumerate(self.books, 1):
                print(f"{idx}. {book}")
            print(f"Total: {len(self.books)} books\n")
```

Now change the test block to:

```python
if __name__ == "__main__":
    lib = Library()
    lib.list_books()                     # should show "No books"
    b = Book("The Hobbit", "J.R.R. Tolkien", 1937)
    lib.add_book(b)
    lib.list_books()                     # should show one book
```

Run `python library.py`. You should see:

```
No books in the library.
Added: 'The Hobbit' by J.R.R. Tolkien (1937)

--- Books ---
1. 'The Hobbit' by J.R.R. Tolkien (1937)
Total: 1 books
```

✅ **Add and list work**.

### 4.3 Find a book by title – `find_book_by_title`

Add this helper method – it will be used by update and delete:

```python
    def find_book_by_title(self, title):
        """Return book object with matching title (case-insensitive)."""
        title_lower = title.lower()
        for book in self.books:
            if book.title.lower() == title_lower:
                return book
        return None
```

**Test quickly** – add to your test block:

```python
    found = lib.find_book_by_title("the hobbit")
    print("Found:", found)
```

Run again – it should print the book.

### 4.4 Update a book – `update_book`

Add this method:

```python
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
```

**What it does**:  
- Finds the book by its current title.  
- Changes only the fields you provide (others stay the same).  
- Saves to JSON immediately.

**Test** – extend your test block:

```python
    lib.update_book("The Hobbit", new_year=1950)
    lib.list_books()
```

Run – you should see the year changed to 1950.

### 4.5 Delete a book – `delete_book`

Add:

```python
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

**Test** – after the update test, add:

```python
    lib.delete_book("The Hobbit")
    lib.list_books()
```

Run – the book should be gone, and `books.json` should be an empty array.

✅ **All book CRUD operations work**.

---

## 👥 Step 5 – Add Member CRUD Operations

Follow the same pattern. Add these methods to the `Library` class **after** the book methods.

### 5.1 Add member – `add_member`

```python
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
```

### 5.2 List members – `list_members`

```python
    def list_members(self):
        """Display all members."""
        if not self.members:
            print("No members in the library.")
        else:
            print("\n--- Members ---")
            for idx, member in enumerate(self.members, 1):
                print(f"{idx}. {member}")
            print(f"Total: {len(self.members)} members\n")
```

### 5.3 Find member by ID – `find_member_by_id`

```python
    def find_member_by_id(self, member_id):
        """Return member object with given ID."""
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None
```

### 5.4 Update member – `update_member`

```python
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
```

### 5.5 Delete member – `delete_member`

```python
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

### 5.6 Test member CRUD

Create a new test block at the bottom of `library.py` (or replace the previous one) to verify:

```python
if __name__ == "__main__":
    lib = Library()
    m = Member("Alice", "M001", "alice@example.com")
    lib.add_member(m)
    lib.list_members()
    lib.update_member("M001", new_name="Alice Cooper")
    lib.list_members()
    lib.delete_member("M001")
    lib.list_members()
```

Run `python library.py`. You should see add, update, and delete working correctly.

---

## 🚀 Step 6 – Build the Interactive Menu (main.py)

Now we combine everything into a user‑friendly console program.

Open `main.py` and write:

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

**Explanation**:  
- The menu calls the methods you built in `Library`.  
- Input handling allows optional fields (year, email).  
- The loop continues until you press `0`.

---

## ✅ Step 7 – Run and Test the Full System

1. **Run** `python main.py`  
2. **Test each option** in order:  
   - Option 2 – Add two books.  
   - Option 1 – List books → you should see them.  
   - Option 3 – Update a book (choose an existing title).  
   - Option 4 – Delete a book.  
   - Option 6,7,8 – Do the same for members.  
3. **Close the program** (option 0) and run `python main.py` again.  
   - Your added books and members are still there – they were saved in `books.json` and `members.json`.

🎉 **Congratulations! You have built a persistent library management system with full CRUD operations.**

---

## 🔧 Challenge Exercises (Optional)

1. **Search books by author** – add a method to `Library` that lists all books by a given author, then add a menu option.  
2. **Prevent duplicate member IDs** – already done, but improve the error message.  
3. **Add a `status` field to books** – e.g., "Good", "Damaged", "Lost". Update `Book` and modify add/update.  
4. **Export library to CSV** – write methods that save books and members to CSV files.  
5. **Add a simple borrowing feature** – `borrow_book(member_id, book_title)` that checks both exist and adds a `borrowed_by` field to `Book`.

---

## 📚 Final Code Summary

- `book.py` – Book class with `to_dict/from_dict`  
- `member.py` – Member class with `to_dict/from_dict`  
- `library.py` – Library class with JSON load/save and CRUD methods  
- `main.py` – Interactive menu  

All files are now complete. Run `python main.py` and enjoy your working library system!