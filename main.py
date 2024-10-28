import json
import os

TASKS_FILE = "tasks.json"

def load_tasks(json_file=TASKS_FILE):
    try:  # tries to file in read-only mode
        with open(json_file, "r") as file: # using a context manager to ensure the file closed automatically
            try: # tries to parse the JSON on file
                data = json.load(file)
            except json.JSONDecodeError: # if decode error...
                print(f"[ERROR] invalid JSON data in {json_file}")
                exit(1) # terminates giving OS error return code 1
            else: # if successful, shows how many tasks have been loaded
                # NOTE: in the final version of the program, the screen will be cleared immediately and this message won't be visible to the user
                print(f"[OK] loaded {len(data)} task(s) from {json_file}")
                return data # parsed data will be returned to main program in a python data structure
    except FileNotFoundError: # if the file doesn't exist
        print(f"[WARNING] No existing {json_file} found. Will attempt to create a new one.")
    except Exception as e: # if any other problems log them
        print(f"[ERROR] Unexpected error opening {json_file}")

def save_tasks(data, json_file=TASKS_FILE):
    try: # tries to file in write mode
        with open(json_file, "w") as file:
            try:
                json.dump(data, file, indent=4) # provides the data list, file to save and indentation value
            except Exception as e: # any error related to converting the Python data structure to JSON will get here
                print(f"\n[ERROR] JSON encoding error\n{e} {json_file}")
                exit(1) # terminate immediately return error code 1 to the OS 
            else:
                print(f"\n[OK] Saved to \"{json_file}\". Total {len(data)} task(s) on file.") # shows a useful message when saving
    except PermissionError: # if the user has no permissions to write to file...
        print(f"\n[ERROR] No permissions to write to {json_file}")
    except Exception as e: # if anything else goes wrong when attempting to save the file
        print(f"\n[ERROR] Unexpected error saving {json_file}")

def clear_screen():
    # depending on user OS, choice is made to select the right statement to clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')

def exit_program():
    clear_screen()
    show_main_screen()
    print("Thanks for using tasker, exiting...")

def view_tasks(data):
    clear_screen()
    show_main_screen()
    print(f"{len(data)} tasks exist\n") # shows the length of data list
    for index, entry in enumerate(data):
        # displays the adjusted index, the description and (uppercase) status of every task
        print(f"[{index + 1:2}] {entry["description"]:25} - {entry["status"].upper()}")
    print()
    
def add_task(data):
    task_name = ""
    # keeps asking for a task name until user enters something
    while not task_name:
        task_name = input("[NEW TASK]: ").title()
    task_status = input("[STATUS - done/pending]: ").lower()
    # append new task to data list
    data.append({
        "description": task_name,
        # if the user entered anything other than "done", the status "pending" will be used
        "status": task_status if task_status == "done" else "pending"
        })
    save_tasks(data) # saves the data
    input(f"\n\"{task_name}\" has been added to tasks\nENTER to continue...")
    clear_screen()

def edit_task(data):
    view_tasks(data)
    task_number = -1
    # increased the number of task by 1 in relation to list index so it must be accounted for with len(data) + 1
    while task_number not in range(len(data) + 1):
        # try block is needed to ensure problem parsing to int is handled
        try:
            # keeps asking the user for a number until 0 (exit) or a valid number have been chosen
            task_number = int(input("[TASK NUMBER or 0 to main menu] "))
        except ValueError:
            # does not give user feedback as it's not hard to choose between numbers...
            pass
    if task_number: # if the user typed a non-zero positive number
        task_name = input("[NEW TASK NAME or leave blank]: ").title() # convert the task description to title case
        task_status = input("[NEW TASK STATUS - done/pending]: ").lower() # convert the status to lowercase
        data[task_number - 1] = {
            "description": task_name if task_name else data[task_number - 1]["description"], # if the task_name was provided blank use the previous value as assuming the user wants to change the status only
            "status": task_status if task_status == "done" else "pending"
        }
        save_tasks(data) # saves the data list to file
        input(f"\nTask {task_number} has been updated\nENTER to continue...")
        clear_screen()
    else:
        return

def del_task(data):
    view_tasks(data)    
    task_number = -1
    # we have increased the number of task by 1 in relation to list index so it must be accounted for with len(data) + 1
    while task_number not in range(len(data) + 1):
        try:
            task_number = int(input("[TASK NUMBER or 0 to main menu] "))
        except ValueError:
            # does not give user feedback as it's not hard to choose between numbers...
            pass
    if task_number:
        # index presented by the user is increased by one so we must adjust to reflect the true index of the element in the list
        data.pop(task_number - 1)
        save_tasks(data) # saves the data
        input(f"\nTask {task_number} has been deleted\nENTER to continue...")
        clear_screen()
    else:
        return

