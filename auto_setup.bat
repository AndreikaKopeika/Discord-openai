@echo off
echo Starting automatic setup!

REM Устанавливаем Git
echo Installing Git...
powershell -Command "Start-Process 'https://github.com/git-for-windows/git/releases/download/v2.42.0.windows.1/Git-2.42.0-64-bit.exe' -ArgumentList '/VERYSILENT', '/NORESTART' -Wait"

REM Проверяем установку Git
git --version
if %errorlevel% neq 0 (
    echo Error: Git is not installed or not in PATH!
    exit /b %errorlevel%
)

REM Устанавливаем Python
echo Installing Python...
powershell -Command "Start-Process 'https://www.python.org/ftp/python/3.11.5/python-3.11.5-amd64.exe' -ArgumentList '/quiet', 'InstallAllUsers=1', 'PrependPath=1' -Wait"

REM Проверяем установку Python
python --version
if %errorlevel% neq 0 (
    echo Error: Python is not installed or not in PATH!
    exit /b %errorlevel%
)

REM Клонируем репозиторий
git clone https://github.com/AndreikaKopeika/Discord-openai.git
cd Discord-openai

echo Starting setup.bat!
start /wait setup.bat

REM Проверяем успешное завершение setup.bat
if %errorlevel% neq 0 (
    echo Error: setup.bat finished with errors!
    exit /b %errorlevel%
)

echo Setup done! Starting bot...

REM Проверяем, что файл bot.py существует
if not exist bot.py (
    echo Error: bot.py not found!
    exit /b 1
)

REM Запускаем бота
python bot.py
if %errorlevel% neq 0 (
    echo Error: Failed to start bot.py!
    exit /b %errorlevel%
)
