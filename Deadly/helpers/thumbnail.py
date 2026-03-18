# Copyright © 2023-2024 by piroxpower@Github
# Optimized for 2026: Cyber-Aura UI Engine

import os
import aiofiles
import aiohttp
from PIL import Image, ImageDraw, ImageFilter, ImageFont

def changeImageSize(maxWidth, maxHeight, image):
    widthRatio = maxWidth / image.size[0]
    heightRatio = maxHeight / image.size[1]
    newWidth = int(widthRatio * image.size[0])
    newHeight = int(heightRatio * image.size[1])
    newImage = image.resize((newWidth, newHeight), Image.LANCZOS)
    return newImage

async def generate_aura_thumb(title, duration, user, thumbnail):
    async with aiohttp.ClientSession() as session:
        async with session.get(thumbnail) as resp:
            if resp.status == 200:
                f = await aiofiles.open("temp_raw.png", mode="wb")
                await f.write(await resp.read())
                await f.close()

    # 1. Base Setup
    img = Image.open("temp_raw.png")
    img = changeImageSize(1280, 720, img)
    
    # Create Blurred Background (Glassmorphism effect)
    background = img.copy().filter(ImageFilter.GaussianBlur(radius=40))
    enhancer = ImageDraw.Draw(background)
    enhancer.rectangle([(0, 0), (1280, 720)], fill=(0, 0, 0, 100)) # Dark Overlay

    # 2. The Spinning CD Circular Crop
    album_art = img.copy().convert("RGBA")
    album_art = changeImageSize(400, 400, album_art)
    
    mask = Image.new("L", (400, 400), 0)
    draw_mask = ImageDraw.Draw(mask)
    draw_mask.ellipse((0, 0, 400, 400), fill=255)
    
    # Paste the circular album art onto the background
    background.paste(album_art, (70, 160), mask)

    # 3. Text & Metadata Branding
    draw = ImageDraw.Draw(background)
    
    # Load fonts (Ensure these .ttf files are in your AWS folder)
    try:
        font_title = ImageFont.truetype("Deadly/assets/font.ttf", 45)
        font_info = ImageFont.truetype("Deadly/assets/font.ttf", 30)
    except:
        font_title = ImageFont.load_default()
        font_info = ImageFont.load_default()

    # Draw Title (Truncate if too long)
    clean_title = title[:30] + "..." if len(title) > 30 else title
    draw.text((520, 250), f"🎧 {clean_title}", fill="white", font=font_title)
    
    # Draw Sub-info
    draw.text((520, 330), f"⏳ ᴅᴜʀᴀᴛɪᴏɴ: {duration}", fill="#E0E0E0", font=font_info)
    draw.text((520, 380), f"👤 ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ: {user}", fill="#E0E0E0", font=font_info)
    draw.text((520, 450), "━━━━━━●──────", fill="white", font=font_info)
    draw.text((520, 500), "✨ ᴅᴇᴀᴅʟʏ ᴀᴜʀᴀ-sᴛʀᴇᴀᴍ ᴠ𝟸", fill="#BB86FC", font=font_info)

    # 4. Save and Return
    final_path = "final_aura_thumb.png"
    background.save(final_path)
    
    # Cleanup raw download
    if os.path.exists("temp_raw.png"):
        os.remove("temp_raw.png")
        
    return final_path