def show_main_screen(options=()):
    # make sure your window is wide enough for the ASCII art to display properly
    print('''
░▒▓████████▓▒░░▒▓██████▓▒░  ░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓████████▓▒░░▒▓███████▓▒░          ░▒▓█▓▒░        ░▒▓████████▓▒░ 
   ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░       ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░       ░▒▓█▓▒░░▒▓█▓▒░      ░▒▓████▓▒░        ░▒▓█▓▒░░▒▓█▓▒░ 
   ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░       ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░       ░▒▓█▓▒░░▒▓█▓▒░         ░▒▓█▓▒░        ░▒▓█▓▒░░▒▓█▓▒░ 
   ░▒▓█▓▒░   ░▒▓████████▓▒░ ░▒▓██████▓▒░ ░▒▓███████▓▒░ ░▒▓██████▓▒░  ░▒▓███████▓▒░          ░▒▓█▓▒░        ░▒▓█▓▒░░▒▓█▓▒░ 
   ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░       ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░       ░▒▓█▓▒░░▒▓█▓▒░         ░▒▓█▓▒░        ░▒▓█▓▒░░▒▓█▓▒░ 
   ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░       ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░       ░▒▓█▓▒░░▒▓█▓▒░         ░▒▓█▓▒░░▒▓██▓▒░░▒▓█▓▒░░▒▓█▓▒░ 
   ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░░▒▓███████▓▒░ ░▒▓█▓▒░░▒▓█▓▒░░▒▓████████▓▒░░▒▓█▓▒░░▒▓█▓▒░         ░▒▓█▓▒░░▒▓██▓▒░░▒▓████████▓▒░
    ''')
        
    if options:
        # if an empty tuple has been passed it's probably a filler so ignore it
        for option in [o for o in options if o != ()]:
            # show the option number and description to the user
            print(f"[{option[0]}] {option[1]} ")

def get_user_choice(options):
    # initializes the command variable with a negative value so program flow goes inside while loop at least once        
    choice = -1
    # keeps refreshing the screen and asking for a number until a valid choice is made
    # if an empty tuple has been passed it's probably a filler so ignore it
    while choice not in [option[0] for option in options if option != ()]:
        clear_screen()
        show_main_screen(options)
        try:
            choice = int(input("Enter a command: "))
        except ValueError: # is parsing of user command to int is not successful...
            # does not give user feedback as it's not hard to choose between 4 numbers but exception must be caught so program doesn't crash
            pass
    return choice

def main(data):
    choices = () # variable needs to be initialized once
    # if there are no tasks, limit the command choices available to the user making add task or exit the only possible choices if there's no data
    while True: # run indefinitely
        if data: # the data list will evaluate to false if it's empty
            choices = (
                # create nested tuple for each possible user command - (command, description and which function to call)
                (), # first tuple is empty so that option number matches its position in the nested tuple
                (1, "View existing tasks", view_tasks),
                (2, "Add a new task", add_task),
                (3, "Edit existing task", edit_task),
                (4, "Delete existing task\n", del_task),
                (0, "Exit\n", exit_program)
            )
        else:
            choices = (
                (), # first tuple is empty so that option number matches its position in the nested tuple
                (), (2, "Add a new task", add_task), (), (), (0, "Exit\n", exit_program) # several tuples are empty as the options to view, edit and delete (as well as their messages and respective functions) don't make sense if the data list is empty (Nothing to view, edit or delete at that moment in time)
            )
        clear_screen()
        show_main_screen(choices)
        
        # choice number has already been validated in "get_user_choice" so if the user gets here, things are working
        match get_user_choice(choices):
            case 1:
                choices[1][2](data) # calls view_tasks()
                input("\nENTER to continue...")
                clear_screen()
            case 2: 
                choices[2][2](data) # calls add_task() (stored in the choices tuple) and passes data
            case 3:
                choices[3][2](data) # calls edit_task() (stored in the choices tuple) and passes data
            case 4:
                choices[4][2](data) # calls del_task() (stored in the choices tuple) and passes data
            case 0:
                choices[-1][2]()
                exit() # calls exit_program which is always the last tuple element
        
# loads only a standalone python program, won't run if called as an external library
if __name__  == ("__main__"):
    # calls load tasks and passes the return data list to the main function
    main(load_tasks())
    