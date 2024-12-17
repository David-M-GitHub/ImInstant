import os
from colorama import Fore

description = "Sets the computer name to the specified name."
usage = "setcomputername <new_name>"

def run(args):
    """
    Sets the computer name to the specified name.
    """
    if len(args) != 1:
        print(f"{Fore.RED}Error: Please specify the new computer name.{Fore.RESET}")
        print(f"Usage: {usage}")
        return

    new_name = args[0]
    print(f"{Fore.YELLOW}Attempting to set computer name to '{new_name}'...{Fore.RESET}")

    try:
        result = os.system(f'wmic computersystem where name="%computername%" call rename name="{new_name}"')
        if result == 0:
            print(f"{Fore.GREEN}Successfully set computer name to '{new_name}'.{Fore.RESET}")
        else:
            print(f"{Fore.RED}Failed to set computer name. Please check your permissions.{Fore.RESET}")
    except Exception as e:
        print(f"{Fore.RED}An unexpected error occurred: {e}{Fore.RESET}")

def complete(text):
    """
    Auto-complete for the 'setcomputername' command.
    """
    return []