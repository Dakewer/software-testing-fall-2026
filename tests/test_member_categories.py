from datetime import date

import pytest

from src.book import Book
from src.library import Library
from src.member import Member


def test_faculty_member_can_borrow_five_books():
    assert Member("F001", "Prof", category="faculty").max_borrow_limit == 5


def test_public_member_can_borrow_two_books():
    assert Member("P001", "Visitor", category="public").max_borrow_limit == 2


def test_unknown_category_is_rejected():
    with pytest.raises(ValueError, match="Unknown category"):
        Member("X001", "Nobody", category="alien")
