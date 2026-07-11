from unittest.mock import patch
from src.auth_service import AuthService


@patch("src.auth_service.NotificationService")
def test_password_reset_calls_notification_service(MockNotificationService):
    """
    Verifies that the AuthService correctly interacts with the external
    NotificationService when a password reset is triggered.
    """
    # Arrange
    test_email = "test@user.com"
    auth_service = AuthService()

    # The mock object passed in by the patch decorator is named
    # MockNotificationService here. We need to access the mock of the
    # *specific method* we care about: .send_email().
    # Hint: Since AuthService uses NotificationService(), you'll need to
    # access the mock instance first: MockNotificationService.return_value.

    # Act
    auth_service.send_password_reset_email(test_email)

    # Assert 1: Check that the primary method was called exactly once
    # YOUR ASSERTION HERE

    # Assert 2: Check that the method was called with the correct arguments
    # YOUR ASSERTION HERE
