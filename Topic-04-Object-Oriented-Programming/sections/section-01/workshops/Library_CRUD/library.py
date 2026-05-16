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
        if not new_title and not new_author and not new_year :
            print(f"Please provide the required data(title or author or year)")
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
        if not new_name and not new_email : 
            print(f"please provide new member data(name or email)")
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