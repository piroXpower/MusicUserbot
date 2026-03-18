# Copyright © 2023-2024 by piroxpower@Github
# Optimized for 2026: Cyber-Aura Help Menu

from pyrogram import Client, filters
from pyrogram.types import Message
from Deadly import HNDLR

@Client.on_message(filters.command(["help", "commands"], prefixes=f"{HNDLR}"))
async def help_menu(client, m: Message):
    # Keep the group clean by deleting the help trigger
    await m.delete()
    
    # Styled Help Menu matching the Cyber-Aura theme
    HELP_TEXT = f"""
✨ **ᴅᴇᴀᴅʟʏ ᴍᴜsɪᴄ ᴜsᴇʀʙᴏᴛ** ✨
━━━━━━━━━━━━━━━━━━━━━━
👋 **ʜᴇʟʟᴏ {m.from_user.first_name}!**
*ʜᴇʀᴇ ɪs ʏᴏᴜʀ ᴀᴜʀᴀ-sᴛʀᴇᴀᴍ ɢᴜɪᴅᴇ:*

🎧 **ɢᴇɴᴇʀᴀʟ ᴄᴏᴍᴍᴀɴᴅs**
├ `{HNDLR}play` - sᴇᴀʀᴄʜ ᴊɪᴏsᴀᴀᴠɴ ᴏʀ ʀᴇᴘʟʏ ᴛᴏ ᴀᴜᴅɪᴏ
├ `{HNDLR}ping` - ᴄʜᴇᴄᴋ ʙᴏᴛ ʟᴀᴛᴇɴᴄʏ & sᴛᴀᴛᴜs
├ `{HNDLR}join` - ᴍᴏᴠᴇ ᴜsᴇʀʙᴏᴛ ᴛᴏ ʏᴏᴜʀ ᴠᴄ
└ `{HNDLR}help` - sʜᴏᴡ ᴛʜɪs ᴍᴇssᴀɢᴇ

🛡️ **ᴀᴅᴍɪɴ ᴄᴏɴᴛʀᴏʟs**
├ `{HNDLR}pause` - ʜᴀʟᴛ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ sᴛʀᴇᴀᴍ
├ `{HNDLR}resume` - ᴄᴏɴᴛɪɴᴜᴇ ᴘᴀᴜsᴇᴅ ᴍᴜsɪᴄ
├ `{HNDLR}skip` - ᴘʟᴀʏ ɴᴇxᴛ ᴛʀᴀᴄᴋ ɪɴ ǫᴜᴇᴜᴇ
└ `{HNDLR}stop` - ᴇɴᴅ sᴇssɪᴏɴ & ᴡɪᴘᴇ ǫᴜᴇᴜᴇ

👑 **ᴏᴡɴᴇʀ ᴇxᴄʟᴜsɪᴠᴇ**
├ `{HNDLR}speedcheck` - ʀᴜɴ sᴇʀᴠᴇʀ ɴᴇᴛᴡᴏʀᴋ ᴀᴜᴅɪᴛ
├ `{HNDLR}restart` - ʀᴇʙᴏᴏᴛ ᴛʜᴇ ᴅᴇᴘʟᴏʏᴍᴇɴᴛ
├ `{HNDLR}stats` - ᴠɪᴇᴡ ɢʟᴏʙᴀʟ ᴜsᴀɢᴇ ᴅᴀᴛᴀ
└ `{HNDLR}eval` - ᴇxᴇᴄᴜᴛᴇ sʏsᴛᴇᴍ ᴄᴏᴅᴇ (ᴅᴀɴɢᴇʀ)
━━━━━━━━━━━━━━━━━━━━━━
✨ **ᴘᴏᴡᴇʀᴇᴅ ʙʏ ᴅᴇᴀᴅʟʏ ᴀᴜᴅɪᴛ ᴇɴɢɪɴᴇ**
"""
    
    await m.reply_text(
        text=HELP_TEXT,
        disable_web_page_preview=True
    )
    
