from src import database

def test_read_cards():
    cards = database.read_cards()
    assert isinstance(cards, list)
