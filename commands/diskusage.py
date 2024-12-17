import shutil
from colorama import Fore

description = "Displays disk usage information."
usage = "diskusage"

def run(args):
    """
    Displays disk usage information.
    """
    total, used, free = shutil.disk_usage("/")
    print(f"{Fore.CYAN}Disk Usage Information:{Fore.RESET}")
    used_percentage = (used / total) * 100

    if used_percentage < 50:
        color = Fore.GREEN
    elif used_percentage < 75:
        color = Fore.YELLOW
    else:
        color = Fore.RED

    print(f"Total: {Fore.MAGENTA}{total // (2**30)} GB{Fore.RESET}")
    print(f"Used: {color}{used // (2**30)} GB ({used_percentage:.2f}%){Fore.RESET}")
    print(f"Free: {Fore.BLUE}{free // (2**30)} GB{Fore.RESET}")

def complete(text):
    """
    Auto-completion for the 'diskusage' command.
    """
    return []