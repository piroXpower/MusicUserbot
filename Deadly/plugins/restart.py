# Copyright © 2023-2024 by piroxpower@Github
# Optimized for 2026: Safe Audio Engine Shutdown

import os
import sys
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from Deadly import HNDLR, OWNER_ID, Music, PLAYER

@Client.on_message(filters.user(OWNER_ID) & filters.command(["restart", "reboot"], prefixes=f"{HNDLR}"))
async def restart(client, m: Message):    
    # 1. Visual Countdown
    reply = await m.reply_text("✨ **ᴀᴜʀᴀ-sᴛʀᴇᴀᴍ ʀᴇʙᴏᴏᴛɪɴɢ...**")
    
    for i in range(3, 0, -1):
        await asyncio.sleep(1)
        await reply.edit_text(f"🔄 **ʀᴇsᴛᴀʀᴛɪɴɢ ɪɴ {i} sᴇᴄᴏɴᴅs...**")
    
    await reply.edit_text("✅ **ᴅᴇᴀᴅʟʏ ᴜsᴇʀʙᴏᴛ ʀᴇsᴛᴀʀᴛᴇᴅ!**\n`ᴄʜᴇᴄᴋ ʟᴏɢɢᴇʀ ғᴏʀ sᴛᴀᴛᴜs.`")

    # 2. CRITICAL: Graceful Shutdown
    # We stop the audio engine and the client before the OS takes over.
    # This prevents "Ghost Sessions" in the Voice Chat.
    try:
        await Music.stop()
        await PLAYER.stop()
    except:
        pass

    # 3. OS Execution
    # This replaces the current process with a fresh one
    os.execl(sys.executable, sys.executable, *sys.argv)
    sys.exit()

