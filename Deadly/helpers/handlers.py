# Copyright © 2023-2024 by piroxpower@Github
# Optimized for 2026: High-Speed Text-Only Queue Logic

import os
from pytgcalls.types.input_stream import AudioPiped
from pytgcalls.types.input_stream.quality import HighQualityAudio

from Deadly import Music
from Deadly.helpers.queues import QUEUE, get_queue, pop_an_item

async def skip_current_song(chat_id):
    """Handles automatic/manual skipping to the next song in queue."""
    if chat_id in QUEUE:
        # 1. Remove the song that just finished or was skipped
        pop_an_item(chat_id)
        
        # 2. Check if the queue is now empty
        if len(QUEUE[chat_id]) == 0:
            try:
                await Music.leave_group_call(chat_id)
            except:
                pass
            del QUEUE[chat_id]
            return 1 # Signal: Queue Ended
            
        else:
            # 3. Fetch next song data from the queue
            # Structure: [title, duration, user, link, type, thumb_url]
            next_song = get_queue(chat_id)
            title = next_song[0]
            duration = next_song[1]
            requested_by = next_song[2]
            link = next_song[3]
            thumb_url = next_song[5]

            # 4. Trigger the next stream immediately
            await Music.change_stream(
                chat_id,
                AudioPiped(link, HighQualityAudio())
            )
            
            # 5. Return data for play/skip messages (Using raw thumb_url as fallback)
            return [title, link, "Audio", thumb_url]
            
    return 0 # Signal: Nothing in queue

async def skip_item(chat_id, position):
    """Removes a specific item from the queue by its index."""
    if chat_id in QUEUE:
        items = QUEUE[chat_id]
        if len(items) > position:
            # Extract song name for the confirmation message
            song_name = items[position][0]
            # Remove the specific index
            items.pop(position)
            return song_name
    return 0
