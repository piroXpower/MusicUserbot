from pyrogram import Client, filters
from pyrogram.types import Message
from Deadly import HNDLR, Music, SUDOERS
from Deadly.helpers.decorators import authorized_users_only
from Deadly.helpers.queues import QUEUE

@Client.on_message(filters.user(SUDOERS) & filters.command(["pause"], prefixes=f"{HNDLR}"))
async def pause(client, m: Message):
    await m.delete()
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await Music.pause_stream(chat_id)
            await m.reply(
                f"**Music paused...**"
            )
        except Exception as e:
            await m.reply(f"**ERROR** \n`{e}`")
    else:
        await m.reply("**No Playlist in queue!**")
