# To-Do Tasks List : 




tasks =[]
completed_tasks = ()

# add a task
def add_task():
    """
        add a task to the task list
    """
    task = input("Please enter your new task : ")
    tasks.append(task)
    print(f"{task} ->> added successfully to the task list : ")

# view tasks
def view_task():
    """
        view all tasks
    """

    if not tasks:
        print("There is no any tasks : ")
    else:
        print("<<========= To-Do List =========>>")
        for i, task in enumerate(tasks):
            status = "✔ completed " if tasks in completed_tasks else "pending" 
            print(f"{i+1}. {task} ->> {status}")

# mark task as completed
def task_completed(task_number):
    """
        Mark a task as completed using it's number. 
    """
    if 1 <= task_number <= len(tasks):
        task_item = tasks[task_number-1]
        completed_tasks.add(task_item)
        print(f"Task ->> {task_item} << marked as completed. \n")
    else: 
        print("Invalid Task number : \n")


# Delete a task 
def delete_task(task_number):
    """
        Delete a task from the list using its number.
    """
    if 1 <= task_number <= len(tasks):
        task_item = tasks.pop(task_number-1)
        completed_tasks.discard(task_item)
        print(f"Task >> {task_item} << deleted successfully. \n")
    else: 
        print("Invalid Task number : \n")

while True:
    print(""" >>>>> To-Do List App <<<<<
            1. Add Task
            2. View Task
            3. Mark Task as Completed
            4. Delete task
            5. Exit
""")

    choice = int(input("Enter your choice(1-5) : "))
    if choice == 1:
        add_task()
    elif choice == 2:
        view_task()
    elif choice == 3:
        task_n = int(input("Enter the task number to mark completed : "))
        task_completed(task_n)
    elif choice == 4:
        task_no = int(input("Enter the task number to Delete : "))
        delete_task(task_no)
    elif choice ==5:
        break
    else: 
        print("Invalid choice please try again : ")