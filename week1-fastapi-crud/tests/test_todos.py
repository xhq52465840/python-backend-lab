"""Uncomment / expand these as you finish each TODO in app/main.py."""

from fastapi.testclient import TestClient

from app.main import app, fake_db

client = TestClient(app)


def setup_function() -> None:
    fake_db.clear()


def test_list_todos_empty_not_implemented_or_ok():
    """Before you implement: may be 501. After: 200 + []."""
    response = client.get("/todos")
    assert response.status_code in (200, 501)
    if response.status_code == 200:
        assert response.json() == []


# def test_create_and_list():
#     created = client.post("/todos", json={"title": "learn fastapi"})
#     assert created.status_code == 201
#     body = created.json()
#     assert body["title"] == "learn fastapi"
#     assert body["completed"] is False
#     assert "id" in body
#
#     listed = client.get("/todos")
#     assert listed.status_code == 200
#     assert len(listed.json()) == 1
