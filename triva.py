import random
import time

# List of trivia questions with options and correct answer
trivia_questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. London", "B. Berlin", "C. Paris", "D. Madrid"],
        "answer": "C"
    },
    {
        "question": "Who wrote 'To Kill a Mockingbird'?",
        "options": ["A. Harper Lee", "B. J.K. Rowling", "C. George Orwell", "D. Mark Twain"],
        "answer": "A"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
        "answer": "C"
    },
    {
        "question": "In which year did World War II end?",
        "options": ["A. 1941", "B. 1945", "C. 1947", "D. 1950"],
        "answer": "B"
    },
    {
        "question": "What is the chemical symbol for gold?",
        "options": ["A. Au", "B. Ag", "C. Pt", "D. Hg"],
        "answer": "A"
    }
]

# Function to ask a random trivia question
def ask_question():
    # Pick a random question
    question = random.choice(trivia_questions)
    
    # Print the question and options
    print("\n" + question["question"])
    for option in question["options"]:
        print(option)
    
    # Get the user's answer
    answer = input("\nYour answer (A, B, C, or D): ").strip().upper()

    # Check if the answer is correct
    if answer == question["answer"]:
        print("\nCorrect! 🎉")
    else:
        print(f"\nWrong! The correct answer was {question['answer']}.")
    
    time.sleep(1)

# Main function to run the trivia game
def main():
    print("Welcome to CLI Trivia!")
    time.sleep(1)
    
    # Ask 3 random questions
    for _ in range(3):
        ask_question()

    print("\nThanks for playing! 🎮")

if __name__ == "__main__":
    main()
