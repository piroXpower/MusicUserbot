import os
import sys
from pyrogram import Client, filters
from pyrogram.types import Message
from Deadly import HNDLR, SUDO_USERS


@Client.on_message(filters.command(["help"], prefixes=f"{HNDLR}"))
async def help(client, m: Message):
    await m.delete()
    HELP = f"""
<b>👋 Hallo {m.from_user.mention}!
🛠 MUSIC PLAYER HELP MENU

⚡ COMMAND FOR EVERYONE
• {HNDLR}play [song title | youtube links | reply audio file] - to play the song
• {HNDLR}vplay [video title | youtube links | reply video file] - to play video (not for heroku)
• {HNDLR}playlist to view playlists
• {HNDLR}ping - to check status
• {HNDLR}help - to see a list of commands
• {HNDLR}join- to join | to the group
⚡ COMMAND TO ALL ADMIN
• {HNDLR}resume - to continue playing a song or video
• {HNDLR}pause - to pause playing a song or video
• {HNDLR}skip - to skip a song or video
• {HNDLR}end - to end playback
⚡ COMMAND TO OWNER
• {HNDLR}restart - to restart the deployment of bot
• {HNDLR}eval - to check some code in terminal
• {HNDLR}stats - to check user total data stats
• {HNDLR}speedtest - to check speed of server
"""
    await m.reply(HELP)
