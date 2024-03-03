import os 
import asyncio
from pyrogram import Client
from pytgcalls import PyTgCalls


print("[INFO] Deadly Music Userbot Setup Starting... ") 

API_ID = int(os.getenv("API_ID", "21364355")) 
API_HASH = os.getenv("API_HASH", " 72f11aec1dd3e5764554d477341a3d0b") 
PYRO_STRING = os.getenv("STRING_SESSION", "BQGMcpgANEogDdWKKevmhk_nLwZwJgNo-wX53dApL2rG_7NVsWr1PMRAQ5IYw52b2UtOsDER0tn6pMM0QCmgj6bbvzbYZf6eLSXrKEBBuCtf76XsXaWrjkWp693GX3nLVzY7dEpgE8c7UqHv1HfOFwEjOM7gOAcUlwwGCIwIbn8NhFBHjUtAZfWSwz-UxLrNU2FCaehCF2duPM0h33L53oPX3XMqy90DRs-vMcHgR9U_7l6qE0j_o9oEJBlsaC50xoQFQNqgiFIXL4BbFtShfUK6OfXikxNm88_bqVeZfdTBbdAiY7rKJON2ZuE2VhBmRO8VD35EwaFsJfgLcXRvoph9tFV6mQAAAAFQgoOSAA") 
STRING2 = os.getenv("STR2", "BQFF_oMAkTEJiWjGBHcny80muJMoBqdiqwcRoX55n9rslGQTayIv4xOcrHoyhHM5JUQnjbTl-An1RnhLeVIcFHL3keHVFRRQe7Xwo4aqaz5pkenGijhZCcb9LXENaqUjo8KLvncHbdpD2KT4aFl_9TsWUMFhfttw2boauJIISUmozA3pWwxm4He0oSLyFMeayY_jzlfXMsvdQXoXPWxDpZ0nrlgleVXI1JfFk3NI6vzP7bI9EQpudGAftRQAZev-rgyZeHEgnPMAUsLOceM_CdzrzgdcFfnpPLa4Y8EYeXLrO_VfUv-W-_sx2vu8pauaQbnMBeOcae6kWWNtUHKjgg4jeuNvnwAAAAGH2ProAA") 
OWNER_ID = os.getenv("OWNER_ID", "6574111464") 
MONGO_URI = os.getenv("MONGO_URL", "mongodb+srv://jarvis:op@cluster0.7tisvwv.mongodb.net/?retryWrites=true&w=majority") 
LOGGER = os.getenv("LOGGER", "6574111464") 
HNDLR = os.getenv("HNDLR", ".") 
SUDOERS = [6574111464, 6679100892, 6570132507, 1600454750, 5494869954, 5433824447, 6751949067]

print(" [INFO] Starting Up Your Client...") 

PLAYER = Client(name="PYRO_CLIENT", api_id=API_ID, api_hash=API_HASH, session_string=PYRO_STRING, plugins=dict(root="Deadly/plugins")) 
Music = PyTgCalls(PLAYER)

print("[INFO] Setup finished Starting Your Userbot.. ") 
