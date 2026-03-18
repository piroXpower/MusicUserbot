# Copyright © 2023-2024 by piroxpower@Github
# Optimized for 2026: Cyber-Aura Cleanup & Safe Shutdown

import os
from pyrogram import Client, filters
from pyrogram.types import Message
from Deadly import HNDLR, Music
from Deadly.helpers.decorators import authorized_users_only
from Deadly.helpers.queues import QUEUE, clear_queue

@Client.on_message(filters.command(["end", "stop", "cstop"], prefixes=f"{HNDLR}"))
@authorized_users_only
async def stop(client, m: Message):
    # Deletes the command to keep the group interface clean
    await m.delete()
    chat_id = m.chat.id
    
    if chat_id in QUEUE:
        try:
            # 1. Leave the Voice Chat
            await Music.leave_group_call(chat_id)
            
            # 2. Wipe the Playlist from Memory
            clear_queue(chat_id)
            
            # 3. DISK CLEANUP (Crucial for AWS)
            # This removes the generated thumbnails so they don't waste space
            temp_files = ["final_aura_thumb.png", "raw_thumb.png", "temp_raw.png"]
            for file in temp_files:
                if os.path.exists(file):
                    try:
                        os.remove(file)
                    except:
                        pass
            
            # 4. Success Message in Aura Style
            await m.reply_text(
                "**⏹️ sᴛʀᴇᴀᴍ ᴇɴᴅᴇᴅ**\n"
                "└ ǫᴜᴇᴜᴇ ᴄʟᴇᴀʀᴇᴅ & ᴄᴀᴄʜᴇ ᴡɪᴘᴇᴅ.\n"
                "**💡 ᴛʜᴀɴᴋs ғᴏʀ ᴜsɪɴɢ ᴅᴇᴀᴅʟʏ ᴍᴜsɪᴄ!**"
            )
            
        except Exception as e:
            await m.reply_text(f"**❌ ᴇʀʀᴏʀ:**\n`{e}`")
    else:
        # Check for ghost sessions (if queue is empty but bot is still in VC)
        try:
            await Music.leave_group_call(chat_id)
            await m.reply_text("**⏹️ ғᴏʀᴄᴇ sᴛᴏᴘᴘᴇᴅ ɢʜᴏsᴛ sᴇssɪᴏɴ.**")
        except:
            await m.reply_text("**❌ ɴᴏᴛʜɪɴɢ ɪs ᴄᴜʀʀᴇɴᴛʟʏ ᴘʟᴀʏɪɴɢ!**")
