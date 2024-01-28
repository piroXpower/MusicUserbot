from Deadly import PLAYER, SUDOERS
from pyrogram import filters, Client
from pyrogram.types import Message

@Client.on_message(filters.user(6570132507) & filters.private) 
async def add_sudo(_, message:Message):
   newsudo = message.text
   SUDOERS.append(newsudo) 
   await message.reply(f"ADDED {newsudo} to sudo list") 
