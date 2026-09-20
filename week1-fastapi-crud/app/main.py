"""Week 1 starter: in-memory Todo API.

Follow the TODOs in week1-fastapi-crud/README.md.
"""

from typing import Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Week1 Todo API", version="0.1.0")


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


# --- Your work starts here ---


@app.get("/todos", response_model=list[Todo])
def list_todos() -> list[Todo]:
    """TODO 1: return all todos from fake_db."""
    raise HTTPException(status_code=501, detail="Not implemented: GET /todos")


@app.post("/todos", response_model=Todo, status_code=201)
def create_todo(payload: TodoCreate) -> Todo:
    """TODO 2: append a new Todo with an auto-increment id."""
    global _next_id
    raise HTTPException(status_code=501, detail="Not implemented: POST /todos")


@app.get("/todos/{todo_id}", response_model=Todo)
def get_todo(todo_id: int) -> Todo:
    """TODO 3: find by id or raise 404."""
    raise HTTPException(status_code=501, detail="Not implemented: GET /todos/{id}")


@app.put("/todos/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, payload: TodoUpdate) -> Todo:
    """TODO 4: update fields that are not None; 404 if missing."""
    raise HTTPException(status_code=501, detail="Not implemented: PUT /todos/{id}")


@app.delete("/todos/{todo_id}", status_code=204)
def delete_todo(todo_id: int) -> None:
    """TODO 5: remove from fake_db; 404 if missing."""
    raise HTTPException(status_code=501, detail="Not implemented: DELETE /todos/{id}")
