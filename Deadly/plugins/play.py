# Copyright © 2023-2024 by piroxpower@Github
# Optimized for 2026: Cyber-Aura Thumbnail & Metadata Integration

import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from pytgcalls.types.input_stream import AudioPiped
from pytgcalls.types.input_stream.quality import HighQualityAudio

from Deadly import HNDLR, Music, SUDOERS
from Deadly.helpers.queues import add_to_queue, QUEUE
from Deadly.helpers.youtube import ytsearch, ytdl
from Deadly.helpers.thumbnail import generate_aura_thumb # Our new UI engine
from Deadly.helpers.decorators import authorized_users_only

@Client.on_message(filters.command(["play", "p"], prefixes=f"{HNDLR}"))
@authorized_users_only
async def play(client, m: Message):
    replied = m.reply_to_message
    chat_id = m.chat.id
    user_name = m.from_user.first_name if m.from_user else "User"
    
    # CASE 1: Playing a Replied Audio File
    if replied and (replied.audio or replied.voice):
        await m.delete()
        huehue = await m.reply_text("✨ **ᴘʀᴏᴄᴇssɪɴɢ ᴛᴇʟᴇɢʀᴀᴍ ғɪʟᴇ...**")
        
        dl = await replied.download()
        songname = (replied.audio.title if replied.audio else "Voice Note")[:30]
        duration = "Media"
        # Use a default music icon for file thumbnails
        thumb_url = "https://telegra.ph/file/default_music_thumb.jpg" 

        final_thumb = await generate_aura_thumb(songname, duration, user_name, thumb_url)
        
        if chat_id in QUEUE:
            pos = add_to_queue(chat_id, songname, dl, replied.link, "Audio", duration, thumb_url, user_name)
            await huehue.delete()
            await m.reply_photo(photo=final_thumb, caption=f"➕ **ᴀᴅᴅᴇᴅ ᴛᴏ ǫᴜᴇᴜᴇ [ᴘᴏs: {pos}]**\n└ 🎧 `{songname}`")
        else:
            await Music.join_group_call(chat_id, AudioPiped(dl, HighQualityAudio()))
            add_to_queue(chat_id, songname, dl, replied.link, "Audio", duration, thumb_url, user_name)
            await huehue.delete()
            await m.reply_photo(photo=final_thumb, caption=f"▶️ **ɴᴏᴡ ᴘʟᴀʏɪɴɢ ғʀᴏᴍ ᴛᴇʟᴇɢʀᴀᴍ**")

    # CASE 2: Searching JioSaavn
    else:
        if len(m.command) < 2:
            return await m.reply_text(f"**💡 ᴜsᴀɢᴇ:** `{HNDLR}play [sᴏɴɢ ɴᴀᴍᴇ]`")
        
        await m.delete()
        huehue = await m.reply_text("🔍 **sᴇᴀʀᴄʜɪɴɢ ᴀᴜᴅɪᴛ ᴇɴɢɪɴᴇ...**")
        query = m.text.split(None, 1)[1]
        
        # ytsearch now returns [title, id, duration, thumb_url]
        search = ytsearch(query)
        if search == 0:
            return await huehue.edit("**❌ sᴏɴɢ ɴᴏᴛ ғᴏᴜɴᴅ ᴏɴ ᴀɴʏ ᴀᴘɪ ᴍɪʀʀᴏʀ!**")
        
        songname, song_id, duration, thumb_url = search
        hm, direct_link = await ytdl(song_id)
        
        if hm == 0:
            return await huehue.edit("**❌ ғᴀɪʟᴇᴅ ᴛᴏ ᴇxᴛʀᴀᴄᴛ 320ᴋʙᴘs sᴛʀᴇᴀᴍ!**")

        # Generate the professional Cyber-Aura card
        try:
            final_thumb = await generate_aura_thumb(songname, duration, user_name, thumb_url)
        except Exception as e:
            print(f"Thumb Error: {e}")
            final_thumb = thumb_url # Fallback to raw image

        if chat_id in QUEUE:
            pos = add_to_queue(chat_id, songname, direct_link, song_id, "Audio", duration, thumb_url, user_name)
            await huehue.delete()
            await m.reply_photo(
                photo=final_thumb, 
                caption=f"➕ **ᴀᴅᴅᴇᴅ ᴛᴏ ǫᴜᴇᴜᴇ [ᴘᴏs: {pos}]**\n└ 🎧 **ᴛɪᴛʟᴇ:** `{songname}`"
            )
            
