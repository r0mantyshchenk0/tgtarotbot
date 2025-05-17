from fastapi.testclient import TestClient
from src.api import app

client = TestClient(app)

def test_cards():
    response = client.get("/cards")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_draw():
    response = client.get("/draw")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

def test_draw3():
    response = client.get("/draw3")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 3

def test_draw5():
    response = client.get("/draw5")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 5
