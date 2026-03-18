# Copyright © 2023-2024 by piroxpower@Github
# Optimized for 2026: High-Speed Text-Only Queue Management

# Global Queue Dictionary
QUEUE = {}

def add_to_queue(chat_id, songname, link, ref, play_type, duration, thumb_url, requested_by):
    """
    Standardizes song data into a list for fast retrieval.
    Index Map:
    [0] Title | [1] Duration | [2] Requested By | [3] Stream Link 
    [4] Type | [5] Thumb URL | [6] Ref ID
    """
    song_data = [
        songname,      # [0]
        duration,      # [1]
        requested_by,  # [2]
        link,          # [3]
        play_type,     # [4]
        thumb_url,     # [5]
        ref            # [6]
    ]

    if chat_id in QUEUE:
        QUEUE[chat_id].append(song_data)
        # Returns position (e.g., if 1 song is playing, next is pos 1)
        return len(QUEUE[chat_id]) - 1
    else:
        # Initialize queue with the first song
        QUEUE[chat_id] = [song_data]
        return 0

def get_queue(chat_id):
    """Returns the next song data packet (Index 0)."""
    if chat_id in QUEUE:
        # Returns the first item in the list
        return QUEUE[chat_id][0]
    return 0

def pop_an_item(chat_id):
    """Removes the current song (index 0) from the queue."""
    if chat_id in QUEUE:
        if len(QUEUE[chat_id]) > 0:
            QUEUE[chat_id].pop(0)
            # Cleanup if the list is now empty
            if len(QUEUE[chat_id]) == 0:
                del QUEUE[chat_id]
            return 1
    return 0

def clear_queue(chat_id):
    """Wipes the entire queue for a specific chat."""
    if chat_id in QUEUE:
        del QUEUE[chat_id]
        return 1
    return 0
    
