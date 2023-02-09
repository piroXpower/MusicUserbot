from pyrogram import Client, filters
from pyrogram.types import Message
from Deadly import HNDLR, Music
from Deadly.helpers.decorators import authorized_users_only
from Deadly.helpers.queues import QUEUE

@Client.on_message(filters.command(["pause"], prefixes=f"{HNDLR}"))
@authorized_users_only
async def pause(client, m: Message):
    await m.delete()
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await Music.pause_stream(chat_id)
            await m.reply(
                f"**⏸ Playback is paused .**\n\n• To resume playback, use the command  » {HNDLR}resume"
            )
        except Exception as e:
            await m.reply(f"**ERROR** \n`{e}`")
    else:
        await m.reply("** ❌ Nothing is playing to pause!**")
