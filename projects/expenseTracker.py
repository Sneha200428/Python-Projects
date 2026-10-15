

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
        print("Edit expense")
    elif choice == "4":
        print("Delete expense")
    elif choice == "5":
        print("Serach expenses")
    elif choice == "6":
        print("Show total spending")
    elif choice == "7":
        print("------------")
        print("| GoodBye! |")
        print("------------")
        break
    else:
        print("Invalid choice")