from telethon import TelegramClient, events
from telethon.tl.types import UpdateMessageReactions, UpdateNewMessage
from conf import TELEGRAM_API_ID, TELEGRAM_API_HASH, CHAT_IDS
import asyncio


client = TelegramClient('current_session', TELEGRAM_API_ID, TELEGRAM_API_HASH)
client.start()


@events.register(events.Raw)
async def contact_join(event):
    if isinstance(event, UpdateMessageReactions) and event.peer.channel_id in CHAT_IDS:
        entity = await client.get_entity(event.peer.channel_id)
        await client.send_read_acknowledge(entity=entity, message=event.msg_id, clear_mentions=True,
                                           clear_reactions=True, max_id=event.msg_id)

loop = asyncio.get_event_loop()
client.add_event_handler(contact_join)
loop.run_forever()
