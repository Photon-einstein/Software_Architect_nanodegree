import pytest  # pyright: ignore[reportMissingImports]
from src.auth import is_valid_email, hash_password, verify_password

# --- FAST UNIT TESTS ---


def test_is_valid_email_rejects_missing_at_sign():
    """Checks for a basic email formatting rule."""
    assert is_valid_email("test.com") is False


def test_is_valid_email_accepts_standard_format():
    """Checks for a standard, correct email format."""
    assert is_valid_email("user@domain.com") is True


# --- SLOW CRYPTO TESTS (Marked) ---


@pytest.mark.crypto
def test_password_hashing_benchmark():
    """A test that measures the time taken to hash a password."""
    assert hash_password("strongpassword") is not None


@pytest.mark.crypto
def test_password_verification_stress_test():
    """A stress test verifying slow verification logic."""
    assert verify_password("correct", "hashed_value") is True
