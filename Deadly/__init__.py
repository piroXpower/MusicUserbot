import os 
import asyncio
from pyrogram import Client
from pytgcalls import PyTgCalls


print("[INFO] Deadly Music Userbot Setup Starting... ") 

API_ID = int(os.getenv("API_ID")) 
API_HASH = os.getenv("API_HASH", None) 
PYRO_STRING = os.getenv("STRING_SESSION", None) 
OWNER_ID = os.getenv("OWNER_ID", None) 
MONGO_URI = os.getenv("MONGO_URL", None) 
LOGGER = os.getenv("LOGGER", None) 
HNDLR = os.getenv("HNDLR", ".") 
SUDOERS = os.getenv("SUDOERS", "") 


print(" [INFO] Starting Up Your Client...") 

PLAYER = Client(name="PYRO_CLIENT", api_id=API_ID, api_hash=API_HASH, session_string=PYRO_STRING, plugins=dict(root="Deadly/plugins")) 

Music = PyTgCalls(PLAYER)

print("[INFO] Setup finished Starting Your Userbot.. ") 
