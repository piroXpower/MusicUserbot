# Copyright © 2023-2024 by piroxpower@Github, < https://github.com/piroxpower >.
#
# This file is part of < https://github.com/Team-Deadly/MusicUserbot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/Team-Deadly/MusicUserbot/blob/main/LICENSE >
#
# All rights reserved ®.

from pyrogram.raw.base import Update
from pytgcalls.types.input_stream import AudioPiped
from pytgcalls.types.input_stream.quality import HighQualityAudio
from pytgcalls.types.stream import StreamAudioEnded, StreamVideoEnded

from ..import PLAYER, Music
from .queues import QUEUE, clear_queue, get_queue, pop_an_item
from .youtube import ytdl
from .thumbnail import generate_aura_thumb # New Import

async def skip_current_song(chat_id):
    if chat_id in QUEUE:
        chat_queue = get_queue(chat_id)
        if len(chat_queue) == 1:
            try: await Music.leave_group_call(chat_id)
            except: pass
            clear_queue(chat_id)
            return 1
        else:
            pop_an_item(chat_id)
            new_q = get_queue(chat_id)
            songname, link_id, ref_link, type, duration, thumb_url, req_by = new_q[0]

            # Refresh Link
            hm, play_url = await ytdl(link_id) if not str(link_id).startswith("http") else (1, link_id)
            
            await Music.change_stream(chat_id, AudioPiped(play_url, HighQualityAudio()))
            
            # Generate Thumbnail for the skip
            final_thumb = await generate_aura_thumb(songname, duration, req_by, thumb_url)
            return [songname, ref_link, type, final_thumb]
    return 0

@Music.on_stream_end()
async def on_end_handler(_, update: Update):
    if isinstance(update, (StreamAudioEnded, StreamVideoEnded)):
        chat_id = update.chat_id
        op = await skip_current_song(chat_id)
        if op in [0, 1]: return
        
        await PLAYER.send_photo(
            chat_id,
            photo=op[3],
            caption=f"⏭️ **sᴋɪᴘᴘᴇᴅ! ɴᴏᴡ ᴘʟᴀʏɪɴɢ:**\n└ 🎧 **ᴛɪᴛʟᴇ:** [{op[0]}]({op[1]})"
        )
        
