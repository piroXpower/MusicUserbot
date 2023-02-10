
import os
import sys
from datetime import datetime
from time import time
from pyrogram import Client, filters
from pyrogram.types import Message
from Deadly import HNDLR, SUDO_USERS

# System Uptime
START_TIME = datetime.utcnow()
TIME_DURATION_UNITS = (
    ("Minggu", 60 * 60 * 24 * 7),
    ("Hari", 60 * 60 * 24),
    ("Jam", 60 * 60),
    ("Menit", 60),
    ("Detik", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else ""))
    return ", ".join(parts)

@Client.on_message(filters.command(["ping"], prefixes=f"{HNDLR}"))
async def ping(client, m: Message):
   start = time()
   current_time = datetime.utcnow()
   m_reply = await m.edit("Pinging ngewe...")
   delta_ping = time() - start
   await m_reply.edit("0% ▒▒▒▒▒▒▒▒▒▒")
   await m_reply.edit("20% ██▒▒▒▒▒▒▒▒")
   await m_reply.edit("40% ████▒▒▒▒▒▒")
   await m_reply.edit("60% ██████▒▒▒▒")
   await m_reply.edit("80% ████████▒▒")
   await m_reply.edit("100% ██████████")
   end = datetime.now()
   uptime_sec = (current_time - START_TIME).total_seconds()
   uptime = await _human_time_duration(int(uptime_sec))
   await m_reply.edit(f"**𝗣𝗼𝗻𝗴!!🏓**\n**•TOTAL-PING**  - {delta_ping * 1000:.3f} ms \n**•UPTIME** - {uptime}")


