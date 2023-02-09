# © piroxpower

import os
import sys
from pyrogram import Client, filters
from pyrogram.types import Message
from Deadly import HNDLR


@Client.on_message(filters.command(["repo"], prefixes=f"{HNDLR}"))
async def repo(client, m: Message):
    await m.delete()
    REPO = f"""
<b>👋 Hello {m.from_user.mention}!
🗃️ Music Player UserBot 
🔰 Telegram UserBot To Play Songs In Telegram Voice Chat .
👩‍💻 Presented By  
• [𝘋𝘦𝘢𝘥𝘭𝘺𝘕𝘦𝘵𝘸𝘰𝘳𝘬](https://t.me/TheDeadlyBots)
📝 Condition
• Python 3.8+
• FFMPEG
• Nodejs v18+
[𝘙𝘌𝘗𝘖-𝘏𝘌𝘙𝘌](https://github.com/piroXpower/MusicUserbot)
📝 Required Variables 
• `API_ID` - Get From [my.telegram.org](https://my.telegram.org)
• `API_HASH` - Get From [my.telegram.org](https://my.telegram.org)
• `SESSION` - Session String Pyrogram.
• `OWNER_ID` - Telegram Account ID of OWNER
• `HNDLR` - Handler to run your userbot 
"""
    await m.reply(REPO, disable_web_page_preview=True)
