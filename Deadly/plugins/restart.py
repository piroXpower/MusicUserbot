
import os
import sys
from pyrogram import Client, filters
from pyrogram.types import Message
from Deadly import HNDLR, SUDO_USERS


@Client.on_message(
    filters.user(SUDO_USERS) & filters.command(["restart"], prefixes=f"{HNDLR}"))
async def restart(client, m: Message):
    await m.delete()
    run = await m.reply("Restarting in 5 second")
    await run.edit("Restarting in 4 second")
    await run.edit("Restarting in 3 second")
    await run.edit("Restarting in 2 second")
    await run.edit("Restarting in 1 second")
    await run.edit("**✅ Music Userbot Restarted**")
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit()
