from library import Library
from book import Book
from member import Member
from colorama import init, Fore, Back, Style

# Initialize colorama (autoreset=True returns colors to default after each print)
init(autoreset=True)

def print_header(text: str):
    """Print a colored header."""
    print(Fore.CYAN + Style.BRIGHT + "=" * 50)
    print(Fore.YELLOW + Style.BRIGHT + text.center(50))
    print(Fore.CYAN + Style.BRIGHT + "=" * 50)

def print_success(msg: str):
    """Print a success message in green."""
    print(Fore.GREEN + f"✓ {msg}")

def print_error(msg: str):
    """Print an error message in red."""
    print(Fore.RED + f"✗ {msg}")

def print_info(msg: str):
    """Print an informational message in blue."""
    print(Fore.BLUE + f"ℹ {msg}")

def main():
    lib = Library()
    
    while True:
        print_header("LIBRARY MANAGEMENT SYSTEM")
        print(Fore.MAGENTA + Style.BRIGHT + "1." + Fore.GREEN + " List all books")
        print(Fore.MAGENTA + Style.BRIGHT + "2." + Fore.GREEN + " Add a book")
        print(Fore.MAGENTA + Style.BRIGHT + "3." + Fore.GREEN + " Update a book")
        print(Fore.MAGENTA + Style.BRIGHT + "4." + Fore.GREEN + " Delete a book")
        print(Fore.MAGENTA + Style.BRIGHT + "5." + Fore.GREEN + " List all members")
        print(Fore.MAGENTA + Style.BRIGHT + "6." + Fore.GREEN + " Add a member")
        print(Fore.MAGENTA + Style.BRIGHT + "7." + Fore.GREEN + " Update a member")
        print(Fore.MAGENTA + Style.BRIGHT + "8." + Fore.GREEN + " Delete a member")
        print(Fore.RED + Style.BRIGHT + "0." + Fore.RED + " Exit")
        
        choice = input(Fore.CYAN + "\nEnter your choice: " + Style.RESET_ALL).strip()
        
        if choice == "1":
            print_info("Listing all books...")
            lib.list_books()   # Assuming this method prints internally – could also be enhanced there
        
        elif choice == "2":
            title = input(Fore.YELLOW + "Title: " + Style.RESET_ALL).strip()
            author = input(Fore.YELLOW + "Author: " + Style.RESET_ALL).strip()
            year_str = input(Fore.YELLOW + "Year (optional, press Enter to skip): " + Style.RESET_ALL).strip()
            year = int(year_str) if year_str.isdigit() else None
            book = Book(title, author, year)
            lib.add_book(book)
            print_success(f"Book '{title}' added successfully.")
        
        elif choice == "3":
            old_title = input(Fore.YELLOW + "Enter current title of the book to update: " + Style.RESET_ALL).strip()
            new_title = input(Fore.YELLOW + "New title (Enter to keep): " + Style.RESET_ALL).strip() or None
            new_author = input(Fore.YELLOW + "New author (Enter to keep): " + Style.RESET_ALL).strip() or None
            year_str = input(Fore.YELLOW + "New year (Enter to keep): " + Style.RESET_ALL).strip()
            new_year = int(year_str) if year_str.isdigit() else None
            lib.update_book(old_title, new_title, new_author, new_year)
            print_success(f"Book '{old_title}' updated.")
        
        elif choice == "4":
            title = input(Fore.YELLOW + "Enter title of book to delete: " + Style.RESET_ALL).strip()
            lib.delete_book(title)
            print_success(f"Book '{title}' deleted (if it existed).")
        
        elif choice == "5":
            print_info("Listing all members...")
            lib.list_members()
        
        elif choice == "6":
            name = input(Fore.YELLOW + "Name: " + Style.RESET_ALL).strip()
            member_id = input(Fore.YELLOW + "Member ID (e.g., M001): " + Style.RESET_ALL).strip()
            email = input(Fore.YELLOW + "Email (optional): " + Style.RESET_ALL).strip() or None
            member = Member(name, member_id, email)
            lib.add_member(member)
            print_success(f"Member '{name}' (ID: {member_id}) added.")
        
        elif choice == "7":
            member_id = input(Fore.YELLOW + "Enter Member ID to update: " + Style.RESET_ALL).strip()
            new_name = input(Fore.YELLOW + "New name (Enter to keep): " + Style.RESET_ALL).strip() or None
            new_email = input(Fore.YELLOW + "New email (Enter to keep): " + Style.RESET_ALL).strip() or None
            lib.update_member(member_id, new_name, new_email)
            print_success(f"Member ID {member_id} updated.")
        
        elif choice == "8":
            member_id = input(Fore.YELLOW + "Enter Member ID to delete: " + Style.RESET_ALL).strip()
            lib.delete_member(member_id)
            print_success(f"Member ID {member_id} deleted (if it existed).")
        
        elif choice == "0":
            print_info("Exiting the system. Goodbye!")
            break
        
        else:
            print_error("Invalid choice. Please enter a number from 0 to 8.")

if __name__ == "__main__":
    main()