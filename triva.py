import random
import time
import os

# ANSI escape codes for text color
RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to display the welcome message with blinking effect
def welcome_message():
    clear_screen()
    for _ in range(5):
        print(f"{GREEN}{'WELCOME TO ALEX HARWOOD\'S CLI TRIVIA GAME!':^50}{RESET}")
        time.sleep(0.5)
        clear_screen()
        time.sleep(0.5)

# Easy questions
easy_questions = [
    ("What is the capital of France?", "Paris"),
    ("What color is the sky?", "Blue"),
    ("How many legs does a spider have?", "8"),
    ("What is 2 + 2?", "4"),
    ("Which planet is known as the Red Planet?", "Mars"),
    ("What is the largest mammal in the world?", "Blue Whale"),
    ("What is the freezing point of water?", "0"),
    ("What is the capital of Japan?", "Tokyo"),
    ("What is the chemical symbol for water?", "H2O"),
    ("What is the currency of the United States?", "Dollar"),
    ("What is the name of the fairy in Peter Pan?", "Tinkerbell"),
    ("What is the main ingredient in guacamole?", "Avocado"),
    ("How many colors are in a rainbow?", "7"),
    ("What is the first letter of the English alphabet?", "A"),
    ("What is the name of the toy cowboy in Toy Story?", "Woody"),
    ("What fruit do kids traditionally give teachers?", "Apple"),
    ("What is the largest continent?", "Asia"),
    ("What is the name of the dog in The Wizard of Oz?", "Toto"),
    ("What is the smallest planet in our solar system?", "Mercury"),
    ("In which country is the Great Pyramid of Giza?", "Egypt"),
    ("What is the name of the first man to walk on the moon?", "Neil Armstrong"),
    ("What is the hottest planet in our solar system?", "Venus"),
    ("What is the name of the main character in The Lion King?", "Simba"),
    ("How many planets are in our solar system?", "8"),
    ("What is the largest ocean on Earth?", "Pacific"),
    ("What is the name of the bear in The Jungle Book?", "Baloo"),
    ("What is the capital of Italy?", "Rome"),
    ("What is the name of Harry Potter's pet owl?", "Hedwig"),
    ("What is the name of the famous clock tower in London?", "Big Ben"),
    ("What is the name of the cat in The Cat in the Hat?", "The Cat"),
    ("What is the capital of Australia?", "Canberra"),
    ("What is the main ingredient in bread?", "Flour"),
    ("What is the name of the fish in Finding Nemo?", "Nemo"),
]

# Medium questions
medium_questions = [
    ("What is the longest river in the world?", "Nile"),
    ("What element does 'O' represent on the periodic table?", "Oxygen"),
    ("Who wrote 'Romeo and Juliet'?", "Shakespeare"),
    ("What is the powerhouse of the cell?", "Mitochondria"),
    ("In which year did the Titanic sink?", "1912"),
    ("What is the hardest natural substance on Earth?", "Diamond"),
    ("What is the largest desert in the world?", "Sahara"),
    ("What is the name of the longest bone in the human body?", "Femur"),
    ("Who painted the Mona Lisa?", "Leonardo da Vinci"),
    ("What gas do plants absorb from the atmosphere?", "Carbon Dioxide"),
    ("What is the capital of Canada?", "Ottawa"),
    ("What is the main language spoken in Brazil?", "Portuguese"),
    ("What is the largest planet in our solar system?", "Jupiter"),
    ("What is the primary ingredient in sushi?", "Rice"),
    ("What is the most widely spoken language in the world?", "Mandarin"),
    ("What is the smallest country in the world?", "Vatican City"),
    ("What is the chemical formula for table salt?", "NaCl"),
    ("What is the name of the first female Prime Minister of the UK?", "Margaret Thatcher"),
    ("What is the currency of Japan?", "Yen"),
    ("What is the main ingredient in beer?", "Barley"),
    ("What is the speed of light in a vacuum?", "299792458"),
    ("What is the second largest country in the world by land area?", "Canada"),
    ("What is the name of the first artificial Earth satellite?", "Sputnik"),
    ("What is the name of the largest internal organ in the human body?", "Liver"),
    ("What is the capital of Egypt?", "Cairo"),
    ("What is the name of the galaxy we live in?", "Milky Way"),
    ("What is the main ingredient in hummus?", "Chickpeas"),
    ("What is the process by which plants make their food?", "Photosynthesis"),
    ("What is the capital of Greece?", "Athens"),
    ("What is the chemical symbol for gold?", "Au"),
    ("What is the name of the first computer programmer?", "Ada Lovelace"),
    ("What is the currency of the European Union?", "Euro"),
]

