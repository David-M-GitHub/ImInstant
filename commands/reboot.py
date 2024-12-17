import os
from colorama import Fore

description = "Reboots the computer."
usage = "reboot"

def run(args):
    """
    Reboots the computer.
    """
    print(f"{Fore.YELLOW}Rebooting...{Fore.RESET}")
    os.system("shutdown /r /t 0" if os.name == 'nt' else "shutdown -r now")

def complete(text):
    """
    Auto-completion for the 'reboot' command.
    """
    return []