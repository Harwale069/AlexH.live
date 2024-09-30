import random
import os

# Function to ask a trivia question
def ask_question(question, answer, options):
    print("\n" + question)
    for option in options:
        print(option)
    user_answer = input("\nYour answer (A, B, C, or D): ").strip().upper()
    return user_answer == answer

# Function to save the leaderboard
def save_leaderboard(player_name, score, rounds_played):
    with open("leaderboard.txt", "a") as f:
        f.write(f"{player_name}: {score}/{rounds_played}\n")

# Function to display the leaderboard
def display_leaderboard():
    if os.path.exists("leaderboard.txt"):
        with open("leaderboard.txt", "r") as f:
            leaderboard = f.readlines()
            print("\nLeaderboard:")
            for entry in leaderboard:
                print(entry.strip())
    else:
        print("\nNo leaderboard data found.")

# Function to run the main trivia loop
def main():
    print("Welcome to Alex Harwoods CLI Trivia!\n")

    # List of questions, options, and correct answers categorized by difficulty
    questions_by_difficulty = {
        "Easy": [
            # Literature
            ("Who wrote 'To Kill a Mockingbird'?", "A", ["A. Harper Lee", "B. J.K. Rowling", "C. George Orwell", "D. Mark Twain"]),
            ("What is the capital of France?", "C", ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"]),
            # Science
            ("Which planet is known as the Red Planet?", "B", ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"]),
            ("What is the chemical symbol for water?", "A", ["A. H2O", "B. O2", "C. CO2", "D. H2"]),
            # History
            ("Who was the first president of the United States?", "C", ["A. Abraham Lincoln", "B. Peter Parker", "C. George Washington", "D. Alexander Hamilton"]),
            ("In which year did the Titanic sink?", "B", ["A. 1911", "B. 1912", "C. 1913", "D. 1914"]),
        ],
        "Medium": [
            # Literature
            ("Who wrote '1984'?", "C", ["A. Aldous Huxley", "B. J.D. Salinger", "C. George Orwell", "D. F. Scott Fitzgerald"]),
            ("What is the title of the famous play by Shakespeare about a Danish prince?", "B", ["A. Othello", "B. Hamlet", "C. Macbeth", "D. King Lear"]),
            # Science
            ("What is the boiling point of water?", "D", ["A. 90°C", "B. 80°C", "C. 100°F", "D. 100°C"]),
            ("What gas do plants absorb from the atmosphere?", "B", ["A. Oxygen", "B. Carbon Dioxide", "C. Nitrogen", "D. Hydrogen"]),
            # History
            ("What was the name of the ship that brought the Pilgrims to America?", "A", ["A. Mayflower", "B. Santa Maria", "C. Nina", "D. Pinta"]),
            ("Who discovered America?", "B", ["A. Leif Erikson", "B. Christopher Columbus", "C. Ferdinand Magellan", "D. Vasco da Gama"]),
        ],
        "Hard": [
            # Literature
            ("Which novel begins with the line 'Call me Ishmael'?", "C", ["A. Moby Dick", "B. The Great Gatsby", "C. To Kill a Mockingbird", "D. Brave New World"]),
            ("In which novel does the character Elizabeth Bennet appear?", "B", ["A. Wuthering Heights", "B. Pride and Prejudice", "C. Jane Eyre", "D. Great Expectations"]),
            # Science
            ("What is the speed of light?", "C", ["A. 300,000 km/h", "B. 150,000 km/h", "C. 300,000 km/s", "D. 30,000 km/s"]),
            ("What type of bond involves the sharing of electron pairs?", "D", ["A. Ionic Bond", "B. Metallic Bond", "C. Hydrogen Bond", "D. Covalent Bond"]),
            # History
            ("What year did World War I begin?", "C", ["A. 1910", "B. 1912", "C. 1914", "D. 1916"]),
            ("In which country did the Renaissance begin?", "A", ["A. Italy", "B. France", "C. Germany", "D. England"]),
        ]
    }

    # Add more questions for each category (easy, medium, hard)
    questions_by_difficulty["Easy"].extend([
        ("Which ocean is the largest?", "C", ["A. Atlantic", "B. Indian", "C. Pacific", "D. Arctic"]),
        ("What is the smallest prime number?", "A", ["A. 2", "B. 1", "C. 3", "D. 5"]),
        ("What is the freezing point of water?", "A", ["A. 0°C", "B. 100°C", "C. 32°F", "D. 100°F"]),
        ("What is the main ingredient in guacamole?", "B", ["A. Tomato", "B. Avocado", "C. Onion", "D. Pepper"]),
        ("What is the currency of Japan?", "D", ["A. Dollar", "B. Won", "C. Yuan", "D. Yen"]),
        ("What color do you get when you mix red and white?", "C", ["A. Pink", "B. Blue", "C. Green", "D. Purple"]),
        ("Which planet is closest to the Sun?", "A", ["A. Mercury", "B. Venus", "C. Earth", "D. Mars"]),
        ("Which animal is known as the 'King of the Jungle'?", "A", ["A. Lion", "B. Elephant", "C. Tiger", "D. Bear"]),
        ("What is the largest mammal in the world?", "D", ["A. Elephant", "B. Blue Whale", "C. Giraffe", "D. Hippopotamus"]),
        ("How many continents are there?", "C", ["A. 5", "B. 6", "C. 7", "D. 8"]),
    ])
    
    questions_by_difficulty["Medium"].extend([
        ("What is the capital of Australia?", "B", ["A. Sydney", "B. Canberra", "C. Melbourne", "D. Brisbane"]),
        ("What is the hardest natural substance on Earth?", "C", ["A. Gold", "B. Iron", "C. Diamond", "D. Sapphire"]),
        ("What does DNA stand for?", "B", ["A. Deoxyribonucleic Acid", "B. Dioxyribonucleic Acid", "C. Deoxyribose Nucleic Acid", "D. Dioxyribose Nucleic Acid"]),
        ("Who painted the Mona Lisa?", "A", ["A. Leonardo da Vinci", "B. Vincent van Gogh", "C. Pablo Picasso", "D. Claude Monet"]),
        ("What is the chemical symbol for gold?", "A", ["A. Au", "B. Ag", "C. Fe", "D. Pb"]),
        ("How many bones are in the adult human body?", "B", ["A. 206", "B. 206", "C. 204", "D. 200"]),
        ("What is the main gas found in the air we breathe?", "B", ["A. Oxygen", "B. Nitrogen", "C. Carbon Dioxide", "D. Hydrogen"]),
        ("Who was the first woman to fly solo across the Atlantic Ocean?", "A", ["A. Amelia Earhart", "B. Bessie Coleman", "C. Harriet Quimby", "D. Jacqueline Cochran"]),
        ("Which planet has the most moons?", "C", ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"]),
        ("What is the longest river in the world?", "C", ["A. Amazon", "B. Nile", "C. Yangtze", "D. Mississippi"]),
    ])
    
    questions_by_difficulty["Hard"].extend([
        ("Who discovered penicillin?", "A", ["A. Alexander Fleming", "B. Louis Pasteur", "C. Thomas Edison", "D. Isaac Newton"]),
        ("What is the capital of Iceland?", "C", ["A. Oslo", "B. Helsinki", "C. Reykjavik", "D. Copenhagen"]),
        ("What is the most spoken language in the world?", "B", ["A. English", "B. Mandarin", "C. Spanish", "D. Hindi"]),
        ("Which physicist developed the theory of general relativity?", "B", ["A. Isaac Newton", "B. Albert Einstein", "C. Niels Bohr", "D. Stephen Hawking"]),
        ("What is the currency of South Africa?", "D", ["A. Dollar", "B. Euro", "C. Pound", "D. Rand"]),
        ("In what year did the Berlin Wall fall?", "A", ["A. 1989", "B. 1991", "C. 1987", "D. 1990"]),
        ("Who wrote 'The Odyssey'?", "B", ["A. Virgil", "B. Homer", "C. Sophocles", "D. Euripides"]),
        ("Which element has the atomic number 1?", "A", ["A. Hydrogen", "B. Helium", "C. Oxygen", "D. Carbon"]),
        ("What is the largest desert in the world?", "C", ["A. Sahara", "B. Arabian", "C. Antarctic", "D. Gobi"]),
        ("Who was the first female Prime Minister of the United Kingdom?", "B", ["A. Margaret Thatcher", "B. Angela Merkel", "C. Indira Gandhi", "D. Golda Meir"]),
    ])

    # Get the difficulty level from the user
    difficulty = ""
    while difficulty not in questions_by_difficulty.keys():
        difficulty = input("Select difficulty (Easy, Medium, Hard): ").capitalize()
        if difficulty not in questions_by_difficulty.keys():
            print("Please choose a valid difficulty level.")

    # Select questions based on difficulty
    questions = questions_by_difficulty[difficulty]

    # Add a Random category
    questions += [
        # Random Questions
        ("What is the capital of Japan?", "C", ["A. Seoul", "B. Beijing", "C. Tokyo", "D. Bangkok"]),
        ("Which planet is known for its rings?", "B", ["A. Earth", "B. Saturn", "C. Neptune", "D. Jupiter"]),
        ("Who was the first man on the moon?", "A", ["A. Neil Armstrong", "B. Buzz Aldrin", "C. Yuri Gagarin", "D. John Glenn"]),
        ("What is the largest planet in our solar system?", "D", ["A. Earth", "B. Saturn", "C. Neptune", "D. Jupiter"]),
        ("What is the chemical symbol for silver?", "B", ["A. Au", "B. Ag", "C. Hg", "D. Pb"]),
        ("How many states are there in the United States?", "C", ["A. 50", "B. 51", "C. 50", "D. 49"]),
        ("Who wrote the play 'Romeo and Juliet'?", "C", ["A. Charles Dickens", "B. George Orwell", "C. William Shakespeare", "D. Mark Twain"]),
        ("What is the tallest mountain in the world?", "A", ["A. Mount Everest", "B. K2", "C. Kangchenjunga", "D. Lhotse"]),
        ("Which element is represented by the symbol 'He'?", "C", ["A. Hydrogen", "B. Helium", "C. Lithium", "D. Beryllium"]),
        ("What year did the first manned moon landing occur?", "A", ["A. 1969", "B. 1971", "C. 1965", "D. 1970"]),
    ]

    # Shuffle the questions so they appear in random order
    random.shuffle(questions)

    # Get the number of rounds from the user
    total_questions = len(questions)
    while True:
        try:
            num_rounds = int(input(f"\nHow many rounds would you like to play? (1-{total_questions}): "))
            if 1 <= num_rounds <= total_questions:
                break
            else:
                print(f"Please choose a number between 1 and {total_questions}.")
        except ValueError:
            print("Please enter a valid number.")
    
    # Set a score counter
    score = 0

    # Ask for player's name for leaderboard
    player_name = input("Enter your name for the leaderboard: ")

    # Loop through the selected number of rounds
    asked_questions = set()  # Track asked questions
    for i in range(num_rounds):
        # Ensure we don't ask the same question twice
        while True:
            question, correct_answer, options = random.choice(questions)
            if question not in asked_questions:
                asked_questions.add(question)
                break
        correct = ask_question(question, correct_answer, options)
        if correct:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {correct_answer}.")
    
    # Final score output
    print(f"\nGame Over! Your score: {score} out of {num_rounds}")

    # Save the score to the leaderboard
    save_leaderboard(player_name, score, num_rounds)

    # Display the leaderboard
    display_leaderboard()

if __name__ == "__main__":
    main()
