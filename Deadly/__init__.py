import os 
import asyncio


print("[INFO] Deadly Music Userbot Setup Starting... ") 

API_ID = int(os.getenv("API_ID")) 
API_HASH = os.getenv("API_HASH", None) 
PYRO_STRING = os.getenv("STRING_SESSION", None) 
OWNER_ID = os.getenv("OWNER_ID", None) 
MONGO_URI = os.getenv("MONGO_URL", None) 
LOGGER = os.getenv("LOGGER", None) 


print(" [INFO] Starting Up Your Client...") 

PLAYER = Client(PYRO_STRING, API_ID, API_HASH, plugins=dict(root="Deadly.plugins"))
Music = PyTgCalls(PLAYER)

print("[INFO] Setup finished Starting Your Userbot.. ") 
