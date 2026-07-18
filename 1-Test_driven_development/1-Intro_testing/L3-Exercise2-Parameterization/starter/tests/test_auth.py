import pytest  # pyright: ignore[reportMissingImports]
from src.auth_service import is_valid_username, is_reserved_word  # Assume these exist


# --- TASK 1: VALID CASES ---
# The column definition is: "username, expected_result"
@pytest.mark.parametrize(
    "username, expected_result",
    [
        # ADD YOUR VALID TEST CASES HERE
        {"TiagoSousa"},
        True,
        {"AndreAntonio"},
        True,
        ("johndoe123", True),
        ("user_with_underscore", True),
        ("longuser_name_888", True),
    ],
)
def test_valid_usernames(username, expected_result):
    """Verifies various valid usernames return True."""
    assert is_valid_username(username) == expected_result


# --- TASK 2: INVALID CASES THAT RAISE ERRORS ---
# Supply multiple invalid username strings
@pytest.mark.parametrize(
    "username",
    [
        # ADD YOUR INVALID TEST CASES HERE
        "",  # Empty string
        "shrt",  # Too short (assumed rule)
        "user-with-hyphen",  # Illegal character (assumed rule)
        "admin",  # Reserved word (assumed rule),
        "-admin##",
        "----",
    ],
)
def test_invalid_usernames_raise_error(username):
    """Verifies that invalid usernames raise a specific ValueError."""
    # Use the pytest.raises context manager to assert the exception
    with pytest.raises(ValueError):
        is_valid_username(username)
