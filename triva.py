import random
import time

# Color codes for terminal output
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

def display_warning():
    print(f"{RED}WARNING: Please make sure Caps Lock is ON!{RESET}")

def get_question_sets():
    easy_questions = [
        ("What is the capital of France?", "paris"),
        ("What color is the sky?", "blue"),
        ("What is 2 + 2?", "4"),
        ("What is the largest mammal?", "blue whale"),
        ("What is the color of grass?", "green"),
        ("What is the first letter of the alphabet?", "a"),
        ("What planet is known as the Red Planet?", "mars"),
        ("What is the main ingredient in guacamole?", "avocado"),
        ("How many days are in a leap year?", "366"),
        ("What is the freezing point of water?", "0"),
        ("What is the capital of Japan?", "tokyo"),
        ("What is 5 * 6?", "30"),
        ("What is the currency used in the United States?", "dollar"),
        ("What is the name of the fairy in Peter Pan?", "tinkerbell"),
        ("How many continents are there?", "7"),
        ("What is the largest ocean on Earth?", "pacific"),
        ("What fruit is known for having seeds on the outside?", "strawberry"),
        ("What is the color of a ripe banana?", "yellow"),
        ("What gas do plants absorb?", "carbon dioxide"),
        ("What is the tallest mountain in the world?", "everest"),
        ("What animal is known as the King of the Jungle?", "lion"),
        ("What is the name of the author who wrote 'Harry Potter'?", "j.k. rowling"),
        ("What is the main language spoken in Spain?", "spanish"),
        ("What is the hardest natural substance on Earth?", "diamond"),
        ("What type of animal is a frog?", "amphibian"),
        ("What is the largest desert in the world?", "sahara"),
        ("What is the primary color of the sun?", "yellow"),
        ("What is the boiling point of water in degrees Celsius?", "100"),
        ("What is the name of the toy cowboy in Toy Story?", "woody"),
        ("What type of tree produces acorns?", "oak"),
        ("What is the name of the main character in 'The Great Gatsby'?", "gatsby"),
        ("How many legs does a spider have?", "8"),
        ("What is the capital of Italy?", "rome"),
    ]

    medium_questions = [
        ("What is the chemical symbol for gold?", "au"),
        ("What is the currency of Japan?", "yen"),
        ("In which year did the Titanic sink?", "1912"),
        ("What is the capital of Australia?", "canberra"),
        ("What is the longest river in the world?", "nile"),
        ("What element does 'O' represent on the periodic table?", "oxygen"),
        ("Who wrote 'To Kill a Mockingbird'?", "harper lee"),
        ("What is the hardest mineral on Earth?", "diamond"),
        ("What is the largest planet in our solar system?", "jupiter"),
        ("What is the capital city of Canada?", "ottawa"),
        ("What is the smallest country in the world?", "vatican city"),
        ("Who painted the Mona Lisa?", "da vinci"),
        ("In which continent is the Amazon rainforest located?", "south america"),
        ("What is the main language spoken in Brazil?", "portuguese"),
        ("Who was the first person to walk on the moon?", "neil armstrong"),
        ("What is the square root of 64?", "8"),
        ("What is the most spoken language in the world?", "mandarin"),
        ("What is the tallest building in the world?", "burj khalifa"),
        ("Which planet is known for its rings?", "saturn"),
        ("What is the currency of the United Kingdom?", "pound"),
        ("Who discovered penicillin?", "alexander fleming"),
        ("What is the capital of Greece?", "athens"),
        ("What is the smallest bone in the human body?", "stapes"),
        ("What is the capital of Egypt?", "cairo"),
        ("What organ is responsible for pumping blood?", "heart"),
        ("What is the chemical symbol for water?", "h2o"),
        ("What gas do living beings need to breathe?", "oxygen"),
        ("What is the largest land animal?", "elephant"),
        ("What is the main ingredient in bread?", "flour"),
        ("In which year did World War II end?", "1945"),
        ("What is the most common gas in the Earth's atmosphere?", "nitrogen"),
        ("What is the name of the first artificial satellite launched into space?", "sputnik"),
        ("What is the capital of Russia?", "moscow"),
    ]

    hard_questions = [
        ("Who developed the theory of relativity?", ["albert einstein", "einstein"]),
        ("What is the capital city of Iceland?", ["reykjavik"]),
        ("What is the largest organ in the human body?", ["skin"]),
        ("Who wrote '1984'?", ["george orwell"]),
        ("What is the name of the longest river in South America?", ["amazon"]),
        ("In which year did the Berlin Wall fall?", ["1989"]),
        ("Who painted 'The Starry Night'?", ["vincent van gogh"]),
        ("What is the chemical symbol for potassium?", ["k"]),
        ("What is the smallest planet in our solar system?", ["mercury"]),
        ("What is the capital of New Zealand?", ["wellington"]),
        ("Who was the first female Prime Minister of the United Kingdom?", ["margaret thatcher"]),
        ("What is the most abundant gas in the Earth's atmosphere?", ["nitrogen"]),
        ("What is the capital of Mongolia?", ["ulaanbaatar"]),
        ("Who discovered the structure of DNA?", ["james watson", "francis crick"]),
        ("What is the currency of South Africa?", ["rand"]),
        ("What is the highest mountain in North America?", ["denali"]),
        ("Who is known as the father of modern physics?", ["albert einstein"]),
        ("What is the capital of Bhutan?", ["thimphu"]),
        ("Who is the author of the 'Harry Potter' series?", ["j.k. rowling"]),
        ("What is the largest volcano in the world?", ["mauna loa"]),
        ("What is the most widely spoken language in the world?", ["mandarin"]),
        ("Who wrote 'Pride and Prejudice'?", ["jane austen"]),
        ("What is the only continent without reptiles or snakes?", ["antartica"]),
        ("What is the capital of Kazakhstan?", ["nur-sultan"]),
        ("What is the hardest natural substance?", ["diamond"]),
        ("Who was the first president of the United States?", ["george washington"]),
        ("What is the longest river in Asia?", ["yangtze"]),
        ("Who invented the telephone?", ["alexander graham bell"]),
        ("What is the currency of India?", ["rupee"]),
        ("Who wrote the play 'Romeo and Juliet'?", ["william shakespeare"]),
        ("What is the capital of Nigeria?", ["abuja"]),
        ("What is the main ingredient in sushi?", ["rice"]),
        ("What is the largest desert in the world?", ["sahara"]),
        ("Who is known as the father of modern chemistry?", ["antoine lavoisier"]),
    ]

    extreme_questions = [
        ("What is the fastest land animal?", ["cheetah"]),
        ("What is the capital of Mongolia?", ["ulaanbaatar"]),
        ("Who was the first person to climb Mount Everest?", ["sir edmund hillary"]),
        ("What is the hardest natural substance?", ["diamond"]),
        ("In which year did the Titanic sink?", ["1912"]),
        ("What is the largest planet in our solar system?", ["jupiter"]),
        ("What is the chemical formula for table salt?", ["nacl"]),
        ("Who invented the light bulb?", ["thomas edison"]),
        ("What is the capital of Canada?", ["ottawa"]),
        ("What is the longest river in the world?", ["nile"]),
        ("What is the main ingredient in hummus?", ["chickpeas"]),
        ("Who painted the ceiling of the Sistine Chapel?", ["michelangelo"]),
        ("What is the capital of Finland?", ["helsinki"]),
        ("What is the largest country in the world?", ["russia"]),
        ("What is the square root of 256?", ["16"]),
        ("Who wrote 'Moby Dick'?", ["herman melville"]),
        ("What is the capital of Australia?", ["canberra"]),
        ("Who is known as the father of psychoanalysis?", ["sigmund freud"]),
        ("What is the most common blood type?", ["o positive", "o+"]),
        ("What is the name of the largest ocean on Earth?", ["pacific"]),
        ("What is the capital of South Korea?", ["seoul"]),
        ("What element has the chemical symbol 'Fe'?", ["iron"]),
        ("Who discovered penicillin?", ["alexander fleming"]),
        ("What is the main gas in the Earth's atmosphere?", ["nitrogen"]),
        ("Who is the author of 'The Catcher in the Rye'?", ["j.d. salinger"]),
    ]

    math_questions = [
        ("What is 5 + 7?", ["12"]),
        ("What is 15 - 6?", ["9"]),
        ("What is 8 * 7?", ["56"]),
        ("What is 81 / 9?", ["9"]),
        ("What is the square root of 144?", ["12"]),
        ("What is 10 % 3?", ["1"]),
        ("What is 9 + 10?", ["19"]),
        ("What is 20 - 4 * 3?", ["8"]),
        ("What is 50 / 2 + 25?", ["50"]),
        ("What is 15 + 5 * 2?", ["25"]),
        ("What is 6 * (2 + 3)?", ["30"]),
        ("What is 3^3?", ["27"]),
        ("What is 8 + 6 / 3?", ["10"]),
        ("What is the value of π (Pi) rounded to two decimal places?", ["3.14"]),
        ("What is 2 + 2 * 2?", ["6"]),
        ("What is the area of a rectangle with length 4 and width 3?", ["12"]),
        ("What is the perimeter of a square with sides of length 5?", ["20"]),
        ("If a triangle has a base of 10 and a height of 5, what is its area?", ["25"]),
        ("If you roll a die, what is the probability of rolling a 3?", ["1/6"]),
        ("What is 100 - (2 * 25)?", ["50"]),
        ("What is the next prime number after 7?", ["11"]),
        ("What is the sum of the angles in a triangle?", ["180"]),
        ("What is 4 + 4 * 4?", ["20"]),
        ("What is the hypotenuse of a right triangle with legs of 3 and 4?", ["5"]),
        ("If I have 3 apples and you give me 2 more, how many do I have?", ["5"]),
        ("If 5x = 20, what is x?", ["4"]),
        ("What is 6 + 4?", ["10"]),
        ("What is the cube of 3?", ["27"]),
        ("What is the next number in the sequence: 2, 4, 6, 8, ...?", ["10"]),
        ("If a train travels 60 miles in 1 hour, how far will it travel in 3 hours?", ["180"]),
        ("What is 12 / 4?", ["3"]),
        ("What is the sum of 1, 2, and 3?", ["6"]),
    ]

    return {
        'easy': easy_questions,
        'medium': medium_questions,
        'hard': hard_questions,
        'extreme': extreme_questions,
        'math': math_questions,
    }

