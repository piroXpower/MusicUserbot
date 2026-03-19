# Copyright © 2023-2024 by piroxpower@Github
# Optimized for 2026: Async Lifecycle & High-Performance Audio

import os
import asyncio
import sys
from pyrogram import Client
from pytgcalls import PyTgCalls
from pyrogram.errors import FloodWait

# --- 1. CONFIGURATION ---
print("[INFO] Deadly Music Userbot: Initializing Config...")

API_ID = int(os.getenv("API_ID", "21364355")) 
API_HASH = os.getenv("API_HASH", "72f11aec1dd3e5764554d477341a3d0b") 
PYRO_STRING = os.getenv("STRING_SESSION", "") 

# dont change or you responsible for your bot
FFMPEG_OPTIONS = {
    'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
    'options': (
        '-vn '                           # No video
        '-acodec libopus '               # Native High-Quality Telegram Codec
        '-b:a 320k '                     # Max Bitrate
        '-ac 2 '                         # Stereo
        '-ar 48000 '                     # Native Telegram Sample Rate
        '-af "volume=1.5,'               # 50% Volume Boost
            'bass=g=3:f=60:w=0.5,'       # Warm Sub-Bass Punch
            'compand=0.3|0.3:1|1:-90/-60|-60/-40|-40/-30/-20/-20:6:0:-90:0.2,' # Pro Compression
            'loudnorm=I=-16:TP=-1.5:LRA=11"' # Intelligent Loudness Normalization
    ),
}


# Support for Multi-Account if needed later
OWNER_ID = int(os.getenv("OWNER_ID", "8407294026")) 
LOGGER = int(os.getenv("LOGGER", "8407294026")) 
HNDLR = os.getenv("HNDLR", "!") 

# Sudoers list (Add your ID here)
SUDOERS = [8407294026, 7301581155, 6741274706, 6750212064]

# --- 2. CLIENT INITIALIZATION ---
print("[INFO] Starting Pyrogram Client...")

# We use 'plugins' to automatically load play.py, skip.py, etc.
PLAYER = Client(
    name="DeadlyMusic",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=PYRO_STRING,
    plugins=dict(root="Deadly/plugins")
)

# Initialize PyTgCalls with the Player
Music = PyTgCalls(PLAYER)

# --- 3. STARTUP LOGIC ---
async def start_bot():
    print("[INFO] Booting Engines...")
    try:
        await PLAYER.start()
        await Music.start()
        
        # Send a startup message to your Logger group
        try:
            await PLAYER.send_message(LOGGER, "**✅ Deadly Music Userbot is Live!**\n\nAudit Engine: `Online`\nThumbnail Engine: `Cyber-Aura v2`")
        except:
            pass
            
        print("[INFO] Bot is now 100% Online. Press Ctrl+C to Stop.")
        # Keep the bot running forever
        await asyncio.Event().wait()
        
    except FloodWait as e:
        print(f"[ERROR] FloodWait: Sleeping for {e.value} seconds...")
        await asyncio.sleep(e.value)
    except Exception as e:
        print(f"[CRITICAL] Startup Failed: {e}")
    finally:
        await PLAYER.stop()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(start_bot())
    except KeyboardInterrupt:
        print("\n[INFO] Shutting down safely...")

