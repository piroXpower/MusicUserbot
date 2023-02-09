from pyrogram import Client, filters
from pyrogram.types import Message
from Deadly import HNDLR, Music
from Deadly.helpers.decorators import authorized_users_only
from Deadly.helpers.queues import QUEUE

@Client.on_message(filters.command(["resume"], prefixes=f"{HNDLR}"))
@authorized_users_only
async def resume(client, m: Message):
    await m.delete()
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await Music.resume_stream(chat_id)
            await m.reply(
                f"**▶ Resume paused playback**\n\n• To pause playback, use the command  » {HNDLR}pause**"
            )
        except Exception as e:
            await m.reply(f"**ERROR** \n`{e}`")
    else:
        await m.reply("**❌ Nothing is paused!**")
