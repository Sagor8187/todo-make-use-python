todo = []

while True:
    print("\nMenu")
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Remove task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        task = input("Enter your task you want to add: ")
        todo.append(task)
        print(f"Task '{task}' added ")

    elif choice == "2":
        if not todo:
            print("No tasks available ")
        else:
            print("\nYour Tasks:")
            for index, task in enumerate(todo, start=1):
                print(f"{index}. {task}")

    elif choice == "3":
        if not todo:
            print("No tasks to remove ")
        else:
            for index, task in enumerate(todo, start=1):
                print(f"{index}. {task}")
            num = int(input("Enter task number to remove: "))
            removed = todo.pop(num - 1)
            print(f"Task '{removed}' removed ")

    elif choice == "4":
        print("Exiting program ")
        break

    else:
        print("Invalid choice! Please enter 1-4 ")
