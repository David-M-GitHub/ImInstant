# ImInstant Command Line Interface

Welcome to **ImInstant**, a versatile and user-friendly command-line interface for managing and automating tasks on Windows systems. This project supports a modular command structure, autocomplete functionality, and colorful, intuitive output.

---

## 🌟 Features

- **Modular Commands:** Each command is stored as a separate Python file, making it easy to extend functionality.
- **Autocomplete:** Tab-completion for all available commands.
- **Stylish Interface:** Colorful output and a sleek welcome screen using Unicode.
- **Cross-Platform Compatibility:** Designed for Windows but expandable for other systems.

---

## 🚀 Getting Started

### Prerequisites

1. **Python 3.8+**
   - Download and install Python from [python.org](https://www.python.org/).
   - Ensure Python is added to your system's PATH.

2. **Git** (optional but recommended)
   - Download and install Git from [git-scm.com](https://git-scm.com/).

### Clone the Repository

```bash
# Clone using Git
git clone https://github.com/your-username/iminstant.git
cd iminstant
```

### Create and Activate Virtual Environment

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment (OS-specific)
# On Windows:
venv\Scripts\activate

# On Linux/macOS:
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 💻 Usage

### Start the Program

1. Launch the program:
   ```bash
   python main.py
   ```

2. Start typing commands! The following commands are included by default:
   - `help`: Displays a list of available commands.
   - `install <software>`: Installs software via Winget.
   - `exit`: Exits the ImInstant console.

3. Autocomplete is available using the `TAB` key.

### Example Session

```plaintext
┌──────────────────────────────────────────────────┐
│ Welcome to ImInstant Command Line Interface      │
├──────────────────────────────────────────────────┤
│ Type 'help' to see available commands.           │
│ Type 'exit' to leave the console.                │
└──────────────────────────────────────────────────┘

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

## 📂 Project Structure

```plaintext
iminstant/
├── commands/
│   ├── __init__.py       # Command folder initializer
│   ├── install.py        # Example command: install software
│   ├── help.py           # Displays all available commands
│   ├── exit.py           # Exits the console
├── completer.py          # Autocomplete functionality
├── main.py               # Main entry point for the application
├── requirements.txt      # Required dependencies
├── README.md             # Documentation for the project
```

---

## 🔧 Extending ImInstant

### Adding a New Command

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

## 📅 Planned Features

1. **Dynamic Argument Parsing:** Add support for flags and options, e.g., `install firefox --silent`.
2. **Command Logging:** Maintain a history of executed commands and their output.
3. **Cross-Platform Enhancements:** Extend compatibility to Linux and macOS.
4. **Custom Themes:** Allow users to customize the appearance of the console interface.
5. **Plugin System:** Enable external plugins for greater extensibility.

---

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes with clear messages.
4. Submit a pull request for review.

---

## 📜 License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## 📧 Contact

For support or questions, please contact:

- Email: david@musa-innovation.com
- GitHub: [David-M-GitHub](https://github.com/David-M-GitHub)

---

Start using **ImInstant** today and simplify your command-line tasks effortlessly!

