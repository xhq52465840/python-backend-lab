from fastapi import Depends, FastAPI
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.db import get_db
from app.models import User
from app.routers import todos

app = FastAPI(title="Week2 Todo API (Postgres)", version="0.2.0")
app.include_router(todos.router)


@app.on_event("startup")
def ensure_demo_user() -> None:
    """Ensure demo user id=1 exists so CRUD can run before auth week."""
    from app.db import SessionLocal

    db = SessionLocal()
    try:
        user = db.get(User, 1)
        if user is None:
            # Prefer fixed id=1 for demos
            db.add(User(id=1, email="demo@example.com", password_hash="not-used-yet"))
            db.commit()
    finally:
        db.close()


@app.get("/health")
def health(db: Session = Depends(get_db)) -> dict[str, str]:
    db.execute(text("SELECT 1"))
    return {"status": "ok", "db": "up"}
