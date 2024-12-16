import os
import importlib
from completer import completer
from colorama import init, Fore, Style

# Initialize colorama for colored output
init(autoreset=True)

COMMAND_DIR = "commands"
commands = {}

def load_commands():
    """
    Dynamically loads all commands from the 'commands' folder.
    """
    global commands
    for filename in os.listdir(COMMAND_DIR):
        if filename.endswith(".py") and filename != "__init__.py":
            command_name = filename[:-3]
            module = importlib.import_module(f"{COMMAND_DIR}.{command_name}")
            commands[command_name] = module

def print_welcome_screen():
    """
    Prints the welcome screen with a stylish Unicode design.
    """
    print(f"{Fore.CYAN}┌{'─'*50}┐")
    print(f"{Fore.CYAN}│ {Style.BRIGHT}Welcome to ImInstant Command Line Interface{Style.RESET_ALL} {Fore.CYAN}│")
    print(f"{Fore.CYAN}├{'─'*50}┤")
    print(f"{Fore.CYAN}│ {Fore.YELLOW}Type 'help' to see available commands.{Style.RESET_ALL} {Fore.CYAN}    │")
    print(f"{Fore.CYAN}│ {Fore.YELLOW}Type 'exit' to leave the console.{Style.RESET_ALL} {Fore.CYAN}         │")
    print(f"{Fore.CYAN}└{'─'*50}┘")

def main():
    load_commands()
    print_welcome_screen()

    # Enable autocomplete for commands
    completer(commands.keys())

    while True:
        try:
            user_input = input(f"{Fore.GREEN}iminstant> {Style.RESET_ALL}").strip()
        except (KeyboardInterrupt, EOFError):
            print(f"\n{Fore.RED}Goodbye!{Style.RESET_ALL}")
            break

        if not user_input:
            continue

        parts = user_input.split()
        command = parts[0]
        args = parts[1:]

        if command in commands:
            try:
                commands[command].run(args)
            except Exception as e:
                print(f"{Fore.RED}Error while executing '{command}': {e}")
        else:
            print(f"{Fore.RED}Unknown command: {command}. Type 'help' to see available commands.")

if __name__ == "__main__":
    main()
