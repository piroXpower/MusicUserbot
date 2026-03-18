# Copyright © 2026 by piroxpower@Github
# High-Speed Triple-Audit: YouTube -> Deezer (Primary) -> JioSaavn (Stream)

import requests
import re
import random
from youtubesearchpython import VideosSearch

# API CONFIGURATION
API_LIST = [
    "https://saavn.me/api",
    "https://saavn.sumit.co/api",
    "https://jiosaavn-apix.arcadopredator.workers.dev/api"
]

def convert_seconds(seconds):
    try:
        seconds = int(seconds)
        return "%02d:%02d" % (seconds // 60, seconds % 60)
    except:
        return "00:00"

def clean_title(title):
    """Strips YouTube noise to find core track metadata."""
    if not title: return ""
    title = re.split(r'\||-|\(|\{|\[', title)[0]
    junk = ["official", "video", "audio", "lyrics", "full song", "4k", "hd", "hq", "remix"]
    for word in junk:
        title = re.sub(rf"\b{word}\b", "", title, flags=re.IGNORECASE)
    return re.sub(r'[^\w\s]', '', title).strip()

def ytsearch(query):
    """
    1. YouTube: Finds the song.
    2. Deezer: Audits for the official Global Metadata.
    3. JioSaavn: Fetches the 320kbps Stream Package.
    """
    try:
        # STEP 1: YouTube Discovery
        yt = VideosSearch(query, limit=1).result()
        if not yt or not yt.get("result"):
            return 0
            
        yt_data = yt["result"][0]
        yt_title = yt_data["title"]
        yt_thumb = yt_data["thumbnails"][0]["url"].split("?")[0]
        cleaned_yt_title = clean_title(yt_title)
        
        # STEP 2: Deezer Primary Metadata Audit
        # We prioritize Deezer's database for the cleanest Title/Artist info
        target_query = cleaned_yt_title
        deezer_thumb = None
        try:
            d_res = requests.get(f"https://api.deezer.com/search?q={cleaned_yt_title}&limit=1", timeout=4).json()
            if d_res.get("data"):
                track = d_res["data"][0]
                # Reconstruct query using official Artist + Title
                target_query = f"{track['title']} {track['artist']['name']}"
                deezer_thumb = track['album']['cover_xl']
        except: 
            pass

        # STEP 3: JioSaavn Stream Fetching
        random.shuffle(API_LIST)
        for base_url in API_LIST:
            try:
                # Use the Deezer-audited query for perfect matching
                res = requests.get(f"{base_url}/search/songs?query={target_query}&limit=1", timeout=6).json()
                if res.get("success") and res["data"]["results"]:
                    song = res["data"]["results"][0]
                    
                    # Return: [Title, ID, Duration, Thumb_URL]
                    return [
                        song["name"][:35],               # [0] Official Title
                        song["id"],                      # [1] JioSaavn ID for ytdl()
                        convert_seconds(song["duration"]), # [2] Duration
                        deezer_thumb or song["image"][-1]["url"] or yt_thumb # [3] High-Res Art
                    ]
            except: 
                continue
                
        return 0
    except Exception as e:
        print(f"Audit Error: {e}")
        return 0

async def ytdl(song_id):
    """Fetches the actual 320kbps .m4a link from the JioSaavn API."""
    random.shuffle(API_LIST)
    for base_url in API_LIST:
        try:
            res = requests.get(f"{base_url}/songs?ids={song_id}", timeout=6).json()
            if res.get("success") and res["data"]:
                # Grabbing the highest quality index (320kbps)
                return 1, res["data"][0]["downloadUrl"][-1]["url"]
        except: 
            continue
    return 0, "Failed to fetch 320kbps stream from mirrors."
                
