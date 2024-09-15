@echo off
REM Устанавливаем зависимости
echo Установка зависимостей...
pip install discord.py openai python-dotenv

REM Проверяем наличие файла .env
if not exist .env (
    echo Создание файла .env...
    echo DISCORD_TOKEN=ваш_токен_Discord > .env
    echo OPENAI_API_KEY=ваш_API_ключ_OpenAI >> .env
    echo Файл .env создан. Пожалуйста, замените ваши токены в файле .env.
) else (
    echo Файл .env уже существует.
)

echo Настройка завершена.
pause
