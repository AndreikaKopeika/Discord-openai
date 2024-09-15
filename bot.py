import discord
from discord.ext import commands
import openai
import random
import asyncio
from datetime import datetime
from openaibot import *

# Флаг для отключения бота
ended = False

# Настройка OpenAI

# Создаем объект Intents для отслеживания сообщений и реакций
intents = discord.Intents.default()
intents.message_content = True
intents.messages = True  # Для отслеживания сообщений
intents.reactions = True  # Для отслеживания реакций на сообщения

# Укажите здесь ID каналов, в которых бот может отправлять сообщения
allowed_channels = [1283777756857106533]

# Создаем экземпляр бота с указанием intents
bot = commands.Bot(command_prefix='!', intents=intents)

# Функция для отправки напоминаний об оплате
async def send_payment_reminder():
    while True:
        await asyncio.sleep(60)
        if ended:
            for guild in bot.guilds:
                for channel in guild.text_channels:
                    if channel.id in allowed_channels:
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
        # await channel.send(f'Бот {bot.user} теперь онлайн, но вы забыли заплатить...😒')

# Событие при новом сообщении
@bot.event
async def on_message(message):
    if not ended:
        if message.channel.id in allowed_channels and message.author != bot.user:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            message_content = message.content

            # Отправка сообщения в OpenAI и получение ответа
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
                await message.channel.send("Бот не может говорить так как его замутили!")

# Событие при добавлении реакции
@bot.event
async def on_reaction_add(reaction, user):
    if user == bot.user:
        return  # Игнорируем реакции самого бота

    message = reaction.message
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Если реакция на сообщение бота в разрешенном канале
    if message.channel.id in allowed_channels and message.author == bot.user:
        if str(reaction.emoji) == "👍":
            new_response_text = await process_message_in_openai(message.content, user, current_time, event_type="Понравилось сообщение")
            await message.reply(new_response_text)
        elif str(reaction.emoji) == "👎":
            new_response_text = await process_message_in_openai(message.content, user, current_time, event_type="Не понравилось сообщение")
            await message.reply(new_response_text)
        elif str(reaction.emoji) == "🔄":
            new_response_text = await process_message_in_openai(message.content, user, current_time, event_type="Перегенерация")
            await message.edit(content=new_response_text)

# Событие при редактировании сообщения
@bot.event
async def on_message_edit(before, after):
    if before.author == bot.user:
        return

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    edit_info = f"Было: {before.content}, стало: {after.content}"

    if before.channel.id in allowed_channels:
        resp = await process_message_in_openai(edit_info, before.author, current_time, event_type="Редактирование")
        await before.reply(resp)

# Событие при удалении сообщения
@bot.event
async def on_message_delete(message):
    if message.channel.id in allowed_channels:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        resp = await process_message_in_openai(message.content, message.author, current_time, event_type="Удаление")
        await message.channel.send(resp)

# Запуск бота (замените 'YOUR_DISCORD_TOKEN' на ваш токен)
bot.run('YOUR_DISCORD_TOKEN')
