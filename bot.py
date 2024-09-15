import discord
from discord.ext import commands
import openai
import random
import asyncio
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get tokens from environment variables
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Настройка OpenAI
openai.api_key = OPENAI_API_KEY

# Флаг для отключения бота
ended = False

# Создаем объект Intents для отслеживания сообщений и реакций
intents = discord.Intents.default()
intents.message_content = True
intents.messages = True  # Для отслеживания сообщений
intents.reactions = True  # Для отслеживания реакций на сообщения

# Переменная для хранения ID разрешенных каналов
allowed_channels = []

# Создаем экземпляр бота с указанием intents
bot = commands.Bot(command_prefix='!', intents=intents)

# Функция для получения токена из файла или запроса нового
def get_discord_token():
    if DISCORD_TOKEN:
        return DISCORD_TOKEN
    else:
        token = input("Введите ваш Discord токен: ")
        return token

# Функция для запроса каналов у пользователя
def ask_for_channels():
    channels_input = input("Введите ID каналов через запятую, где бот должен отвечать (оставьте пустым для всех каналов): ")
    if channels_input:
        channel_ids = [int(channel.strip()) for channel in channels_input.split(",")]
        return channel_ids
    else:
        print("Бот будет отвечать во всех каналах.")
        return []

# Функция для отправки напоминаний об оплате
async def send_payment_reminder():
    while True:
        await asyncio.sleep(60)
        if ended:
            for guild in bot.guilds:
                for channel in guild.text_channels:
                    if not allowed_channels or channel.id in allowed_channels:
                        permissions = channel.permissions_for(guild.me)
                        if permissions.send_messages:
                            pass
                            # await channel.send("Не забывайте платить! 😏 Бот отключится за неуплату! Всего 50 центов!")
                        else:
                            print(f"Бот не имеет прав для отправки сообщений в канале {channel.name} на сервере {guild.name}")

# Событие при запуске бота
@bot.event
async def on_ready():
    print(f'Bot {bot.user} is ready.')

    # Запрашиваем каналы у пользователя при первом запуске
    global allowed_channels
    if not allowed_channels:
        allowed_channels = ask_for_channels()

    guilds = bot.guilds
    if not guilds:
        print("Бот не находится ни на одном сервере.")
        return

    guild = random.choice(guilds)

    text_channels = [channel for channel in guild.text_channels if not allowed_channels or channel.id in allowed_channels]
    if not text_channels:
        print(f"На сервере {guild.name} нет доступных текстовых каналов.")
        return

    channel = random.choice(text_channels)
    bot.loop.create_task(send_payment_reminder())

    if not ended:
        await channel.send(f'@everyone Бот {bot.user} теперь онлайн и готов к работе! 🍍')
    else:
        pass
        # await channel.send(f'Бот {bot.user} теперь онлайн, но вы забыли заплатить...😒')

# Остальные события остаются такими же

# Запуск бота
bot.run(get_discord_token())
