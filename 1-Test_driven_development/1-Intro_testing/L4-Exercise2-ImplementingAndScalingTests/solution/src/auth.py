import time


def is_valid_email(email):
    return "@" in email


def hash_password(password):
    # Simulate a slow cryptographic operation
    time.sleep(0.1)
    return f"hashed_{password}"


def verify_password(plain, hashed):
    # Simulate a slow verification process
    time.sleep(0.1)
    return True
