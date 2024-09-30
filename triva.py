import random
import os
import time
from threading import Timer

# Function to print blinking text (hotel sign style)
def print_blinking_text():
    text = "WELCOME TO ALEX HARWOOD'S CLI TRIVIA GAME"
    for _ in range(3):  # Blinks three times
        print(f"\033[1;33;40m{'*' * 3} {text} {'*' * 3}\033[0m", end="\r", flush=True)
        time.sleep(0.5)
        print(" " * len(text) * 2, end="\r", flush=True)
        time.sleep(0.5)
    print(f"\033[1;33;40m{'*' * 3} {text} {'*' * 3}\033[0m")  # Final show

# Function to ask a trivia question
def ask_question(question, answer, options=None):
    print("\n" + question)
    if options:
        for option in options:
            print(option)
        user_answer = input("\nYour answer (A, B, C, or D): ").strip().upper()
    else:
        user_answer = input("\nYour answer: ").strip().lower()
    return user_answer == answer.lower()

# Function to save the leaderboard globally (this assumes we are syncing to a shared file location)
def save_leaderboard(player_name, score, rounds_played, correct, incorrect):
    with open("global_leaderboard.txt", "a") as f:
        f.write(f"{player_name}: {score} points, {correct} correct, {incorrect} incorrect, {score}/{rounds_played}\n")

# Function to display the leaderboard
def display_leaderboard():
    if os.path.exists("global_leaderboard.txt"):
        with open("global_leaderboard.txt", "r") as f:
            leaderboard = f.readlines()
            print("\nGlobal Leaderboard:")
            for entry in leaderboard:
                print(entry.strip())
    else:
        print("\nNo leaderboard data found.")

# Function to calculate points based on difficulty
def calculate_points(difficulty, correct_ratio):
    difficulty_multiplier = {"Easy": 1, "Medium": 2, "Hard": 3}
    return int(10 * difficulty_multiplier[difficulty] * correct_ratio)

# Function to run the main trivia loop
def main():
    print_blinking_text()

    while True:
        # List of questions, options, and correct answers categorized by difficulty
        questions_by_difficulty = {
            "Easy": [
                ("Who wrote 'To Kill a Mockingbird'?", "A", ["A. Harper Lee", "B. J.K. Rowling", "C. George Orwell", "D. Mark Twain"]),
                ("What is the capital of France?", "C", ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"]),
                ("Name a color in the rainbow.", "rainbow", None),
                ("What is the chemical symbol for water?", "H2O", None),
            ],
            "Medium": [
                ("Who wrote '1984'?", "C", ["A. Aldous Huxley", "B. J.D. Salinger", "C. George Orwell", "D. F. Scott Fitzgerald"]),
                ("What is the boiling point of water?", "D", ["A. 90°C", "B. 80°C", "C. 100°F", "D. 100°C"]),
            ],
            "Hard": [
                ("Which novel begins with the line 'Call me Ishmael'?", "C", ["A. The Great Gatsby", "B. To Kill a Mockingbird", "C. Moby Dick", "D. Brave New World"]),
                ("What is the speed of light?", "300000", None),
            ]
        }

        # Get the difficulty level from the user
        difficulty = ""
        while difficulty not in questions_by_difficulty.keys():
            difficulty = input("Select difficulty (Easy, Medium, Hard): ").capitalize()
            if difficulty not in questions_by_difficulty.keys():
                print("Please choose a valid difficulty level.")

        # Select questions based on difficulty
        questions = questions_by_difficulty[difficulty]

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

        # Set score and correct/incorrect counters
        score = 0
        correct_answers = 0
        incorrect_answers = 0

        # Ask for player's name for leaderboard
        player_name = input("Enter your name for the leaderboard: ")

        # Loop through the selected number of rounds
        asked_questions = set()  # Track asked questions
        for i in range(num_rounds):
            while True:
                question, correct_answer, options = random.choice(questions)
                if question not in asked_questions:
                    asked_questions.add(question)
                    break
            correct = ask_question(question, correct_answer, options)
            if correct:
                print("Correct!")
                correct_answers += 1
            else:
                print(f"Wrong! The correct answer was {correct_answer}.")
                incorrect_answers += 1

        # Calculate points based on performance
        correct_ratio = correct_answers / num_rounds if num_rounds > 0 else 0
        score = calculate_points(difficulty, correct_ratio)

        # Final score output
        print(f"\nGame Over! Your score: {score} points")

        # Save the score to the global leaderboard
        save_leaderboard(player_name, score, num_rounds, correct_answers, incorrect_answers)

        # Display the leaderboard
        display_leaderboard()

        # Ask if they want to play another round
        play_again = input("\nWould you like to play another round? (yes/no): ").strip().lower()
        if play_again != "yes":
            break

if __name__ == "__main__":
    main()
