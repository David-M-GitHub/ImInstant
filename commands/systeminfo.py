import platform
import os
from colorama import Fore

def run(args):
    """
    Displays system information.
    """
    print(f"{Fore.CYAN}System Information:{Fore.RESET}")
    print(f"Operating System: {platform.system()} {platform.release()}")
    print(f"Version: {platform.version()}")
    print(f"Processor: {platform.processor()}")
    print(f"Architecture: {' '.join(platform.architecture())}")
    print(f"Machine: {platform.machine()}")
    
    if platform.system() == "Windows":
        os.system("systeminfo | findstr /B /C:\"OS\" /C:\"System\"")

def complete(text):
    """
    Auto-completion for the 'systeminfo' command.
    """
    return []