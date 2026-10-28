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


def test_library_can_register_member(library, member):
    library.register_member(member)
    assert library.get_member("M001") is member


def test_library_rejects_duplicate_member(library, member):
    library.register_member(member)
    with pytest.raises(ValueError, match="already registered"):
        library.register_member(Member("M001", "Bob"))


def test_borrow_book_gives_book_to_member_and_reduces_copies(library, book, member):
    library.add_book(book)
    library.register_member(member)
    library.borrow_book("M001", "1234567890")
    assert member.borrowed_books == ["1234567890"]
    assert book.available_copies == 1
