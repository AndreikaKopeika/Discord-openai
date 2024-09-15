@echo off
REM Установка зависимостей
echo Установка зависимостей...
pip install discord.py openai python-dotenv

REM Запрос токенов у пользователя
set /p DISCORD_TOKEN="Введите ваш токен Discord: "
set /p OPENAI_API_KEY="Введите ваш API-ключ OpenAI: "

REM Создание файла .env
echo Создание файла .env...
echo DISCORD_TOKEN=%DISCORD_TOKEN% > .env
echo OPENAI_API_KEY=%OPENAI_API_KEY% >> .env

echo Файл .env создан.
echo Настройка завершена.
pause
