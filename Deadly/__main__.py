# Copyright © 2023-2024 by piroxpower@Github
# Optimized for 2026: Safe-Boot & Engine Guard

import asyncio
import importlib
from pyrogram import idle
from Deadly import PLAYER, Music, LOGGER_ID
from Deadly.plugins import __init__ as plugins_root

# Utility to load all plugins safely
def load_plugins():
    import os
    import glob
    # Path to your plugins folder
    path = "Deadly/plugins/*.py"
    files = glob.glob(path)
    for file in files:
        if file.endswith("__init__.py"):
            continue
        name = file.replace("/", ".").replace("\\", ".")[:-3]
        try:
            importlib.import_module(name)
        except Exception as e:
            print(f"[CRITICAL] Failed to load plugin {name}: {e}")

async def main():
    print("✨ [INFO]: ɪɴɪᴛɪᴀʟɪᴢɪɴɢ ᴀᴜʀᴀ-sᴛʀᴇᴀᴍ ᴇɴɢɪɴᴇs...")
    
    try:
        # 1. Start the Userbot Client
        await PLAYER.start()
        print("✅ [INFO]: ᴜsᴇʀʙᴏᴛ ᴀᴄᴛɪᴠᴀᴛᴇᴅ.")

        # 2. Start the Music Engine (PyTgCalls)
        await Music.start()
        print("✅ [INFO]: ᴍᴜsɪᴄ ᴇɴɢɪɴᴇ ᴀᴄᴛɪᴠᴀᴛᴇᴅ.")

        # 3. Load Plugins Manually for better error catching
        load_plugins()
        print("✅ [INFO]: ᴀʟʟ ᴘʟᴜɢɪɴs sʏɴᴄʜʀᴏɴɪᴢᴇᴅ.")

        # 4. Notify Logger Group
        try:
            await PLAYER.send_message(
                LOGGER_ID, 
                "🚀 **ᴅᴇᴀᴅʟʏ ᴍᴜsɪᴄ ᴜsᴇʀʙᴏᴛ ɪs ɴᴏᴡ ᴏɴʟɪɴᴇ!**\n"
                "└ sʏsᴛᴇᴍ: `ᴀᴡs-ᴜʙᴜɴᴛᴜ-2026`"
            )
        except:
            pass

        print("⚡ [READY]: ʙᴏᴛ ɪs ɴᴏᴡ ʟɪᴠᴇ. ᴘʀᴇss ᴄᴛʀʟ+ᴄ ᴛᴏ sᴛᴏᴘ.")
        await idle()

    except Exception as e:
        print(f"[ERROR]: sʏsᴛᴇᴍ ᴄʀᴀsʜ ᴅᴜʀɪɴɢ sᴛᴀʀᴛᴜᴘ: {e}")

    finally:
        # --- SAFE SHUTDOWN PROTOCOL ---
        # This prevents the "ConnectionError: Client is already terminated"
        print("\n[INFO]: sʜᴜᴛᴛɪɴɢ ᴅᴏᴡɴ ᴇɴɢɪɴᴇs sᴀғᴇʟʏ...")
        
        if PLAYER.is_connected:
            try:
                await PLAYER.stop()
                print("🛑 [INFO]: ᴜsᴇʀʙᴏᴛ ᴅɪsᴄᴏɴɴᴇᴄᴛᴇᴅ.")
            except Exception as e:
                print(f"[DEBUG]: ᴜsᴇʀʙᴏᴛ sᴛᴏᴘ ᴇʀʀᴏʀ: {e}")

        # Ensure PyTgCalls stops if it was active
        try:
            await Music.stop()
            print("🛑 [INFO]: ᴍᴜsɪᴄ ᴇɴɢɪɴᴇ ʜᴀʟᴛᴇᴅ.")
        except:
            pass

if __name__ == "__main__":
    # Standard Python 3.12+ Async Loop
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        pass
    finally:
        loop.close()
        
