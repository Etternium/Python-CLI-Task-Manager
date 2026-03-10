from services.task_service import add_task, mark_complete, delete_task, edit_task
from storage.json_storage import save_tasks, load_tasks
from fastapi import FastAPI, HTTPException

app = FastAPI()
tasks = load_tasks()

@app.get("/tasks")
def get_tasks(completed: bool | None = None):
    
    if completed is None:
        return tasks
    
    return [task for task in tasks if task["complete"] == completed]

@app.get("/task/{index}")
def get_task_by_index(index: int):
    return tasks[index - 1]

@app.post("/tasks")
def create_task(desc: str):
    task = add_task(tasks, desc)
    save_tasks(tasks)
    return task

@app.put("/tasks/{index}/complete")
def complete_task(index: int):
    try:
        task = mark_complete(tasks, index - 1)
        save_tasks(tasks)
        return task
    except IndexError:
        return HTTPException(status_code=404, detail="Task not found")

@app.put("/update")
def update_task(index: int, desc: str):
    try:
        task = edit_task(tasks, index - 1, desc)
        save_tasks(tasks)
        return task
    except IndexError:
        return HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{index}")
def remove_task(index: int):
    try:
        task = delete_task(tasks, index - 1)
        save_tasks(tasks)
        return {"deleted": task}
    except IndexError:
        return HTTPException(status_code=404, detail="Task not found")