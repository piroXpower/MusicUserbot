# Copyright © 2023-2024 by piroxpower@Github
# Optimized for 2026: Cyber-Aura Thumbnail Integration

from pyrogram import Client, filters
from pyrogram.types import Message
from Deadly import HNDLR, SUDOERS
from Deadly.helpers.decorators import authorized_users_only
from Deadly.helpers.handlers import skip_current_song, skip_item
from Deadly.helpers.queues import QUEUE

@Client.on_message(filters.command(["skip", "next"], prefixes=f"{HNDLR}"))
@authorized_users_only
async def skip(client, m: Message):
    # Keep the chat clean by deleting the command
    await m.delete()
    chat_id = m.chat.id
    
    # CASE 1: Normal Skip (Next Song)
    if len(m.command) < 2:
        op = await skip_current_song(chat_id)
        
        if op == 0:
            return await m.reply_text("**❌ ᴛʜᴇʀᴇ's ɴᴏᴛʜɪɴɢ ɪɴ ᴛʜᴇ ǫᴜᴇᴜᴇ ᴛᴏ sᴋɪᴘ!**")
        
        if op == 1:
            return await m.reply_text("**⏹️ ǫᴜᴇᴜᴇ ᴇɴᴅᴇᴅ. ʟᴇᴀᴠɪɴɢ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ.**")
        
        # op[0]=Title, op[1]=Link, op[2]=Type, op[3]=Thumbnail Path
        try:
            await m.reply_photo(
                photo=op[3],
                caption=f"⏭️ **sᴋɪᴘᴘᴇᴅ! ɴᴏᴡ ᴘʟᴀʏɪɴɢ:**\n└ 🎧 **ᴛɪᴛʟᴇ:** [{op[0]}]({op[1]})",
            )
        except Exception:
            # Fallback to text if thumbnail generation fails on AWS
            await m.reply_text(f"⏭️ **sᴋɪᴘᴘᴇᴅ! ɴᴏᴡ ᴘʟᴀʏɪɴɢ:**\n└ 🎧 **ᴛɪᴛʟᴇ:** [{op[0]}]({op[1]})")

    # CASE 2: Specific Queue Removal (e.g., !skip 2 5)
    else:
        skip_raw = m.text.split(None, 1)[1]
        output_msg = "**🗑️ ʀᴇᴍᴏᴠᴇᴅ ғʀᴏᴍ ǫᴜᴇᴜᴇ:**"
        
        if chat_id in QUEUE:
            # Parse numbers and sort in reverse to maintain index integrity
            items = [int(x) for x in skip_raw.split(" ") if x.isdigit()]
            items.sort(reverse=True)
            
            removed_any = False
            for x in items:
                # We skip index 0 as it's handled by skip_current_song logic
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
        
