import asyncio
from pyrogram import Client
from Deadly import PLAYER


async def join(PLAYER):
    try:        
        await PLAYER.join_chat("TheDeadlyBots") 
        await PLAYER.join_chat("TheBotUpdates") 
        await PLAYER.join_chat("hindi_international_chatting") 
        await PLAYER.join_chat("international_hindi_chatting") 
    except Exception as e:
        print(f"{e}")   
    
