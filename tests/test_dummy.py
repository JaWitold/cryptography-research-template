"""Dummy tests."""

from src.main import add


def test_add() -> None:
    """Test the add function."""
    assert add(1, 2) == 3
