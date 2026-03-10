import os
import json

JSON_FILE = "tasks.json"

def save_tasks(tasks):
    with open(JSON_FILE, "w") as f:
        json.dump(tasks, f)

def load_tasks():
    if os.path.exists(JSON_FILE):
        with open(JSON_FILE, "r") as f:
            return json.load(f)
    return []