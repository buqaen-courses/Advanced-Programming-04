# Step‑by‑Step Workshop: Building a Persistent Library System with OOP

**Level**: Beginner  
**Prerequisites**: Basic Python (variables, loops, lists, functions)  
**Est. Time**: 2–3 hours (can be split over several sessions)

---

## 🎯 Learning Objectives

By the end of this workshop, you will be able to:

1. Define simple classes (`Book`, `Member`) with attributes and methods.
2. Use `if __name__ == '__main__'` to test your code.
3. Store and retrieve data using **JSON** files.
4. Build **Manager classes** that handle saving, loading, searching, updating, and deleting objects.
5. Combine everything into a **Library** class that ties books and members together.

You will work **step by step**, testing each new feature before moving to the next.

---

## 📁 Project Setup

Create a new folder. Inside it, create these empty Python files:

```
library_project/
├── book.py
├── member.py
├── book_manager.py      (will be created later)
├── member_manager.py    (will be created later)
└── library.py           (will be created later)
```

We will start with `book.py` and `member.py`, then gradually add the other files as we progress.

---

# Step 1: Simple Classes Without Persistence

## 1.1 Create the `Book` Class

Open `book.py` and write:

```python
class Book:
    """A simple Book class."""
    def __init__(self, title, author, year=None):
        self.title = title
        self.author = author
        self.year = year

    def __repr__(self):
        year_str = f" ({self.year})" if self.year else ""
        return f"'{self.title}' by {self.author}{year_str}"
```

Now add a test section at the bottom that creates an empty list, asks the user to enter books, and prints them:

```python
if __name__ == "__main__":
    books = []   # empty list to hold Book objects

    while True:
        print("\n--- Book Menu ---")
        print("1. Add a book")
        print("2. Show all books")
        print("3. Exit")
        choice = input("Choose: ")

        if choice == "1":
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year (optional): ")
            year = int(year) if year.isdigit() else None
            book = Book(title, author, year)
            books.append(book)
            print(f"Added: {book}")

        elif choice == "2":
            if not books:
                print("No books yet.")
            else:
                print("\n--- Your Books ---")
                for i, book in enumerate(books, 1):
                    print(f"{i}. {book}")

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")
```

**Test it:** Run `python book.py`. Add a few books, list them, exit. Notice that after you exit, the books disappear – they are not saved. We will fix that in the next step.

## 1.2 Create the `Member` Class (same pattern)

Open `member.py` and write:

```python
class Member:
    def __init__(self, name, member_id, email=None):
        self.name = name
        self.member_id = member_id
        self.email = email

    def __repr__(self):
        email_str = f" <{self.email}>" if self.email else ""
        return f"{self.name} (ID: {self.member_id}){email_str}"
```

Add a similar test loop:

```python
if __name__ == "__main__":
    members = []

    while True:
        print("\n--- Member Menu ---")
        print("1. Add a member")
        print("2. Show all members")
        print("3. Exit")
        choice = input("Choose: ")

        if choice == "1":
            name = input("Name: ")
            member_id = input("ID (e.g., M001): ")
            email = input("Email (optional): ") or None
            member = Member(name, member_id, email)
            members.append(member)
            print(f"Added: {member}")

        elif choice == "2":
            if not members:
                print("No members yet.")
            else:
                print("\n--- Your Members ---")
                for i, m in enumerate(members, 1):
                    print(f"{i}. {m}")

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")
```

Run `python member.py` and test it. Now we have two independent programs. Next we will make them **saved to disk** using JSON.

---

# Step 2: Adding Persistence with JSON

## 2.1 Learn JSON basics

JSON (JavaScript Object Notation) is a text format that looks like Python dictionaries and lists. Python can convert objects to JSON using the `json` module.

Add `import json` at the top of `book.py` and `member.py`.

## 2.2 Add `to_dict` and `from_dict` methods to `Book`

Inside the `Book` class, add:

```python
    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "year": self.year
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            title=data["title"],
            author=data["author"],
            year=data.get("year")
        )
```

Similarly, add to `Member` class:

