def is_valid_username(username: str) -> bool:
    """Checks if a username is between 5 and 15 characters long."""
    # FIXED: Changed > 5 to >= 5 to include a minimum length of 5.
    return len(username) >= 5 and len(username) < 15


def get_user_full_name(first_name: str, last_name: str) -> str:
    """Returns the user's full name, capitalized."""
    return f"{first_name.title()} {last_name.title()}"


def calculate_login_cooldown(failed_attempts: int) -> int:
    """Calculates cooldown time (in seconds) for too many failed login attempts."""
    # FIXED: Changed >= 3 to > 3 to apply the cooldown starting at 4 attempts.
    if failed_attempts > 3:
        return 10
    return 0
