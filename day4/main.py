from todo_funcs import *
   
def main():
    print("Welcome to SnOw ToDo ApP")

    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. View Task")
        print("3. Remove Task")
        print("4. Exit\n")
        option = input("Enter an option (1-4): ")

        if option == '1':
            task = input("Enter Task: ")
            add_task(task)
        elif option == '2':
            view_tasks()
        elif option == '3':
            task_index = input("Enter task index: ")
            remove_task(task_index)
        elif option == '4':
            break
        else:
            print("\nChoose a valid Option")

if __name__ == "__main__":
    main()