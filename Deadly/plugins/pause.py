# Copyright © 2023-2024 by piroxpower@Github
# Optimized for 2026: Cyber-Aura UI & Cached Auth

from pyrogram import Client, filters
from pyrogram.types import Message
from Deadly import HNDLR, Music, SUDOERS
from Deadly.helpers.decorators import authorized_users_only
from Deadly.helpers.queues import QUEUE

@Client.on_message(filters.command(["pause"], prefixes=f"{HNDLR}"))
@authorized_users_only
async def pause(client, m: Message):
    # Use the helper to delete the command message to keep the chat clean
    await m.delete()
    chat_id = m.chat.id
    
    # Check if there is actually music playing in the queue
    if chat_id in QUEUE:
        try:
            # Tell PyTgCalls to pause the current stream
            await Music.pause_stream(chat_id)
            
            # Send a styled "Player Paused" message
            await m.reply_text(
                "**⏸️ ᴘᴀᴜsᴇᴅ**\n"
                "└ sᴛʀᴇᴀᴍ ʜᴀs ʙᴇᴇɴ ʜᴀʟᴛᴇᴅ.\n"
                f"**💡 ᴜsᴇ** `{HNDLR}resume` **ᴛᴏ ᴄᴏɴᴛɪɴᴜᴇ.**"
            )
        except Exception as e:
            # Log error if the stream is already paused or not joined
            await m.reply_text(f"**❌ ᴇʀʀᴏʀ:**\n`{e}`")
    else:
        await m.reply_text("**❌ ɴᴏᴛʜɪɴɢ ɪs ᴄᴜʀʀᴇɴᴛʟʏ ᴘʟᴀʏɪɴɢ!**")

