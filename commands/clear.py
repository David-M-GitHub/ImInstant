import os

description = "Clears the console screen."
usage = "clear"

def run(args):
    """
    Clears the console screen.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def complete(text):
    """
    Auto-completion for the 'clear' command.
    """
    return []