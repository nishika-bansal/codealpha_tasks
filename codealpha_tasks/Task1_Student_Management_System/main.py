students = []

while True:

    print("\nStudent Management System")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        name = input("Enter Name: ")
        roll = input("Enter Roll No: ")
        course = input("Enter Course: ")

        students.append([name, roll, course])

    elif choice == "2":

        for student in students:
            print(student)

    elif choice == "3":
        break

    else:
        print("Invalid Choice")