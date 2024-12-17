from colorama import Fore
import requests
from version import CURRENT_VERSION, UPDATE_URL

description = "Displays the current version of ImInstant and checks for updates."
usage = "version"

def run(args):
    """
    Displays the current version of ImInstant and checks for updates.
    """
    print(f"{Fore.CYAN}Current Version: {CURRENT_VERSION}{Fore.RESET}")
    
    try:
        response = requests.get(UPDATE_URL, timeout=5)
        if response.status_code == 200:
            latest_version = response.text.strip()
            if latest_version != CURRENT_VERSION:
                print(f"{Fore.GREEN}A new version of ImInstant is available: {latest_version}{Fore.RESET}")
                print(f"{Fore.YELLOW}You are currently using version {CURRENT_VERSION}.{Fore.RESET}")
                print(f"{Fore.CYAN}Please update ImInstant to enjoy the latest features and improvements.{Fore.RESET}")
            else:
                print(f"{Fore.GREEN}You are using the latest version of ImInstant ({CURRENT_VERSION}).{Fore.RESET}")
        else:
            print(f"{Fore.RED}Failed to check for updates. Server returned status code {response.status_code}.{Fore.RESET}")
    except requests.RequestException as e:
        print(f"{Fore.RED}Could not check for updates: {e}{Fore.RESET}")

def complete(text):
    """
    Auto-completion for the 'version' command.
    """
    return []