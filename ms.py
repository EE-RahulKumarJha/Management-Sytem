students = {}  # create an empty dictionary to store student data

def add_student():
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    grade = input("Enter student grade: ")
    students[name] = {"age": age, "grade": grade}  # add the student data to the dictionary

def remove_student():
    name = input("Enter name of student to remove: ")
    if name in students:
        del students[name]  # remove the student data from the dictionary
        print(name, "has been removed from the system.")
    else:
        print(name, "is not in the system.")

def view_students():
    if len(students) == 0:
        print("There are no students in the system.")
    else:
        for name, data in students.items():
            print(name)
            print("\tAge:", data["age"])
            print("\tGrade:", data["grade"])

def main():
    while True:
        print("1. Add student")
        print("2. Remove student")
        print("3. View students")
        print("4. Quit")
        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            add_student()
        elif choice == "2":
            remove_student()
        elif choice == "3":
            view_students()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
