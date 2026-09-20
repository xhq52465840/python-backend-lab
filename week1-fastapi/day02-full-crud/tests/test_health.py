from fastapi.testclient import TestClient
from app.main import app, fake_db

client = TestClient(app)


def setup_function():
    fake_db.clear()


def test_health():
    assert client.get("/health").status_code == 200


def test_create_and_list():
    r = client.post("/todos", json={"title": "a"})
    assert r.status_code == 201
    assert client.get("/todos").json()[0]["title"] == "a"
