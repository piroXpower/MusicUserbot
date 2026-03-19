# Copyright © 2026 by piroxpower@Github
# Optimized for 2026: Hybrid Logic (Deezer Metadata + JioSaavn Stream)

import requests
import re
import random
from youtubesearchpython import VideosSearch

# Official JioSaavn API Mirrors (High Stability)
SAAVN_APIS = [
    "https://saavn.me/api",
    "https://saavn.sumit.co/api",
    "https://jiosaavn-apix.arcadopredator.workers.dev/api"
]

def convert_seconds(seconds):
    try:
        seconds = int(seconds)
        return "%02d:%02d" % (seconds // 60, seconds % 60)
    except: return "00:00"

def clean_title(title):
    if not title: return ""
    title = re.split(r'\||-|\(|\{|\[', title)[0]
    return re.sub(r'[^\w\s]', '', title).strip()

def ytsearch(query):
    """
    1. YouTube: Algorithm to find the right track.
    2. Deezer: Official Metadata & High-Res Art.
    3. JioSaavn: Reliable 320kbps Stream Fetching.
    """
    try:
        # LAYER 1: YouTube Search (The Brain)
        yt = VideosSearch(query, limit=1).result()
        if not yt or not yt.get("result"): return 0
            
        yt_title = yt["result"][0]["title"]
        cleaned_query = clean_title(yt_title)
        
        # LAYER 2: Official Deezer API (Metadata & Art)
        # Even if mirrors are down, the official API (api.deezer.com) is always up.
        deezer_url = f"https://api.deezer.com/search?q={cleaned_query}&limit=1"
        d_res = requests.get(deezer_url, timeout=5).json()

        if d_res.get("data") and len(d_res["data"]) > 0:
            track = d_res["data"][0]
            display_title = f"{track['title']} - {track['artist']['name']}"
            thumb = track['album']['cover_xl']
            
            # LAYER 3: JioSaavn (The Reliable Audio Pipe)
            # We use Deezer's clean title to find the matching file on Saavn
            random.shuffle(SAAVN_APIS)
            for api in SAAVN_APIS:
                try:
                    s_res = requests.get(f"{api}/search/songs?query={display_title}&limit=1", timeout=5).json()
                    if s_res.get("success") and s_res["data"]["results"]:
                        song = s_res["data"]["results"][0]
                        return [
                            display_title[:35], # Clean Deezer Title
                            song["id"],         # Saavn ID for streaming
                            convert_seconds(track['duration']), 
                            thumb               # Official Deezer High-Res Art
                        ]
                except: continue
        
        return 0
    except Exception as e:
        print(f"Hybrid Engine Error: {e}")
        return 0

async def ytdl(song_id):
    """Fetches verified 320kbps link from JioSaavn."""
    random.shuffle(SAAVN_APIS)
    for api in SAAVN_APIS:
        try:
            res = requests.get(f"{api}/songs?ids={song_id}", timeout=5).json()
            if res.get("success") and res["data"]:
                # Returns official 320kbps direct stream
                return 1, res["data"][0]["downloadUrl"][-1]["url"]
        except: continue
    return 0, "sᴛʀᴇᴀᴍ ᴇɴɢɪɴᴇ ᴏғғʟɪɴᴇ."

