from fastapi import FastAPI
import sqlite3
import random

app = FastAPI()

def get_cards():
    conn = sqlite3.connect("tarot.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tarot_cards")
    rows = cursor.fetchall()
    conn.close()

    return [{
        "id": row[0],
        "name_ru": row[1],
        "name_en": row[2],
        "name_cz": row[3],
        "description_ru": row[4],
        "description_en": row[5],
        "description_cz": row[6]
    } for row in rows]

@app.get("/cards")
def read_cards():
    return get_cards()

@app.get("/draw")
def draw_card():
    cards = get_cards()
    return random.choice(cards)

@app.get("/draw3")
def draw_three():
    cards = get_cards()
    return random.sample(cards, 3)

@app.get("/draw5")
def draw_five():
    cards = get_cards()
    return random.sample(cards, 5)
