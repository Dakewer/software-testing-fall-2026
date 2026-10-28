from datetime import date, timedelta

import pytest

from src.book import Book
from src.library import Library
from src.member import Member

BORROW_DATE = date(2026, 1, 1)


@pytest.fixture
def library():
    lib = Library()
    lib.add_book(Book("1234567890", "Clean Code", "Robert Martin", copies=2))
    lib.add_book(Book("0987654321", "Refactoring", "Martin Fowler", copies=2))
    lib.register_member(Member("M001", "Alice"))
    return lib


def test_due_date_is_14_days_after_borrow(library):
    library.borrow_book("M001", "1234567890", borrow_date=BORROW_DATE)
    assert library.get_due_date("M001", "1234567890") == date(2026, 1, 15)


def test_borrow_date_defaults_to_today(library):
    library.borrow_book("M001", "1234567890")
    assert library.get_due_date("M001", "1234567890") == date.today() + timedelta(days=14)
