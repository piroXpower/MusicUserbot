# Copyright © 2023-2024 by piroxpower@Github
# Entry Point for Deadly Music Userbot (2026 Version)

import asyncio
from pyrogram import idle
from pyrogram.errors import FloodWait, Unauthorized

from Deadly import PLAYER, Music, LOGGER
from Deadly.helpers.join import join

async def main():
    print("[INFO] Starting Deadly Music Userbot Engines...")
    
    try:
        # 1. Start the Pyrogram Client (The Userbot account)
        await PLAYER.start() 
        print("[INFO] Client Started Successfully!") 
        
        # 2. Join the dedicated support/log chat if configured
        try:
            await join(PLAYER) 
        except Exception as je:
            print(f"[WARNING] Could not join support chat: {je}")

        # 3. Start the PyTgCalls Player (The Audio Engine)
        print("[INFO] Initializing Audio Streaming Engine...")
        await Music.start()
        
        # 4. Final Startup Notification
        print(
            """
        ---------------------------------
       |   DEADLY USERBOT IS NOW LIVE!   |
       |  Audit: 100% | Aura: Enabled    |
        ---------------------------------
        """
        )
        
        # Send a log message so you know it's working without looking at AWS
        try:
            await PLAYER.send_message(
                LOGGER, 
                "**🚀 Deadly Music Userbot Started Successfully!**\n\n"
                "• **Audit Engine:** `Verified`\n"
                "• **API Pool:** `Active`\n"
                "• **Thumbnail:** `Cyber-Aura v2`"
            )
        except:
            pass

        # 5. Keep the bot alive and responsive
        print("[DONE] Your MusicBot is waiting for commands.") 
        await idle()
        
    except FloodWait as fw:
        print(f"[CRITICAL] Telegram FloodWait: Must wait {fw.value} seconds.")
    except Unauthorized:
        print("[CRITICAL] Session Expired! Please generate a new STRING_SESSION.")
    except Exception as e:
        print(f"[CRITICAL] Failed to start bot: {e}")
    finally:
        # 6. Graceful Shutdown
        print("[INFO] Shutting down engines safely...")
        if PLAYER.is_connected:
            await PLAYER.stop()
        print("[INFO] Userbot Stopped! Good Bye.")

if __name__ == "__main__":
    # Get the event loop and run the main function
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        pass
    finally:
        loop.close()
