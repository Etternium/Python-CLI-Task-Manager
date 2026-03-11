from models.task_model import Task
from sqlalchemy.orm import Session

def add_task(db: Session, desc: str):
    task = Task(description=desc)

    db.add(task)
    db.commit()
    db.refresh(task)

    return task

def get_all_tasks(db: Session):
    return db.query(Task).all()

def get_task_by_id(db: Session, index: int):
    task = db.query(Task).filter(Task.id == index).first()

    if task:
        return task
    
    return

def mark_complete(db: Session, index: int):
    task = db.query(Task).filter(Task.id == index).first()

    if task:
        task.complete = True
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
        db.commit()

    return task

# def add_task(tasks, description):
#     task = {
#         "description": description,
#         "complete": False
#     }

#     tasks.append(task)
#     return task

# def mark_complete(tasks, index):
#     tasks[index]["complete"] = True
#     return tasks[index]

# def delete_task(tasks, index):
#     return tasks.pop(index)

# def edit_task(tasks, index: int, edited: str):
#     tasks[index]["description"] = edited
#     return tasks[index]