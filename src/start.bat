@echo off
cd /d "%~dp0"
echo [1/3] Activating virtual environment...
call ..\.venv\Scripts\activate.bat

echo [2/3] Launching FastAPI server...
start cmd /k "uvicorn api:app --reload"

timeout /t 3 > nul

echo [3/3] Launching Telegram bot...
python bot.py

pause
