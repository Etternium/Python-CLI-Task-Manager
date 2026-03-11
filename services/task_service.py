from models.task_model import Task
from sqlalchemy.orm import Session
from sqlalchemy.sql import func

def add_task(db: Session, desc: str):
    task = Task(description=desc)

    db.add(task)
    db.commit()
    db.refresh(task)

    return task

def get_all_tasks(db: Session, completed: bool = None):
    if completed is None:
        return db.query(Task).all()
    return db.query(Task).filter(Task.complete == completed).all()

def get_task_by_id(db: Session, index: int):
    task = db.query(Task).filter(Task.id == index).first()

    if task:
        return task
    
    return

def mark_complete(db: Session, index: int):
    task = db.query(Task).filter(Task.id == index).first()

    if task:
        task.complete = True
        task.updated_at = func.now()
        db.commit()
        db.refresh(task)
    
    return task

def delete_task(db: Session, index: int):
    task = db.query(Task).filter(Task.id == index).first()

    if task:
        db.delete(task)
        db.commit()
    
    return task

def edit_task(db: Session, index: int, new_desc: str):
    task = db.query(Task).filter(Task.id == index).first()

    if task:
        task.description = new_desc
        task.updated_at = func.now()
        db.commit()

    return task