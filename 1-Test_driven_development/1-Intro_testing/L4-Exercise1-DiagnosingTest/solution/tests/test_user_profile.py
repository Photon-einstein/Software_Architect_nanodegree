import time
import pytest
from src.profile_service import get_user_avatar_url  # Assume this exists


# Helper function to wait for a condition to be true (DO NOT MODIFY)
def wait_for_condition(check_function, timeout=2, interval=0.1):
    start_time = time.time()
    while time.time() < start_time + timeout:
        if check_function():
            return True
        time.sleep(interval)
    # Run one last time for the final assertion failure if condition is still False
    return check_function()


# THE FLAKY TEST (Now Robust)
def test_user_avatar_url_is_fetched():
    user_id = "user_42"

    # 1. Initiate the slow background process
    get_user_avatar_url(user_id)

    # 2. Define a lambda function to check the expected condition repeatedly
    check = lambda: get_user_avatar_url(user_id) is not None

    # 3. Execute the polling helper. It returns True if the condition is met
    # within the timeout, or False if the timeout expires.
    result = wait_for_condition(check)

    # 4. Final assertion. This assertion will only fail if the service failed
    # to provide a URL even after 2 seconds.
    assert result is True
