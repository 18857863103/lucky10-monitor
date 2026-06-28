from telethon import TelegramClient, events
from telethon.sessions import StringSession
import os
import requests

api_id = int(os.environ["API_ID"])
api_hash = os.environ["API_HASH"]
session = os.environ["SESSION"]
bot_token = os.environ["BOT_TOKEN"]
chat_id = int(os.environ["CHAT_ID"])

client = TelegramClient(
    StringSession(session),
    api_id,
    api_hash
)

async def send(text):
    requests.post(
        f"https://api.telegram.org/bot{bot_token}/sendMessage",
        data={
            "chat_id": chat_id,
            "text": text
        }
    )
  @client.on(events.NewMessage(chats="az10plan"))
async def handler(event):
    await send(event.raw_text)

print("Monitor started...")

client.start()
client.run_until_disconnected()
