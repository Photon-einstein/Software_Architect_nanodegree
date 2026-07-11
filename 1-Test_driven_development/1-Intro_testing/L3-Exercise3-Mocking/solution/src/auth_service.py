from src.notification_service import NotificationService


class AuthService:
    def send_password_reset_email(self, user_email: str) -> bool:
        subject = "Password Reset Request"
        body = f"Click here to reset your password for {user_email}."

        # Instantiates the service and calls the method
        return NotificationService().send_email(user_email, subject, body)
