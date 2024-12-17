import os
from colorama import Fore

description = "Shuts down the computer."
usage = "shutdown"

def run(args):
    """
    Shuts down the computer.
    """
    print(f"{Fore.YELLOW}Shutting down...{Fore.RESET}")
    os.system("shutdown /s /t 0" if os.name == 'nt' else "shutdown -h now")

def complete(text):
    """
    Auto-completion for the 'shutdown' command.
    """
    return []