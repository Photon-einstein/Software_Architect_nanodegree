class NotificationService:
    def send_email(self, recipient: str, subject: str, body: str) -> bool:
        # Simulates a slow external process
        print(f"--- Firing email to {recipient} ---")
        return True
