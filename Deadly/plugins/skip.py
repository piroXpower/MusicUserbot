# Copyright © 2023-2024 by piroxpower@Github
# Optimized for 2026: Ultra-Fast Text-Only Skip

from pyrogram import Client, filters
from pyrogram.types import Message
from Deadly import HNDLR
from Deadly.helpers.decorators import authorized_users_only
from Deadly.helpers.handlers import skip_current_song, skip_item
from Deadly.helpers.queues import QUEUE

@Client.on_message(filters.command(["skip", "next"], prefixes=f"{HNDLR}"))
@authorized_users_only
async def skip(client, m: Message):
    # Keep the chat clean by deleting the command trigger
    await m.delete()
    chat_id = m.chat.id
    
    # CASE 1: Standard Skip (Play Next Song)
    if len(m.command) < 2:
        op = await skip_current_song(chat_id)
        
        if op == 0:
            return await m.reply_text("**❌ ᴛʜᴇʀᴇ's ɴᴏᴛʜɪɴɢ ɪɴ ᴛʜᴇ ǫᴜᴇᴜᴇ ᴛᴏ sᴋɪᴘ!**")
        
        if op == 1:
            return await m.reply_text("**⏹️ ǫᴜᴇᴜᴇ ᴇɴᴅᴇᴅ. ʟᴇᴀᴠɪɴɢ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ.**")
        
        # op structure from handlers.py: [title, link, type, thumb_url]
        # We use disable_web_page_preview to ensure instant text delivery
        await m.reply_text(
            f"⏭️ **sᴋɪᴘᴘᴇᴅ! ɴᴏᴡ ᴘʟᴀʏɪɴɢ:**\n"
            f"━━━━━━━━━━━━━━━━━━━\n"
            f"🎧 **ᴛɪᴛʟᴇ:** [{op[0]}]({op[1]})\n"
            f"━━━━━━━━━━━━━━━━━━━",
            disable_web_page_preview=True
        )

    # CASE 2: Specific Queue Removal (e.g., !skip 2 5)
    else:
        try:
            skip_raw = m.text.split(None, 1)[1]
        except IndexError:
            return
            
        output_msg = "**🗑️ ʀᴇᴍᴏᴠᴇᴅ ғʀᴏᴍ ǫᴜᴇᴜᴇ:**"
        
        if chat_id in QUEUE:
            # Parse numbers and sort in reverse to maintain index integrity during pop()
            items = [int(x) for x in skip_raw.split(" ") if x.isdigit()]
            items.sort(reverse=True)
            
            removed_any = False
            for x in items:
                # Index 0 is the currently playing song; only remove upcoming ones
                if x > 0:
                    hm = await skip_item(chat_id, x)
                    if hm != 0:
                        output_msg += f"\n**#⃣ {x}** — `{hm}`"
                        removed_any = True
            
            if removed_any:
                await m.reply_text(output_msg)
            else:
                await m.reply_text("**❌ ɴᴏ ᴠᴀʟɪᴅ ǫᴜᴇᴜᴇ ᴘᴏsɪᴛɪᴏɴs ғᴏᴜɴᴅ.**")
        else:
            await m.reply_text("**❌ ǫᴜᴇᴜᴇ ɪs ᴀʟʀᴇᴀᴅʏ ᴇᴍᴘᴛʏ!**")
            
