from commands import __all__ as commands_list
from colorama import Fore, Style
import os
import importlib

description = "Displays a list of available commands with their descriptions and usage."
usage = "help"


def run(args):
    print(f"{Style.BRIGHT}Available Commands:{Style.RESET_ALL}\n")
    
    commands_dir = os.path.join(os.path.dirname(__file__))
    for file in os.listdir(commands_dir):
        if file.endswith(".py") and file != "__init__.py":
            command_name = file[:-3]  # Entferne die .py-Erweiterung
            try:
                module = importlib.import_module(f"commands.{command_name}")
                desc = getattr(module, "description", "No description available.")
                usage = getattr(module, "usage", "No usage information available.")
                print(f"{Fore.CYAN}{command_name}{Style.RESET_ALL}")
                print(f"  {Fore.YELLOW}Description:{Style.RESET_ALL} {desc}")
                print(f"  {Fore.YELLOW}Usage:{Style.RESET_ALL} {usage}\n")
            except Exception as e:
                print(f"{Fore.RED}Error loading command '{command_name}': {e}{Style.RESET_ALL}")

def complete(text):
    """
    Auto-completion for the 'help' command.
    """
    return []