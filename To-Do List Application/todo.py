# To-Do List Application

def display_tasks(tasks):
    if not tasks:
        print("No tasks in the list.")
    else:
        for index, task in enumerate(tasks):
            print(f"{index + 1}. {task['name']} - {'Completed' if task['completed'] else 'Pending'}")

def add_task(tasks, task_name):
    tasks.append({"name": task_name, "completed": False})
    print(f"Task '{task_name}' added.")

def remove_task(tasks, task_identifier):
    if task_identifier.isdigit():
        index = int(task_identifier) - 1
        if 0 <= index < len(tasks):
            removed_task = tasks.pop(index)
            print(f"Task '{removed_task['name']}' removed.")
        else:
            print("Invalid task number.")
    else:
        for task in tasks:
            if task['name'] == task_identifier:
                tasks.remove(task)
                print(f"Task '{task_identifier}' removed.")
                return
        print("Task not found.")

def mark_task(tasks, task_identifier, status):
    if task_identifier.isdigit():
        index = int(task_identifier) - 1
        if 0 <= index < len(tasks):
            tasks[index]['completed'] = (status.lower() == 'completed')
            print(f"Task '{tasks[index]['name']}' marked as {status}.")
        else:
            print("Invalid task number.")
    else:
        for task in tasks:
            if task['name'] == task_identifier:
                task['completed'] = (status.lower() == 'completed')
                print(f"Task '{task_identifier}' marked as {status}.")
                return
        print("Task not found.")

def main():
    tasks = []
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Mark Task")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            task_name = input("Enter task name: ")
            add_task(tasks, task_name)
        elif choice == '2':
            display_tasks(tasks)
        elif choice == '3':
            task_identifier = input("Enter task name or number to remove: ")
            remove_task(tasks, task_identifier)
        elif choice == '4':
            task_identifier = input("Enter task name or number to mark: ")
            status = input("Enter status (completed/pending): ")
            mark_task(tasks, task_identifier, status)
        elif choice == '5':
            print("Exiting the To-Do List Application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
