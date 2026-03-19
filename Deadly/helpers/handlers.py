# v1.1.6 Compatible: Auto-Skip & VC Leave

from pytgcalls.types.input_stream import AudioPiped
from ..import PLAYER, Music, FFMPEG_OPTIONS
from .queues import QUEUE, clear_queue, pop_an_item
from .youtube import ytdl
from pyrogram.types import Message
from pytgcalls.types import AudioQuality, AudioParameters

async def skip_current_song(chat_id):
    if chat_id in QUEUE:
        pop_an_item(chat_id)
        
        if chat_id not in QUEUE or len(QUEUE[chat_id]) == 0:
            try: await Music.leave_group_call(chat_id)
            except: pass
            clear_queue(chat_id)
            return 1
            
        else:
            # Match your QUEUE index mapping
            next_s = QUEUE[chat_id][0]
            title, direct_link, song_id = next_s[0], next_s[1], next_s[3]

            # Refresh Link
            status, play_url = await ytdl(song_id) if not str(song_id).startswith("http") else (1, direct_link)
            
            if status == 0: return await skip_current_song(chat_id)

            # v1.1.6 Change Stream logic
            await Music.change_stream(
                chat_id,
                AudioPiped(
                    play_url,
                    audio_parameters=AudioParameters.from_quality(AudioQuality.HIGH), 
                    additional_ffmpeg_parameters=FFMPEG_OPTIONS['options']
                )
            )
            return title
    return 0
