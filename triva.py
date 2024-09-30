import random
import time

# Questions categorized by difficulty
questions = {
    'easy': [
        {"question": "What is the capital of France?", "options": ["A) PARIS", "B) LONDON", "C) BERLIN", "D) ROME"], "answer": "A"},
        {"question": "What is 2 + 2?", "options": ["A) 3", "B) 4", "C) 5", "D) 6"], "answer": "B"},
        {"question": "What is the color of the sky?", "options": ["A) GREEN", "B) BLUE", "C) RED", "D) YELLOW"], "answer": "B"},
        {"question": "What is the largest mammal?", "options": ["A) ELEPHANT", "B) BLUE WHALE", "C) GIRAFFE", "D) KANGAROO"], "answer": "B"},
        {"question": "What is the main ingredient in guacamole?", "options": ["A) TOMATO", "B) ONION", "C) AVOCADO", "D) PEPPER"], "answer": "C"},
        {"question": "What is the smallest continent?", "options": ["A) AUSTRALIA", "B) EUROPE", "C) ASIA", "D) AFRICA"], "answer": "A"},
        {"question": "What gas do plants absorb?", "options": ["A) OXYGEN", "B) CARBON DIOXIDE", "C) NITROGEN", "D) HELIUM"], "answer": "B"},
        {"question": "What is the boiling point of water?", "options": ["A) 100°C", "B) 0°C", "C) 50°C", "D) 25°C"], "answer": "A"},
        {"question": "Which animal is known as the King of the Jungle?", "options": ["A) TIGER", "B) LION", "C) BEAR", "D) ELEPHANT"], "answer": "B"},
        {"question": "Which planet is known as the Red Planet?", "options": ["A) EARTH", "B) MARS", "C) JUPITER", "D) SATURN"], "answer": "B"},
    ],
    'medium': [
        {"question": "What is the capital of Canada?", "options": ["A) TORONTO", "B) OTTAWA", "C) VANCOUVER", "D) MONTREAL"], "answer": "B"},
        {"question": "In which year did the Titanic sink?", "options": ["A) 1912", "B) 1905", "C) 1920", "D) 1915"], "answer": "A"},
        {"question": "What is the largest ocean on Earth?", "options": ["A) ATLANTIC", "B) INDIAN", "C) PACIFIC", "D) ARCTIC"], "answer": "C"},
        {"question": "Who painted the Mona Lisa?", "options": ["A) VINCENT VAN GOGH", "B) PABLO PICASSO", "C) LEONARDO DA VINCI", "D) MICHELANGELO"], "answer": "C"},
        {"question": "What is the currency used in the United States?", "options": ["A) EURO", "B) POUND", "C) YEN", "D) DOLLAR"], "answer": "D"},
        {"question": "Which gas is most abundant in the Earth's atmosphere?", "options": ["A) OXYGEN", "B) CARBON DIOXIDE", "C) NITROGEN", "D) HELIUM"], "answer": "C"},
        {"question": "What is the capital of Australia?", "options": ["A) SYDNEY", "B) MELBOURNE", "C) CANBERRA", "D) BRISBANE"], "answer": "C"},
        {"question": "Who wrote 'Romeo and Juliet'?", "options": ["A) CHARLES DICKENS", "B) MARK TWAIN", "C) JANE AUSTEN", "D) WILLIAM SHAKESPEARE"], "answer": "D"},
        {"question": "Which element has the chemical symbol 'O'?", "options": ["A) GOLD", "B) OXYGEN", "C) SILVER", "D) CARBON"], "answer": "B"},
        {"question": "What is the largest desert in the world?", "options": ["A) SAHARA", "B) GOBI", "C) ARCTIC", "D) ANTARCTIC"], "answer": "A"},
    ],
    'hard': [
        {"question": "What is the smallest country in the world?", "options": ["A) MONACO", "B) VATICAN CITY", "C) SAN MARINO", "D) NAURU"], "answer": "B"},
        {"question": "In which year did World War I begin?", "options": ["A) 1914", "B) 1912", "C) 1916", "D) 1918"], "answer": "A"},
        {"question": "What is the main language spoken in Brazil?", "options": ["A) SPANISH", "B) PORTUGUESE", "C) FRENCH", "D) ENGLISH"], "answer": "B"},
        {"question": "Which planet is known for its rings?", "options": ["A) JUPITER", "B) SATURN", "C) URANUS", "D) NEPTUNE"], "answer": "B"},
        {"question": "What is the hardest natural substance on Earth?", "options": ["A) IRON", "B) DIAMOND", "C) GOLD", "D) SILVER"], "answer": "B"},
        {"question": "Which organ is responsible for pumping blood through the body?", "options": ["A) LIVER", "B) KIDNEY", "C) HEART", "D) LUNG"], "answer": "C"},
        {"question": "What is the process of converting a liquid into a gas called?", "options": ["A) CONDENSATION", "B) EVAPORATION", "C) PRECIPITATION", "D) SUBLIMATION"], "answer": "B"},
        {"question": "Who discovered penicillin?", "options": ["A) ALEXANDER FLEMING", "B) LOUIS PASTEUR", "C) EDWARD JENNER", "D) JOSEPH LISTER"], "answer": "A"},
        {"question": "Which vitamin is known as the sunshine vitamin?", "options": ["A) VITAMIN A", "B) VITAMIN B12", "C) VITAMIN C", "D) VITAMIN D"], "answer": "D"},
        {"question": "What is the main ingredient in a traditional sushi roll?", "options": ["A) NOODLES", "B) RICE", "C) FISH", "D) VEGETABLES"], "answer": "B"},
    ]
}

# Function to display the welcome message
def display_welcome():
    print("\nWELCOME TO ALEX HARWOOD'S CLI TRIVIA GAME".center(80, ' '))
    time.sleep(1)

# Function to conduct the trivia game
def trivia_game():
    display_welcome()
    total_score = 0
    rounds_played = 0

    while True:
        rounds_played += 1
        score = 0
        difficulty = input("Choose difficulty (easy, medium, hard): ").lower()

        if difficulty not in questions:
            print("Invalid difficulty. Please choose easy, medium, or hard.")
            continue

        random.shuffle(questions[difficulty])

        for question in questions[difficulty]:
            print(f"\n{question['question']}")
            for option in question['options']:
                print(option)
            answer = input("Your answer: ").strip().upper()

            if answer == question['answer']:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct answer is {question['answer']}.")

        total_score += score
        print(f"\nYour score for this round: {score}/{len(questions[difficulty])}")
        print(f"Total score: {total_score}")

        play_again = input("\nDo you want to play another round? (yes/no): ").strip().lower()
        if play_again != 'yes':
            break

    print(f"\nThank you for playing! You played {rounds_played} round(s) with a total score of {total_score}.")

# Start the game
if __name__ == "__main__":
    trivia_game()
