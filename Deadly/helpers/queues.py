# Updated for 2026: Supports Metadata Auditing and Dynamic Thumbnails
# © @VIPxLaksh | GitHub@piroxpower
QUEUE = {}

def add_to_queue(chat_id, songname, link, ref, play_type, duration, thumb_url, requested_by):
    """
    Adds a song to the queue with full metadata for thumbnail generation.
    Returns: The position of the song in the queue (1-based index).
    """
    # Create the song data packet
    song_data = [
        songname,      # [0] Title
        link,          # [1] Stream URL or Song ID
        ref,           # [2] Original Link (for caption)
        play_type,     # [3] Audio/Video
        duration,      # [4] MM:SS format
        thumb_url,     # [5] Raw image URL
        requested_by   # [6] User's First Name
    ]

    if chat_id in QUEUE:
        chat_queue = QUEUE[chat_id]
        chat_queue.append(song_data)
        # Return position (e.g., if 1 song exists, new one is pos 1 in list, so user sees 1)
        return len(chat_queue) - 1
    else:
        QUEUE[chat_id] = [song_data]
        return 0

def get_queue(chat_id):
    """Returns the list of songs for a specific chat."""
    if chat_id in QUEUE:
        return QUEUE[chat_id]
    return 0

def pop_an_item(chat_id):
    """Removes the current song (index 0) from the queue."""
    if chat_id in QUEUE:
        chat_queue = QUEUE[chat_id]
        if chat_queue:
            chat_queue.pop(0)
            # If queue becomes empty after popping, clean up the dictionary
            if not chat_queue:
                QUEUE.pop(chat_id)
            return 1
    return 0

def clear_queue(chat_id):
    """Deletes the entire queue for a chat (used on .stop)."""
    if chat_id in QUEUE:
        QUEUE.pop(chat_id)
        return 1
    return 0
            
