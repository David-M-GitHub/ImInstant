import requests
from colorama import Fore

description = "Fetches and displays all contributors from the GitHub project."
usage = "contributors"

GITHUB_API_URL = "https://api.github.com/repos/David-M-GitHub/ImInstant/contributors"

def run(args):
    """
    Fetches and displays all contributors from the GitHub project.
    """
    print(f"{Fore.YELLOW}Thanks to all of you! Contributors:{Fore.RESET}")

    try:
        response = requests.get(GITHUB_API_URL)
        response.raise_for_status()
        contributors = response.json()

        for contributor in contributors:
            print(f"{Fore.GREEN}- {contributor['login']}{Fore.RESET}")

    except requests.RequestException as e:
        print(f"{Fore.RED}Error fetching contributors: {e}{Fore.RESET}")

def complete(text):
    """
    Auto-completion for the 'contributors' command.
    """
    return []