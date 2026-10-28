import pytest

from src.member import Member


def test_member_can_be_created():
    member = Member("M001", "Alice")
    assert member.name == "Alice"


def test_member_has_default_borrow_limit_of_three():
    member = Member("M001", "Alice")
    assert member.max_borrow_limit == 3


def test_member_starts_with_no_borrowed_books():
    member = Member("M001", "Alice")
    assert member.borrowed_books == []


def test_member_can_borrow_when_below_limit():
    member = Member("M001", "Alice")
    assert member.can_borrow() is True
