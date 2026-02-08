students = []

def add_student():
    roll = input("Enter roll number: ")
    name = input("Enter name: ")
    marks = input("Enter marks: ")

    student = {
        "roll": roll,
        "name": name,
        "marks": marks
    }
    students.append(student)
    print("Student added successfully.\n")

def view_students():
    if not students:
        print("No student records found.\n")
        return

    for s in students:
        print("Roll:", s["roll"])
        print("Name:", s["name"])
        print("Marks:", s["marks"])
        print("-------------------")

def update_student():
    roll = input("Enter roll number to update: ")
    for s in students:
        if s["roll"] == roll:
            s["marks"] = input("Enter new marks: ")
            print("Student record updated.\n")
            return
    print("Student not found.\n")

def delete_student():
    roll = input("Enter roll number to delete: ")
    for s in students:
        if s["roll"] == roll:
            students.remove(s)
            print("Student deleted.\n")
            return
    print("Student not found.\n")

while True:
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        update_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Program exited.")
        break
    else:
        print("Invalid choice.\n")
