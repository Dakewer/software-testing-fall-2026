import pytest

from src.book import Book
from src.library import Library
from src.member import Member


@pytest.fixture
def library():
    return Library()


@pytest.fixture
def book():
    return Book("1234567890", "Clean Code", "Robert Martin", copies=2)


@pytest.fixture
def member():
    return Member("M001", "Alice")


def test_library_can_add_book_to_catalog(library, book):
    library.add_book(book)
    assert library.get_book("1234567890") is book


def test_library_rejects_duplicate_isbn(library, book):
    library.add_book(book)
    with pytest.raises(ValueError, match="already in catalog"):
        library.add_book(Book("1234567890", "Other", "Someone"))
