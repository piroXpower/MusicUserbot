# Copyright © 2023-2024 by piroxpower@Github
# Modified for JioSaavn Integration (No Cookies Needed)

import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from pytgcalls.types.input_stream import AudioPiped
from pytgcalls.types import AudioParameters, AudioQuality

from Deadly import HNDLR, Music, SUDOERS
from Deadly.helpers.queues import QUEUE, add_to_queue, get_queue
from Deadly.helpers.youtube import * # Keep this import if your file is still named youtube.py

@Client.on_message(filters.user(SUDOERS) & filters.command(["play"], prefixes=f"{HNDLR}"))
async def play(client, m: Message):
    replied = m.reply_to_message
    chat_id = m.chat.id
    
    if replied:
        if replied.audio or replied.voice:
            await m.delete()
            huehue = await replied.reply("**✧ Processing File...**")
            dl = await replied.download()
            link = replied.link
            
            if replied.audio:
                songname = (replied.audio.title or replied.audio.file_name)[:35] + "..."
            else:
                songname = "Voice Note"
                
            if chat_id in QUEUE:
                pos = add_to_queue(chat_id, songname, dl, link, "Audio", 0)
                await huehue.delete()
                await m.reply_text(f"➕ **{songname}**\nAdded to queue at pos {pos}")
            else:
                await Music.join_group_call(
                    chat_id,
                    AudioPiped(dl, AudioParameters.from_quality(AudioQuality.STUDIO))
                )
                add_to_queue(chat_id, songname, dl, link, "Audio", 0)
                await huehue.delete()
                await m.reply_text(f"▶ **Playing:** {songname}")
    else:
        if len(m.command) < 2:
            await m.reply("Provide a song name to play from JioSaavn")
        else:
            await m.delete()
            huehue = await m.reply("**✧ Searching JioSaavn...**")
            query = m.text.split(None, 1)[1]
            
            search = ytsearch(query) # This now calls Saavn search
            if search == 0:
                await huehue.edit("**❌ Song not found on JioSaavn!**")
            else:
                songname, url, duration = search[0], search[1], search[2]
                hm, direct_link = await ytdl(url) # This now gets direct MP3 link
                
                if hm == 0:
                    await huehue.edit(f"**❌ Failed to get audio from Saavn!**")
                else:
                    if chat_id in QUEUE:
                        pos = add_to_queue(chat_id, songname, direct_link, url, "Audio", 0)
                        await huehue.delete()                        
                        await m.reply_text(f"➕ **{songname}**\nAdded to queue at pos {pos}") 
                    else:
                        try:
                            await Music.join_group_call(
                                chat_id,
                                AudioPiped(
                                    direct_link,
                                    AudioParameters.from_quality(AudioQuality.STUDIO),
                                ),
                            )
                            add_to_queue(chat_id, songname, direct_link, url, "Audio", 0)
                            await huehue.delete()
                            await m.reply_text(f"▶ **Now Playing:** {songname}\n**Duration:** {duration}")
                        except Exception as ep:
                            await huehue.edit(f"Error: `{ep}`")
                
