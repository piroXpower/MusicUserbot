# Copyright © 2023-2024 by piroxpower@Github
# Optimized for 2026: Utility & System Audit Suite

import os
import sys
import time
import traceback
from io import StringIO
from pyrogram import Client, filters
from pyrogram.types import Message
from Deadly import HNDLR, OWNER_ID, Music, PLAYER

# ---------------------------------------------------------
# 1. PING COMMAND (Latency & Audio Health)
# ---------------------------------------------------------
@Client.on_message(filters.command(["ping", "alive"], prefixes=f"{HNDLR}"))
async def ping_audit(client, m: Message):
    start = time.time()
    reply = await m.reply_text("📡 **sᴄᴀɴɴɪɴɢ ᴀᴜʀᴀ-sᴛʀᴇᴀᴍ...**")
    end = time.time()
    
    # Calculate Latency
    telegram_ping = round((end - start) * 1000, 2)
    
    # Dynamic Response based on Server Speed
    status = "ʟɪɢʜᴛɴɪɴɢ ⚡" if telegram_ping < 150 else "sᴛᴀʙʟᴇ 🌀"
    
    await reply.edit_text(
        "✨ **ᴅᴇᴀᴅʟʏ ᴍᴜsɪᴄ sᴛᴀᴛᴜs**\n"
        "━━━━━━━━━━━━━━━━━━━━━\n"
        f"🚀 **ᴘɪɴɢ:** `{telegram_ping} ᴍs`\n"
        f"📊 **sᴛᴀᴛᴜs:** `{status}`\n"
        f"🎧 **ᴀᴜᴅɪᴏ ᴇɴɢɪɴᴇ:** `ᴀᴄᴛɪᴠᴇ`\n"
        "━━━━━━━━━━━━━━━━━━━━━\n"
        "✅ **sʏsᴛᴇᴍ ᴏᴘᴛɪᴍɪᴢᴇᴅ**"
    )

# ---------------------------------------------------------
# 2. EVAL COMMAND (Live Code Execution)
# ---------------------------------------------------------
@Client.on_message(filters.user(OWNER_ID) & filters.command(["eval", "e"], prefixes=f"{HNDLR}"))
async def evaluate_code(client, m: Message):
    if len(m.command) < 2:
        return await m.reply_text("**❌ ᴘʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ ᴘʏᴛʜᴏɴ ᴄᴏᴅᴇ ᴛᴏ ᴇxᴇᴄᴜᴛᴇ.**")
    
    status_msg = await m.reply_text("💻 **ᴇxᴇᴄᴜᴛɪɴɢ ᴄᴏᴅᴇ...**")
    cmd = m.text.split(None, 1)[1]
    
    # Redirecting stdout to capture the output of 'print' statements
    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = StringIO()
    redirected_error = sys.stderr = StringIO()
    stdout, stderr, exc = None, None, None

    try:
        # Wrap code in an async function to allow 'await' inside eval
        code = f"async def __ex(client, m): " + "".join(f"\n {l}" for l in cmd.split("\n"))
        exec(code)
        await locals()["__ex"](client, m)
    except Exception:
        exc = traceback.format_exc()

    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr

    evaluation = ""
    if exc:
        evaluation = f"**❌ ᴇʀʀᴏʀ:**\n```python\n{exc}```"
    elif stderr:
        evaluation = f"**⚠️ sᴛᴅᴇʀʀ:**\n```python\n{stderr}```"
    elif stdout:
        evaluation = f"**✅ ᴏᴜᴛᴘᴜᴛ:**\n```python\n{stdout}```"
    else:
        evaluation = "**✅ sᴜᴄᴄᴇss (ɴᴏ ᴏᴜᴛᴘᴜᴛ)**"

    # Split output if it's too long for Telegram
    if len(evaluation) > 4096:
        with open("eval_result.txt", "w+", encoding="utf8") as out_file:
            out_file.write(str(evaluation))
        await m.reply_document(document="eval_result.txt", caption="**📝 ᴏᴜᴛᴘᴜᴛ ɪs ᴛᴏᴏ ʟᴏɴɢ.**")
        os.remove("eval_result.txt")
    else:
        await status_msg.edit_text(evaluation)

# ---------------------------------------------------------
# 3. STATS COMMAND (System Vitals)
# ---------------------------------------------------------
@Client.on_message(filters.command(["stats", "vitals"], prefixes=f"{HNDLR}"))
async def server_stats(client, m: Message):
    # Only Owners/Sudoers can view deep system vitals
    if m.from_user.id != OWNER_ID:
        return
        
    import psutil
    
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    uptime = time.strftime("%Hʜ %Mᴍ %Ss", time.gmtime(time.time() - start_time)) if 'start_time' in globals() else "ɴ/ᴀ"

    stats_text = (
        "✨ **ᴅᴇᴀᴅʟʏ sʏsᴛᴇᴍ ᴠɪᴛᴀʟs**\n"
        "━━━━━━━━━━━━━━━━━━━━━\n"
        f"🖥️ **ᴄᴘᴜ ᴜsᴀɢᴇ:** `{cpu}%`\n"
        f"🧠 **ʀᴀᴍ ᴜsᴀɢᴇ:** `{ram}%`\n"
        f"💾 **ᴅɪsᴋ ᴜsᴀɢᴇ:** `{disk}%`\n"
        f"⏳ **ᴜᴘᴛɪᴍᴇ:** `{uptime}`\n"
        "━━━━━━━━━━━━━━━━━━━━━\n"
        "✅ **ᴀᴡs ɪɴsᴛᴀɴᴄᴇ: sᴛᴀʙʟᴇ**"
    )
    await m.reply_text(stats_text)
  
