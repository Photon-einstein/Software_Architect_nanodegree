import pytest
from src.user_service import (
    is_valid_username,
    calculate_login_cooldown,
    get_user_full_name,
)


def test_valid_username_boundary_5():
    """Test that a 5-character username is considered valid."""
    assert is_valid_username("user1") is True


def test_valid_username_too_short():
    """Test that a 4-character username is invalid."""
    assert is_valid_username("user") is False


def test_calculate_cooldown_boundary_3_attempts():
    """Test that 3 failed attempts result in 0 cooldown."""
    assert calculate_login_cooldown(3) == 0


def test_calculate_cooldown_trigger():
    """Test that 4 failed attempts result in 10 seconds cooldown."""
    assert calculate_login_cooldown(4) == 10


def test_get_user_full_name():
    """Test that names are capitalized correctly."""
    assert get_user_full_name("jane", "doe") == "Jane Doe"
