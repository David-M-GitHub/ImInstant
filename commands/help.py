from commands import __all__ as commands_list
from colorama import Fore

def run(args):
    """
    Displays a list of all available commands.
    """
    if commands_list:
        print(f"{Fore.CYAN}Available commands:")
        for command in commands_list:
            print(f"  - {command}")
    else:
        print(f"{Fore.RED}No commands available.")
