tasks = []

while True:

    print("\nTO DO LIST")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        task = input("Enter Task: ")
        tasks.append(task)

    elif choice == "2":

        for i, task in enumerate(tasks, 1):
            print(i, task)

    elif choice == "3":

        num = int(
            input("Enter Task Number: ")
        )

        if 1 <= num <= len(tasks):
            tasks.pop(num-1)

    elif choice == "4":
        break