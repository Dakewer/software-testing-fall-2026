import pytest

from src.member import Member


def test_member_can_be_created():
    member = Member("M001", "Alice")
    assert member.name == "Alice"
