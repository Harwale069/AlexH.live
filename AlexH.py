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
|_| |_|\__,_|_|    \_/\_/ \___/ \___/ \__,_|                 
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
    colors = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]  # Red, Green, Yellow, Blue, Magenta, Cyan
    frame = r"""
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
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
    for color in itertools.cycle([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,,24,25,26,27,28,29,30,31]):
        clear_screen()
        print(f"\033[38;5;{color}m{frame}\033[0m")
        time.sleep(0.1)

# Main function to run the animation
def main():
    print_text()
    time.sleep(5)  # Show the text for 5 seconds
    bullet_animation()
    walter_white_animation()

if __name__ == "__main__":
    main()
