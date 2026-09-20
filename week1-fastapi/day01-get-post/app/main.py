"""Day01 starter: implement GET/POST /todos."""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Week1 Day01 Todo API", version="0.1.0")


class TodoCreate(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    completed: bool = False


class Todo(BaseModel):
    id: int
    title: str
    completed: bool


fake_db: list[Todo] = []
_next_id = 1


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/todos", response_model=list[Todo])
def list_todos() -> list[Todo]:
    """TODO: return fake_db."""
    raise HTTPException(status_code=501, detail="TODO: GET /todos")


@app.post("/todos", response_model=Todo, status_code=201)
def create_todo(payload: TodoCreate) -> Todo:
    """TODO: create Todo with new id, append to fake_db, return it.
    Hint: use global _next_id then increment.
    """
    global _next_id
    raise HTTPException(status_code=501, detail="TODO: POST /todos")
