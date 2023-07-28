import json

def add_task(task):
    try:
        with open('tasks.json', 'r') as file:
            tasks = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        tasks = []
    
    tasks.append(task)

    with open('tasks.json', 'w') as file:
        json.dump(tasks, file)

    print(f'Task added succesfully')

def view_tasks():
    try:
        with open('tasks.json', 'r') as file:
            tasks = json.load(file)
            if tasks:
                for index, task in enumerate(tasks, 1):
                    print(f"{index}. {task}")
            else:
                print("Your to-do list is empty.")

    except FileNotFoundError:
        print("Your to-do list is empty.")

def remove_task(index_num):
    try:
        index_num = int(index_num)
        if index_num <= 0:
            raise ValueError()
        with open('tasks.json', 'r') as file:
            tasks = json.load(file)
        if index_num > len(tasks):
            raise IndexError()
        
        # tasks.pop(index_num - 1)
        del tasks[index_num -1]

        with open('tasks.json', 'w') as file:
            json.dump(tasks, file)
            
        print("Task successfully removed")
    except FileNotFoundError:
        print("Your to-do list is empty.")
    except IndexError:
        print("Invalid Task number")
    except ValueError:
        print("Invalid Task number")