import os


CURRENT_VERSION = None
UPDATE_URL = "https://raw.githubusercontent.com/David-M-GitHub/ImInstant/refs/heads/master/VERSION.txt"

with open(os.path.join("VERSION.txt"), "r") as file:
    CURRENT_VERSION = file.read().strip()