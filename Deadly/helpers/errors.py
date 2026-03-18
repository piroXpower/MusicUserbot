# Copyright © 2023-2024 by piroxpower@Github
# Enhanced Error Logging for 2026 Audit Engine

import sys
import traceback
from functools import wraps
from pyrogram import Client
from Deadly import OWNER_ID as SUPPORT_CHAT
from pyrogram.errors import ChatWriteForbidden, FloodWait
import asyncio

# Replace this with your actual log group ID or Username


def split_limits(text):
    """Splits long error logs to fit Telegram's 4096 character limit."""
    if len(text) < 2048:
        return [text]
    lines = text.splitlines(True)
    small_msg = ""
    result = []
    for line in lines:
        if len(small_msg) + len(line) < 2048:
            small_msg += line
        else:
            result.append(small_msg)
            small_msg = line
    if small_msg:
        result.append(small_msg)
    return result

def capture_err(func):
    @wraps(func)
    async def capture(client, message, *args, **kwargs):
        try:
            return await func(client, message, *args, **kwargs)
        except ChatWriteForbidden:
            # If the bot is muted/banned from writing, leave to save resources
            try:
                await client.leave_chat(message.chat.id)
            except:
                pass
            return
        except Exception:
            # Get full traceback details
            exc_type, exc_obj, exc_tb = sys.exc_info()
            errors = traceback.format_exception(exc_type, exc_obj, exc_tb)
            
            # Format a professional error report
            user_id = message.from_user.id if message.from_user else "Unknown User"
            chat_id = message.chat.id if message.chat else "Private"
            input_text = message.text or message.caption or "None"
            
            error_msg = (
                "**❌ CRITICAL ERROR DETECTED**\n\n"
                f"👤 **User:** `{user_id}`\n"
                f"📍 **Chat:** `{chat_id}`\n"
                f"⌨️ **Command:** `{input_text}`\n\n"
                f"📝 **Traceback:**\n```python\n"
                f"{''.join(errors)}```"
            )
            
            error_feedback = split_limits(error_msg)
            
            for x in error_feedback:
                try:
                    # Send error directly to your Support/Log chat
                    await client.send_message(SUPPORT_CHAT, x)
                except FloodWait as e:
                    await asyncio.sleep(e.value)
                except Exception as e:
                    print(f"Logging Failed: {e}")
            
            # Keep this raised so you can see it in your AWS terminal too
            raise 

    return capture
            
