import os

FILE_NAME = "expenses.txt"

def add_expense():
    try:
        date = input("Enter Date (DD-MM-YYYY): ")
        category = input("Enter Category: ")
        amount = float(input("Enter Amount: "))
        description = input("Enter Description: ")

        with open(FILE_NAME, "a") as file:
            file.write(f"{date},{category},{amount},{description}\n")

        print("\nExpense Added Successfully!\n")

    except ValueError:
        print("\nInvalid amount! Please enter a numeric value.\n")


def view_expenses():
    if not os.path.exists(FILE_NAME):
        print("\nNo expense records found.\n")
        return

    with open(FILE_NAME, "r") as file:
        records = file.readlines()

    if not records:
        print("\nNo expense records available.\n")
        return

    print("\n----------- Expense Records -----------")

    for i, record in enumerate(records, start=1):
        data = record.strip().split(",")

        print(f"\nExpense {i}")
        print(f"Date        : {data[0]}")
        print(f"Category    : {data[1]}")
        print(f"Amount      : ₹{data[2]}")
        print(f"Description : {data[3]}")

    print("---------------------------------------\n")

def delete_expense():
    if not os.path.exists(FILE_NAME):
        print("\nNo expense records found.\n")
        return

    with open(FILE_NAME, "r") as file:
        records = file.readlines()

    if not records:
        print("\nNo expense records available.\n")
        return

    print("\nExpense List:")

    for i, record in enumerate(records, start=1):
        data = record.strip().split(",")
        print(f"{i}. {data[0]} | {data[1]} | ₹{data[2]} | {data[3]}")

    try:
        choice = int(input("\nEnter Expense Number to Delete: "))

        if 1 <= choice <= len(records):
            records.pop(choice - 1)

            with open(FILE_NAME, "w") as file:
                file.writelines(records)

            print("\nExpense Deleted Successfully!\n")

        else:
            print("\nInvalid Expense Number!\n")

    except ValueError:
        print("\nPlease enter a valid number.\n")


def total_spending():
    if not os.path.exists(FILE_NAME):
        print("\nNo expense records found.\n")
        return

    total = 0

    with open(FILE_NAME, "r") as file:
        for record in file:
            data = record.strip().split(",")

            try:
                total += float(data[2])
            except:
                pass

    print(f"\nTotal Spending = ₹{total:.2f}\n")

def menu():

    while True:

        print("=======================================")
        print("      PERSONAL EXPENSE TRACKER")
        print("=======================================")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Calculate Total Spending")
        print("5. Exit")

        choice = input("\nEnter Your Choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            delete_expense()

        elif choice == "4":
            total_spending()

        elif choice == "5":
            print("\nThank you for using Expense Tracker!")
            break

        else:
            print("\nInvalid Choice! Please try again.\n")


menu()