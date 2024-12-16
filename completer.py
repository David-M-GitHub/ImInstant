import readline

def completer(commands):
    """
    Adds autocomplete functionality for a list of commands.
    """
    def complete(text, state):
        options = [cmd for cmd in commands if cmd.startswith(text)]
        if state < len(options):
            return options[state]
        return None

    readline.parse_and_bind("tab: complete")
    readline.set_completer(complete)
