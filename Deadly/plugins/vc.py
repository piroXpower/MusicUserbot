from random import randint
from pyrogram import Client, filters
from Deadly import HNDLR, PLAYER as USER, SUDOERS
from Deadly.helpers.decorators import authorized_users_only
from pyrogram.errors import UserAlreadyParticipant
from pyrogram.raw.functions.phone import CreateGroupCall


@Client.on_message(filters.user(SUDOERS) & filters.command(["join"], prefixes=f"{HNDLR}"))
async def join(client, message):
    flags = " ".join(message.command[1:])
    try:
        await USER.join_chat(flags)
        await message.reply("**Userbot Joined**")
    except UserAlreadyParticipant:
        await message.reply("**Userbot already participants of the given link**")


@Client.on_message(filters.user(SUDOERS) & filters.command(["openvc"], prefixes=f"{HNDLR}"))
async def opengc(client, message):    
    try:
        await USER.send(CreateGroupCall(
            peer=(await USER.resolve_peer(chat_id)),
            random_id=randint(10000, 999999999)
        )
        )
    except Exception:
        await message.reply(
            "**Error:** Add userbot as admin of your group/channel with permission **Can manage voice chat**"
        )
