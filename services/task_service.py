def add_task(tasks, description):
    task = {
        "description": description,
        "complete": False
    }

    tasks.append(task)
    return task

def mark_complete(tasks, index):
    tasks[index]["complete"] = True
    return tasks[index]

def delete_task(tasks, index):
    return tasks.pop(index)

def edit_task(tasks, index: int, edited: str):
    tasks[index]["description"] = edited
    return tasks[index]