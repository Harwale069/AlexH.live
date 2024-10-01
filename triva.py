import random
import time

# Questions for all difficulties
questions_easy = [
    {
        'question': "What is the capital of France?",
        'answers': ["paris", "Paris"],
        'correct': 0
    },
    {
        'question': "What color do you get when you mix red and white?",
        'answers': ["pink", "Pink"],
        'correct': 0
    },
    # Add more easy questions (total 30)
]

questions_medium = [
    {
        'question': "What is the largest planet in our solar system?",
        'answers': ["jupiter", "Jupiter"],
        'correct': 0
    },
    {
        'question': "In which year did the Titanic sink?",
        'answers': ["1912"],
        'correct': 0
    },
    # Add more medium questions (total 30)
]

questions_hard = [
    {
        'question': "What is the chemical symbol for Gold?",
        'answers': ["au", "Au"],
        'correct': 0
    },
    {
        'question': "What is the hardest natural substance on Earth?",
        'answers': ["diamond", "Diamond"],
        'correct': 0
    },
    # Add more hard questions (total 30)
]

questions_extreme = [
    {
        'question': "What is the speed of light in vacuum (in m/s)?",
        'answers': ["299792458"],
        'correct': 0
    },
    {
        'question': "What is the derivative of x^2?",
        'answers': ["2x"],
        'correct': 0
    },
    # Add more extreme questions (total 30)
]

# Type-in difficulty questions
questions_type_in = [
    {
        'question': "Name a color in the rainbow.",
        'answers': ["red", "orange", "yellow", "green", "blue", "indigo", "violet"],
        'correct': 0
    },
    {
        'question': "What is your favorite ice cream flavor?",
        'answers': ["vanilla", "chocolate", "strawberry", "mint", "cookie dough"],
        'correct': 0
    },
    # Add more type-in questions (total 20)
]

# Math game mode
def math_game(num_questions):
    score = 0
    for _ in range(num_questions):
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        correct_answer = a + b
        answer = input(f"What is {a} + {b}? ")
        if answer.isdigit() and int(answer) == correct_answer:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {correct_answer}.")
    print(f"Your score: {score}/{num_questions}")

def trivia_game(difficulty, num_questions):
    score = 0
    if difficulty == 'easy':
        questions = random.sample(questions_easy, num_questions)
    elif difficulty == 'medium':
        questions = random.sample(questions_medium, num_questions)
    elif difficulty == 'hard':
        questions = random.sample(questions_hard, num_questions)
    elif difficulty == 'extreme':
        questions = random.sample(questions_extreme, num_questions)
    else:  # type-in difficulty
        questions = random.sample(questions_type_in, num_questions)

    for q in questions:
        answer = input(q['question'] + " ")
        if answer in q['answers']:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was: {', '.join(q['answers'])}")

    print(f"Your score: {score}/{num_questions}")

def main():
    print("WELCOME TO ALEX HARWOOD'S CLI TRIVIA GAME\n")
    time.sleep(1)
    
    while True:
        mode = input("Select game mode: 1) Trivia 2) Math 3) Exit: ")
        
        if mode == '1':
            difficulty = input("Select difficulty (easy, medium, hard, extreme, type-in): ").lower()
            num_questions = int(input("How many questions per round? (up to 30): "))
            if difficulty == 'extreme' and score < (num_questions / 2):
                print("You must beat the hard difficulty with at least half the questions correct to access extreme difficulty.")
                continue
            trivia_game(difficulty, num_questions)

        elif mode == '2':
            num_questions = int(input("How many math questions per round? (up to 30): "))
            math_game(num_questions)

        elif mode == '3':
            print("Thanks for playing!")
            break
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()
