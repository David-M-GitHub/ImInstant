import os
import subprocess
from colorama import Fore

PROGRAMS = {}

def list_apps():
    """
    Fetches the list of installed applications using 'winget list'.
    Populates the PROGRAMS dictionary with app IDs as keys and their names as values.
    """
    global PROGRAMS
    try:
        # Execute 'winget list' and capture the output
        output = subprocess.check_output("winget list", shell=True, text=True)
        
        # Parse the output to extract program IDs
        for line in output.splitlines()[1:]:  # Skip the header line
            parts = line.split()
            if len(parts) >= 2:
                app_id = parts[0]
                app_name = " ".join(parts[1:])
                PROGRAMS[app_id] = app_name

    except subprocess.CalledProcessError as e:
        print(f"{Fore.RED}Error while fetching installed applications: {e}{Fore.RESET}")

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



def completer(text, state):
    """
    Provides auto-completion for uninstallable applications based on 'winget list'.
    """
    options = [app_id for app_id in PROGRAMS.keys() if app_id.startswith(text)]
    if state < len(options):
        return options[state]
    return None

# Initialize the program list for autocomplete
list_apps()
