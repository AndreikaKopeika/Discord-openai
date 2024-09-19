import discord
from discord.ext import commands
import openai
import random
import asyncio
from datetime import datetime
import os
from dotenv import load_dotenvа
from openaibot import process_message_in_opena

# Load environment variables from .env file
load_dotenv()

# Get tokens from environment variables
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Настройка OpenAI
openai.api_key = OPENAI_API_KEY

# Флаг для отключения бота
ended = False

# Создаем объект Intents
intents = discord.Intents.default()
intents.message_content = True
intents.messages = True
intents.reactions = True

# Укажите здесь ID каналов, в которых бот может отправлять сообщения
allowed_channels = [1283777756857106533]

# Создаем экземпляр бота с указанием intents
bot = commands.Bot(command_prefix='!', intents=intents)

# Функция для отправки напоминаний об оплате
async def send_payment_reminder():
    while True:
        await asyncio.sleep(60)  # Change to a configurable interval
        if ended:
            for guild in bot.guilds:
                for channel in guild.text_channels:
                    if channel.id in allowed_channels:
                        permissions = channel.permissions_for(guild.me)
                        if permissions.send_messages:
                            pass
                            # Uncomment if needed
                            # await channel.send("Не забывайте платить! 😏 Бот отключится за неуплату! Всего 50 центов!")
                        else:
                            print(f"Бот не имеет прав для отправки сообщений в канале {channel.name} на сервере {guild.name}")

@bot.event
async def on_ready():
    print(f'Bot {bot.user} is ready.')

    guilds = bot.guilds
    if not guilds:
        print("Бот не находится ни на одном сервере.")
        return

    guild = random.choice(guilds)
    text_channels = [channel for channel in guild.text_channels if channel.id in allowed_channels]
    if not text_channels:
        print(f"На сервере {guild.name} нет доступных текстовых каналов.")
        return

    channel = random.choice(text_channels)
    bot.loop.create_task(send_payment_reminder())

    if not ended:
        await channel.send(f'@everyone Бот {bot.user} теперь онлайн и готов к работе! 🍍')
    else:
        pass
        # Uncomment if needed
        # await channel.send(f'Бот {bot.user} теперь онлайн, но вы забыли заплатить...😒')

@bot.command()
async def bot_help(ctx):
    """Display a list of available commands."""
    help_text = (
        "**Available Commands:**\n"
        "!help - Show this message\n"
        "!ping - Check the bot's responsiveness\n"
        # Add more commands here
    )
    await ctx.send(help_text)

@bot.command()
async def ping(ctx):
    """Check the bot's responsiveness."""
    await ctx.send(f'Pong! Latency is {round(bot.latency * 1000)}ms')

@bot.event
async def on_message(message):
    if not ended:
        if message.channel.id in allowed_channels:
            if message.author == bot.user:
                return

            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            message_content = message.content

            # Отправка в OpenAI и получение ответа
            response_text = await process_message_in_openai(message_content, message.author, current_time)

            # Проверка на упоминание бота или ответ на его сообщение
            if bot.user in message.mentions or message.reference or 'бот' in message.content.lower(): 
                if response_text:
                    sent_message = await message.channel.send(response_text)
                    
                    # Добавляем реакции к сообщению бота
                    await sent_message.add_reaction("👍")
                    await sent_message.add_reaction("👎")
                    await sent_message.add_reaction("🔄")

            await bot.process_commands(message)
    else:
        if message.author != bot.user and message.channel.id in allowed_channels:
            if random.randint(0, 3) == 1:
                # Uncomment if needed
                # await message.channel.send("Бот отключен за неуплату 😔 Заплатите всего 50 центов чтобы продолжить использование 😭")
                await message.channel.send("Бот не может говорить так как его замутили!")

@bot.event
async def on_reaction_add(reaction, user):
    if user == bot.user:
        return

    message = reaction.message
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if message.channel.id in allowed_channels and message.author == bot.user:
        if str(reaction.emoji) == "👍":
            new_response_text = await process_message_in_openai(message.content, user, current_time, event_type="Понравилось сообщение")
            await message.reply(new_response_text)
        
        elif str(reaction.emoji) == "👎":
            new_response_text = await process_message_in_openai(message.content, user, current_time, event_type="Не понравилось сообщение")
            await message.reply(new_response_text)
        elif str(reaction.emoji) == "🔄":
            new_response_text = await process_message_in_openai(message.content, user, current_time, event_type="перегенерация")
            await message.edit(content=new_response_text)

@bot.event
async def on_message_edit(before, after):
    if before.author == bot.user:
        return

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    edit_info = f"Было: {before.content}, стало: {after.content}"

    if before.channel.id in allowed_channels:
        resp = await process_message_in_openai(edit_info, before.author, current_time, event_type="редактирование")
        await before.reply(resp)

@bot.event
async def on_message_delete(message):
    if message.channel.id in allowed_channels:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        resp = await process_message_in_openai(message.content, message.author, current_time, event_type="удаление")
        await message.channel.send(resp)

# Запуск бота
bot.run(DISCORD_TOKEN)
