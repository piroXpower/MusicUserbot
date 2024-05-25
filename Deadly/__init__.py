import asyncio
import logging
import datetime
from config import Config
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.functions.phone import (
    EditGroupCallParticipantRequest,
    GetGroupCallRequest
)
from telethon.tl.types import (
    Chat,
    ChatBannedRights,
    ChatForbidden,
    PeerChannel,
    UpdateGroupCallParticipants
)

logging.basicConfig(
    format="%(levelname)s %(name)s: %(message)s",
    level=logging.INFO,
)

LOG_CHAT = Config.LOG_CHAT
APP_ID = Config.API_ID
API_HASH = Config.API_HASH
STRING_SESSION = Config.STRING_SESSION
LIMIT = 31536000

async def global_ban(client, channel):  # Add client parameter
    i = 0
    j = 0
    async for d in client.iter_dialogs():
        try:
            if d.is_user or isinstance(d.entity, ChatForbidden):
                continue
            if not (d.entity.creator or d.entity.admin_rights):
                continue
            if isinstance(d.entity, Chat):
                continue
            await client(
                EditBannedRequest(
                    d.input_entity,
                    channel,
                    banned_rights=ChatBannedRights(
                        until_date=datetime.timedelta(days=999999),
                        view_messages=True,
                    ),
                )
            )
            i += 1
        except Exception as e:
            logging.warning(f"Exception on Banning {channel} from {d.title}")
            logging.warning(str(e))
            await client.send_message(LOG_CHAT, str(e))
            j += 1
    logging.info(f"Banned {channel} from {i} chats. Failed in {j} chats.")
    await client.send_message(LOG_CHAT, f"Banned {channel} from {i} chats. Failed in {j} chats.")

async def handle_event(client, event):  # Add client parameter
    if isinstance(event, UpdateGroupCallParticipants):
        channel_part = [
            p for p in event.participants
            if isinstance(p.peer, PeerChannel) and p.just_joined
        ]
        group_call = await client(GetGroupCallRequest(event.call, LIMIT))
        if len(channel_part) < 1:
            return
        await client.send_message(LOG_CHAT, f"Got {len(channel_part)} channels in VC")
        for part in channel_part:
            channel_entity = await client.get_input_entity(part.peer)
            await client(
                EditGroupCallParticipantRequest(
                    call=group_call.call,
                    participant=channel_entity,
                    muted=True,
                )
            )
            logging.info(f"Muting {part.peer}")
            await client.send_message(LOG_CHAT, f"Muted {part.peer}.")
            await asyncio.sleep(0.8)
            logging.info(f"Going to ban {part.peer}")
            await client.send_message(LOG_CHAT, f"Going to ban {part.peer}")
            try:
                await global_ban(client, channel_entity)  # Pass client parameter
            except Exception as e:
                logging.exception(str(e))
                await client.send_message(LOG_CHAT, str(e))

async def main():
    print("Started Client")
    async with TelegramClient(
        StringSession(STRING_SESSION),
        APP_ID,
        API_HASH,
    ) as client:
        client.add_event_handler(lambda event: handle_event(client, event))
        await client.run_until_disconnected()

if __name__ == "__main__":
    asyncio.run(main())
