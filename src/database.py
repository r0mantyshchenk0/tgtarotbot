import sqlite3

# Создаём и подключаемся к БД
conn = sqlite3.connect("tarot.db")
cursor = conn.cursor()

# Создаём таблицу
cursor.execute('''
CREATE TABLE IF NOT EXISTS tarot_cards (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name_ru TEXT,
    name_en TEXT,
    name_cz TEXT,
    description_ru TEXT,
    description_en TEXT,
    description_cz TEXT
)
''')

# Добавим хотя бы 5 карт
cards = [
    ("Шут", "The Fool", "Blázen", "Новая жизнь", "New life", "Nový život"),
    ("Маг", "The Magician", "Mág", "Сила воли", "Willpower", "Síla vůle"),
    ("Императрица", "Empress", "Císařovna", "Изобилие", "Abundance", "Hojnost"),
    ("Смерть", "Death", "Smrt", "Конец и трансформация", "End and change", "Konec a změna"),
    ("Влюблённые", "Lovers", "Zamilovaní", "Отношения", "Relationships", "Vztahy")
]

cursor.executemany('''
INSERT INTO tarot_cards (name_ru, name_en, name_cz, description_ru, description_en, description_cz)
VALUES (?, ?, ?, ?, ?, ?)
''', cards)

conn.commit()
conn.close()
