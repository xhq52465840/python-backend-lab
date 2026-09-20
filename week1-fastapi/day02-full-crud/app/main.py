"""Day02 starter: GET/POST done; finish get/update/delete."""

from typing import Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Week1 Day02 Todo API", version="0.2.0")


class TodoCreate(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    completed: bool = False


class TodoUpdate(BaseModel):
    title: Optional[str] = Field(default=None, min_length=1, max_length=200)
    completed: Optional[bool] = None


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
    return fake_db


@app.post("/todos", response_model=Todo, status_code=201)
def create_todo(payload: TodoCreate) -> Todo:
    global _next_id
    todo = Todo(id=_next_id, title=payload.title, completed=payload.completed)
    _next_id += 1
    fake_db.append(todo)
    return todo


@app.get("/todos/{todo_id}", response_model=Todo)
def get_todo(todo_id: int) -> Todo:
    """TODO: find by id or 404."""
    raise HTTPException(status_code=501, detail="TODO: GET /todos/{id}")


@app.put("/todos/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, payload: TodoUpdate) -> Todo:
    """TODO: update fields that are not None; 404 if missing."""
    raise HTTPException(status_code=501, detail="TODO: PUT /todos/{id}")


@app.delete("/todos/{todo_id}", status_code=204)
def delete_todo(todo_id: int) -> None:
    """TODO: remove or 404."""
    raise HTTPException(status_code=501, detail="TODO: DELETE /todos/{id}")
