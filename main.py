import asyncio
from bot_handler import bot
from session_manager import get_session_clients
from tagger import start_tagger

async def start_all():
    clients = get_session_clients()
    
    # Start userbot sessions
    for client in clients:
        await client.start()
        print(f"✅ Started user session: {client.session.save()}")

    # Run both bot and userbots
    await asyncio.gather(
        bot.run_until_disconnected(),
        *[client.run_until_disconnected() for client in clients]
    )

if __name__ == "__main__":
    print("🚀 Starting bot and user sessions...")
    
    try:
        asyncio.get_event_loop().run_until_complete(start_all())
    except KeyboardInterrupt:
        print("🛑 Exiting due to keyboard interrupt.")
