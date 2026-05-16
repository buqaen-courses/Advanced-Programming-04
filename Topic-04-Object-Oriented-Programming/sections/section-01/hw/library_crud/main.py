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