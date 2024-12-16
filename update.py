import os
from colorama import Fore

def run(args):
    """
    Updates ImInstant by pulling the latest version from the GitHub repository.
    """
    print(f"{Fore.YELLOW}Updating ImInstant...{Fore.RESET}")
    result = os.system("git pull origin main")
    if result == 0:
        print(f"{Fore.GREEN}ImInstant has been successfully updated!{Fore.RESET}")
    else:
        print(f"{Fore.RED}Failed to update ImInstant. Please check your internet connection or repository configuration.{Fore.RESET}")