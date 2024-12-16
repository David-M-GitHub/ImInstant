import os
import subprocess
from colorama import Fore

def is_winget_installed():
    """
    Checks if Winget is installed on the system.
    """
    try:
        subprocess.run(["winget", "--version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        return True
    except FileNotFoundError:
        return False

def install_winget():
    """
    Installs Winget if it is not installed.
    """
    print(f"{Fore.YELLOW}Winget is not installed. Installing Winget...{Fore.RESET}")
    
    # Winget installation process (assumes Windows 10/11)
    try:
        subprocess.run(
            ["powershell", "-Command", "Start-Process ms-settings:appsfeatures"],
            check=True
        )
        print(f"{Fore.CYAN}Please install Winget manually through 'App Installer' in the opened settings.{Fore.RESET}")
    except Exception as e:
        print(f"{Fore.RED}Failed to guide Winget installation: {e}{Fore.RESET}")
        return False
    
    return True

def run(args):
    """
    Installs the specified software using Winget.
    """
    if not args:
        print(f"{Fore.RED}Please specify the software to install.{Fore.RESET}")
        return

    if not is_winget_installed():
        if not install_winget():
            print(f"{Fore.RED}Winget installation failed or was not completed. Aborting.{Fore.RESET}")
            return

    software = " ".join(args)
    print(f"{Fore.CYAN}Installing {software}...{Fore.RESET}")
    
    try:
        subprocess.run(["winget", "install", "-e", "--id", software], check=True)
        print(f"{Fore.GREEN}{software} has been successfully installed!{Fore.RESET}")
    except subprocess.CalledProcessError:
        print(f"{Fore.RED}Failed to install {software}. Please check the software ID or try again.{Fore.RESET}")
