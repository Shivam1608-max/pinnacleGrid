import os

FILE_NAME = "employees.txt"


class Employee:
    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary

    def to_string(self):
        return f"{self.emp_id},{self.name},{self.department},{self.salary}\n"



def read_records():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as file:
        return file.readlines()


def write_records(records):
    with open(FILE_NAME, "w") as file:
        file.writelines(records)


def append_record(record):
    with open(FILE_NAME, "a") as file:
        file.write(record)


def add_employee():
    try:
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Employee Name: ")
        department = input("Enter Department: ")
        salary = float(input("Enter Salary: "))

        employee = Employee(emp_id, name, department, salary)
        append_record(employee.to_string())

        print("\nEmployee Added Successfully!\n")

    except ValueError:
        print("\nInvalid Salary! Please enter a number.\n")



def view_employees():
    records = read_records()

    if not records:
        print("\nNo Employee Records Found.\n")
        return

    print("\n========== Employee Records ==========")

    for record in records:
        emp = record.strip().split(",")

        print(f"Employee ID : {emp[0]}")
        print(f"Name        : {emp[1]}")
        print(f"Department  : {emp[2]}")
        print(f"Salary      : ₹{emp[3]}")
        print("--------------------------------------")


def search_employee():
    emp_id = input("Enter Employee ID to Search: ")

    records = read_records()

    for record in records:
        emp = record.strip().split(",")

        if emp[0] == emp_id:
            print("\nEmployee Found")
            print(f"Employee ID : {emp[0]}")
            print(f"Name        : {emp[1]}")
            print(f"Department  : {emp[2]}")
            print(f"Salary      : ₹{emp[3]}")
            return

    print("\nEmployee Not Found.\n")



def update_employee():
    emp_id = input("Enter Employee ID to Update: ")

    records = read_records()

    updated = []
    found = False

    for record in records:
        emp = record.strip().split(",")

        if emp[0] == emp_id:

            print("\nEnter New Details")

            name = input("New Name: ")
            department = input("New Department: ")
            salary = input("New Salary: ")

            updated.append(f"{emp_id},{name},{department},{salary}\n")

            found = True

        else:
            updated.append(record)

    write_records(updated)

    if found:
        print("\nEmployee Updated Successfully!\n")
    else:
        print("\nEmployee Not Found.\n")


def delete_employee():
    emp_id = input("Enter Employee ID to Delete: ")

    records = read_records()

    updated = []
    found = False

    for record in records:
        emp = record.strip().split(",")

        if emp[0] == emp_id:
            found = True
        else:
            updated.append(record)

    write_records(updated)

    if found:
        print("\nEmployee Deleted Successfully!\n")
    else:
        print("\nEmployee Not Found.\n")



def menu():

    while True:

        print("\n======================================")
        print("     EMPLOYEE MANAGEMENT SYSTEM")
        print("======================================")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search Employee")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Exit")

        choice = input("\nEnter Your Choice: ")

        if choice == "1":
            add_employee()

        elif choice == "2":
            view_employees()

        elif choice == "3":
            search_employee()

        elif choice == "4":
            update_employee()

        elif choice == "5":
            delete_employee()

        elif choice == "6":
            print("\nThank You for Using Employee Management System!")
            break

        else:
            print("\nInvalid Choice! Please try again.\n")


menu()