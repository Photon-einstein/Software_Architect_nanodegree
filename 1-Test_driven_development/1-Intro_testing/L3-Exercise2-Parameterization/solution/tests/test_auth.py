import pytest
from src.auth_service import is_valid_username  # Assumed existence based on exercise


# --- TASK 1: VALID CASES (Green Path) ---
@pytest.mark.parametrize(
    "username, expected_result",
    [
        # 1. Standard alphanumeric user
        ("johndoe123", True),
        # 2. User with an allowed special character (underscore)
        ("user_with_underscore", True),
        # 3. Longer, more complex valid username
        ("longuser_name_888", True),
    ],
)
def test_valid_usernames(username, expected_result):
    """Verifies various valid usernames return True."""
    assert is_valid_username(username) == expected_result


# --- TASK 2: INVALID CASES (Red Path) ---
@pytest.mark.parametrize(
    "username",
    [
        # 1. Boundary Condition: Empty string
        "",
        # 2. Boundary Condition: Too short
        "shrt",
        # 3. Invalid Character Rule
        "user-with-hyphen",
        # 4. Reserved Word Rule
        "admin",
    ],
)
def test_invalid_usernames_raise_error(username):
    """Verifies that invalid usernames raise a specific ValueError."""
    # Context manager asserts that the code block raises ValueError
    with pytest.raises(ValueError):
        is_valid_username(username)
