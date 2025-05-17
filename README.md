# Telegram Tarot Bot

This is a simple Telegram bot written in Python that simulates Tarot card fortune-telling. It can draw one, three, or five cards randomly from a pre-defined database and provide basic descriptions of the cards in multiple languages (RU, EN, CZ).

The goal of the project was to create a small working application that uses API interaction, database operations, and supports a Telegram bot interface. The code was written in a simple way to keep it understandable for learning purposes.

## Features

- 🔮 Draw 1, 3, or 5 Tarot cards randomly using /draw, /draw3, or /draw5 commands.
- 🌐 Supports three languages: Russian, English, Czech.
- 📦 Uses SQLite to store card data.
- 🔗 FastAPI is used to provide endpoints like /cards, /draw, etc.
- 🧪 Contains basic PyTest tests for the API and DB access.


## How to start
 - python -m venv .venv
.venv\Scripts\activate  # On Windows
 - pip install -r requirements.txt
 - python src/database.py
 - uvicorn src.api:app --reload
 - python src/bot.py
 - Or just use the provided batch file: start.bat

## Notes

The project was made as part of a university assignment.
Code is kept minimal and may lack advanced structure or error handling — the focus was on getting things working.
Tested on Windows 11 with Python 3.11.8


### Author Roman Tyshchenko 
