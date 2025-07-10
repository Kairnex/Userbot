from telethon import TelegramClient, events
from config import API_ID, API_HASH, BOT_TOKEN
from session_manager import save_session_string, get_session_clients
from tagger import start_tagger, stop_tagger

bot = TelegramClient("bot", API_ID, API_HASH).start(bot_token=BOT_TOKEN)

@bot.on(events.NewMessage(pattern='/starttag'))
async def handler_starttag(event):
    sender = await event.get_sender()
    chat = await event.get_chat()
    if not sender.bot and (await event.client.get_permissions(chat, sender)).is_admin:
        for client in get_session_clients():
            await client.connect()
            asyncio.create_task(start_tagger(client, event.chat_id))
        await event.reply("✅ Tagging started.")

@bot.on(events.NewMessage(pattern='/stop'))
async def handler_stop(event):
    await stop_tagger(event.chat_id)
    await event.reply("🛑 Tagging stopped.")

@bot.on(events.NewMessage(pattern='/restart'))
async def handler_restart(event):
    await stop_tagger(event.chat_id)
    for client in get_session_clients():
        await client.connect()
        asyncio.create_task(start_tagger(client, event.chat_id))
    await event.reply("🔁 Tagging restarted.")

@bot.on(events.NewMessage(pattern='/addsession (.+)'))
async def add_session(event):
    session_str = event.pattern_match.group(1)
    save_session_string(session_str)
    await event.reply("✅ Session added.")
  
