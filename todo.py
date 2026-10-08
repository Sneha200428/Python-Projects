
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


def add_task():
    while True:
        task = input("Enter your task: ")
    
        if task.strip():
            tasks.append([task, False])
            break
        print("Task cannot be empty. Please try again.")


def view_task():
    if not tasks:
        print("You have not added any task yet.")
        return
    
    for index, t in enumerate(tasks, start=1):
    
        if t[1]:
            print(index, ".", t[0], "✓")
        else:
            print(index, ".", t[0])


def delete_task():
    if not tasks:
        print("You have not added any task yet.")
        return
    
    try:
        delete = int(input("Which task u want to delete: "))
    
        if 1 <= delete <= len(tasks):
            confirm = input(f'Are you sure you want to delete "{tasks[delete - 1][0]}"? (y/n): ')

            if confirm.lower() == "y":
                tasks.pop(delete - 1)
                print("Task deleted.")
            else:
                print("Task was not deleted.")
        else:
            print("Invalid task number")
    
    except ValueError:
            print("Please enter a number")


def complete_task():
    if not tasks:
        print("You have not added any task yet.")
        return
    try:
        complete = int(input("Which task did you complete: "))
    
        if 1 <= complete <= len(tasks):
            tasks[complete - 1][1] = True
        else:
            print("Invalid task number")
    
    except ValueError:
                print("Please enter a number")


def edit_task():
    if not tasks:
        print("You have not added any task yet.")
        return

    try:
        taskNumber = int(input("Which task do you want to edit: "))
        if 1 <= taskNumber <= len(tasks):
            newTask = input("Enter new task: ")
            if newTask.strip():
                tasks[taskNumber - 1][0] = newTask
            else:
                print("Task cannot be empty.")
        else:
            print("Invalid task number")
    except ValueError:
        print("Please enter a number")


def incomplete_task():
    if not tasks:
        print("You have not added any task yet.")
        return
    try:
        task_number = int(input("Which task do you want to mark as incomplete: "))
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1][1] = False
        else:
            print("Invalid task number")
    except ValueError:
        print("Please enter a number")


def search_task():
    if not tasks:  
        print("You have not added any task yet.")
        return
    
    search = input("What task do you want to search: ").lower()
    found = False
    for task in tasks:
        if search in task[0].lower():
            print(task[0])
            found = True
    if not found:
        print("No matching task found.")


def clear_completed_tasks():
    if not tasks:
        print("You have not added any task yet.")
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
        print("Completed tasks cleared.")
    else:
        print("No completed tasks found.")


def task_summary():
    total_task = len(tasks)
    completedTask = 0

    for task in tasks:
        if task[1]:
            completedTask += 1

    pending_task = total_task - completedTask
    print("=========== Task Summary ===========")
    print("Total task:", total_task)
    print("Completed task:", completedTask)
    print("Pending Task:", pending_task)


def clear_all_tasks():
    if not tasks:
        print("You have not added any task yet.")
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
    print("3. Edit task") #3
    print("4. Delete task") #4
    print("5. Mark task as completed")#5
    print("6. Mark task as incomplete")#6
    print("7. Search task")#7
    print("8. Task summary")#8
    print("9. clear completed tasks")#9
    print("10. Clear all tasks")#10
    print("11. Exit")#11

    choice = input("Choose an option: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_task()

    elif choice == "3":
        edit_task()

    elif choice == "4":
        delete_task()

    elif choice == "5":
        complete_task()
    
    elif choice == "6":
        incomplete_task()

    elif choice == "7":
        search_task()

    elif choice == "8":
        task_summary()

    elif choice == "9":
        clear_completed_tasks()

    elif choice == "10":
        clear_all_tasks()

    elif choice == "11":
        save_tasks()
        print("------------")
        print("| Goodbye! |")
        print("------------")
        running = False

    else :
        print("Invalid Option")