import pytest  # pyright: ignore[reportMissingImports]
from src.auth import is_valid_email, hash_password, verify_password

# FAST UNIT TEST (In-memory logic check)


def test_is_valid_email_rejects_missing_at_sign():
    """Checks for a basic email formatting rule."""
    assert is_valid_email("test.com") is False


# FAST UNIT TEST (In-memory logic check)


def test_is_valid_email_accepts_standard_format():
    """Checks for a standard, correct email format."""

    assert is_valid_email("user@domain.com") is True


# SLOW CRYPTO TEST (Requires computational time)


@pytest.mark.crypto
def test_password_hashing_benchmark():
    """A test that measures the time taken to hash a password, which is intentionally slow."""
    # (Actual hashing code here)
    assert hash_password("strongpassword") is not None


# SLOW CRYPTO TEST (Requires computational time)


@pytest.mark.crypto
def test_password_verification_stress_test():
    """A stress test verifying slow verification logic across many attempts."""
    # (Actual verification code here)
    assert verify_password("correct", "hashed_value") is True


# The purpose of applying the crypto custom marker is to make it more intentional when run or not run
# most demanding tests during the different phases of development of an application.
