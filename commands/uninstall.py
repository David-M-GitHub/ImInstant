import os
import subprocess
from colorama import Fore

description = "Uninstalls a given application using Winget."
usage = "uninstall <app_name>"

PROGRAMS = {}

def run(args):
    """
    Uninstalls a given application using Winget.
    """
    if not args:
        print(f"{Fore.RED}Error: Please specify the application to uninstall.")
        return

    app_name = " ".join(args)
    print(f"{Fore.YELLOW}Attempting to uninstall {app_name}...{Fore.RESET}")
    
    if os.system("winget --version") != 0:
        print(f"{Fore.RED}Error: Winget is not installed on your system. Install Winget to use this command.{Fore.RESET}")
        return

    result = os.system(f"winget uninstall --id \"{app_name}\" --silent")
    if result == 0:
        print(f"{Fore.GREEN}{app_name} has been successfully uninstalled!{Fore.RESET}")
    else:
        print(f"{Fore.RED}Failed to uninstall {app_name}. Please check the application name or try manually.{Fore.RESET}")



# TODO: Implement auto-completion for the 'uninstall' command.