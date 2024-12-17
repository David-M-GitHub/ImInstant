import os
from colorama import Fore

description = "Sets the group of a user to the specified group."
usage = "setgroup <user> <group>"

# List of standard Windows groups
STANDARD_GROUPS = [
    "Administrators",
    "Users",
    "Guests",
    "Power Users",
    "Backup Operators",
    "Remote Desktop Users"
]

def run(args):
    """
    Sets the group of a user.
    """
    if len(args) != 2:
        print(f"{Fore.RED}Error: Please specify both a user and a group.{Fore.RESET}")
        print(f"Usage: {usage}")
        print(f"Available standard groups: {', '.join(STANDARD_GROUPS)}")
        return

    user, group = args
    group_exists = group in STANDARD_GROUPS or os.system(f'net localgroup "{group}" >nul 2>&1') == 0

    if not group_exists:
        print(f"{Fore.RED}Error: Group '{group}' does not exist.{Fore.RESET}")
        print(f"Available standard groups: {', '.join(STANDARD_GROUPS)}")
        return

    print(f"{Fore.YELLOW}Attempting to set group '{group}' for user '{user}'...{Fore.RESET}")
    result = os.system(f'net localgroup "{group}" "{user}" /add')

    if result == 0:
        print(f"{Fore.GREEN}Successfully added '{user}' to group '{group}'.{Fore.RESET}")
    else:
        print(f"{Fore.RED}Failed to add '{user}' to group '{group}'. Please check your permissions.{Fore.RESET}")


def complete(text):
    """
    Auto-complete for the 'setgroup' command.
    """
    # Include both standard groups and dynamically fetched local groups
    local_groups = os.popen("net localgroup").read().strip().split("\n")[4:-2]  # Adjusts for command output format
    all_groups = STANDARD_GROUPS + [g.strip() for g in local_groups]
    return [g for g in all_groups if g.lower().startswith(text.lower())]
