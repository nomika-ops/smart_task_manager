tasks = []

def show_menu():
    print("\n--- Task Manager ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Mark Completed")
    print("5. Exit")

while True:
    show_menu()
    choice = input("Enter choice: ")

    if choice == '1':
        name = input("Enter task name: ")
        priority = input("Enter priority (High/Medium/Low): ")
        deadline = input("Enter deadline (YYYY-MM-DD): ")

        task = {
            "name": name,
            "priority": priority,
            "deadline": deadline,
            "completed": False
        }

        tasks.append(task)
        print("Task added!")

    elif choice == '2':
        if not tasks:
            print("No tasks available.")
        else:
            priority_order = {"High": 1, "Medium": 2, "Low": 3}
            sorted_tasks = sorted(tasks, key=lambda x: priority_order.get(x["priority"], 4))

            print("\n--- Your Tasks ---")
            for i, task in enumerate(sorted_tasks):
                status = "Done" if task["completed"] else "Pending"
                print(f"{i+1}. {task['name']} | {task['priority']} | {task['deadline']} | {status}")

    elif choice == '3':
        if not tasks:
            print("No tasks to delete.")
        else:
            index = int(input("Enter task number to delete: ")) - 1
            if 0 <= index < len(tasks):
                tasks.pop(index)
                print("Task deleted!")
            else:
                print("Invalid index.")

    elif choice == '4':
        if not tasks:
            print("No tasks available.")
        else:
            index = int(input("Enter task number to mark completed: ")) - 1
            if 0 <= index < len(tasks):
                tasks[index]["completed"] = True
                print("Task marked as completed!")
            else:
                print("Invalid index.")

    elif choice == '5':
        print("Exiting...")
        break

    else:
        print("Invalid choice")