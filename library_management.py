def add_student():
    roll = input("Enter Roll Number: ")
    with open("students.txt", "a+") as file:
        file.seek(0)
        for line in file:
            data = line.strip().split(",")
            if data[0] == roll:
                print("Student already exists")
                return
        name = input("Enter Student Name: ")
        age = input("Enter Age: ")
        course = input("Enter Course: ")
        marks = input("Enter Marks: ")
        file.seek(0, 2)
        file.write(f"{roll},{name},{age},{course},{marks}\n")
    print("Student added successfully")
def view_students():
    try:
        with open("students.txt", "r") as file:
            students = file.readlines()
            if len(students) == 0:
                print("No student records found")
            else:
                for student in students:
                    data = student.strip().split(",")
                    print("\nRoll Number:", data[0])
                    print("Name:", data[1])
                    print("Age:", data[2])
                    print("Course:", data[3])
                    print("Marks:", data[4])
    except FileNotFoundError:
        print("No student records found")
def search_student():
    roll = input("Enter Roll Number to Search: ")
    try:
        with open("students.txt", "r") as file:
            for line in file:
                data = line.strip().split(",")
                if data[0] == roll:
                    print("\nStudent Found")
                    print("Roll Number:", data[0])
                    print("Name:", data[1])
                    print("Age:", data[2])
                    print("Course:", data[3])
                    print("Marks:", data[4])
                    return
        print("Student not found")
    except FileNotFoundError:
        print("No student records found")
def update_student():
    roll = input("Enter Roll Number to Update: ")
    try:
        with open("students.txt", "r") as file:
            students = file.readlines()
        found = False
        with open("students.txt", "w") as file:
            for student in students:
                data = student.strip().split(",")

                if data[0] == roll:
                    print("Enter New Details")

                    name = input("Enter Name: ")
                    age = input("Enter Age: ")
                    course = input("Enter Course: ")
                    marks = input("Enter Marks: ")

                    file.write(
                        f"{roll},{name},{age},{course},{marks}\n"
                    )

                    found = True
                else:
                    file.write(student)

        if found:
            print("Student updated successfully")
        else:
            print("Student not found")

    except FileNotFoundError:
        print("No student records found")


def delete_student():
    roll = input("Enter Roll Number to Delete: ")

    try:
        with open("students.txt", "r") as file:
            students = file.readlines()

        found = False

        with open("students.txt", "w") as file:
            for student in students:
                data = student.strip().split(",")

                if data[0] == roll:
                    found = True
                else:
                    file.write(student)

        if found:
            print("Student deleted successfully")
        else:
            print("Student not found")

    except FileNotFoundError:
        print("No student records found")


while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("Program closed")
        break

    else:
        print("Invalid choice")