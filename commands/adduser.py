from colorama import Fore
import subprocess
import platform

description = "Adds a new user to the Windows system."
usage = "useradd <username> [password]"

def run(args):
    if platform.system() != "Windows":
        print(f"{Fore.RED}This command is only supported on Windows.{Fore.RESET}")
        return

    if len(args) < 1:
        print(f"{Fore.RED}Usage: {usage}{Fore.RESET}")
        print(f"Example: useradd <username> [password]")
        return

    username = args[0]
    password = args[1] if len(args) > 1 else ""  # Default password if none is provided

    print(f"{Fore.GREEN}Attempting to add user: {username}{Fore.RESET}")

    # Check if the user already exists
    try:
        command = [
            "powershell",
            "-Command",
            f"Get-LocalUser -Name \"{username}\""
        ]
        subprocess.run(command, check=True, capture_output=True, text=True)
        print(f"{Fore.RED}Error: User '{username}' already exists.{Fore.RESET}")
        return
    except subprocess.CalledProcessError:
        pass  # User does not exist, continue to create

    try:
        # PowerShell command to create a new user
        password_cmd = f"-Password (ConvertTo-SecureString \"{password}\" -AsPlainText -Force)" if password else ""
        command = [
            "powershell",
            "-Command",
            f"New-LocalUser -Name \"{username}\" {password_cmd} -PasswordNeverExpires:$true"
        ]
        subprocess.run(command, check=True, capture_output=True, text=True)
        print(f"{Fore.GREEN}User '{username}' added successfully.{Fore.RESET}")

    except subprocess.CalledProcessError as e:
        print(f"{Fore.RED}Error: {e.stderr.strip()}{Fore.RESET}")
    except Exception as e:
        print(f"{Fore.RED}An unexpected error occurred: {e}{Fore.RESET}")

def complete(text):
    """
    Auto-complete for the 'useradd' command.
    """
    return []
