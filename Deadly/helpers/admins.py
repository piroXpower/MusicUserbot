# Copyright © 2023-2024 by piroxpower@Github
# Optimized for 2026 Performance & Permission Handling

from typing import List
from pyrogram.types import Chat
from pyrogram.enums import ChatMembersFilter

# Assuming these are your custom caching helpers
from Deadly.helpers.get_admins import get as get_cache
from Deadly.helpers.get_admins import set as set_cache

async def get_administrators(chat: Chat) -> List[int]:
    """
    Fetches and caches the list of authorized administrators for a chat.
    Authorized = Users with 'Manage Video Chats' permissions.
    """
    # 1. Try to fetch from local cache first
    cached_admins = get_cache(chat.id)
    if cached_admins:
        return cached_admins

    # 2. If not cached, fetch from Telegram API
    administrators = []
    try:
        # Use the updated filter for 2026 Pyrogram/Telegram API
        async for admin in chat.get_members(filter=ChatMembersFilter.ADMINISTRATORS):
            # Check for specific music/video control permissions
            # In 2026, 'can_manage_video_chats' is the standard for Music Bots
            if admin.privileges and admin.privileges.can_manage_video_chats:
                if admin.user: # Ensure it's a real user and not a service
                    administrators.append(admin.user.id)
        
        # 3. Save to cache to prevent redundant API calls
        set_cache(chat.id, administrators)
        return administrators

    except Exception as e:
        print(f"Admin Fetch Error in {chat.id}: {e}")
        # Return empty list on failure to prevent bot crashing
        return []
        
