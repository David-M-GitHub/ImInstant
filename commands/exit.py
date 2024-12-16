from colorama import Fore

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