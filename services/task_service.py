def add_task(tasks, description):
    tasks.append({
        "description": description,
        "complete": False
    })

def mark_complete(tasks, index):
    tasks[index]["complete"] = True

def delete_task(tasks, index):
    tasks.pop(index)

def edit_task(tasks, index, edited):
    tasks[index]["description"] = edited