```python
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

## 2.3 Save and load in the test section

We will modify the `if __name__ == '__main__'` block in `book.py` so that on startup it loads existing books from `books.json`, and after each change (add, delete, update – we haven't added delete/update yet) it saves automatically.

For now, we will load at the beginning and save after adding a book. Replace the test section in `book.py` with:

```python
if __name__ == "__main__":
    import json
    import os

    DATA_FILE = "books.json"

    # Load existing books if any
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            books_data = json.load(f)
        books = [Book.from_dict(data) for data in books_data]
        print(f"Loaded {len(books)} books from {DATA_FILE}")
    else:
        books = []
        print("No saved books found. Starting fresh.")

    while True:
        print("\n--- Book Menu ---")
        print("1. Add a book")
        print("2. Show all books")
        print("3. Exit")
        choice = input("Choose: ")

        if choice == "1":
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year (optional): ")
            year = int(year) if year.isdigit() else None
            book = Book(title, author, year)
            books.append(book)

            # Save immediately
            with open(DATA_FILE, "w") as f:
                json.dump([b.to_dict() for b in books], f, indent=2)

            print(f"Added and saved: {book}")

        elif choice == "2":
            if not books:
                print("No books yet.")
            else:
                print("\n--- Your Books ---")
                for i, book in enumerate(books, 1):
                    print(f"{i}. {book}")

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")
```

**Test:** Run `python book.py`. Add some books. Exit. Run again – you should see the loaded books.

Do the same for `member.py` (use `members.json`). After this, both files work independently and store data.

---

# Step 3: Building Manager Classes (CRUD Operations)

Now we will create **Manager** classes that handle all operations on a collection of `Book` or `Member` objects. These managers will contain methods like `add`, `list`, `find`, `update`, `delete`, and they will automatically save to JSON.

We will add **one or two methods at a time**, testing each thoroughly.

## 3.1 Create `BookManager` in `book_manager.py`

Create a new file `book_manager.py`. It will import the `Book` class from `book.py`. Write:

```python
import json
import os
from book import Book

class BookManager:
    def __init__(self, filename="books.json"):
        self.filename = filename
        self.books = []
        self._load()

    def _load(self):
        """Load books from JSON file."""
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                data = json.load(f)
            self.books = [Book.from_dict(item) for item in data]
        else:
            self.books = []

    def _save(self):
        """Save current books to JSON file."""
        with open(self.filename, "w") as f:
            json.dump([b.to_dict() for b in self.books], f, indent=2)
```

Now we will add methods one by one, testing after each addition.

### Method 1: `add_book`

Add this method to `BookManager`:

```python
    def add_book(self, book):
        self.books.append(book)
        self._save()
        print(f"Added: {book}")
```

Now create a test section at the bottom of `book_manager.py`:

```python
if __name__ == "__main__":
    manager = BookManager()
    print("Welcome to Book Manager")

    while True:
        print("\n1. Add a book")
        print("2. List all books")
        print("3. Exit")
        choice = input("Choose: ")

        if choice == "1":
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            year = int(year) if year.isdigit() else None
            book = Book(title, author, year)
            manager.add_book(book)

        elif choice == "2":
            if not manager.books:
                print("No books.")
            else:
                for i, b in enumerate(manager.books, 1):
                    print(f"{i}. {b}")

        elif choice == "3":
            break
```

Run `python book_manager.py`. Add some books – they are saved. Exit and restart – they persist.

### Method 2: `list_books` (we already have it, but we can make it nicer)

Replace the manual listing with a method:

```python
    def list_books(self):
        """Return a list of all books."""
        return self.books
```

Then in the test section you can do: `for b in manager.list_books(): print(b)`. Keep the test simple.

### Method 3: `find_book`

Add:

```python
    def find_book(self, title):
        """Find book by exact title (case‑insensitive)."""
        title_lower = title.lower()
        for book in self.books:
            if book.title.lower() == title_lower:
                return book
        return None
```

Test by adding an option:

```python
        elif choice == "3":
            title = input("Enter title to search: ")
            book = manager.find_book(title)
            if book:
                print(f"Found: {book}")
            else:
                print("Not found.")
```

Adjust menu numbering accordingly.

### Method 4: `update_book`

```python
    def update_book(self, old_title, new_title=None, new_author=None, new_year=None):
        book = self.find_book(old_title)
        if not book:
            print(f"Book '{old_title}' not found.")
            return False
        if new_title:
            book.title = new_title
        if new_author:
            book.author = new_author
        if new_year is not None:
            book.year = new_year
        self._save()
        print(f"Updated: {book}")
        return True
```

Add a test menu option that asks for the old title and the new details.

### Method 5: `delete_book`

```python
    def delete_book(self, title):
        book = self.find_book(title)
        if not book:
            print(f"Book '{title}' not found.")
            return False
        self.books.remove(book)
        self._save()
        print(f"Deleted: {book}")
        return True
```

Add a menu option to delete.

**Now `book_manager.py` is complete.** The students have learned: loading/saving JSON, CRUD operations, and using a manager class.

## 3.2 Create `MemberManager` (parallel)

Create `member_manager.py` with identical structure, using `Member` class.

```python
import json
import os
from member import Member

