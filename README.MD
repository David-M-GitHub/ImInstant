![ImInstant](./img/github-header-image.png)

Welcome to **ImInstant**, a powerful and intuitive command-line interface for managing and automating tasks. Designed with versatility and ease of use in mind, this project combines modularity, auto-completion, and a stylish interface to enhance your productivity.

---

# ✨ Key Features

- **Modular Commands:** Each command is implemented as a separate Python file, simplifying extension and maintenance.
- **Autocomplete:** Tab-completion for seamless command execution.
- **Interactive Interface:** Modern, colorful, and user-friendly terminal output.
- **Cross-Platform Support:** Built for Windows with expandability for Linux and macOS.
- **Customizable Modules:** Easy to add or modify commands to fit your needs.

---

# 🚀 Getting Started

## Prerequisites

1. **Python 3.8+**
   - Download and install Python from [python.org](https://www.python.org/).
   - Ensure Python is added to your system's PATH.

2. **Git** (optional but recommended)
   - Download and install Git from [git-scm.com](https://git-scm.com/).

## Clone the Repository

```bash
# Clone using Git
git clone https://github.com/your-username/iminstant.git
cd iminstant
```

## Create and Activate Virtual Environment

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment (OS-specific)
# On Windows:
venv\Scripts\activate

# On Linux/macOS:
source venv/bin/activate
```

## Install Dependencies

```bash
# Update PIP
python -m pip install --upgrade pip

# Install Requirements
pip install -r requirements.txt
```

---

# 💻 Usage

## Start the Program

1. Launch the program:
   ```bash
   python main.py
   ```

2. Start typing commands! The following commands are included by default:
   - `help`: Displays a list of available commands.
   - `install <software>`: Installs software via Winget.
   - `exit`: Exits the ImInstant console.
   - `uninstall <software>`: Uninstalls specified software using Winget.
   - `list_apps`: Lists all installed applications on your system.
   - `system_info`: Displays detailed system information.
   - `clear`: Clears the console screen.
   - `update`: Updates all applications to the latest version using Winget.

3. Autocomplete is available using the `TAB` key.

## Example Session

```plaintext
┌───────────────────────────────────────────────────────────┐
│ Welcome to ImInstant Command Line Interface               │
├───────────────────────────────────────────────────────────┤
│ Type 'help' to see available commands.                   │
│ Type 'exit' to leave the console.                        │
└───────────────────────────────────────────────────────────┘

iminstant> help
Available commands:
  install
  help
  exit

iminstant> install firefox
Installing firefox...
firefox has been successfully installed!

iminstant> exit
Exiting ImInstant. Goodbye!
```

---

# 📂 Project Structure

```plaintext
iminstant/
├── commands/
│   ├── __init__.py       # Command folder initializer
│   ├── install.py        # Command: install software
│   ├── help.py           # Command: display all commands
│   ├── exit.py           # Command: exit the console
│   └── ....              #
├── completer.py          # Autocomplete functionality
├── main.py               # Main entry point
├── requirements.txt      # Required dependencies
└── README.md             # Documentation
```

---

# 🔧 Extending ImInstant

## Adding a New Command

1. **Create a New Command File:**
   Add a new `.py` file in the `commands/` directory. The file name becomes the command name.

   Example: `commands/status.py`

2. **Define the `run` Function:**
   Each command file must define a `run(args)` function to process input arguments.

   Example:
   ```python
   from colorama import Fore

   def run(args):
       """
       Example command: Displays system status.
       """
       print(f"{Fore.GREEN}System is running smoothly!")
   ```

3. **Run the Program:**
   Your new command will automatically load and become available.

   ```bash
   python main.py
   ```

---

# 🔜 Planned Features

1. **Dynamic Argument Parsing:** Add support for flags and options, e.g., `install firefox --silent`.
2. **Command Logging:** Maintain a history of executed commands and their output.
3. **Cross-Platform Enhancements:** Extend compatibility to Linux and macOS.
4. **Custom Themes:** Allow users to customize the appearance of the console interface.
5. **Plugin System:** Enable external plugins for greater extensibility.
6. **Integrated Update Checker:** Notify users when new updates are available for ImInstant or installed software.   
7. **Remote Command Execution:** Execute commands on remote systems via SSH.
8. **Task Scheduling:** Schedule commands to run at specific times.
9. **Dependency Management:** Automatically handle software dependencies during installation.
10. **Command Aliases:** Let users define shortcuts for frequently used commands.

---

# 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes with clear messages.
4. Submit a pull request for review.

---

# 📓 License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

# 📧 Contact

For support or questions, please contact:

- Email: david@musa-innovation.com
- GitHub: [David-M-GitHub](https://github.com/David-M-GitHub)

---

Start using **ImInstant** today and take command of your tasks effortlessly!

