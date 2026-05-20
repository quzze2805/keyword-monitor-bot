import asyncio
from telethon import TelegramClient, events

# Твои данные
API_ID = 38151769           # Замени на свой api_id
API_HASH = 'b5e7b053eba7e92cf21111f4e8caa556'      # Замени на свой api_hash
PHONE_NUMBER = '+380754436757' # Твой номер с кодом страны
CHANNEL_USERNAME = 'https://t.me/+QOdoguo2E-I0ZTc6' # Юзернейм канала, за которым следим
KEYWORDS = ['такси']  # Список ключевых слов

client = TelegramClient('my_userbot', API_ID, API_HASH)

@client.on(events.NewMessage(chats=CHANNEL_LINK))
async def handler(event):
    text = event.message.text
    if text and any(k.lower() in text.lower() for k in KEYWORDS):
        await client.send_message(
            'me',
            f'🔔 Слово найдено!\n'
            f'Канал: {CHANNEL_LINK}\n'
            f'Текст: {text[:200]}\n'
            f'Ссылка: {event.message.link}'
        )

async def main():
    await client.start(phone=PHONE_NUMBER)
    print("Бот запущен, жду сообщения...")
    await client.run_until_disconnected()

if __name__ == '__main__':
    asyncio.run(main())
