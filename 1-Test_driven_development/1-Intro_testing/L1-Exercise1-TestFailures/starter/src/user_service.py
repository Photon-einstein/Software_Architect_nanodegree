def is_valid_username(username: str) -> bool:
    """Checks if a username is between 5 and 15 characters long."""
    # A tiny logic bug lives here!
    return len(username) >= 5 and len(username) <= 15


def get_user_full_name(first_name: str, last_name: str) -> str:
    """Returns the user's full name, capitalized."""
    return f"{first_name.title()} {last_name.title()}"


def calculate_login_cooldown(failed_attempts: int) -> int:
    """Calculates cooldown time (in seconds) for too many failed login attempts."""
    # Cooldown should be 0 for <= 3 attempts.
    # It should be 10 for more than 3 attempts.
    if failed_attempts > 3:
        return 10
    return 0