class MemberManager:
    def __init__(self, filename="members.json"):
        self.filename = filename
        self.members = []
        self._load()

    def _load(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                data = json.load(f)
            self.members = [Member.from_dict(item) for item in data]
        else:
            self.members = []

    def _save(self):
        with open(self.filename, "w") as f:
            json.dump([m.to_dict() for m in self.members], f, indent=2)

    def add_member(self, member):
        self.members.append(member)
        self._save()
        print(f"Added: {member}")

    def list_members(self):
        return self.members

    def find_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

    def update_member(self, member_id, new_name=None, new_email=None):
        member = self.find_member(member_id)
        if not member:
            print(f"Member '{member_id}' not found.")
            return False
        if new_name:
            member.name = new_name
        if new_email is not None:
            member.email = new_email
        self._save()
        print(f"Updated: {member}")
        return True

    def delete_member(self, member_id):
        member = self.find_member(member_id)
        if not member:
            print(f"Member '{member_id}' not found.")
            return False
        self.members.remove(member)
        self._save()
        print(f"Deleted: {member}")
        return True
```

Add a test block similar to `book_manager.py` but for members. Include searching by ID, updating, deleting. Test thoroughly.

---

# Step 4: Bringing It Together – The `Library` Class

Now we create `library.py` that imports both managers and provides a unified interface. It will also allow us to add borrowed books later (optional extension).

```python
from book_manager import BookManager
from member_manager import MemberManager

class Library:
    def __init__(self):
        self.book_manager = BookManager()
        self.member_manager = MemberManager()

    def add_book(self, title, author, year=None):
        from book import Book
        book = Book(title, author, year)
        self.book_manager.add_book(book)

    def list_books(self):
        return self.book_manager.list_books()

    def find_book(self, title):
        return self.book_manager.find_book(title)

    def update_book(self, old_title, new_title=None, new_author=None, new_year=None):
        self.book_manager.update_book(old_title, new_title, new_author, new_year)

    def delete_book(self, title):
        self.book_manager.delete_book(title)

    def add_member(self, name, member_id, email=None):
        from member import Member
        member = Member(name, member_id, email)
        self.member_manager.add_member(member)

    def list_members(self):
        return self.member_manager.list_members()

    def find_member(self, member_id):
        return self.member_manager.find_member(member_id)

    def update_member(self, member_id, new_name=None, new_email=None):
        self.member_manager.update_member(member_id, new_name, new_email)

    def delete_member(self, member_id):
        self.member_manager.delete_member(member_id)
```

Now we can create a `main.py` (or just test inside `library.py`'s `if __name__ == '__main__'`) that uses the `Library` class to demonstrate everything.

Example test for `library.py`:

```python
if __name__ == "__main__":
    lib = Library()

    while True:
        print("\n=== LIBRARY SYSTEM ===")
        print("1. Add book")
        print("2. List books")
        print("3. Update book")
        print("4. Delete book")
        print("5. Add member")
        print("6. List members")
        print("7. Update member")
        print("8. Delete member")
        print("9. Exit")
        choice = input("Choose: ")

        if choice == "1":
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            year = int(year) if year.isdigit() else None
            lib.add_book(title, author, year)
        elif choice == "2":
            for b in lib.list_books():
                print(b)
        elif choice == "3":
            old = input("Old title: ")
            new_title = input("New title (enter to skip): ") or None
            new_author = input("New author: ") or None
            year_str = input("New year: ")
            new_year = int(year_str) if year_str.isdigit() else None
            lib.update_book(old, new_title, new_author, new_year)
        elif choice == "4":
            title = input("Title to delete: ")
            lib.delete_book(title)
        elif choice == "5":
            name = input("Name: ")
            mid = input("Member ID: ")
            email = input("Email: ") or None
            lib.add_member(name, mid, email)
        elif choice == "6":
            for m in lib.list_members():
                print(m)
        elif choice == "7":
            mid = input("Member ID: ")
            new_name = input("New name: ") or None
            new_email = input("New email: ") or None
            lib.update_member(mid, new_name, new_email)
        elif choice == "8":
            mid = input("Member ID to delete: ")
            lib.delete_member(mid)
        elif choice == "9":
            break
```

Run `python library.py`. Everything works, and all data is saved to JSON files.

---

## 🎉 What You Have Learned

1. **Object‑Oriented Design** – Classes, methods, encapsulation.
2. **Testing with `if __name__ == '__main__'`** – Keeps your code modular.
3. **JSON persistence** – Saving Python objects to text files.
4. **Manager pattern** – Separate class for handling collections (CRUD).
5. **Composition** – Library class uses BookManager and MemberManager.
6. **Stepwise development** – Adding one small feature at a time and testing.

---

## 🔧 Suggested Extensions (Homework)

- Add a `borrow_book(member_id, book_title)` method to the `Library` class. You will need to track which book is borrowed by which member (add a `borrowed_by` field to `Book` and update both book.json and member's borrowed list).
- Add search by author or partial title.
- Add a simple command‑line interface with numbered commands (like we did in the final test).

---

## 📂 Final Project Structure

```
library_project/
├── book.py            # Book class + to_dict/from_dict
├── member.py          # Member class + to_dict/from_dict
├── book_manager.py    # BookManager class (CRUD, JSON)
├── member_manager.py  # MemberManager class (CRUD, JSON)
├── library.py         # Library class (ties both managers)
├── books.json         # automatically created
└── members.json       # automatically created
```

All code from this tutorial fits in those files. Students can run `library.py` for the complete system.

---

**Workshop Version**: 3.0 (True step‑by‑step for beginners)  
**Last Updated**: March 2026  
**Estimated Total Time**: 2–3 hours (including testing each step)