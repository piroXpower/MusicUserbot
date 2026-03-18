# Copyright © 2023-2024 by piroxpower@Github
# Optimized for 2026 Performance & High-Speed Caching

from typing import Callable
from pyrogram import Client
from pyrogram.types import Message
from Deadly import SUDOERS
from Deadly.helpers.admins import get_administrators

# Cache to store admin IDs per chat to prevent API flooding
ADMIN_CACHE = {}

def authorized_users_only(func: Callable) -> Callable:
    async def decorator(client: Client, message: Message):
        # 1. Immediate bypass for SUDOERS (Fastest path)
        if message.from_user and message.from_user.id in SUDOERS:
            return await func(client, message)

        chat_id = message.chat.id
        user_id = message.from_user.id if message.from_user else None
        
        if not user_id:
            return # Ignore system messages or anonymous users

        # 2. Check Local Cache first
        if chat_id in ADMIN_CACHE and user_id in ADMIN_CACHE[chat_id]:
            return await func(client, message)

        # 3. If not cached, fetch from Telegram and update cache
        try:
            administrators = await get_administrators(chat_id)
            ADMIN_CACHE[chat_id] = administrators # Update cache for this group
            
            if user_id in administrators:
                return await func(client, message)
            else:
                return await message.reply_text(
                    "**❌ Admin Only:** You must be an administrator to perform this action."
                )
        except Exception as e:
            print(f"Authorization Error: {e}")
            return # Fail-safe: don't execute the command if auth fails

    return decorator

