import time
import os
import itertools

# Function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to print the text "Made by Alex Harwood"
def print_text():
    text = r"""
 __  __           _        _                _    _           
|  \/  | __ _  __| | ___  | |__  _   _     / \  | | _____  __
| |\/| |/ _` |/ _` |/ _ \ | '_ \| | | |   / _ \ | |/ _ \ \/ /
| |  | | (_| | (_| |  __/ | |_) | |_| |  / ___ \| |  __/>  < 
|_|  |_|\__,_|\__,_|\___| |_.__/ \__, | /_/   \_\_|\___/_/\_\
| | | | __ _ _ ____      _____   |___/ __| |                 
| |_| |/ _` | '__\ \ /\ / / _ \ / _ \ / _` |                 
|  _  | (_| | |   \ V  V / (_) | (_) | (_| |                 
|_| |_|\__,_|_|    \_/\_/ \___/ \___/ \__,_| bcus hes a sigma                
    """
    print(text)

# Function to print bullet animation shooting down
def bullet_animation():
    frames = [
        "•",
        "•\n•",
        "•\n•\n•",
        "•\n•\n•\n•",
        "•\n•\n•\n•\n•",
    ]
    for frame in frames:
        clear_screen()
        print(frame)
        time.sleep(0.2)

# Function to print the Walter White ASCII art with color change
def walter_white_animation():
    colors = range(1, 32)  # Terminal color codes from 1 to 31
    frame = r"""
Alex Harwood⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢺⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠆⠜⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⠿⠿⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣿⣿⣿⣿
⣿⣿⡏⠁⠀⠀⠀⠀⠀⣀⣠⣤⣤⣶⣶⣶⣶⣶⣦⣤⡄⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿
⣿⣿⣷⣄⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⡧⠇⢀⣤⣶⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣾⣮⣭⣿⡻⣽⣒⠀⣤⣜⣭⠐⢐⣒⠢⢰⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣏⣿⣿⣿⣿⣿⣿⡟⣾⣿⠂⢈⢿⣷⣞⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣷⣶⣾⡿⠿⣿⠗⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠻⠋⠉⠑⠀⠀⢘⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡿⠟⢹⣿⣿⡇⢀⣶⣶⠴⠶⠀⠀⢽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⢸⣿⣿⠀⠀⠣⠀⠀⠀⠀⠀⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⡿⠟⠋⠀⠀⠀⠀⠸⣿⣧⣀⠀⠀⠀⠀⡀⣴⠁⢘⡙⢿⣿⣿⣿⣿⣿⣿⣿⣿
⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⠗⠂⠄⠀⣴⡟⠀⠀⡃⠀⠉⠉⠟⡿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢷⠾⠛⠂⢹⠀⠀⠀⢡⠀⠀⠀⠀⠀⠙⠛⠿⢿
    """
    for color in itertools.cycle(colors):
        clear_screen()
        print(f"\033[38;5;{color}m{frame}\033[0m")
        time.sleep(0.5)

# Main function to run the animation
def main():
    print_text()
    time.sleep(5)  # Show the text for 5 seconds
    bullet_animation()
    walter_white_animation()

if __name__ == "__main__":
    main()
