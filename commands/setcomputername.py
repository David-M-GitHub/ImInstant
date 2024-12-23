import os
from colorama import Fore
from main import messages

description = messages["set_computer_name_description"]
usage = messages["set_computer_name_usage"]

def run(args):
    """
    Sets the computer name to the specified name.
    """
    if len(args) != 1:
        print(f"{Fore.RED}{messages['error_specify_computer_name']}{Fore.RESET}")
        print(f"Usage: {usage}")
        return

    new_name = args[0]
    print(f"{Fore.YELLOW}{messages['attempting_set_computer_name']} '{new_name}'...{Fore.RESET}")

    try:
        result = os.system(f'wmic computersystem where name="%computername%" call rename name="{new_name}"')
        if result == 0:
            print(f"{Fore.GREEN}{messages['success_set_computer_name']} '{new_name}'.{Fore.RESET}")
        else:
            print(f"{Fore.RED}{messages['failed_set_computer_name']}{Fore.RESET}")
    except Exception as e:
        print(f"{Fore.RED}{messages['unexpected_error']}: {e}{Fore.RESET}")

def complete(text):
    """
    Auto-complete for the 'setcomputername' command.
    """
    return []