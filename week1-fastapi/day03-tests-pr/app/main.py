"""Day03: paste your full CRUD here if needed; focus on tests."""

from typing import Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Week1 Day03 Todo API", version="0.3.0")


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
    for t in fake_db:
        if t.id == todo_id:
            return t
    raise HTTPException(status_code=404, detail="Todo not found")


@app.put("/todos/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, payload: TodoUpdate) -> Todo:
    for i, t in enumerate(fake_db):
        if t.id == todo_id:
            data = t.model_dump()
            if payload.title is not None:
                data["title"] = payload.title
            if payload.completed is not None:
                data["completed"] = payload.completed
            updated = Todo(**data)
            fake_db[i] = updated
            return updated
    raise HTTPException(status_code=404, detail="Todo not found")


@app.delete("/todos/{todo_id}", status_code=204)
def delete_todo(todo_id: int) -> None:
    for i, t in enumerate(fake_db):
        if t.id == todo_id:
            fake_db.pop(i)
            return
    raise HTTPException(status_code=404, detail="Todo not found")
