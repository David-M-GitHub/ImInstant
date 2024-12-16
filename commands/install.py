import os
from colorama import Fore

description = "Installs the specified software using Winget."
usage = "install <software_name>"

# Dictionary of simple names mapped to Winget IDs
PROGRAMS = {
    # Browsers
    "firefox": "Mozilla.Firefox",
    "chrome": "Google.Chrome",
    "edge": "Microsoft.Edge",
    "opera": "Opera.Opera",
    "brave": "Brave.Brave",

    # Media Players
    "vlc": "VideoLAN.VLC",
    "spotify": "Spotify.Spotify",
    "audacity": "Audacity.Audacity",
    "itunes": "Apple.iTunes",
    "plex": "Plex.Plex",

    # Communication
    "discord": "Discord.Discord",
    "teams": "Microsoft.Teams",
    "zoom": "Zoom.Zoom",
    "skype": "Microsoft.Skype",
    "slack": "SlackTechnologies.Slack",

    # Office Tools
    "notepad++": "Notepad++.Notepad++",
    "libreoffice": "TheDocumentFoundation.LibreOffice",
    "microsoft-office": "Microsoft.Office",
    "onenote": "Microsoft.OneNote",
    "foxit-pdf": "Foxit.FoxitPDFReader",

    # Utilities
    "7zip": "7zip.7zip",
    "winrar": "RARLab.WinRAR",
    "ccleaner": "Piriform.CCleaner",
    "teamviewer": "TeamViewer.TeamViewer",
    "everything": "VoidTools.Everything",

    # Development
    "python": "Python.Python.3",
    "nodejs": "OpenJS.NodeJS",
    "git": "Git.Git",
    "visual-studio-code": "Microsoft.VisualStudioCode",
    "eclipse": "EclipseFoundation.EclipseIDE",

    # Virtualization and Databases
    "docker": "Docker.DockerDesktop",
    "virtualbox": "Oracle.VirtualBox",
    "vmware-workstation": "VMware.WorkstationPlayer",
    "mysql-workbench": "Oracle.MySQLWorkbench",
    "pgadmin": "PostgreSQL.pgAdmin",

    # Gaming
    "steam": "Valve.Steam",
    "epic-games": "EpicGames.EpicGamesLauncher",
    "gog-galaxy": "GOG.Galaxy",
    "origin": "ElectronicArts.Origin",
    "blizzard-battlenet": "Blizzard.BattleNet",

    # Security Tools
    "kaspersky": "Kaspersky.Kaspersky",
    "malwarebytes": "Malwarebytes.Malwarebytes",
    "bitdefender": "Bitdefender.Bitdefender",
    "avast": "Avast.AvastFreeAntivirus",
    "norton": "Norton.Norton360",

    # Graphics and Design
    "gimp": "GIMP.GIMP",
    "blender": "BlenderFoundation.Blender",
    "paint.net": "dotPDNLLC.Paint.NET",
    "adobe-photoshop": "Adobe.Photoshop",
    "inkscape": "Inkscape.Inkscape",

    # File Management
    "dropbox": "Dropbox.Dropbox",
    "google-drive": "Google.GoogleDrive",
    "onedrive": "Microsoft.OneDrive",
    "winmerge": "WinMerge.WinMerge",
    "teracopy": "CodeSector.TeraCopy",

    # Programming IDEs
    "jetbrains-pycharm": "JetBrains.PyCharm",
    "jetbrains-intellij": "JetBrains.IntelliJIDEA.Ultimate",
    "atom": "GitHub.Atom",
    "sublime-text": "SublimeHQ.SublimeText",
    "android-studio": "Google.AndroidStudio",

    # Streaming Services
    "netflix": "Netflix.Netflix",
    "prime-video": "Amazon.PrimeVideo",
    "hulu": "Hulu.Hulu",
    "disney-plus": "Disney.DisneyPlus",
    "twitch": "Twitch.Twitch",

    # Compression Tools
    "winzip": "Corel.WinZip",
    "bandizip": "Bandisoft.Bandizip",
    "peazip": "PeaZip.PeaZip",
    "ashampoo-zip": "Ashampoo.ZipFree",
    "zipgenius": "ZipGenius.ZipGenius",

    # File Transfer
    "filezilla": "FileZilla.Client",
    "cyberduck": "Cyberduck.Cyberduck",
    "winscp": "WinSCP.WinSCP",
    "transmission": "Transmission.Transmission",
    "utorrent": "BitTorrent.uTorrent",

    # Text Editors
    "vim": "Vim.Vim",
    "emacs": "GNU.Emacs",
    "nano": "GNU.Nano",
    "textpad": "Helios.TextPad",
    "gedit": "GNOME.Gedit",

    # System Tools
    "cpuz": "CPUID.CPU-Z",
    "hwinfo": "HWiNFO.HWiNFO",
    "speccy": "Piriform.Speccy",
    "sysinternals": "Microsoft.SysinternalsSuite",
    "powershell": "Microsoft.PowerShell",

    # Cloud Services
    "aws-cli": "Amazon.AWSCLI",
    "azure-cli": "Microsoft.AzureCLI",
    "google-cloud-sdk": "Google.CloudSDK",
    "heroku-cli": "Heroku.HerokuCLI",
    "terraform": "HashiCorp.Terraform",

    # Programming Languages
    "java": "Oracle.JavaRuntimeEnvironment",
    "rust": "Mozilla.Rust",
    "go": "Google.Go",
    "ruby": "RubyInstallerTeam.Ruby",
    "php": "PHP.PHP",

    # Miscellaneous
    "obs-studio": "OBSProject.OBSStudio",
    "camscanner": "INTSIG.CamScanner",
    "lastpass": "LastPass.LastPass",
    "dashlane": "Dashlane.Dashlane",
    "postman": "Postman.Postman",

    # Networking Tools
    "wireshark": "WiresharkFoundation.Wireshark",
    "putty": "SimonTatham.PuTTY",
    "openvpn": "OpenVPNTechnologies.OpenVPN",
    "winsock": "Winsock.Winsock",
    "ngrok": "Ngrok.Ngrok"
}

def run(args):
    """
    Installs software using Winget.
    """
    if not args:
        print(f"{Fore.RED}Error: Please specify the application to install.{Fore.RESET}")
        print(f"Available applications: {', '.join(PROGRAMS.keys())}")
        return
    
    app_name = " ".join(args).lower()
    app_id = PROGRAMS.get(app_name)
    
    if not app_id:
        print(f"{Fore.RED}Error: '{app_name}' is not available in the predefined list.{Fore.RESET}")
        print(f"Available applications: {', '.join(PROGRAMS.keys())}")
        return

    print(f"{Fore.YELLOW}Attempting to install {app_name}...{Fore.RESET}")
    
    # Check if Winget is installed
    if os.system("winget --version") != 0:
        print(f"{Fore.RED}Winget is not installed on your system. Attempting to install Winget...{Fore.RESET}")
        os.system("start ms-windows-store://pdp/?productid=9NBLGGH4NNS1")
        return
    
    # Install the application
    result = os.system(f"winget install --id {app_id} --silent")
    if result == 0:
        print(f"{Fore.GREEN}{app_name.capitalize()} has been successfully installed!{Fore.RESET}")
    else:
        print(f"{Fore.RED}Failed to install {app_name}. Please check your Winget configuration or try manually.{Fore.RESET}")

def complete(text):
    """
    Auto-complete for the 'install' command.
    """
    return [p for p in PROGRAMS.keys() if p.startswith(text)]
