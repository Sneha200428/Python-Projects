
import json

def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []        

def add_tasks():
    task = input("Enter your task: ")
    tasks.append([task, False])

def view_task():
    if not tasks:
        print("You have not add any task yet.")
    
    for index, t in enumerate(tasks, start=1):
    
        if t[1]:
            print(index, ".", t[0], "✓")
        else:
            print(index, ".", t[0])


def delete_task():
    if not tasks:
        print("You have not add any task yet.")
    
    try:
        delete = int(input("Which task u want to delete: "))
    
        if 1 <= delete <= len(tasks):
            tasks.pop(delete - 1)
        else:
            print("Invalid task number")
    
    except ValueError:
            print("Please enter a number")


def complete_task():
    if not tasks:
        print("You have not add any task yet.")
    try:
        complete = int(input("Which task did you complete: "))
    
        if 1 <= complete <= len(tasks):
            tasks[complete - 1][1] = True
        else:
            print("Invalid task number")
    
    except ValueError:
                print("Please enter a number")


def edit_task():
    try:
        taskNumber = int(input("Which task do you want to edit: "))
        if 1 <= taskNumber <= len(tasks):
            newTask = input("Enter new task: ")
            tasks[taskNumber - 1][0] = newTask
        else:
            print("Invalid task number")
    except ValueError:
        print("Please enter a number")

def incomplete_task():
    if not tasks:
        print("You have not add any task yet.")
        return
    try:
        task_number = int(input("Which task do you want to mark incomplete: "))
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1][1] = False
        else:
            print("Invalid task number")
    except ValueError:
        print("Please enter a number")


def search_task():
    if not tasks:  
        print("You have not add any task yet.")
        return
    
    search = input("What task do you want to search: ")
    search = search.lower()
    found = False
    for task in tasks:
        if search in task[0].lower():
            print(task[0])
            found = True
    if not found:
        print("No matching task found.")


def clear_completed_tasks():
    if not tasks:
        print("You have not add any task yet.")
        return
    
    remainingTask = []
    completed_task_found = False

    for task in tasks:
        if not task[1]:
            remainingTask.append(task)
        else:
            completed_task_found = True

    tasks[:] = remainingTask
    if completed_task_found:
        print("Completed tasks cleared")
    else:
        print("No completed tasks found")


def task_summary():
    total_task = len(tasks)
    completed = 0

    for task in tasks:
        if task[1]:
            completed += 1

    pending_task = total_task - completed
    print("=========== Task Summary ===========")
    print("Total task:", total_task)
    print("Completed task:", completed)
    print("Pending Task:", pending_task)

def clear_all_task():
    if not tasks:
        print("You have not add any task yet.")
        return

    confirm = input("Are you sure you want to delete all tasks? (y/n): ")

    if confirm.lower() == "y":
        tasks.clear()
        print("All tasks cleared.")
    else:
        print("Tasks were not cleared.")

running  = True


tasks = load_tasks()


while running:

    print("===== MY TO-DO LIST =====")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Mark task as completed")
    print("5. Exit")
    print("6. Edit task")
    print("7. Mark task as incomplete")
    print("8. Search task")
    print("9. clear completed task")
    print("10. Task summary")
    print("11. Clear all tasks")

    choice = input("Choose an option: ")

    if choice == "1":
        add_tasks()

    elif choice == "2":
        view_task()

    elif choice == "3":
        delete_task()

    elif choice == "4":
        complete_task()

    elif choice == "5":
        save_tasks()
        print("------------")
        print("| Goodbye! |")
        print("------------")
        running = False
    
    elif choice == "6":
        edit_task()

    elif choice == "7":
        incomplete_task()

    elif choice == "8":
        search_task()

    elif choice == "9":
        clear_completed_tasks()

    elif choice == "10":
        task_summary()

    elif choice == "11":
        clear_all_task()

    else :
        print("Invaild Option")