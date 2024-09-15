@echo off
REM Installing dependencies
echo Installing...
pip install discord.py openai python-dotenv

REM Prompting user for tokens
set /p DISCORD_TOKEN="Discord token: "
set /p OPENAI_API_KEY="OpenAI API key: "

REM Creating .env file
echo Creating .env file...
echo DISCORD_TOKEN=%DISCORD_TOKEN% > .env
echo OPENAI_API_KEY=%OPENAI_API_KEY% >> .env

echo .env file created.
echo Setup complete.

start run.bat