def get_random_question(difficulty):
    questions = get_question_sets()[difficulty]
    return random.choice(questions)

def check_answer(question, answer):
    return answer.lower() in question[1] if isinstance(question[1], list) else answer.lower() == question[1]

def play_game():
    print(f"{GREEN}WELCOME TO ALEX HARWOOD'S CLI TRIVIA GAME{RESET}")
    time.sleep(1)
    
    scores = {difficulty: 0 for difficulty in get_question_sets()}
    rounds = {'easy': 0, 'medium': 0, 'hard': 0, 'extreme': 0, 'math': 0}

    while True:
        difficulty = input("Choose a difficulty level (easy, medium, hard, extreme, math) or type 'exit' to quit: ").lower()
        if difficulty == 'exit':
            break
        if difficulty not in rounds:
            print("Invalid difficulty. Please choose again.")
            continue

        rounds[difficulty] += 1
        question = get_random_question(difficulty)
        display_warning()

        print(f"Question: {question[0]}")
        user_answer = input("Your answer: ")

        if check_answer(question, user_answer):
            print(f"{GREEN}Correct!{RESET}")
            scores[difficulty] += 1
        else:
            print(f"{RED}Wrong! The correct answer was: {', '.join(question[1])}{RESET}")

        print(f"Score for {difficulty} difficulty: {scores[difficulty]}/{rounds[difficulty]}")
        print()

    print("Final Scores:")
    for diff, score in scores.items():
        print(f"{diff.capitalize()}: {score} correct answers in {rounds[diff]} rounds")

if __name__ == "__main__":
    play_game()
