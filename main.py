import asyncio
from bot_handler import bot
from session_manager import get_session_clients
from tagger import start_tagger

async def main():
    await bot.start()

    clients = get_session_clients()
    for client in clients:
        await client.start()
        print(f"Started session: {client.session.save()}")

    print("Bot and userbots running...")
    await asyncio.gather(bot.run_until_disconnected(), *[client.run_until_disconnected() for client in clients])

asyncio.run(main())
