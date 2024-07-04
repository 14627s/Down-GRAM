import instaloader
import os
import time
# Clearing the SCREEN


class colors:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    LIGHT_GRAY = '\033[37m'
    DARK_GRAY = '\033[90m'
    LIGHT_RED = '\033[91m'
    LIGHT_GREEN = '\033[92m'
    LIGHT_YELLOW = '\033[93m'
    LIGHT_BLUE = '\033[94m'
    LIGHT_MAGENTA = '\033[95m'
    LIGHT_CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'
    REVERSE = '\033[7m'
    HIDDEN = '\033[8m'
    STRIKETHROUGH = '\033[9m'
    DOUBLE_UNDERLINE = '\033[21m'
    NORMAL_COLOR = '\033[22m'
    NORMAL_INTENSITY = '\033[22m'
    RESET_UNDERLINE = '\033[24m'
    RESET_BLINK = '\033[25m'
    RESET_REVERSE = '\033[27m'
    RESET_HIDDEN = '\033[28m'
    RESET_STRIKETHROUGH = '\033[29m'
    ORANGE = '\033[38;5;214m'  # Light Orange
    PURPLE = '\033[38;5;141m'  # Light Purple
    TEAL = '\033[38;5;37m'     # Teal
    PINK = '\033[38;5;206m'    # Light Pink
    LIME = '\033[38;5;154m'    # Lime Green
    CYAN_BLUE = '\033[38;5;39m'  # Cyan Blue
    DARK_GREEN = '\033[38;5;22m'  # Dark Green
    SKY_BLUE = '\033[38;5;111m'  # Sky Blue
    DARK_ORANGE = '\033[38;5;166m'  # Dark Orange
    INDIGO = '\033[38;5;57m'   # Indigo
    GRAY = '\033[38;5;242m'    # Light Gray
    MAROON = '\033[38;5;52m'   # Maroon
    OCEAN_BLUE = '\033[38;5;21m'  # Ocean Blue
    GOLD = '\033[38;5;220m'    # Gold
def ascii():
    print(f'{colors.RED}·▄▄▄▄        ▄▄▌ ▐ ▄▌ ▐ ▄  ▄▄ • ▄▄▄   ▄▄▄· • ▌ ▄ ·. {colors.CYAN_BLUE} --> Current Version: 1.0\n{colors.RED}██▪ ██ ▪     ██· █▌▐█•█▌▐█▐█ ▀ ▪▀▄ █·▐█ ▀█ ·██ ▐███▪{colors.GOLD}--> Developed and debugged by 14627s alone.\n{colors.RED}▐█· ▐█▌ ▄█▀▄ ██▪▐█▐▐▌▐█▐▐▌▄█ ▀█▄▐▀▀▄ ▄█▀▀█ ▐█ ▌▐▌▐█·{colors.LIGHT_GREEN}--> GitHub: https://github.com/14627s\n{colors.RED}██. ██ ▐█▌.▐▌▐█▌██▐█▌██▐█▌▐█▄▪▐█▐█•█▌▐█ ▪▐▌██ ██▌▐█▌\n▀▀▀▀▀•  ▀█▄▀▪ ▀▀▀▀ ▀▪▀▀ █▪·▀▀▀▀ .▀  ▀ ▀  ▀ ▀▀  █▪▀▀▀')


while True:
 os.system('cls' if os.name == 'nt' else 'clear')
 ascii()
 def fetch_profile_info(username):
     L = instaloader.Instaloader()
     profile = instaloader.Profile.from_username(L.context, username)
     print(f"{colors.SKY_BLUE}\n\nUsername: {colors.LIGHT_YELLOW}{profile.username}")
     print(f"{colors.SKY_BLUE}Post Number: {colors.LIGHT_YELLOW}{profile.mediacount}")
     print(f"{colors.SKY_BLUE}Followers: {colors.LIGHT_YELLOW}{profile.followers:,}")
     print(f"{colors.SKY_BLUE}Followings: {colors.LIGHT_YELLOW}{profile.followees:,} ")
     print(f"{colors.SKY_BLUE}Bio: {colors.LIGHT_YELLOW}{profile.biography}\n")
     # Trying to download the profile and the informations about the account on a folder with the inputed username
     try:
         L.download_profile(colors.LIGHT_GREEN ,username, profile_pic_only=True)
         print(f"{colors.LIGHT_GREEN}\n\nProfile picture of {username} downloaded successfully.")
         time.sleep(3)
     except Exception as e:
         print(f"{colors.LIGHT_RED}\n\nFailed to download profile picture: {str(e)}")
 
 # Requesting to the user to input the username of the account he want to fetch informations.
 username = input(f"{colors.LIGHT_GREEN}\n\n\n[+] Enter Instagram username: {colors.LIGHT_YELLOW}")
 fetch_profile_info(username)