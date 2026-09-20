from fastapi.testclient import TestClient
from app.main import app, fake_db

client = TestClient(app)


def setup_function():
    fake_db.clear()


def test_health():
    assert client.get("/health").json()["status"] == "ok"


def test_crud_happy_path():
    created = client.post("/todos", json={"title": "learn"}).json()
    tid = created["id"]
    assert client.get("/todos").status_code == 200
    assert client.get(f"/todos/{tid}").json()["title"] == "learn"
    assert client.put(f"/todos/{tid}", json={"completed": True}).json()["completed"] is True
    assert client.delete(f"/todos/{tid}").status_code == 204


def test_404():
    assert client.get("/todos/999").status_code == 404


# TODO(student): add more edge-case tests (empty title -> 422, etc.)
