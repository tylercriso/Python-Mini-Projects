
to_do_list = []

def add_task(task):
    to_do_list.append(task)
    print("Task added: " + task)

def view_tasks():
    for i in range(len(to_do_list)):
        print("[" + str(i + 1) + "] " + to_do_list[i])

def mark_task_complete(task_number):
    print("Task removed: " + str(to_do_list[int(task_number) - 1]))
    to_do_list.pop(int(task_number) - 1)

while True:
    user_input = str.lower(input("Enter a command [add / view / complete / q (quit)]: "))

    match user_input:
        case "add":
            task_to_add = input("What task do you want to add?: ")
            add_task(task_to_add)
        case "view":
            view_tasks()
        case "complete":
            view_tasks()
            task_number = input("Which task do you want to complete? Type in the number of the task: ")
            mark_task_complete(task_number)
        case "q":
            print("Program stopping.")
            break

