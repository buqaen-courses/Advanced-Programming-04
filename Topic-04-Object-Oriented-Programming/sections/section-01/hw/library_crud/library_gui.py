import tkinter as tk
from tkinter import ttk, messagebox
from library import Library
from book import Book
from member import Member

class LibraryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("800x600")
        self.lib = Library()

        # Create notebook (tabs)
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill='both', expand=True)

        # Book tab
        self.book_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.book_frame, text="Books")
        self.setup_book_tab()

        # Member tab
        self.member_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.member_frame, text="Members")
        self.setup_member_tab()

        # Refresh both views on startup
        self.refresh_book_list()
        self.refresh_member_list()

    # ------------------ Book Tab ------------------
    def setup_book_tab(self):
        # Left side: book list
        left_frame = ttk.Frame(self.book_frame)
        left_frame.pack(side='left', fill='both', expand=True, padx=5, pady=5)

        ttk.Label(left_frame, text="Book List", font=('Arial', 12, 'bold')).pack(pady=5)
        self.book_listbox = tk.Listbox(left_frame, height=20, width=40)
        self.book_listbox.pack(side='left', fill='both', expand=True)
        scrollbar = ttk.Scrollbar(left_frame, orient='vertical', command=self.book_listbox.yview)
        scrollbar.pack(side='right', fill='y')
        self.book_listbox.config(yscrollcommand=scrollbar.set)
        self.book_listbox.bind('<<ListboxSelect>>', self.on_book_select)

        # Right side: book form
        right_frame = ttk.LabelFrame(self.book_frame, text="Book Operations", padding=10)
        right_frame.pack(side='right', fill='both', expand=True, padx=5, pady=5)

        # Fields
        ttk.Label(right_frame, text="Title:").grid(row=0, column=0, sticky='e', pady=5)
        self.book_title_entry = ttk.Entry(right_frame, width=30)
        self.book_title_entry.grid(row=0, column=1, pady=5)

        ttk.Label(right_frame, text="Author:").grid(row=1, column=0, sticky='e', pady=5)
        self.book_author_entry = ttk.Entry(right_frame, width=30)
        self.book_author_entry.grid(row=1, column=1, pady=5)

        ttk.Label(right_frame, text="Year:").grid(row=2, column=0, sticky='e', pady=5)
        self.book_year_entry = ttk.Entry(right_frame, width=30)
        self.book_year_entry.grid(row=2, column=1, pady=5)

        # Buttons
        btn_frame = ttk.Frame(right_frame)
        btn_frame.grid(row=3, column=0, columnspan=2, pady=10)

        ttk.Button(btn_frame, text="Add Book", command=self.add_book).pack(side='left', padx=5)
        ttk.Button(btn_frame, text="Update Book", command=self.update_book).pack(side='left', padx=5)
        ttk.Button(btn_frame, text="Delete Book", command=self.delete_book).pack(side='left', padx=5)
        ttk.Button(btn_frame, text="Clear", command=self.clear_book_form).pack(side='left', padx=5)

        # Additional info
        self.book_status = ttk.Label(right_frame, text="", foreground="blue")
        self.book_status.grid(row=4, column=0, columnspan=2, pady=5)

    def refresh_book_list(self):
        self.book_listbox.delete(0, tk.END)
        for book in self.lib.books:   # Assuming Library has a list `books` or a method to get all
            self.book_listbox.insert(tk.END, f"{book.title} by {book.author} ({book.year or 'N/A'})")

    def on_book_select(self, event):
        selection = self.book_listbox.curselection()
        if not selection:
            return
        index = selection[0]
        book = self.lib.books[index]
        self.book_title_entry.delete(0, tk.END)
        self.book_title_entry.insert(0, book.title)
        self.book_author_entry.delete(0, tk.END)
        self.book_author_entry.insert(0, book.author)
        self.book_year_entry.delete(0, tk.END)
        self.book_year_entry.insert(0, str(book.year) if book.year else "")

    def add_book(self):
        title = self.book_title_entry.get().strip()
        author = self.book_author_entry.get().strip()
        year_str = self.book_year_entry.get().strip()
        year = int(year_str) if year_str.isdigit() else None
        if not title or not author:
            messagebox.showerror("Error", "Title and author are required.")
            return
        book = Book(title, author, year)
        self.lib.add_book(book)
        self.refresh_book_list()
        self.clear_book_form()
        self.book_status.config(text=f"Book '{title}' added.", foreground="green")
        self.root.after(2000, lambda: self.book_status.config(text=""))

    def update_book(self):
        selection = self.book_listbox.curselection()
        if not selection:
            messagebox.showerror("Error", "Select a book to update.")
            return
        old_title = self.lib.books[selection[0]].title
        new_title = self.book_title_entry.get().strip() or None
        new_author = self.book_author_entry.get().strip() or None
        year_str = self.book_year_entry.get().strip()
        new_year = int(year_str) if year_str.isdigit() else None
        self.lib.update_book(old_title, new_title, new_author, new_year)
        self.refresh_book_list()
        self.clear_book_form()
        self.book_status.config(text=f"Book '{old_title}' updated.", foreground="green")
        self.root.after(2000, lambda: self.book_status.config(text=""))

    def delete_book(self):
        selection = self.book_listbox.curselection()
        if not selection:
            messagebox.showerror("Error", "Select a book to delete.")
            return
        title = self.lib.books[selection[0]].title
        if messagebox.askyesno("Confirm Delete", f"Delete '{title}'?"):
            self.lib.delete_book(title)
            self.refresh_book_list()
            self.clear_book_form()
            self.book_status.config(text=f"Book '{title}' deleted.", foreground="red")
            self.root.after(2000, lambda: self.book_status.config(text=""))

    def clear_book_form(self):
        self.book_title_entry.delete(0, tk.END)
        self.book_author_entry.delete(0, tk.END)
        self.book_year_entry.delete(0, tk.END)
        self.book_listbox.selection_clear(0, tk.END)

    # ------------------ Member Tab ------------------
    def setup_member_tab(self):
        left_frame = ttk.Frame(self.member_frame)
        left_frame.pack(side='left', fill='both', expand=True, padx=5, pady=5)

        ttk.Label(left_frame, text="Member List", font=('Arial', 12, 'bold')).pack(pady=5)
        self.member_listbox = tk.Listbox(left_frame, height=20, width=40)
        self.member_listbox.pack(side='left', fill='both', expand=True)
        scrollbar = ttk.Scrollbar(left_frame, orient='vertical', command=self.member_listbox.yview)
        scrollbar.pack(side='right', fill='y')
        self.member_listbox.config(yscrollcommand=scrollbar.set)
        self.member_listbox.bind('<<ListboxSelect>>', self.on_member_select)

        right_frame = ttk.LabelFrame(self.member_frame, text="Member Operations", padding=10)
        right_frame.pack(side='right', fill='both', expand=True, padx=5, pady=5)

        ttk.Label(right_frame, text="Name:").grid(row=0, column=0, sticky='e', pady=5)
        self.member_name_entry = ttk.Entry(right_frame, width=30)
        self.member_name_entry.grid(row=0, column=1, pady=5)

        ttk.Label(right_frame, text="Member ID:").grid(row=1, column=0, sticky='e', pady=5)
        self.member_id_entry = ttk.Entry(right_frame, width=30)
        self.member_id_entry.grid(row=1, column=1, pady=5)

        ttk.Label(right_frame, text="Email:").grid(row=2, column=0, sticky='e', pady=5)
        self.member_email_entry = ttk.Entry(right_frame, width=30)
        self.member_email_entry.grid(row=2, column=1, pady=5)

        btn_frame = ttk.Frame(right_frame)
        btn_frame.grid(row=3, column=0, columnspan=2, pady=10)

        ttk.Button(btn_frame, text="Add Member", command=self.add_member).pack(side='left', padx=5)
        ttk.Button(btn_frame, text="Update Member", command=self.update_member).pack(side='left', padx=5)
        ttk.Button(btn_frame, text="Delete Member", command=self.delete_member).pack(side='left', padx=5)
        ttk.Button(btn_frame, text="Clear", command=self.clear_member_form).pack(side='left', padx=5)

        self.member_status = ttk.Label(right_frame, text="", foreground="blue")
        self.member_status.grid(row=4, column=0, columnspan=2, pady=5)

    def refresh_member_list(self):
        self.member_listbox.delete(0, tk.END)
        for member in self.lib.members:   # Assuming Library has a list `members`
            self.member_listbox.insert(tk.END, f"{member.name} (ID: {member.member_id})")

    def on_member_select(self, event):
        selection = self.member_listbox.curselection()
        if not selection:
            return
        member = self.lib.members[selection[0]]
        self.member_name_entry.delete(0, tk.END)
        self.member_name_entry.insert(0, member.name)
        self.member_id_entry.delete(0, tk.END)
        self.member_id_entry.insert(0, member.member_id)
        self.member_email_entry.delete(0, tk.END)
        self.member_email_entry.insert(0, member.email if member.email else "")

    def add_member(self):
        name = self.member_name_entry.get().strip()
        member_id = self.member_id_entry.get().strip()
        email = self.member_email_entry.get().strip() or None
        if not name or not member_id:
            messagebox.showerror("Error", "Name and Member ID are required.")
            return
        # Check for duplicate ID
        for m in self.lib.members:
            if m.member_id == member_id:
                messagebox.showerror("Error", "Member ID already exists.")
                return
        member = Member(name, member_id, email)
        self.lib.add_member(member)
        self.refresh_member_list()
        self.clear_member_form()
        self.member_status.config(text=f"Member '{name}' added.", foreground="green")
        self.root.after(2000, lambda: self.member_status.config(text=""))

    def update_member(self):
        selection = self.member_listbox.curselection()
        if not selection:
            messagebox.showerror("Error", "Select a member to update.")
            return
        old_id = self.lib.members[selection[0]].member_id
        new_name = self.member_name_entry.get().strip() or None
        new_email = self.member_email_entry.get().strip() or None
        self.lib.update_member(old_id, new_name, new_email)
        self.refresh_member_list()
        self.clear_member_form()
        self.member_status.config(text=f"Member ID {old_id} updated.", foreground="green")
        self.root.after(2000, lambda: self.member_status.config(text=""))

    def delete_member(self):
        selection = self.member_listbox.curselection()
        if not selection:
            messagebox.showerror("Error", "Select a member to delete.")
            return
        member = self.lib.members[selection[0]]
        if messagebox.askyesno("Confirm Delete", f"Delete member '{member.name}' (ID: {member.member_id})?"):
            self.lib.delete_member(member.member_id)
            self.refresh_member_list()
            self.clear_member_form()
            self.member_status.config(text=f"Member '{member.name}' deleted.", foreground="red")
            self.root.after(2000, lambda: self.member_status.config(text=""))

    def clear_member_form(self):
        self.member_name_entry.delete(0, tk.END)
        self.member_id_entry.delete(0, tk.END)
        self.member_email_entry.delete(0, tk.END)
        self.member_listbox.selection_clear(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryApp(root)
    root.mainloop()