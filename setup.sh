#!/bin/bash

# Установка зависимостей
echo "Installing..."
pip install discord.py openai python-dotenv

# Запрос токенов у пользователя
read -p "Discord token: " DISCORD_TOKEN
read -p "OpenAI API key: " OPENAI_API_KEY

# Создание файла .env
echo "Creating .env file..."
echo "DISCORD_TOKEN=${DISCORD_TOKEN}" > .env
echo "OPENAI_API_KEY=${OPENAI_API_KEY}" >> .env

echo ".env file created."
echo "Setup complete."

# Запуск другого скрипта (замените run.sh на имя вашего скрипта)
./run.sh
