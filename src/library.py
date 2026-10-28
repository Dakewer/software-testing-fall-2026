from datetime import date, timedelta

LOAN_DAYS = 14


class Library:
    def __init__(self):
        self._books = {}
        self._members = {}
        self._loans = {}

    def add_book(self, book):
        if book.isbn in self._books:
            raise ValueError("Book already in catalog")
        self._books[book.isbn] = book

    def get_book(self, isbn):
        if isbn not in self._books:
            raise ValueError("Unknown book")
        return self._books[isbn]

    def register_member(self, member):
        if member.member_id in self._members:
            raise ValueError("Member already registered")
        self._members[member.member_id] = member

    def get_member(self, member_id):
        if member_id not in self._members:
            raise ValueError("Unknown member")
        return self._members[member_id]

    def borrow_book(self, member_id, isbn, borrow_date=None):
        member = self.get_member(member_id)
        book = self.get_book(isbn)
        if not book.is_available():
            raise ValueError("No copies available")
        member.add_borrowed_book(isbn)
        book.borrow()
        self._loans[(member_id, isbn)] = borrow_date or date.today()

    def return_book(self, member_id, isbn):
        member = self.get_member(member_id)
        book = self.get_book(isbn)
        member.return_book(isbn)
        book.return_copy()

    def search_by_title(self, title):
        return self._search("title", title)

    def search_by_author(self, author):
        return self._search("author", author)

    def get_available_books(self):
        return [book for book in self._books.values() if book.is_available()]

    def _search(self, field, query):
        if not query.strip():
            raise ValueError("Search query cannot be empty")
        needle = query.lower()
        return [b for b in self._books.values() if needle in getattr(b, field).lower()]

    def get_due_date(self, member_id, isbn):
        return self._loans[(member_id, isbn)] + timedelta(days=LOAN_DAYS)

    def calculate_late_fee(self, member_id, as_of):
        fee = 0
        for (loan_member, isbn), borrowed_on in self._loans.items():
            due = borrowed_on + timedelta(days=LOAN_DAYS)
            if loan_member == member_id and as_of > due:
                fee += (as_of - due).days
        return fee
