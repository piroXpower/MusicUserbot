# Copyright © 2023-2024 by piroxpower@Github
# Optimized for 2026: Direct AWS Network Audit

import speedtest
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from Deadly import HNDLR, OWNER_ID

def run_speedtest():
    """Executes the blocking speedtest logic."""
    test = speedtest.Speedtest()
    test.get_best_server()
    test.download()
    test.upload()
    return test.results.dict()

@Client.on_message(filters.command(["speedcheck", "speed"], prefixes=f"{HNDLR}"))
async def speedtest_function(client, message: Message):
    # SECURITY: Restrict to Owner to prevent CPU spikes during music playback
    if message.from_user.id != OWNER_ID:
        return
        
    status = await message.reply_text("⚡ **ᴀᴜʀᴀ-ɴᴇᴛᴡᴏʀᴋ ᴀᴜᴅɪᴛ ɪɴ ᴘʀᴏɢʀᴇss...**")
    
    try:
        # Move blocking speedtest to a background thread to keep audio smooth
        loop = asyncio.get_event_loop()
        result = await loop.run_in_executor(None, run_speedtest)
        
        # Convert bits to Megabytes per second
        download = result['download'] / 1024 / 1024
        upload = result['upload'] / 1024 / 1024
        ping = result['ping']
        isp = result['client']['isp']
        server_name = result['server']['name']
        country = result['client']['country']
        
        # Comprehensive Data Report
        report = (
            "✨ **ᴀᴜʀᴀ-sᴛʀᴇᴀᴍ ɴᴇᴛᴡᴏʀᴋ ʀᴇᴘᴏʀᴛ**\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━\n"
            f"📥 **ᴅᴏᴡɴʟᴏᴀᴅ:** `{download:.2f} ᴍʙᴘs`\n"
            f"📤 **ᴜᴘʟᴏᴀᴅ:** `{upload:.2f} ᴍʙᴘs`\n"
            f"⏳ **ᴘɪɴɢ:** `{ping} ᴍs`\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━\n"
            f"🌐 **ɪsᴘ:** `{isp}`\n"
            f"📍 **ʟᴏᴄᴀᴛɪᴏɴ:** `{country}`\n"
            f"🖥️ **sᴇʀᴠᴇʀ:** `{server_name}`\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━\n"
            "✅ **ᴀᴜᴅɪᴛ ᴄᴏᴍᴘʟᴇᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ.**"
        )
        
        await status.edit_text(report)
        
    except Exception as e:
        await status.edit_text(f"**❌ ᴀᴜᴅɪᴛ ғᴀɪʟᴇᴅ:**\n`{e}`")
