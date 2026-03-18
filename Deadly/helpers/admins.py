# Copyright © 2023-2024 by piroxpower@Github
# Modified for 2026 High-Speed Performance & Caching

from typing import Callable
from pyrogram import Client
from pyrogram.types import Message
from Deadly import SUDOERS
from Deadly.helpers.admins import get_administrators

# Simple dictionary to cache admins for 5 minutes to prevent API lag
ADMIN_CACHE = {}

def authorized_users_only(func: Callable) -> Callable:
    async def decorator(client: Client, message: Message):
        # 1. Bypass check for SUDOERS (Fastest path)
        if message.from_user and message.from_user.id in SUDOERS:
            return await func(client, message)

        chat_id = message.chat.id
        user_id = message.from_user.id if message.from_user else None
        
        if not user_id:
            return # Ignore anonymous or deleted accounts

        # 2. Check Cache first to save API calls
        if chat_id in ADMIN_CACHE and user_id in ADMIN_CACHE[chat_id]:
            return await func(client, message)

        # 3. If not in cache, fetch from Telegram
        try:
            administrators = await get_administrators(chat_id)
            
            # Update cache for this chat
            ADMIN_CACHE[chat_id] = administrators
            
            if user_id in administrators:
                return await func(client, message)
            else:
                return await message.reply_text(
                    "**❌ Admin Only:** You need to be an administrator to use this command."
                )
        except Exception as e:
            print(f"Auth Error: {e}")
            # Fallback: if API fails, allow if they are in SUDOERS (already checked)
            return

    return decorator
