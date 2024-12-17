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
        return

    username = args[0]
    password = args[1] if len(args) > 1 else ""  # Default password if none is provided

    print(f"{Fore.GREEN}Attempting to add user: {username}{Fore.RESET}")
    command = [
        "powershell",
        "-Command",
        f"Get-LocalUser -Name \"{username}\""
    ]
    try:
        subprocess.run(command, check=True, capture_output=True, text=True)
        print(f"{Fore.RED}Error: User '{username}' already exists.{Fore.RESET}")
        return
    except subprocess.CalledProcessError:
        try:
            # PowerShell command to create a new user
            command = [
                "powershell",
                "-Command",
                f"New-LocalUser -Name \"{username}\" -Password (ConvertTo-SecureString \"{password}\" -AsPlainText -Force) -PasswordNeverExpires:$true"
            ]
            subprocess.run(command, check=True, capture_output=True, text=True)
            print(f"{Fore.GREEN}User '{username}' added successfully.{Fore.RESET}")
        except subprocess.CalledProcessError as e:
            print(f"{Fore.RED}Error: {e.stderr}{Fore.RESET}")
        except Exception as e:
            print(f"{Fore.RED}An unexpected error occurred: {e}{Fore.RESET}")
    
