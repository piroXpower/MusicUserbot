# Β© piroxpower

import os
import sys
from pyrogram import Client, filters
from pyrogram.types import Message
from Deadly import HNDLR


@Client.on_message(filters.command(["repo"], prefixes=f"{HNDLR}"))
async def repo(client, m: Message):
    await m.delete()
    REPO = f"""
<b>π Hello {m.from_user.mention}!
ποΈ Music Player UserBot 
π° Telegram UserBot To Play Songs In Telegram Voice Chat .
π©βπ» Presented By  
β’ [ππ¦π’π₯π­πΊππ¦π΅πΈπ°π³π¬](https://t.me/TheDeadlyBots)
π Condition
β’ Python 3.8+
β’ FFMPEG
β’ Nodejs v18+
[ππππ-ππππ](https://github.com/piroXpower/MusicUserbot)
π Required Variables 
β’ `API_ID` - Get From [my.telegram.org](https://my.telegram.org)
β’ `API_HASH` - Get From [my.telegram.org](https://my.telegram.org)
β’ `SESSION` - Session String Pyrogram.
β’ `OWNER_ID` - Telegram Account ID of OWNER
β’ `HNDLR` - Handler to run your userbot 
"""
    await m.reply(REPO, disable_web_page_preview=True)
