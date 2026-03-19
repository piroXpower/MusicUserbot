# Copyright © 2023-2024 by piroxpower@Github
# Optimized for 2026: Auto-Skip, VC Leave, and 320kbps Audio

from pytgcalls.types.input_stream import AudioPiped
from pytgcalls.types.input_stream.quality import HighQualityAudio
from pytgcalls.types.stream import StreamAudioEnded, StreamVideoEnded

from ..import PLAYER, Music, FFMPEG_OPTIONS
from .queues import QUEUE, clear_queue, pop_an_item
from .youtube import ytdl

async def skip_current_song(chat_id):
    """
    Handles transitioning to the next song or leaving the VC.
    Used by both !skip command and the Auto-Skip listener.
    """
    if chat_id in QUEUE:
        # 1. Remove the song that just finished/was skipped
        pop_an_item(chat_id)
        
        # 2. Check if the queue is now empty
        if chat_id not in QUEUE or len(QUEUE[chat_id]) == 0:
            try:
                await Music.leave_group_call(chat_id)
            except:
                pass
            clear_queue(chat_id)
            return 1 # Signal: Queue Ended
            
        else:
            # 3. Fetch next song data from the queue
            # Index Map: [0] Title, [1] Duration, [2] ReqBy, [3] LinkID, [5] Thumb, [6] Ref
            next_song = QUEUE[chat_id][0]
            title = next_song[0]
            link_id = next_song[3]
            ref_link = next_song[6]

            # 4. Refresh Link (Crucial for expiring API links)
            if not str(link_id).startswith("http"):
                status, play_url = await ytdl(link_id)
            else:
                status, play_url = 1, link_id
                
            if status == 0:
                # If the link is broken, skip to the next one automatically
                return await skip_current_song(chat_id)

            # 5. Start the next stream
            try:
                await Music.change_stream(
                    chat_id, 
                    AudioPiped(play_url, audio_parameters=FFMPEG_OPTIONS)
                )
            except Exception as e:
                print(f"Stream Change Error: {e}")
                return await skip_current_song(chat_id)
            
            return [title, ref_link]
            
    return 0 # Signal: No active queue

async def skip_item(chat_id, position):
    """
    Removes a specific song from the queue (e.g., !skip 2).
    This function fixes your 'ImportError' startup crash.
    """
    if chat_id in QUEUE:
        chat_queue = QUEUE[chat_id]
        if len(chat_queue) > position:
            song_name = chat_queue[position][0]
            chat_queue.pop(position)
            
            # Cleanup if queue becomes empty
            if not chat_queue:
                clear_queue(chat_id)
                
            return song_name
    return 0

@Music.on_stream_end()
async def on_end_handler(_, update):
    """
    The Auto-Skip Listener:
    Triggers automatically whenever a song finishes playing.
    """
    chat_id = update.chat_id
    
    # Trigger the skip logic
    op = await skip_current_song(chat_id)
    
    # If Queue Ended, send a final message
    if op == 1:
        await PLAYER.send_message(
            chat_id,
            "⏹️ **ǫᴜᴇᴜᴇ ᴇɴᴅᴇᴅ. ʟᴇᴀᴠɪɴɢ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ.**"
        )
        return

    # If a new song started, notify the group
    if isinstance(op, list):
        await PLAYER.send_message(
            chat_id,
            f"▶️ **ɴᴏᴡ ᴘʟᴀʏɪɴɢ**\n"
            f"━━━━━━━━━━━━━━━━━━━\n"
            f"🎧 **ᴛɪᴛʟᴇ:** [{op[0]}]({op[1]})\n"
            f"━━━━━━━━━━━━━━━━━━━",
            disable_web_page_preview=True
                )
            
