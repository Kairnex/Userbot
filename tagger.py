import asyncio
import random
from telethon.tl.types import User
from messages import casual_messages  # Make sure this file exists
from telethon import events

active_tags = {}

async def start_tagger(client, chat_id):
    if chat_id in active_tags:
        return  # Already tagging

    active_tags[chat_id] = True

    while active_tags.get(chat_id):
        members = [
            user async for user in client.iter_participants(chat_id)
            if isinstance(user, User) and not user.bot
        ]

        for user in members:
            if not active_tags.get(chat_id):
                break  # Stop early if /stop is used

            if user.username:
                mention = f"@{user.username}"
            else:
                mention = f"[{user.first_name}](tg://user?id={user.id})"

            msg = f"{random.choice(casual_messages)}\n{mention}"
            try:
                await client.send_message(chat_id, msg, parse_mode="md")
            except Exception as e:
                print(f"Failed to tag: {e}")

            await asyncio.sleep(5)  # Delay between tags

    # Cleanup
    active_tags.pop(chat_id, None)

async def stop_tagger(chat_id):
    active_tags.pop(chat_id, None)
