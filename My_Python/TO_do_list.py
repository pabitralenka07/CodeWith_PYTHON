tasks = []

while True:
    print("\n--- TO-DO LIST ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == '1':
        task = input("Enter task: ")
        tasks.append({"task": task, "done": False})
        print("Task added!")

    elif choice == '2':
        if not tasks:
            print("No tasks found.")
        else:
            for i, t in enumerate(tasks, 1):
                status = "✓" if t["done"] else "✗"
                print(f"{i}. [{status}] {t['task']}")

    elif choice == '3':
        num = int(input("Enter task number: "))

        if 1 <= num <= len(tasks):
            tasks[num - 1]["done"] = True
            print("Task marked as completed!")
        else:
            print("Invalid task number.")

    elif choice == '4':
        print("Goodbye!")
        break

    else:
        print("Invalid option.")
        
        