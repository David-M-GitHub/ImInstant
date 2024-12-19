import os
from colorama import Fore

description = "Updates all applications and Windows using Winget and Windows Update."
usage = "updateall"

def run(args):
    """
    Updates all applications and Windows using Winget and Windows Update.
    """
    print(f"{Fore.YELLOW}Updating all applications and Windows...{Fore.RESET}")
    
    # Check if Winget is installed
    if os.system("winget --version") != 0:
        print(f"{Fore.RED}Error: Winget is not installed on your system. Install Winget to use this command.{Fore.RESET}")
        return
    
    # Update all applications using Winget
    os.system("winget upgrade --all --silent")
    
    # Update Windows using Windows Update
    print(f"{Fore.YELLOW}Checking for Windows updates...{Fore.RESET}")
    os.system("powershell -Command \"Install-Module PSWindowsUpdate -Force -SkipPublisherCheck\"")
    os.system("powershell -Command \"Get-WindowsUpdate -Install -AcceptAll -AutoReboot\"")

def complete(text):
    """
    Auto-completion for the 'updateall' command.
    """
    return []