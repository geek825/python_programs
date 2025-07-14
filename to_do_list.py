def display_menu():
    print("\nTo-Do List Menu:")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as done")
    print("4. Exit")

def add_task(tasks):
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks in the list.")
        return
    print("\nTasks:")
    for index, task in enumerate(tasks):
        print(f"{index + 1}. {task}")

def mark_task_done(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        task_number = int(input("Enter task number to mark as done :"))
        if 1<=task_number<=len(tasks):
            completed_task = tasks.pop(task_number - 1)
            print(f"Task '{completed_task}' marked as done.")  
            
    except Exception as e:
        print("Invalid input.") 
def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_task_done(tasks)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()