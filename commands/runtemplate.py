import os
from colorama import Fore
import commands

description = "Executes templates with pre-defined commands."
usage = "runtemplate <template_name>"

TEMPLATES_FOLDER = "templates"

def run(args):
    if len(args) < 1:
        print(f"{Fore.RED}Usage: {usage}{Fore.RESET}")
        list_templates()
        return

    template_name = args[0]
    template_path = os.path.join(TEMPLATES_FOLDER, f"{template_name}.iit")

    if not os.path.exists(template_path):
        print(f"{Fore.RED}Error: Template '{template_name}' does not exist in {TEMPLATES_FOLDER}.{Fore.RESET}")
        return

    print(f"{Fore.GREEN}Executing template: {template_name}{Fore.RESET}")
    try:
        with open(template_path, "r") as file:
            for line_number, line in enumerate(file, start=1):
                line = line.strip()
                if not line or line.startswith("#"):  # Skip comments and empty lines
                    continue
                print(f"{Fore.YELLOW}Executing command ({line_number}): {line}{Fore.RESET}")
                
                # Execute the command
                command_name = line.split()[0]
                command_args = line.split()[1:]
                command = getattr(commands, command_name, None)
                if command is None:
                    print(f"{Fore.RED}Error: Command '{command_name}' not found.{Fore.RESET}")
                    continue
                command.run(command_args)

        print(f"{Fore.GREEN}Template '{template_name}' executed successfully.{Fore.RESET}")
    except Exception as e:
        print(f"{Fore.RED}An unexpected error occurred: {e}{Fore.RESET}")


def list_templates():
    """
    Lists all available .iit templates in the templates folder.
    """
    if not os.path.exists(TEMPLATES_FOLDER):
        print(f"{Fore.YELLOW}No templates directory found. Create a folder named '{TEMPLATES_FOLDER}' and add .iit files.{Fore.RESET}")
        return

    if not available_templates():
        print(f"{Fore.YELLOW}No templates found in the folder '{TEMPLATES_FOLDER}'.{Fore.RESET}")
    else:
        print(f"{Fore.GREEN}Available templates:{Fore.RESET}")
        for template in available_templates():
            print(f"  - {template}")


# Add a completer for commands and templates
def complete(text):
    """
    Autocomplete for commands and templates.
    """
    return [t for t in available_templates() if t.lower().startswith(text)]


def available_templates():
    """
    Returns a list of all available template names.
    """
    if not os.path.exists(TEMPLATES_FOLDER):
        return []
    return [
        f.replace(".iit", "")
        for f in os.listdir(TEMPLATES_FOLDER)
        if f.endswith(".iit")
    ]