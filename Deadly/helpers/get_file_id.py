# Copyright © 2023-2024 by piroxpower@Github
# Optimized for 2026: Fast Media Type Detection

from pyrogram.types import Message

def get_file_id(msg: Message):
    """
    Identifies the media type and returns the file object with a custom 'type' attribute.
    Optimized to prioritize Audio and Voice for Music Userbots.
    """
    if not msg.media:
        return None

    # Priority list for a Music Bot: Check audio and voice first
    media_types = [
        "audio", "voice", "video", "photo", "animation", 
        "document", "video_note", "sticker", "contact", 
        "dice", "poll", "location", "venue"
    ]

    for m_type in media_types:
        obj = getattr(msg, m_type, None)
        if obj:
            # We add a 'file_type' attribute so other plugins 
            # know exactly what they are dealing with.
            setattr(obj, "file_type", m_type)
            return obj
            
    return None
