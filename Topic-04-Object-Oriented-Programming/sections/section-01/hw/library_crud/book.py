class Book:
    def __init__(self, title, author, year=None):
        self.title = title
        self.author = author
        self.year = year   # optional publication year

    def __repr__(self):
        year_str = f" ({self.year})" if self.year else ""
        return f"'{self.title}' by {self.author}{year_str}"+ "\n" +"-"*50
    
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



if __name__ == "__main__":
    b1 = Book("1984", "George Orwell", 1949)
    print(b1)
    print(b1.to_dict())
    b2 = Book.from_dict(
        {
             "title": "Blazor",
            "author": "Somerset",
            "year": 1996
        }
    )
    print(b2)