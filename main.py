from services.task_service import add_task, mark_complete, delete_task, edit_task
from storage.json_storage import save_tasks, load_tasks

tasks = load_tasks()

def get_tasks():
    if not tasks:
        print("No tasks available")
        return

    for i, task in enumerate(tasks):
        print(f"{i + 1}. {task['description']} [{task['complete']}]")

def get_filtered_tasks(completed=None):
    if not tasks:
        print("No tasks available")
        return

    if completed is None:
        filtered_tasks = tasks
    else:
        filtered_tasks = [task for task in tasks if task["complete"] == completed]

    for i, task in enumerate(filtered_tasks):
        print(f"{i + 1}. {task["description"]} [{task["complete"]}]")

while(True):
    print("--------------------------------------")
    print("TASK MANAGER")
    print("--------------------------------------")
    print("1. Add Task")
    print("2. Complete Task")
    print("3. Delete Task")
    print("4. List All Tasks")
    print("5. List Completed Tasks")
    print("6. List Pending Tasks")
    print("7. Edit Task Description")
    print("8. Exit")
    print("--------------------------------------")

    user_input = int(input("Choose an option: "))

    if user_input == 1:
        desc = input("Enter task description: ")
        add_task(tasks, desc)
        save_tasks(tasks)

    elif user_input == 2:
        get_tasks()
        index = int(input("Enter task index: ")) - 1

        try:
            mark_complete(tasks, index)
            save_tasks(tasks)
        except IndexError:
            print("Invalid index")
        except ValueError:
            print("Please enter a valid index")

    elif user_input == 3:
        get_tasks()
        index = int(input("Enter task index: ")) - 1

        try:
            delete_task(tasks, index)
            save_tasks(tasks)
        except IndexError:
            print("Invalid index")
        except ValueError:
            print("Please enter a valid index")

    elif user_input == 4:
        get_filtered_tasks()

    elif user_input == 5:
        get_filtered_tasks(True)

    elif user_input == 6:
        get_filtered_tasks(False)

    elif user_input == 7:
        get_tasks()
        index = int(input("Enter task index: ")) - 1

        try:
            new_desc = input("Enter new description: ")
            edit_task(tasks, index, new_desc)
            save_tasks(tasks)
        except IndexError:
            print("Invalid index")
        except ValueError:
            print("Please enter a valid index")

    elif user_input == 8:
        print("\nExiting program...")
        save_tasks(tasks)
        break

    else:
        print("Invalid input!!")
