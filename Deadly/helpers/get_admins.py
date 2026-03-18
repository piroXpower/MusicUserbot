# Copyright © 2023-2024 by piroxpower@Github
# Optimized for 2026: Time-Based Cache Expiration

import time
from typing import Dict, List, Union

# Structure: {chat_id: {"admins": [ids], "expiry": timestamp}}
_admin_cache: Dict[int, dict] = {}

# Cache duration in seconds (30 minutes = 1800 seconds)
CACHE_TTL = 1800

def set(chat_id: int, admins_list: List[int]):
    """Sets the admin list for a chat with a 30-minute expiry timestamp."""
    _admin_cache[chat_id] = {
        "admins": admins_list,
        "expiry": time.time() + CACHE_TTL
    }

def get(chat_id: int) -> Union[List[int], bool]:
    """
    Returns the cached admin list if it exists and hasn't expired.
    Returns False if cache is missing or too old.
    """
    if chat_id in _admin_cache:
        data = _admin_cache[chat_id]
        # Check if the cache is still fresh
        if time.time() < data["expiry"]:
            return data["admins"]
        else:
            # Cache expired, remove it so it can be re-fetched
            _admin_cache.pop(chat_id)
            
    return False

def clear_cache():
    """Manually clear all cached admins (useful for global refreshes)."""
    _admin_cache.clear()
