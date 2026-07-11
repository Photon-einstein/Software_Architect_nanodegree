from unittest.mock import patch
from src.auth_service import AuthService


# Patch where the class is IMPORTED/USED, not where it is defined
@patch("src.auth_service.NotificationService")
def test_password_reset_calls_notification_service(MockNotificationService):
    """Verifies interactions without sending real emails."""
    # Arrange
    test_email = "test@user.com"
    auth_service = AuthService()

    # Access the mock of the INSTANCE (since the code calls NotificationService())
    mock_instance = MockNotificationService.return_value

    # Act
    auth_service.send_password_reset_email(test_email)

    # Assert 1: Verify the method was called exactly once
    mock_instance.send_email.assert_called_once()

    # Assert 2: Verify the exact arguments passed to the method
    mock_instance.send_email.assert_called_with(
        test_email,
        "Password Reset Request",
        f"Click here to reset your password for {test_email}.",
    )
