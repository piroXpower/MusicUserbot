# Copyright © 2023-2024 by piroxpower@Github, < https://github.com/piroxpower >.
#
# This file is part of < https://github.com/Team-Deadly/MusicUserbot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/Team-Deadly/MusicUserbot/blob/main/LICENSE >
#
# All rights reserved ®.


import asyncio
import requests

# 2026 Stable API Endpoints
API_LIST = [
    "https://saavn.sumit.co/api",
    "https://jiosaavn-apix.arcadopredator.workers.dev/api"
]

def convert_seconds(seconds):
    try:
        seconds = int(seconds)
        minutes = seconds // 60
        seconds %= 60
        return "%02d:%02d" % (minutes, seconds)
    except:
        return "00:00"

def ytsearch(query):
    """Searches JioSaavn for song metadata."""
    for base_url in API_LIST:
        try:
            search_url = f"{base_url}/search/songs?query={query}&limit=1"
            response = requests.get(search_url, timeout=10)
            if response.status_code == 200:
                data = response.json()
                if data.get("success") and data["data"]["results"]:
                    song = data["data"]["results"][0]
                    songname = song["name"][:35] + "..." if len(song["name"]) > 34 else song["name"]
                    # Your curl shows 'id' is what we need for the next step
                    return [songname, song["id"], convert_seconds(song["duration"])]
        except Exception as e:
            print(f"Search failed for {base_url}: {e}")
            continue
    return 0

async def ytdl(song_id):
    """Fetches the 320kbps direct stream URL using song ID."""
    for base_url in API_LIST:
        try:
            details_url = f"{base_url}/songs?ids={song_id}"
            response = requests.get(details_url, timeout=10)
            if response.status_code == 200:
                data = response.json()
                if data.get("success") and data["data"]:
                    song_data = data["data"][0]
                    # FIX: Your curl showed the key is 'url', not 'link'
                    download_options = song_data.get("downloadUrl", [])
                    if download_options:
                        # Grab the last item (320kbps) and the 'url' key
                        stream_link = download_options[-1]["url"]
                        return 1, stream_link
        except Exception as e:
            print(f"Link fetch failed for {base_url}: {e}")
            continue
    return 0, "Could not extract stream URL from JioSaavn."
