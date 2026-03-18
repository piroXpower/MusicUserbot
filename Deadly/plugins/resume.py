# Copyright © 2023-2024 by piroxpower@Github
# Optimized for 2026: Cyber-Aura UI & Cached Auth

from pyrogram import Client, filters
from pyrogram.types import Message
from Deadly import HNDLR, Music
from Deadly.helpers.decorators import authorized_users_only
from Deadly.helpers.queues import QUEUE

@Client.on_message(filters.command(["resume"], prefixes=f"{HNDLR}"))
@authorized_users_only
async def resume(client, m: Message):
    # Deletes the command to keep the group interface clean
    await m.delete()
    chat_id = m.chat.id
    
    # Check if there is an active session in the queue
    if chat_id in QUEUE:
        try:
            # Command PyTgCalls to resume the audio/video stream
            await Music.resume_stream(chat_id)
            
            # Send a styled "Resume" card matching the Aura theme
            await m.reply_text(
                "**▶️ ʀᴇsᴜᴍᴇᴅ**\n"
                "└ ʙᴀᴄᴋ ᴛᴏ ᴛʜᴇ ʙᴇᴀᴛ!\n"
                f"**💡 ᴜsᴇ** `{HNDLR}pause` **ᴛᴏ sᴛᴏᴘ ᴛᴇᴍᴘᴏʀᴀʀɪʟʏ.**"
            )
        except Exception as e:
            # Handle cases where the stream is already playing or disconnected
            await m.reply_text(f"**❌ ᴇʀʀᴏʀ:**\n`{e}`")
    else:
        await m.reply_text("**❌ ǫᴜᴇᴜᴇ ɪs ᴇᴍᴘᴛʏ, ɴᴏᴛʜɪɴɢ ᴛᴏ ʀᴇsᴜᴍᴇ!**")
