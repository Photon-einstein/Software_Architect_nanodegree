import time

# Mock implementation simulating a delayed external avatar fetch
_avatar_cache = {}


def get_user_avatar_url(user_id):
    # If already fetched, return immediately
    if user_id in _avatar_cache:
        return _avatar_cache[user_id]

    # Simulate slow fetch
    time.sleep(0.3)
    _avatar_cache[user_id] = f"https://example.com/avatars/{user_id}.png"
    return _avatar_cache[user_id]
