import os
from colorama import Fore
from main import messages

description = messages["set_settings_description"]
usage = messages["set_settings_usage"]

# List of supported settings with descriptions
SUPPORTED_SETTINGS = {
    "wallpaper": {
        "command": "Set-ItemProperty -Path 'HKCU:\\Control Panel\\Desktop' -Name Wallpaper -Value",
        "description": messages["description_wallpaper"],
        "usage": "setsettings wallpaper <path_to_image>"
    },
    "screensaver": {
        "command": "Set-ItemProperty -Path 'HKCU:\\Control Panel\\Desktop' -Name SCRNSAVE.EXE -Value",
        "description": messages["description_screensaver"],
        "usage": "setsettings screensaver <path_to_screensaver>"
    },
    "timezone": {
        "command": "Set-TimeZone",
        "description": messages["description_timezone"],
        "usage": "setsettings timezone <timezone_id>"
    },
    "powerplan": {
        "command": "powercfg /setactive",
        "description": messages["description_powerplan"],
        "usage": "setsettings powerplan <power_plan_guid>"
    },
    "hostname": {
        "command": "Rename-Computer -NewName",
        "description": messages["description_hostname"],
        "usage": "setsettings hostname <new_hostname>"
    },
    "lockscreen": {
        "command": "Set-ItemProperty -Path 'HKCU:\\Control Panel\\Desktop' -Name LockScreenImage -Value",
        "description": messages["description_lockscreen"],
        "usage": "setsettings lockscreen <path_to_image>"
    },
    "brightness": {
        "command": "(Get-WmiObject -Namespace root/WMI -Class WmiMonitorBrightnessMethods).WmiSetBrightness(1,",
        "description": messages["description_brightness"],
        "usage": "setsettings brightness <brightness_level>"
    },
    "volume": {
        "command": "(New-Object -ComObject WScript.Shell).SendKeys([char]",
        "description": messages["description_volume"],
        "usage": "setsettings volume <volume_level>"
    },
    "language": {
        "command": "Set-WinUILanguageOverride -Language",
        "description": messages["description_language"],
        "usage": "setsettings language <language_code>"
    },
    "sleep": {
        "command": "powercfg -change -standby-timeout-ac",
        "description": messages["description_sleep"],
        "usage": "setsettings sleep <timeout_in_minutes>"
    },
    "hibernate": {
        "command": "powercfg -change -hibernate-timeout-ac",
        "description": messages["description_hibernate"],
        "usage": "setsettings hibernate <timeout_in_minutes>"
    },
    "screensaver_timeout": {
        "command": "Set-ItemProperty -Path 'HKCU:\\Control Panel\\Desktop' -Name ScreenSaveTimeOut -Value",
        "description": messages["description_screensaver_timeout"],
        "usage": "setsettings screensaver_timeout <timeout_in_seconds>"
    },
    "desktop_icon_size": {
        "command": "Set-ItemProperty -Path 'HKCU:\\Control Panel\\Desktop' -Name IconSize -Value",
        "description": messages["description_desktop_icon_size"],
        "usage": "setsettings desktop_icon_size <size>"
    },
    "remove_taskbar_icons": {
        "command": "Remove-ItemProperty -Path 'HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Taskband' -Name",
        "description": messages["description_remove_taskbar_icons"],
        "usage": "setsettings taskbar_icons"
    },
    "powercfg_sleep": {
        "command": "powercfg /change standby-timeout-ac",
        "description": messages["description_powercfg_sleep"],
        "usage": "setsettings powercfg_sleep <timeout_in_minutes>"
    },
    "powercfg_hibernate": {
        "command": "powercfg /change hibernate-timeout-ac",
        "description": messages["description_powercfg_hibernate"],
        "usage": "setsettings powercfg_hibernate <timeout_in_minutes>"
    },
    "powercfg_display": {
        "command": "powercfg /change monitor-timeout-ac",
        "description": messages["description_powercfg_display"],
        "usage": "setsettings powercfg_display <timeout_in_minutes>"
    }
}

def run(args):
    """
    Sets various Windows settings.
    """
    if len(args) == 0:
        print(f"{Fore.YELLOW}{messages['supported_settings']}{Fore.RESET}")
        for setting, details in SUPPORTED_SETTINGS.items():
            print(f"{Fore.CYAN}{SUPPORTED_SETTINGS[setting]['usage']}{Fore.RESET}: {details['description']}")
        return
    elif len(args) == 1:
        setting = args[0]
        if setting in SUPPORTED_SETTINGS:
            print(f"{Fore.CYAN}{SUPPORTED_SETTINGS[setting]['usage']}{Fore.RESET}: {SUPPORTED_SETTINGS[setting]['description']}")
        else:
            print(f"{Fore.RED}{messages['error_unsupported_setting']} '{setting}'.{Fore.RESET}")
            print(f"{messages['supported_settings']} {', '.join(SUPPORTED_SETTINGS.keys())}")
        return
    elif len(args) < 2 and setting != "taskbar_icons":
        print(f"{Fore.RED}{messages['error_specify_setting_value']}{Fore.RESET}")
        print(f"Usage: {usage}")
        print(f"{messages['supported_settings']} {', '.join(SUPPORTED_SETTINGS.keys())}")
        return

    setting, value = args[0], " ".join(args[1:])
    if setting not in SUPPORTED_SETTINGS:
        print(f"{Fore.RED}{messages['error_unsupported_setting']} '{setting}'.{Fore.RESET}")
        print(f"{messages['supported_settings']} {', '.join(SUPPORTED_SETTINGS.keys())}")
        return

    command = SUPPORTED_SETTINGS[setting]["command"]
    if setting == "timezone":
        command = f"{command} -Id '{value}'"
    elif setting == "brightness":
        command = f"{command} {value})"
    elif setting == "volume":
        command = f"{command} {value})"
    elif setting == "remove_taskbar_icons":
        command = f"{command} 'Favorites'"
    else:
        command = f"{command} '{value}'"

    print(f"{Fore.YELLOW}{messages['attempting_set_setting']} {setting} to '{value}'...{Fore.RESET}")

    try:
        result = os.system(f"powershell -Command \"{command}\"")
        if result == 0:
            print(f"{Fore.GREEN}{messages['success_set_setting']} {setting} to '{value}'.{Fore.RESET}")
        else:
            print(f"{Fore.RED}{messages['failed_set_setting']}{Fore.RESET}")
    except Exception as e:
        print(f"{Fore.RED}{messages['unexpected_error']}: {e}{Fore.RESET}")

def complete(text):
    """
    Auto-complete for the 'setsettings' command.
    """
    return [s for s in SUPPORTED_SETTINGS.keys() if s.startswith(text)]