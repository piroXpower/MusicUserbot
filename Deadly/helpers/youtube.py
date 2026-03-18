import requests
import re
import asyncio
import random
from youtubesearchpython import VideosSearch

# 1. API CONFIGURATION
API_LIST = [
    "https://saavn.sumit.co/api",
    "https://jiosaavn-apix.arcadopredator.workers.dev/api",
    "https://saavn.me/api" # Added one more mirror for 100% uptime
]

def convert_seconds(seconds):
    try:
        seconds = int(seconds)
        return "%02d:%02d" % (seconds // 60, seconds % 60)
    except:
        return "00:00"

def clean_title(title):
    """Strips YouTube noise to find the core studio track."""
    if not title: return ""
    title = re.split(r'\||-|\(|\{|\[', title)[0]
    junk = ["official", "video", "audio", "lyrics", "full song", "4k", "hd", "hq", "remix"]
    for word in junk:
        title = re.sub(rf"\b{word}\b", "", title, flags=re.IGNORECASE)
    return re.sub(r'[^\w\s]', '', title).strip()

def ytsearch(query):
    """
    Triple-Layer Accuracy: YT Discovery -> Deezer Audit -> Saavn Fetch
    """
    try:
        # LAYER 1: Discovery
        yt = VideosSearch(query, limit=1).result()
        if not yt or not yt.get("result"):
            return 0
            
        yt_title = yt["result"][0]["title"]
        # Grab YT thumbnail as a fallback for the CD art
        yt_thumb = yt["result"][0]["thumbnails"][0]["url"].split("?")[0]
        cleaned_yt_title = clean_title(yt_title)
        
        # LAYER 2: Deezer Metadata Audit
        target_query = cleaned_yt_title
        try:
            d_res = requests.get(f"https://api.deezer.com/search?q={cleaned_yt_title}&limit=1", timeout=5).json()
            if d_res.get("data"):
                track = d_res["data"][0]
                target_query = f"{track['title']} {track['artist']['name']}"
        except: pass

        # LAYER 3: JioSaavn Execution (Failover across API_LIST)
        random.shuffle(API_LIST)
        for base_url in API_LIST:
            try:
                res = requests.get(f"{base_url}/search/songs?query={target_query}&limit=1", timeout=10).json()
                if res.get("success") and res["data"]["results"]:
                    song = res["data"]["results"][0]
                    
                    # Return all 4 essential pieces for play.py
                    # [Title, ID, Duration, Thumbnail]
                    return [
                        song["name"][:35], 
                        song["id"], 
                        convert_seconds(song["duration"]), 
                        song["image"][-1]["url"] if song.get("image") else yt_thumb
                    ]
            except: continue
                
        return 0
    except Exception as e:
        print(f"CRITICAL Search Error: {e}")
        return 0

async def ytdl(song_id):
    """Fetches verified 320kbps link."""
    random.shuffle(API_LIST)
    for base_url in API_LIST:
        try:
            res = requests.get(f"{base_url}/songs?ids={song_id}", timeout=10).json()
            if res.get("success") and res["data"]:
                # The last item in downloadUrl is 320kbps
                return 1, res["data"][0]["downloadUrl"][-1]["url"]
        except: continue
    return 0, "All API endpoints failed."
        
