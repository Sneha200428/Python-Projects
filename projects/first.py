
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

    else :
        print("Invaild Option")