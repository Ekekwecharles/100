def add_task(task):
    with open('tasks.txt', 'a+') as file:
        file.write(task+"\n")
    print(f'Task added succesfully')

def view_tasks():
    try:
        with open('tasks.txt', 'r') as file:
            tasks = file.readlines()
            if tasks:
                for index, tasks in enumerate(tasks, 1):
                    print(f"{index}. {tasks.strip()}")
            elif tasks == "" or tasks == " ":
                print("Your to-do list is empty.")
            else:
                print("Your to-do list is empty.")

    except FileNotFoundError:
        print("Your to-do list is empty.")

def remove_task(index_num):
    try:
        index_num = int(index_num)
        if index_num <= 0:
            raise ValueError()
        with open('tasks.txt', 'r') as file:
            tasks = file.readlines()
        if index_num > len(tasks):
            raise IndexError()
        with open('tasks.txt', 'w') as file:
            for index, tasks in enumerate(tasks, 1):
                if index != index_num:
                    file.write(tasks)
        print("Task successfully removed")
    except FileNotFoundError:
        print("Your to-do list is empty.")
    except IndexError:
        print("Invalid Task number")
    except ValueError:
        print("Invalid Task number")