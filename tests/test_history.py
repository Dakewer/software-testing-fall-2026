from datetime import date

import pytest

from src.book import Book
from src.library import Library
from src.member import Member


@pytest.fixture
def library():
    lib = Library()
    lib.add_book(Book("1234567890", "Clean Code", "Robert Martin", copies=3))
    lib.add_book(Book("0987654321", "Refactoring", "Martin Fowler", copies=3))
    lib.register_member(Member("M001", "Alice"))
    lib.register_member(Member("M002", "Bob"))
    return lib


def test_borrow_is_recorded_in_member_history(library):
    library.borrow_book("M001", "1234567890", borrow_date=date(2026, 1, 1))
    event = library.get_history("M001")[0]
    assert (event.action, event.isbn, event.date) == ("borrow", "1234567890", date(2026, 1, 1))
