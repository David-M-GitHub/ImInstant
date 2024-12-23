import os
from colorama import Fore

description = "Sets various Windows settings."
usage = "setsettings <setting> <value>"

# List of supported settings with descriptions
SUPPORTED_SETTINGS = {
    "wallpaper": {
        "command": "Set-ItemProperty -Path 'HKCU:\\Control Panel\\Desktop' -Name Wallpaper -Value",
        "description": "Sets the desktop wallpaper.",
        "usage": "setsettings wallpaper <path_to_image>"
    },
    "screensaver": {
        "command": "Set-ItemProperty -Path 'HKCU:\\Control Panel\\Desktop' -Name SCRNSAVE.EXE -Value",
        "description": "Sets the screensaver.",
        "usage": "setsettings screensaver <path_to_screensaver>"
    },
    "timezone": {
        "command": "Set-TimeZone",
        "description": "Sets the system timezone.",
        "usage": "setsettings timezone <timezone_id>"
    },
    "powerplan": {
        "command": "powercfg /setactive",
        "description": "Sets the active power plan.",
        "usage": "setsettings powerplan <power_plan_guid>"
    },
    "hostname": {
        "command": "Rename-Computer -NewName",
        "description": "Sets the computer hostname.",
        "usage": "setsettings hostname <new_hostname>"
    },
    "lockscreen": {
        "command": "Set-ItemProperty -Path 'HKCU:\\Control Panel\\Desktop' -Name LockScreenImage -Value",
        "description": "Sets the lock screen image.",
        "usage": "setsettings lockscreen <path_to_image>"
    },
    "brightness": {
        "command": "(Get-WmiObject -Namespace root/WMI -Class WmiMonitorBrightnessMethods).WmiSetBrightness(1,",
        "description": "Sets the screen brightness.",
        "usage": "setsettings brightness <brightness_level>"
    },
    "volume": {
        "command": "(New-Object -ComObject WScript.Shell).SendKeys([char]",
        "description": "Sets the system volume.",
        "usage": "setsettings volume <volume_level>"
    },
    "language": {
        "command": "Set-WinUILanguageOverride -Language",
        "description": "Sets the display language.",
        "usage": "setsettings language <language_code>"
    },
    "sleep": {
        "command": "powercfg -change -standby-timeout-ac",
        "description": "Sets the sleep timeout.",
        "usage": "setsettings sleep <timeout_in_minutes>"
    },
    "hibernate": {
        "command": "powercfg -change -hibernate-timeout-ac",
        "description": "Sets the hibernate timeout.",
        "usage": "setsettings hibernate <timeout_in_minutes>"
    },
    "screensaver_timeout": {
        "command": "Set-ItemProperty -Path 'HKCU:\\Control Panel\\Desktop' -Name ScreenSaveTimeOut -Value",
        "description": "Sets the screensaver timeout.",
        "usage": "setsettings screensaver_timeout <timeout_in_seconds>"
    },
    "desktop_icon_size": {
        "command": "Set-ItemProperty -Path 'HKCU:\\Control Panel\\Desktop' -Name IconSize -Value",
        "description": "Sets the desktop icon size.",
        "usage": "setsettings desktop_icon_size <size>"
    }
}

def run(args):
    """
    Sets various Windows settings.
    """
    if len(args) == 0:
        print(f"{Fore.YELLOW}Supported settings:{Fore.RESET}")
        for setting, details in SUPPORTED_SETTINGS.items():
            print(f"{Fore.CYAN}{SUPPORTED_SETTINGS[setting]['usage']}{Fore.RESET}: {details['description']}")
        return
    elif len(args) == 1:
        setting = args[0]
        if setting in SUPPORTED_SETTINGS:
            print(f"{Fore.CYAN}{SUPPORTED_SETTINGS[setting]['usage']}{Fore.RESET}: {SUPPORTED_SETTINGS[setting]['description']}")
        else:
            print(f"{Fore.RED}Error: Unsupported setting '{setting}'.{Fore.RESET}")
            print(f"Supported settings: {', '.join(SUPPORTED_SETTINGS.keys())}")
        return
    elif len(args) < 2:
        print(f"{Fore.RED}Error: Please specify a setting and a value.{Fore.RESET}")
        print(f"Usage: {usage}")
        print(f"Supported settings: {', '.join(SUPPORTED_SETTINGS.keys())}")
        return

    setting, value = args[0], " ".join(args[1:])
    if setting not in SUPPORTED_SETTINGS:
        print(f"{Fore.RED}Error: Unsupported setting '{setting}'.{Fore.RESET}")
        print(f"Supported settings: {', '.join(SUPPORTED_SETTINGS.keys())}")
        return

    command = SUPPORTED_SETTINGS[setting]["command"]
    if setting == "timezone":
        command = f"{command} -Id '{value}'"
    elif setting == "brightness":
        command = f"{command} {value})"
    elif setting == "volume":
        command = f"{command} {value})"
    else:
        command = f"{command} '{value}'"

    print(f"{Fore.YELLOW}Attempting to set {setting} to '{value}'...{Fore.RESET}")

    try:
        result = os.system(f"powershell -Command \"{command}\"")
        if result == 0:
            print(f"{Fore.GREEN}Successfully set {setting} to '{value}'.{Fore.RESET}")
        else:
            print(f"{Fore.RED}Failed to set {setting}. Please check your permissions and the value provided.{Fore.RESET}")
    except Exception as e:
        print(f"{Fore.RED}An unexpected error occurred: {e}{Fore.RESET}")

def complete(text):
    """
    Auto-complete for the 'setsettings' command.
    """
    return [s for s in SUPPORTED_SETTINGS.keys() if s.startswith(text)]