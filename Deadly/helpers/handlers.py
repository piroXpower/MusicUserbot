
# Copyright © 2023-2024 by piroxpower@Github
# Optimized for 2026: Cyber-Aura Metadata & Queue Logic

import os
from pytgcalls.types.input_stream import AudioPiped
from pytgcalls.types.input_stream.quality import HighQualityAudio

from Deadly import Music
from Deadly.helpers.queues import QUEUE, get_queue, pop_an_item
from Deadly.helpers.thumbnail import generate_aura_thumb

async def skip_current_song(chat_id):
    if chat_id in QUEUE:
        # Remove the song that just finished/was skipped
        pop_an_item(chat_id)
        
        # Check if there is another song waiting
        if len(QUEUE[chat_id]) == 0:
            await Music.leave_group_call(chat_id)
            del QUEUE[chat_id]
            return 1 # Queue Ended
        else:
            # Get the next song data
            # QUEUE stores: [title, dur, user, link, type, thumb_url]
            next_song = get_queue(chat_id)
            title = next_song[0]
            link = next_song[3]
            duration = next_song[1]
            thumb_url = next_song[5]
            requested_by = next_song[2]

            # 1. Start the next stream
            await Music.change_stream(
                chat_id,
                AudioPiped(link, HighQualityAudio())
            )

            # 2. Generate the new Cyber-Aura card for the next song
            try:
                thumb_path = await generate_aura_thumb(title, duration, requested_by, thumb_url)
            except:
                thumb_path = thumb_url # Fallback
            
            # Return data for skip.py to display
            return [title, link, "Audio", thumb_path]
    return 0 # Nothing in queue

async def skip_item(chat_id, position):
    """The missing function that was causing your crash."""
    if chat_id in QUEUE:
        items = QUEUE[chat_id]
        if len(items) > position:
            # Remove specific index
            song_name = items[position][0]
            items.pop(position)
            return song_name
    return 0
            
