import time
import pytest  # pyright: ignore[reportMissingImports]
from src.profile_service import get_user_avatar_url  # Assume this exists


# Helper function to wait for a condition to be true (DO NOT MODIFY)
def wait_for_condition(check_function, timeout=2, interval=0.1):
    start_time = time.time()
    while time.time() < start_time + timeout:
        if check_function():
            return True
        time.sleep(interval)
    return (
        check_function()
    )  # Run one last time for the final assertion failure if condition is still False


# THE FLAKY TEST
def test_user_avatar_url_is_fetched():
    user_id = "user_42"

    # Simulate a delayed network fetch
    # This call initiates a slow background process in the application
    # get_user_avatar_url(user_id)

    # ORIGINAL FLAWED ASSERTION (Sometimes fails if fetch is slow):
    # url = get_user_avatar_url(user_id)
    # assert url is not None

    # ------------------------------------------------------------------
    # YOUR TASK: Replace the two lines above with the robust polling logic.
    # The polling check_function should be a lambda that checks the expected condition.
    # ------------------------------------------------------------------

    # Define a lambda function to check the condition:
    check = lambda: get_user_avatar_url(user_id) is not None

    # Execute the polling helper:
    result = wait_for_condition(check)

    # Final assertion (this should only fail if the fetch failed after the timeout):
    assert result is True

    # ------------------------------------------------------------------
    # pass  # Remove this line after implementing the solution
