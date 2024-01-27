from pyrogram import Client, filters
from pyrogram.types import Message
from Deadly import HNDLR, Music, SUDOERS
from Deadly.helpers.decorators import authorized_users_only
from Deadly.helpers.queues import QUEUE, clear_queue

@Client.on_message(filters.user(SUDOERS) & filters.command(["end", "stop"], prefixes=f"{HNDLR}"))
async def stop(client, m: Message):
    await m.delete()
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await Music.leave_group_call(chat_id)
            clear_queue(chat_id)
            await m.reply("**✅ Streaming Stopped**")
        except Exception as e:
            await m.reply(f"**ERROR** \n`{e}`")
    else:
        await m.reply("**❌ Nothing is playing to end!**")
