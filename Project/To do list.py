tasks = []

def display_menu():
    """Display the main menu options."""
    print("\nTo-Do List Application\n")
    print("1. Add a task\n")
    print("2. Remove a task\n")
    print("3. View tasks\n")
    print("4. Exit\n")

def add_task():
    '''Add task in the list '''
    task=input("Enter the task you want to add:\n")
    tasks.append(task)
    print(f"Your task '{tasks}' is added\n")

def view_task():
    '''Viewing list'''
    for i in tasks:
        print(i)


def remove_task():
    '''Remove all task'''
    view_task()
    index=int(input("Input no of task you want to delete"))-1
    if 0< index <=len(tasks):
        task1=tasks.pop(index)
        print(f"The task {task1} is removed")
    else:
        print("Invalid input")
    
def main():
    '''Running the application'''
    while True:
        display_menu()
        choice=input('Which programme you wanna start (1-4)?"\n')

        if choice=="1":
            add_task()
        elif choice=="2":
            remove_task()
        elif choice=="3":
            view_task()
        elif choice=="4":
            print("Bye user <3")
        else:
            print("Euta muji kam pani dhanga sitah garna aaudaina hai?")                    
if __name__ == "__main__":
    main()            


