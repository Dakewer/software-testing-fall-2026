from datetime import date

import pytest

from src.book import Book
from src.library import Library
from src.member import Member


def test_faculty_member_can_borrow_five_books():
    assert Member("F001", "Prof", category="faculty").max_borrow_limit == 5
