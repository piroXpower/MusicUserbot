from pyrogram import Client, filters
from Deadly import HNDLR, PLAYER as USER, SUDOERS
from pyrogram.errors import UserAlreadyParticipant


@Client.on_message(filters.user(SUDOERS) & filters.command(["join"], prefixes=f"{HNDLR}"))
async def join(client, message):
    flags = " ".join(message.command[1:])
    try:
        await USER.join_chat(flags)
        await message.reply("**Userbot Joined**")
    except UserAlreadyParticipant:
        await message.reply("**Userbot already participants of the given link**")


