import os

import pytest
from fastapi.testclient import TestClient

# Skip if DB is not up — CI for week2 can be enabled later.
pytestmark = pytest.mark.skipif(
    os.getenv("WEEK2_DB_TESTS") != "1",
    reason="Set WEEK2_DB_TESTS=1 with Postgres running to enable",
)

from app.main import app

client = TestClient(app)


def test_health_db_up():
    r = client.get("/health")
    assert r.status_code == 200
    body = r.json()
    assert body["status"] == "ok"
    assert body["db"] == "up"
