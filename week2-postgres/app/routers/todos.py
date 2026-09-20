"""Week 2: implement these endpoints against Postgres.

Hint for frontend folks:
- Session = short-lived DB handle (request-scoped), like a per-request Prisma client.
- commit() = persist; rollback happens if you raise before commit.
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db import get_db
from app.models import Todo
from app.schemas import TodoCreate, TodoOut, TodoUpdate

router = APIRouter(prefix="/todos", tags=["todos"])

# Temporary: Week 3 will replace this with the logged-in user.
DEMO_USER_ID = 1


@router.get("", response_model=list[TodoOut])
def list_todos(db: Session = Depends(get_db)) -> list[Todo]:
    """TODO: return all todos for DEMO_USER_ID (or all rows for now)."""
    raise HTTPException(status_code=501, detail="Not implemented: GET /todos")


@router.post("", response_model=TodoOut, status_code=status.HTTP_201_CREATED)
def create_todo(payload: TodoCreate, db: Session = Depends(get_db)) -> Todo:
    """TODO: insert Todo(user_id=DEMO_USER_ID, ...), commit, refresh, return."""
    raise HTTPException(status_code=501, detail="Not implemented: POST /todos")


@router.get("/{todo_id}", response_model=TodoOut)
def get_todo(todo_id: int, db: Session = Depends(get_db)) -> Todo:
    """TODO: select by id; 404 if missing."""
    raise HTTPException(status_code=501, detail="Not implemented: GET /todos/{id}")


@router.put("/{todo_id}", response_model=TodoOut)
def update_todo(todo_id: int, payload: TodoUpdate, db: Session = Depends(get_db)) -> Todo:
    """TODO: load row; apply non-None fields; commit; 404 if missing."""
    raise HTTPException(status_code=501, detail="Not implemented: PUT /todos/{id}")


@router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(todo_id: int, db: Session = Depends(get_db)) -> None:
    """TODO: delete row; 404 if missing."""
    raise HTTPException(status_code=501, detail="Not implemented: DELETE /todos/{id}")


# --- helpers you may use (optional) ---

def _get_or_404(db: Session, todo_id: int) -> Todo:
    todo = db.get(Todo, todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo
