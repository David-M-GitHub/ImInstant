import os
from colorama import Fore

def run(args):
    """
    Updates all applications using Winget.
    """
    print(f"{Fore.YELLOW}Updating all applications...{Fore.RESET}")
    
    if os.system("winget --version") != 0:
        print(f"{Fore.RED}Error: Winget is not installed on your system. Install Winget to use this command.{Fore.RESET}")
        return
    
    os.system("winget upgrade --all --silent")

def complete(text):
    """
    Auto-completion for the 'updateall' command.
    """
    return []