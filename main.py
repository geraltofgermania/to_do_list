import sys
from colorama import Fore
import datetime
import calendar

def home():
    """
    show the current time
    list all the current to do's
    may list completed to do's???
    """
    pass

def main():
    print(f"{Fore.GREEN}To Do List\n")

    # today's date as a string
    date = datetime.date
    today = date.today()

    # get individual date members for calendar
    deconstructed_date = str(today).split("-")

    # print this month's calendar
    my_calendar = calendar.TextCalendar()
    text_calendar = my_calendar.formatmonth(int(deconstructed_date[0]), int(deconstructed_date[1]))
    print(text_calendar)

    # print today's date
    print(f"Today's date {date.today()}")

    home()

    #reset terminal colors
    print(Fore.RESET)
if __name__ == "__main__":
    main()
