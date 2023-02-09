import asyncio
from pytgcalls import idle
from Deadly import PLAYER, Music
From helpers.join import join


async def main():
    print("[INFO] Starting client...")
    await PLAYER.start()
    await join(PLAYER) 
    print("[INFO] Client Started Successfully!") 
    print("[INFO] STARTING Musicplayer..")
    await Music.start()
    print("[INFO] Player Started Finishing Setup") 
    print(
        """
    ------------------------
   | ALL DONE NOW WAIT...! |
    ------------------------
"""
    )
    print("[DONE] Your MusicBot Started Successfully ") 
    await idle()
    print("[INFO] Userbot Stopped! Good Bye..")
    await bot.stop()


loop = asyncio.get_event_loop()
loop.run_until_complete(main())

