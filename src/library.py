class Library:
    def __init__(self):
        self._books = {}
        self._members = {}

    def add_book(self, book):
        if book.isbn in self._books:
            raise ValueError("Book already in catalog")
        self._books[book.isbn] = book

    def get_book(self, isbn):
        return self._books[isbn]

    def register_member(self, member):
        if member.member_id in self._members:
            raise ValueError("Member already registered")
        self._members[member.member_id] = member

    def get_member(self, member_id):
        return self._members[member_id]

    def borrow_book(self, member_id, isbn):
        if member_id not in self._members:
            raise ValueError("Unknown member")
        if isbn not in self._books:
            raise ValueError("Unknown book")
        member = self._members[member_id]
        book = self._books[isbn]
        if not book.is_available():
            raise ValueError("No copies available")
        member.add_borrowed_book(isbn)
        book.borrow()

    def return_book(self, member_id, isbn):
        if member_id not in self._members:
            raise ValueError("Unknown member")
        if isbn not in self._books:
            raise ValueError("Unknown book")
        member = self._members[member_id]
        book = self._books[isbn]
        member.return_book(isbn)
        book.return_copy()
