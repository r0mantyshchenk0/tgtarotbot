import telebot
import requests

bot = telebot.TeleBot("8071783434:AAGlJOs7f2r6ix9MTadRr9gHzq8gKTwZdEA")

API_URL = "http://127.0.0.1:8000"

# Язык по умолчанию
user_languages = {}

# Получение одной карты
def get_card():
    return requests.get(f"{API_URL}/draw").json()

# Получение трёх карт
def get_three_cards():
    return requests.get(f"{API_URL}/draw3").json()

# Получение пяти карт
def get_five_cards():
    return requests.get(f"{API_URL}/draw5").json()

# Все карты
def get_all_cards():
    return requests.get(f"{API_URL}/cards").json()

# Обработка команды /start
@bot.message_handler(commands=["start"])
def send_welcome(message):
    user_languages[message.chat.id] = "ru"
    bot.send_message(message.chat.id, "🧙 Привет! Напиши /draw, /draw3 или /cards")

# Установка языка
@bot.message_handler(commands=["lang"])
def set_language(message):
    args = message.text.split()
    if len(args) > 1 and args[1] in ["ru", "en", "cz"]:
        user_languages[message.chat.id] = args[1]
        bot.send_message(message.chat.id, f"Язык установлен: {args[1]}")
    else:
        bot.send_message(message.chat.id, "Использование: /lang ru|en|cz")

def format_card(card, lang):
    name = card.get(f"name_{lang}", "???")
    desc = card.get(f"description_{lang}", "")
    return f"🔮 {name} — {desc}"

@bot.message_handler(commands=["draw"])
def draw_card(message):
    lang = user_languages.get(message.chat.id, "ru")
    card = get_card()
    text = format_card(card, lang)
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["draw3"])
def draw_three(message):
    lang = user_languages.get(message.chat.id, "ru")
    cards = get_three_cards()
    text = "\n\n".join(format_card(card, lang) for card in cards)
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["draw5"])
def draw_five(message):
    lang = user_languages.get(message.chat.id, "ru")
    cards = get_five_cards()
    text = "\n\n".join(format_card(card, lang) for card in cards)
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["cards"])
def show_all_cards(message):
    lang = user_languages.get(message.chat.id, "ru")
    cards = get_all_cards()
    text = "\n\n".join(format_card(card, lang) for card in cards)
    bot.send_message(message.chat.id, text)

bot.polling(none_stop=True)
