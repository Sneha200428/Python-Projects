import json
from datetime import datetime

def save_expenses():
    with open("expenses.json","w") as file:
        json.dump(expenses, file)

def load_expenses():
    try:
        with open("expenses.json","r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def add_expense():
    while True:
        description = input("Description: ").strip()
        if description == "":
            print("Description cannot be empty")
            continue
        break
    while True:
        try:
            amount = float(input("Amount: "))
            if amount <= 0:
                print("Amount must be greater than zero")
                continue
            break
        except ValueError:
            print("Please enter valid number")
            continue
    while True:
        category = input("Category: ").strip()
        if category == "":
            print("Category cannot be empty.")
            continue
        break
    while True:
        try :
            date = input("Date: ").strip()
            if date == "":
                print("Please enter a valid date in DD-MM-YYYY format")
                continue
            datetime.strptime(date, "%d-%m-%Y")
            break
        except ValueError:
            print("Please enter a valid date in DD-MM-YYYY format")
            continue

    expense = {
        "Description" : description,
        "Amount" : amount,
        "Category" : category,
        "Date" : date
    }

    expenses.append(expense)
    save_expenses()
    print("Expense added successfully!")

def view_expense():
    if not expenses:
        print("No expense found")
        return
    count = 1
    for exp in expenses:
        print(f"\nExpense {count}")
        for key, value in exp.items():
            print(f"{key}: {value}")
        count += 1

def edit_expense():
    if not expenses:
        print("No expense found")
        return
    for index, exp in enumerate(expenses, start=1):
        print(f"{index}. {exp['Description']} - ₹{exp['Amount']}") 
    while True:   
        try:
            choice = int(input("Enter expense number to edit: "))
            if choice < 1 or choice > len(expenses):
                print("Invalid expense number.")
                continue
            break
        except ValueError:
            print("Please Enter valid expense number.")
            continue
    print(expenses[choice - 1]["Description"])
    print("1. Description")
    print("2. Amount")
    print("3. Category")
    print("4. Date")
    while True:
        field_choice = input("What do you want to edit? ")
        if field_choice == "1":
            while True:
                new_description = input("Enter new description: ").strip()
                if new_description == "":
                    print("Description cannot be empty.")
                    continue
                expenses[choice - 1]["Description"] = new_description
                break
            break
        elif field_choice == "2":
            while True:
                try:
                    new_amount = float(input("Enter new amount: "))
                    if new_amount <= 0:
                        print("Amount must be greater than zero.")
                        continue
                    expenses[choice - 1]["Amount"] = new_amount
                    break
                except ValueError:
                    print("Please enter a valid number.")
                    continue
            break
        elif field_choice == "3":
            while True:
                new_category = input("Enter new category: ").strip()
                if new_category == "":
                    print("Category cannot be empty.")
                    continue
                expenses[choice - 1]["Category"] = new_category
                break
            break
        elif field_choice == "4":
            while True:
                try:
                    new_date = input("Enter new date: ").strip()
                    if new_date == "":
                        print("Date Cannot be empty.")
                        continue
                    datetime.strptime(new_date, "%d-%m-%Y")
                    expenses[choice - 1]["Date"] = new_date
                    break
                except ValueError:
                    print("Please enter a valid date in DD-MM-YYYY format.")
                    continue
            break
        else:
            print("Invalid choice")
            continue
    save_expenses()
    print("Expense updated successfully!")

def delete_expense():
    if not expenses:
        print("No expense found")
        return
    for index, exp in enumerate(expenses, start=1):
        print(f"{index}. {exp['Description']} - ₹{exp['Amount']}")
    try:
        choice = int(input("Enter expense number to delete: "))
    except ValueError:
        print("Please enter valid number")
        return
    if choice < 1 or choice > len(expenses):
        print("Invalid expense number")
        return
    expenses.pop(choice - 1)
    save_expenses()
    print("Expense deleted successfully!")

def search_expense():
    if not expenses:
        print("No expense found")
        return
    search_term = input("What description you want to search: ").strip()
    found = False
    for expense in expenses:
        if search_term.lower() in expense["Description"].lower():
            found = True
            print(f"{expense['Description']} - ₹{expense['Amount']}")
    if not found:
        print("No matching expense found")

def show_total():
    if not expenses:
        print("No expense found")
        return
    total = 0
    for expense in expenses:
        total += expense["Amount"]
    print(f"Total spending: ₹{total:.2f}")

expenses = load_expenses()

def show_menu():
    print("===== EXPENSE TRACKER =====")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Edit expense")
    print("4. Delete expense")
    print("5. Search expenses")
    print("6. Show total spending")
    print("7. Exit")

while True:
    show_menu()
    choice = input("Choose: ")
    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expense()
    elif choice == "3":
        edit_expense()
    elif choice == "4":
        delete_expense()
    elif choice == "5":
        search_expense()
    elif choice == "6":
        show_total()
    elif choice == "7":
        print("------------")
        print("| GoodBye! |")
        print("------------")
        break
    else:
        print("Invalid choice")