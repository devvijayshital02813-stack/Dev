# Basic Student Record Management System

students = []

def add_student():
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    grade = input("Enter student grade: ")
    students.append({"name": name, "age": age, "grade": grade})
    print("Student added successfully!")

def view_students():
    if not students:
        print("No records found.")
    else:
        for i, s in enumerate(students, start=1):
            print(f"{i}. Name: {s['name']}, Age: {s['age']}, Grade: {s['grade']}")

def update_student():
    view_students()
    if students:
        idx = int(input("Enter student number to update: ")) - 1
        if 0 <= idx < len(students):
            students[idx]["name"] = input("Enter new name: ")
            students[idx]["age"] = input("Enter new age: ")
            students[idx]["grade"] = input("Enter new grade: ")
            print("Student updated successfully!")

def delete_student():
    view_students()
    if students:
        idx = int(input("Enter student number to delete: ")) - 1
        if 0 <= idx < len(students):
            removed = students.pop(idx)
            print(f"Deleted {removed['name']} successfully!")

def menu():
    while True:
        print("\n===== Student Record Management System =====")
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
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

menu()
