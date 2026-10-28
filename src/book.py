class Book:
    def __init__(self, isbn, title, author, copies=1):
        if len(isbn) not in (10, 13) or not isbn.isdigit():
            raise ValueError("ISBN must be 10 or 13 digits")
        if not title or not title.strip():
            raise ValueError("Title is required")
        if copies < 0:
            raise ValueError("Copies cannot be negative")
        self.isbn = isbn
        self.title = title
        self.author = author
        self.total_copies = copies
        self.available_copies = copies

    def is_available(self):
        return self.available_copies > 0
