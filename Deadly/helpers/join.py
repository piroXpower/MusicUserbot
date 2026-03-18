import asyncio
from pyrogram import Client
from Deadly import PLAYER


async def join(PLAYER):
   try:        
       await PLAYER.join_chat("ThriveGuy") 
   except Exception as e:
       print(f"{e}")
