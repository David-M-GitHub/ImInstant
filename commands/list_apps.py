import os
from colorama import Fore

description = "Lists all installed applications on the system using Winget."
usage = "list_apps"

def run(args):
    """
    Lists all installed applications on the system using Winget.
    """
    print(f"{Fore.YELLOW}Fetching list of installed applications...{Fore.RESET}")
    
    if os.system("winget --version") != 0:
        print(f"{Fore.RED}Error: Winget is not installed on your system. Install Winget to use this command.{Fore.RESET}")
        return
    
    os.system("winget list")

def complete(text):
    """
    Auto-completion for the 'list_apps' command.
    """
    return []