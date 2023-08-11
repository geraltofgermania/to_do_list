import sys
from colorama import Fore, Style
import datetime
import calendar

# global variables
to_do = []
completed =[]

def set_complete():
    if to_do:
        while True:
            set_complete = input("Enter the number of the completed To do: ")
            if set_complete.isdigit() and 1 <= int(set_complete) <= len(to_do):
                item_completed = to_do.pop(int(set_complete) - 1)
                completed.append(item_completed)
                print(f"'{item_completed}' has been set as complete!\n")
                break
            else:
                print(f"Unable to recognize {set_complete}, please try again: ")
    else:
        print("There is nothing to set as completed.\n")

def show_completed():
    item_number = 1

    if completed:
        print("Completed To Do's")
        for i in completed:
            if i == completed[-1]:
                print(f"\t{item_number}. {i}\n")
            else:
                print(f"\t{item_number}. {i}")
            item_number += 1
    else:
        print("Nothing to show at the moment!\n")

def display_help():
    print("""
Type 'n' to create a To do
Type 'r' to remove a To do
Type 's' to set complete
Type 'c' to view completed To do's
Type 'h' for help
Type 'q' to exit
        """)

def remove_to_do():
    if to_do:
        while True:
            to_remove = input("Enter the number of the item you wish to remove: ")
            if to_remove.isdigit() and 1 <= int(to_remove) <= len(to_do):
                item_removed = to_do.pop(int(to_remove) - 1)
                print(f"'{item_removed}' has been removed!\n")
                break
            else:
                print(f"Unable to recognize {to_remove}, please try again: ")
    else:
        print("There is nothing to remove.\n")

def create_to_do():
    new_to_do = input("Type your To do: ")
    to_do.append(new_to_do)

def list_to_do():
    item_number = 1

    if to_do:
        print("Pending To Do's")
        for i in to_do:
            if i == to_do[-1]:
                print(f"\t{item_number}. {i}\n")
            else:
                print(f"\t{item_number}. {i}")
            item_number += 1
    else:
        print("Nothing to remember at the moment!\n")

def home():
    """
    show the current time
    list all the current to do's
    may list completed to do's???
    """
    while True:
        list_to_do()
        command = input(">>> ")
        if command == "q":
            break
        elif command == "n":
            create_to_do()
        elif command == "r":
            remove_to_do()
        elif command == 's':
            set_complete()
        elif command == 'c':
            show_completed()
        elif command == "h":
            display_help()
        else:
            print(f"Command {command} not found try again!\n")

def main():
    print(f"{Fore.GREEN}{Style.BRIGHT}To Do List\n")

    # today's date as a string
    date = datetime.datetime
    today = date.today()

    # get individual date members for calendar
    deconstructed_date = str(today).split("-")

    # print this month's calendar
    my_calendar = calendar.TextCalendar()
    text_calendar = my_calendar.formatmonth(int(deconstructed_date[0]), int(deconstructed_date[1]))
    print(text_calendar)

    # print today's date
    print(f"Today's date {today}\n")

    print("Type 'h' for available commands.\n")
    home()

    #reset terminal colors
    print(Fore.RESET)
if __name__ == "__main__":
    main()
