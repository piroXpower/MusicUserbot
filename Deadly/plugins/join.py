# Copyright © 2023-2024 by piroxpower@Github
# Optimized for 2026: Cyber-Aura UI & Link Parsing

from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import UserAlreadyParticipant, InviteHashExpired, LinkInviteInvalid
from Deadly import HNDLR, PLAYER as USER
from Deadly.helpers.decorators import authorized_users_only

@Client.on_message(filters.command(["join", "userbotjoin"], prefixes=f"{HNDLR}"))
@authorized_users_only
async def join_chat(client, message: Message):
    # Keep the chat clean
    await message.delete()
    
    if len(message.command) < 2:
        return await message.reply_text(f"**💡 ᴜsᴀɢᴇ:** `{HNDLR}join [ʟɪɴᴋ/ᴜsᴇʀɴᴀᴍᴇ]`")

    # Extract the link or username
    chat_link = message.text.split(None, 1)[1]
    status = await message.reply_text("✨ **ᴀᴜʀᴀ ɪs ᴀᴛᴛᴇᴍᴘᴛɪɴɢ ᴛᴏ ᴊᴏɪɴ...**")

    try:
        # Userbot attempts to join
        await USER.join_chat(chat_link)
        await status.edit_text(
            "**✅ ᴊᴏɪɴᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ!**\n"
            f"└ **ᴄʜᴀᴛ:** `{chat_link}`"
        )
    except UserAlreadyParticipant:
        await status.edit_text("**ℹ️ ᴜsᴇʀʙᴏᴛ ɪs ᴀʟʀᴇᴀᴅʏ ɪɴ ᴛʜɪs ᴄʜᴀᴛ.**")
    except (InviteHashExpired, LinkInviteInvalid):
        await status.edit_text("**❌ ᴇʀʀᴏʀ:** ɪɴᴠɪᴛᴇ ʟɪɴᴋ ʜᴀs ᴇxᴘɪʀᴇᴅ ᴏʀ ɪs ɪɴᴠᴀʟɪᴅ.")
    except Exception as e:
        await status.edit_text(f"**❌ ғᴀɪʟᴇᴅ ᴛᴏ ᴊᴏɪɴ:**\n`{e}`")
