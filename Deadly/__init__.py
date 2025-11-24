import os 
import asyncio
from pyrogram import Client
from pytgcalls import PyTgCalls


print("[INFO] Deadly Music Userbot Setup Starting... ") 

API_ID = int(os.getenv("API_ID", "21364355")) 
API_HASH = os.getenv("API_HASH", "72f11aec1dd3e5764554d477341a3d0b") 
PYRO_STRING = os.getenv("STRING_SESSION", "") 
STRING2 = os.getenv("STR2", "") 
OWNER_ID = os.getenv("OWNER_ID", "7930301153") 
MONGO_URI = os.getenv("MONGO_URL", "mongodb+srv://jarvis:op@cluster0.7tisvwv.mongodb.net/?retryWrites=true&w=majority") 
LOGGER = os.getenv("LOGGER", "7930301153") 
HNDLR = os.getenv("HNDLR", "!") 
SUDOERS = [7930301153]

print(" [INFO] Starting Up Your Client...") 

PLAYER = Client(name="PYRO_CLIENT", api_id=API_ID, api_hash=API_HASH, session_string=PYRO_STRING, plugins=dict(root="Deadly/plugins")) 
Music = PyTgCalls(PLAYER)

print("[INFO] Setup finished Starting Your Userbot.. ") 