# Hard questions
hard_questions = [
    ("What is the square root of 144?", "12"),
    ("What is the capital of Iceland?", "Reykjavik"),
    ("Who developed the theory of relativity?", "Einstein"),
    ("What is the name of the longest river in South America?", "Amazon"),
    ("What is the scientific name for the common cold?", "Rhinovirus"),
    ("What is the most abundant gas in the Earth's atmosphere?", "Nitrogen"),
    ("What is the capital of Australia?", "Canberra"),
    ("Who was the first woman to fly solo across the Atlantic Ocean?", "Amelia Earhart"),
    ("What is the primary component of natural gas?", "Methane"),
    ("What is the name of the first electronic computer?", "ENIAC"),
    ("What is the process by which a liquid turns into a gas?", "Evaporation"),
    ("What is the hardest rock?", "Diamond"),
    ("What is the main ingredient in traditional pesto sauce?", "Basil"),
    ("What is the capital of Mongolia?", "Ulaanbaatar"),
    ("What is the formula for calculating the area of a circle?", "πr²"),
    ("What is the capital of Kazakhstan?", "Nur-Sultan"),
    ("What is the primary ingredient in the dish paella?", "Rice"),
    ("What is the main ingredient in tofu?", "Soybeans"),
    ("What is the capital of Nepal?", "Kathmandu"),
    ("Who painted the ceiling of the Sistine Chapel?", "Michelangelo"),
    ("What is the scientific term for the fear of spiders?", "Arachnophobia"),
    ("What is the name of the first successful vaccine?", "Smallpox"),
    ("What is the primary function of red blood cells?", "Carry oxygen"),
    ("What is the name of the first human in space?", "Yuri Gagarin"),
    ("What is the capital of Croatia?", "Zagreb"),
    ("What is the chemical formula for water?", "H2O"),
    ("What is the currency of Russia?", "Ruble"),
    ("What is the largest organ in the human body?", "Skin"),
    ("What is the capital of Switzerland?", "Bern"),
    ("What is the main ingredient in traditional Japanese miso soup?", "Miso"),
    ("What is the smallest unit of life?", "Cell"),
    ("What is the capital of Finland?", "Helsinki"),
]

# Function to ask a question and check the answer
def ask_question(question, answer):
    user_answer = input(f"\n{question} ")
    return user_answer.strip().lower() == answer.strip().lower()

# Main game function
def trivia_game():
    welcome_message()

    print(f"{RED}WARNING: PLEASE TURN ON CAPS LOCK FOR BETTER ACCURACY!{RESET}")
    time.sleep(2)

    print("Select Difficulty Level: ")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    
    difficulty = input("Enter your choice (1-3): ")
    
    if difficulty == '1':
        questions = easy_questions
    elif difficulty == '2':
        questions = medium_questions
    elif difficulty == '3':
        questions = hard_questions
    else:
        print("Invalid choice, exiting game.")
        return

    rounds = int(input("Enter the number of rounds (up to 30): "))
    rounds = min(rounds, 30)  # Limit rounds to 30

    score = 0
    selected_questions = random.sample(questions, rounds)

    for question, answer in selected_questions:
        if ask_question(question, answer):
            print(f"{GREEN}Correct!{RESET}")
            score += 1
        else:
            print(f"{RED}Wrong answer! The correct answer was: {answer}{RESET}")

    print(f"\nGame Over! Your score: {score}/{rounds}")

if __name__ == "__main__":
    trivia_game()
