# Copyright © 2023-2024 by piroxpower@Github
# v1.1.6 Compatible: 320kbps Boosted Engine

import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from pytgcalls.types.input_stream import AudioPiped, AudioParameters

from Deadly import HNDLR, Music, FFMPEG_OPTIONS
from Deadly.helpers.queues import add_to_queue, QUEUE
from Deadly.helpers.youtube import ytsearch, ytdl
from Deadly.helpers.decorators import authorized_users_only


@Client.on_message(filters.command(["play", "p"], prefixes=f"{HNDLR}"))
@authorized_users_only
async def play(client, m: Message):
    chat_id = m.chat.id
    user_name = m.from_user.first_name if m.from_user else "User"
    
    if len(m.command) < 2:
        return await m.reply_text(f"**💡 ᴜsᴀɢᴇ:** `{HNDLR}play [sᴏɴɢ ɴᴀᴍᴇ]`")
    
    await m.delete()
    huehue = await m.reply_text("🔍 **sᴇᴀʀᴄʜɪɴɢ...**")
    query = m.text.split(None, 1)[1]
    
    search = ytsearch(query)
    if search == 0:
        return await huehue.edit("**❌ sᴏɴɢ ɴᴏᴛ ғᴏᴜɴᴅ!**")
    
    title, song_id, duration, thumb_url, *others = search
    
    status, direct_link = await ytdl(song_id)
    if status == 0:
        return await huehue.edit(f"**❌ ᴇxᴛʀᴀᴄᴛɪᴏɴ ᴇʀʀᴏʀ:**\n`{direct_link}`")

    if chat_id in QUEUE:
        pos = add_to_queue(chat_id, title, direct_link, song_id, "Audio", duration, thumb_url, user_name)
        await huehue.edit(f"➕ **ᴀᴅᴅᴇᴅ ᴛᴏ ǫᴜᴇᴜᴇ [ᴘᴏs: {pos}]**\n└ 🎧 `{title}`")
    else:
        try:
            # v1.1.6 Engine: Manual Parameters + Custom FFmpeg Filters
            await Music.join_group_call(
                chat_id,
                AudioPiped(
                    direct_link, 
                    audio_parameters=AudioParameters.from_quality(AudioQuality.HIGH), 
                    additional_ffmpeg_parameters=FFMPEG_OPTIONS['options']
                )
            )
            
            add_to_queue(chat_id, title, direct_link, song_id, "Audio", duration, thumb_url, user_name)
            
            await huehue.edit(
                f"▶️ **ɴᴏᴡ ᴘʟᴀʏɪɴɢ**\n"
                f"━━━━━━━━━━━━━━━━━━━\n"
                f"🎧 **ᴛɪᴛʟᴇ:** `{title}`\n"
                f"👤 **ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ:** {user_name}\n"
                f"━━━━━━━━━━━━━━━━━━━",
                disable_web_page_preview=True
            )
            
        except Exception as e:
            await huehue.edit(f"**❌ ᴀᴜᴅɪᴏ ᴇʀʀᴏʀ:**\n`{e}`")
