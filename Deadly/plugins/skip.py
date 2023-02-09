from pyrogram import Client, filters
from pyrogram.types import Message
from Deadly import HNDLR, Music
from Deadly.helpers.decorators import authorized_users_only
from Deadly.helpers.handlers import skip_current_song, skip_item
from Deadly.helpers.queues import QUEUE, clear_queue


@Client.on_message(filters.command(["skip"], prefixes=f"{HNDLR}"))
@authorized_users_only
async def skip(client, m: Message):
    await m.delete()
    chat_id = m.chat.id
    if len(m.command) < 2:
        op = await skip_current_song(chat_id)
        if op == 0:
            await m.reply("**❌ There's nothing in the queue to skip !**")
        elif op == 1:
            await m.reply("No more queue leaving voicechat**")
        else:
            await m.reply(
                f"**⏭ Skip playback** \n**🎵 Now play** - [{op[0]}]({op[1]}) | `{op[2]}`",
                disable_web_page_preview=True,
            )
    else:
        skip = m.text.split(None, 1)[1]
        OP = "**🗑️ Removes the following songs from the Queue : -**"
        if chat_id in QUEUE:
            items = [int(x) for x in skip.split(" ") if x.isdigit()]
            items.sort(reverse=True)
            for x in items:
                if x == 0:
                    pass
                else:
                    hm = await skip_item(chat_id, x)
                    if hm == 0:
                        pass
                    else:
                        OP = OP + "\n" + f"**#⃣{x}** - {hm}"
            await m.reply(OP)
