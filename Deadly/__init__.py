import os 
import asyncio
from pyrogram import Client
from pytgcalls import PyTgCalls


print("[INFO] Deadly Music Userbot Setup Starting... ") 

API_ID = int(os.getenv("API_ID", "21364355")) 
API_HASH = os.getenv("API_HASH", "72f11aec1dd3e5764554d477341a3d0b") 
PYRO_STRING = os.getenv("STRING_SESSION", "BQA7fDIAjbhFITdQH-3ShqVmFEgrWt7vfS4MjQDAILU2le6Nhj3IhDZzUSyQB3gM03PnajSMoII-02GxTozzOUNGCLpGaDQ1FB_v-6wcqVagkKzAN7oVtQbOlfC2tDOrvyY1yM_sVvW4PvVRIbI_dLGKXnZAI3sH6JUVjA5WuTVP_6UpAPzX-t547JgPHVvTncYDKqHoWB558QvvIwRjjzls86bopbXNHPVf5rWc1PI83NKDI4j2JRy_OOOvj5cNEG3dH-vm9rmhsSt6A9P55OqglUw6sJXFCYJDrRz3xTblB4VUzs4-wkrYQFm9dlvBJ6OWVZvpmMnzI1Onuzzl2uqYk4yxqQAAAAH1HSBKAA") 
STRING2 = os.getenv("STR2", "") 
OWNER_ID = os.getenv("OWNER_ID", "8407294026") 
MONGO_URI = os.getenv("MONGO_URL", "mongodb+srv://jarvis:op@cluster0.7tisvwv.mongodb.net/?retryWrites=true&w=majority") 
LOGGER = os.getenv("LOGGER", "8407294026") 
HNDLR = os.getenv("HNDLR", "!") 
SUDOERS = [8407294026]

print(" [INFO] Starting Up Your Client...") 

PLAYER = Client(name="PYRO_CLIENT", api_id=API_ID, api_hash=API_HASH, session_string=PYRO_STRING, plugins=dict(root="Deadly/plugins")) 
Music = PyTgCalls(PLAYER)

print("[INFO] Setup finished Starting Your Userbot.. ") 
