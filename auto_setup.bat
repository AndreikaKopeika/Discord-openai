echo Staring automatic setup!
git clone https://github.com/AndreikaKopeika/Discord-openai.git
cd Discord-openai
echo Starting setup.bat!
start /wait setup.bat

REM Добавляем проверку успешного завершения setup.bat
if %errorlevel% neq 0 (
    echo Error: setup.bat finished with errors!
    exit /b %errorlevel%
)

echo Setup done! Starting bot...
python --version

REM Проверяем, установлен ли Python
if %errorlevel% neq 0 (
    echo Error: Python is not installed or not in PATH!
    exit /b %errorlevel%
)

REM Проверяем, что файл bot.py существует
if not exist bot.py (
    echo Error: bot.py not found!
    exit /b 1
)

python bot.py
if %errorlevel% neq 0 (
    echo Error: Failed to start bot.py!
    exit /b %errorlevel%
)
