import os
import importlib
import json
from completer import Completer
import requests
import sys
from version import CURRENT_VERSION, UPDATE_URL
from colorama import init, Fore, Style

# Initialize colorama for colored output
init(autoreset=True)

COMMAND_DIR = "commands"
commands = {}
completer = Completer()
LANGUAGE = "en"  # Default language

sys.stdout = open(sys.stdout.fileno(), 'w', encoding='utf-8', buffering=1)

def load_language(language):
    """
    Loads the language file for the specified language.
    """
    try:
        with open(f"locales/{language}.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"{Fore.RED}Error: Language file for '{language}' not found. Falling back to English.{Fore.RESET}")
        with open("locales/en.json", "r", encoding="utf-8") as file:
            return json.load(file)

# Load the selected language
messages = load_language(LANGUAGE)

def check_for_updates():
    """
    Checks if a new version of ImInstant is available.
    """
    print(f"{Fore.YELLOW}{messages['checking_updates']}{Fore.RESET}")
    try:
        response = requests.get(UPDATE_URL, timeout=5)
        if response.status_code == 200:
            latest_version = response.text.strip()
            if latest_version != CURRENT_VERSION:
                print(f"{Fore.GREEN}{messages['new_version_available']}: {latest_version}{Fore.RESET}")
                print(f"{Fore.YELLOW}{messages['current_version']}: {CURRENT_VERSION}.{Fore.RESET}")
                print(f"{Fore.CYAN}{messages['stay_productive']}{Fore.RESET}")
            else:
                print(f"{Fore.GREEN}{messages['using_latest_version']} ({CURRENT_VERSION}).{Fore.RESET}")
        else:
            print(f"{Fore.RED}{messages['failed_check_updates']} {response.status_code}.{Fore.RESET}")
    except requests.RequestException as e:
        print(f"{Fore.RED}{messages['could_not_check_updates']}: {e}{Fore.RESET}")

def load_commands():
    """
    Dynamically loads all commands from the 'commands' folder.
    Registers their autocomplete functions if available.
    """
    global commands
    for filename in os.listdir(COMMAND_DIR):
        if filename.endswith(".py") and filename != "__init__.py":
            command_name = filename[:-3]
            module = importlib.import_module(f"{COMMAND_DIR}.{command_name}")
            commands[command_name] = module

            # Check if the module defines a `complete` function for auto-completion
            if hasattr(module, "complete"):
                completer.register_completer(command_name, module.complete)

def print_welcome_screen():
    """
    Prints the welcome screen with a stylish Unicode design.
    """

    welcome_screen = (
        "\n"
        f"{Fore.CYAN}┌{'─'*50}┐\n"
        f"{Fore.CYAN}│ {Style.BRIGHT}{messages['welcome']}{Style.RESET_ALL} {Fore.CYAN}     │\n"
        f"{Fore.CYAN}├{'─'*50}┤\n"
        f"{Fore.CYAN}│ {Fore.YELLOW}{messages['type_help']}{Style.RESET_ALL} {Fore.CYAN}          │\n"
        f"{Fore.CYAN}│ {Fore.YELLOW}{messages['type_exit']}{Style.RESET_ALL} {Fore.CYAN}               │\n"
        f"{Fore.CYAN}├{'─'*50}┤\n"
        f"{Fore.CYAN}│ {Fore.MAGENTA}{messages['current_version']}: {CURRENT_VERSION}{Style.RESET_ALL} {Fore.CYAN}                         │\n"
        f"{Fore.CYAN}│ {Fore.GREEN}{messages['stay_productive']}{Style.RESET_ALL} {Fore.CYAN}                   │\n"
        f"{Fore.CYAN}└{'─'*50}┘"
    )

    print(welcome_screen)

def main():

    load_commands()

    print_welcome_screen()
    check_for_updates()

    # Register default command completer
    completer.set_default_completer(lambda text: [cmd for cmd in commands.keys() if cmd.startswith(text)])
    completer.enable()

    while True:
        try:
            user_input = input(f"{Fore.GREEN}iminstant> {Style.RESET_ALL}").strip()
        except (KeyboardInterrupt, EOFError):
            print(f"\n{Fore.RED}{messages['goodbye']}{Style.RESET_ALL}")
            break

        if not user_input:
            continue

        run_command(user_input)

def run_command(command, *args):
    """
    Runs a command with the specified arguments.
    """
    parts = command.split()
    commandstart = parts[0]
    args = parts[1:]

    if commandstart in commands:
        try:
            commands[commandstart].run(args)
        except Exception as e:
            print(f"{Fore.RED}Error while executing '{commandstart}': {e}")
    else:
        print(f"{Fore.RED}{messages['unknown_command']}: {commandstart}. {messages['type_help']}{Fore.RESET}")

if __name__ == "__main__":
    main()