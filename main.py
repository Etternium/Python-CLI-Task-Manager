from services.task_service import *
from fastapi import FastAPI, HTTPException, Depends

from database import Base, engine, LocalSession
from schemas.task_schema import TaskResponse
from sqlalchemy.orm import Session

Base.metadata.create_all(bind=engine)
app = FastAPI()

def get_db():
    db = LocalSession()

    try:
        yield db
    finally:
        db.close()

@app.get("/tasks", response_model=list[TaskResponse])
def get_tasks(db: Session = Depends(get_db)):
    return get_all_tasks(db)

@app.get("/task/{index}", response_model=TaskResponse)
def get_task_by_index(index: int, db: Session = Depends(get_db)):
    task = get_task_by_id(db, index)

    if not task:
        raise HTTPException(404, "Task not found")
    
    return task

@app.post("/newtask", response_model=TaskResponse)
def create_task(desc: str, db: Session = Depends(get_db)):
    return add_task(db, desc)

@app.put("/tasks/{index}/complete", response_model=TaskResponse)
def complete_task(index: int, db: Session = Depends(get_db)):
    task = mark_complete(db, index)

    if not task:
        raise HTTPException(404, "Task not found")
    
    return task

@app.put("/update", response_model=TaskResponse)
def update_task(index: int, new_desc: str, db: Session = Depends(get_db)):
    task = edit_task(db, index, new_desc)

    if not task:
        raise HTTPException(404, "Task not found")
    
    return task

@app.delete("/tasks/{index}")
def remove_task(index: int, db: Session = Depends(get_db)):
    task = delete_task(db, index)

    if not task:
        raise HTTPException(404, "Task not found")
    
    return {"message": "Task deleted"}