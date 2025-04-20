todo_list=[]
def show_menu():
    print("\nTo-Do List Menu : ")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

while True:
    show_menu()
    choice=input("Enter you choice (1-4): ")

    if choice=='1':
        if not todo_list:
            print("No tasks yet.")
        else:
            print("\nYour tasks : ")
            for i, task in enumerate(todo_list,1):
                print(f"{i}.{task}")

    elif choice == '2':
        task=input("Enter new task : ")
        todo_list.append(task)
        print("task added!")

    elif choice == '3':
        task_no=int(input("Enter task number to delete : "))
        if 0<task_no<=len(todo_list):
            removed=todo_list.pop(task_no-1)
            print(f"Removed :{removed}")
        else:
            print("invalid task number !")

    elif choice == '4':
        print("Thank You for using my To-Do list")
        break

    else:
        print("Invalid choice. Try again!")
