import random

# Function to ask a trivia question
def ask_question(question, answer, options):
    print("\n" + question)
    for option in options:
        print(option)
    user_answer = input("\nYour answer (A, B, C, or D): ").strip().upper()
    return user_answer == answer

# Function to run the main trivia loop
def main():
    print("Welcome to CLI Trivia!\n")

     # List of questions, options, and correct answers
    questions = [
        ("Who wrote 'To Kill a Mockingbird'?", "A", ["A. Harper Lee", "B. J.K. Rowling", "C. George Orwell", "D. Mark Twain"]),
        ("What is the capital of France?", "C", ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"]),
        ("Which planet is known as the Red Planet?", "B", ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"]),
        ("What is the chemical symbol for water?", "A", ["A. H2O", "B. O2", "C. CO2", "D. H2"]),
        ("Which element is known as the King of the Jungle?", "A", ["A. Lion", "B. Elephant", "C. Tiger", "D. Leopard"]),
        ("Which language is primarily spoken in Brazil?", "B", ["A. Spanish", "B. Portuguese", "C. French", "D. English"]),
        ("What is the largest ocean on Earth?", "D", ["A. Atlantic", "B. Indian", "C. Arctic", "D. Pacific"]),
        ("[Is alex cool]", "[a]", ["A. yes", "B. no", "C. idk", "D.yesn't "]),
        ("[how do you change the isotope of an element ]", "[D]", ["A. change the number of protons", "B. Buy it tea", "C. remove a oxygen atom", "D. change the amount of neutrons"]),
        ("[who was the first president]", "[c]", ["A. abhraham lincon", "B. peter parker", "C. daddy gorge washington", "D. alexander hamilton"]),
       
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

    # Loop through the selected number of rounds
    asked_questions = set()  # Track asked questions
    for i in range(num_rounds):
        question, correct_answer, options = questions[i]
        correct = ask_question(question, correct_answer, options)
        asked_questions.add(question)
        if correct:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {correct_answer}.")
    
    # Final score output
    print(f"\nGame Over! Your score: {score} out of {num_rounds}")

if __name__ == "__main__":
    main()
