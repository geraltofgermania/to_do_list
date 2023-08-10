import sys
from colorama import Fore

def home():
    """
    show the current time
    list all the current to do's
    may list completed to do's
    """
    pass

def main():
    print(f"{Fore.BLUE}To Do List\n")

    #reset terminal colors
    print(Fore.RESET)
if __name__ == "__main__":
    main()
