from colorama import Fore

description = "Exits the ImInstant console."
usage = "exit"

def run(args):
    """
    Exits the ImInstant console.
    """
    print(f"{Fore.YELLOW}Exiting ImInstant. Goodbye!")
    exit(0)

def complete(text):
    """
    Auto-completion for the 'exit' command.
    """
    return []