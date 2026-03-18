# Copyright © 2023-2024 by piroxpower@Github
# Optimized for 2026: Clean-Exit & Queue Wipe

from pyrogram import Client, filters
from pyrogram.types import Message
from Deadly import HNDLR, Music
from Deadly.helpers.decorators import authorized_users_only
from Deadly.helpers.queues import clear_queue

@Client.on_message(filters.command(["stop", "end", "leave"], prefixes=f"{HNDLR}"))
@authorized_users_only
async def stop_music(client, m: Message):
    chat_id = m.chat.id
    
    # 1. Clean up the chat by deleting the trigger command
    await m.delete()
    
    # 2. Safety Check: Is the bot actually in a call?
    # We use a try-except to prevent crashes if the bot was manually kicked
    try:
        # Stop the stream and leave the group call
        await Music.leave_group_call(chat_id)
    except Exception:
        # If already disconnected, we just ignore the error
        pass

    # 3. Wipe the Queue for this specific chat
    # This prevents the KeyError you saw earlier by removing the chat_id safely
    clear_queue(chat_id)

    # 4. Final Text Confirmation
    await m.reply_text(
        "⏹️ **sᴛʀᴇᴀᴍ ᴛᴇʀᴍɪɴᴀᴛᴇᴅ**\n"
        "━━━━━━━━━━━━━━━━━━━\n"
        "✅ **ǫᴜᴇᴜᴇ ᴄʟᴇᴀʀᴇᴅ**\n"
        "🌐 **sᴛᴀᴛᴜs:** `ɪᴅʟᴇ`\n"
        "━━━━━━━━━━━━━━━━━━━"
    )

# Alias for 'end' if you prefer that command name
@Client.on_message(filters.command(["cstop"], prefixes=f"{HNDLR}"))
@authorized_users_only
async def clear_and_stop(client, m: Message):
    """Force clears everything and leaves."""
    await stop_music(client, m)
