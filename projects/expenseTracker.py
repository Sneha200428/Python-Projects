

expenses = []

def add_expense():
    description = input("Description: ").strip()
    if not description:
        print("Description cannot be empty")
        return
    try:
        amount = float(input("Amount: "))
        if amount <= 0:
            print("Amount must be greater than zero")
            return
    except ValueError:
        print("Please enter valid number")
        return
    category = input("Category: ").strip()
    date = input("Date: ").strip()

    expense = {
        "Description" : description,
        "Amount" : amount,
        "Category" : category,
        "Date" : date
    }

    expenses.append(expense)
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
    choice = int(input("Enter expense number to edit: "))
    if choice < 1 or choice > len(expenses):
        print("Invalid expense number.")
        return
    else:
        print(expenses[choice - 1]["Description"])
        print("1. Description")
        print("2. Amount")
        print("3. Category")
        print("4. Date")

        field_choice = input("What do you want to edit? ")
    if field_choice == "1":
        new_description = input("Enter new description: ")
        expenses[choice - 1]["Description"] = new_description
    elif field_choice == "2":
        new_amount = input("Enter new amount: ")
        expenses[choice - 1]["Amount"] = new_amount
    elif field_choice == "3":
        new_category = input("Enter new category: ")
        expenses[choice - 1]["Category"] = new_category
    elif field_choice == "4":
        new_date = input("Enter new date: ")
        expenses[choice - 1]["Date"] = new_date
    else:
        print("Invalid choice")
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
        print("Show total spending")
    elif choice == "7":
        print("------------")
        print("| GoodBye! |")
        print("------------")
        break
    else:
        print("Invalid choice")