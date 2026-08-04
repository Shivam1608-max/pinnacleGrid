
students = []

def add_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    course = input("Enter Course: ")
    marks = input("Enter Marks: ")

    student = {
        "ID": student_id,
        "Name": name,
        "Course": course,
        "Marks": marks
    }

    students.append(student)
    print("\nStudent Added Successfully!\n")


def view_students():
    if len(students) == 0:
        print("\nNo student records found.\n")
        return

    print("\n----- Student Records -----")
    for student in students:
        print(f"ID     : {student['ID']}")
        print(f"Name   : {student['Name']}")
        print(f"Course : {student['Course']}")
        print(f"Marks  : {student['Marks']}")
        print("-" * 30)


def update_student():
    student_id = input("Enter Student ID to Update: ")

    for student in students:
        if student["ID"] == student_id:
            print("\nEnter New Details")
            student["Name"] = input("Enter New Name: ")
            student["Course"] = input("Enter New Course: ")
            student["Marks"] = input("Enter New Marks: ")

            print("\nStudent Updated Successfully!\n")
            return

    print("\nStudent ID Not Found!\n")


def delete_student():
    student_id = input("Enter Student ID to Delete: ")

    for student in students:
        if student["ID"] == student_id:
            students.remove(student)
            print("\nStudent Deleted Successfully!\n")
            return

    print("\nStudent ID Not Found!\n")

def menu():
    while True:
        print("===================================")
        print("     STUDENT MANAGEMENT SYSTEM")
        print("===================================")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            update_student()

        elif choice == "4":
            delete_student()

        elif choice == "5":
            print("\nThank you for using Student Management System!")
            break

        else:
            print("\nInvalid Choice! Please try again.\n")


menu()