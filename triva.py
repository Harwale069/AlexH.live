\import random

# Questions categorized by difficulty
questions = {
    "easy": [
        ("What is the capital of France?", ["Paris", "London", "Berlin", "Madrid"], "Paris"),
        ("What is 2 + 2?", ["3", "4", "5", "6"], "4"),
        ("What color is the sky?", ["Blue", "Green", "Red", "Yellow"], "Blue"),
        ("What is the largest mammal?", ["Elephant", "Blue Whale", "Giraffe", "Shark"], "Blue Whale"),
        ("What is the capital of the USA?", ["Washington, D.C.", "New York", "Los Angeles", "Chicago"], "Washington, D.C."),
        ("What is the smallest prime number?", ["0", "1", "2", "3"], "2"),
        ("What is the main ingredient in guacamole?", ["Tomato", "Avocado", "Lettuce", "Pepper"], "Avocado"),
        ("Which planet is known as the Red Planet?", ["Mars", "Jupiter", "Saturn", "Earth"], "Mars"),
        ("What is the chemical symbol for gold?", ["Ag", "Au", "Pb", "Fe"], "Au"),
        ("What is the largest ocean on Earth?", ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"], "Pacific Ocean"),
        ("What is the capital of Canada?", ["Toronto", "Ottawa", "Vancouver", "Montreal"], "Ottawa"),
        ("What is the name of the fairy in Peter Pan?", ["Wendy", "Tinker Bell", "Dorothy", "Alice"], "Tinker Bell"),
        ("How many colors are there in a rainbow?", ["5", "6", "7", "8"], "7"),
        ("What is the capital of Italy?", ["Rome", "Milan", "Venice", "Florence"], "Rome"),
        ("What is the freezing point of water?", ["0°C", "32°F", "100°F", "100°C"], "0°C"),
        ("What is the longest river in the world?", ["Amazon", "Nile", "Yangtze", "Mississippi"], "Nile"),
        ("What is the largest planet in our solar system?", ["Earth", "Mars", "Jupiter", "Saturn"], "Jupiter"),
        ("What is the currency of Japan?", ["Yen", "Dollar", "Euro", "Pound"], "Yen"),
        ("What is the capital of Australia?", ["Sydney", "Canberra", "Melbourne", "Brisbane"], "Canberra"),
        ("What is the main ingredient in bread?", ["Flour", "Sugar", "Salt", "Water"], "Flour"),
        ("What is the capital of Egypt?", ["Cairo", "Alexandria", "Luxor", "Aswan"], "Cairo"),
    ],
    "medium": [
        ("What is the largest desert in the world?", ["Sahara", "Arabian", "Gobi", "Antarctic"], "Antarctic"),
        ("Who wrote 'Romeo and Juliet'?", ["Mark Twain", "Jane Austen", "William Shakespeare", "Charles Dickens"], "William Shakespeare"),
        ("What is the capital of Brazil?", ["Brasilia", "Rio de Janeiro", "São Paulo", "Salvador"], "Brasilia"),
        ("What is the hardest natural substance?", ["Gold", "Iron", "Diamond", "Graphite"], "Diamond"),
        ("Which planet is known for its rings?", ["Earth", "Mars", "Saturn", "Venus"], "Saturn"),
        ("Who painted the Mona Lisa?", ["Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Claude Monet"], "Leonardo da Vinci"),
        ("What is the capital city of Canada?", ["Toronto", "Ottawa", "Vancouver", "Montreal"], "Ottawa"),
        ("Who discovered penicillin?", ["Marie Curie", "Alexander Fleming", "Isaac Newton", "Albert Einstein"], "Alexander Fleming"),
        ("What is the largest organ in the human body?", ["Heart", "Liver", "Skin", "Lung"], "Skin"),
        ("What is the main language spoken in Brazil?", ["Spanish", "Portuguese", "French", "English"], "Portuguese"),
        ("What is the boiling point of water?", ["100°C", "90°C", "110°C", "80°C"], "100°C"),
        ("What is the capital of Thailand?", ["Bangkok", "Hanoi", "Phnom Penh", "Kuala Lumpur"], "Bangkok"),
        ("What is the tallest mountain in the world?", ["K2", "Kangchenjunga", "Lhotse", "Mount Everest"], "Mount Everest"),
        ("What is the primary ingredient in tofu?", ["Soybeans", "Peas", "Rice", "Corn"], "Soybeans"),
        ("What is the capital of Russia?", ["Moscow", "Saint Petersburg", "Kiev", "Minsk"], "Moscow"),
        ("What is the chemical formula for salt?", ["NaCl", "H2O", "CO2", "O2"], "NaCl"),
        ("What is the largest land animal?", ["Elephant", "Giraffe", "Rhino", "Hippo"], "Elephant"),
        ("What is the national sport of Japan?", ["Soccer", "Baseball", "Sumo", "Martial Arts"], "Sumo"),
        ("What is the capital of Mexico?", ["Mexico City", "Guadalajara", "Cancún", "Tijuana"], "Mexico City"),
        ("What is the main ingredient in pesto?", ["Basil", "Spinach", "Parsley", "Kale"], "Basil"),
    ],
    "hard": [
        ("What is the smallest country in the world?", ["Monaco", "Nauru", "Vatican City", "San Marino"], "Vatican City"),
        ("Who was the first female Prime Minister of the UK?", ["Theresa May", "Margaret Thatcher", "Angela Merkel", "Golda Meir"], "Margaret Thatcher"),
        ("What is the most abundant element in the universe?", ["Hydrogen", "Oxygen", "Carbon", "Helium"], "Hydrogen"),
        ("What is the only planet that rotates on its side?", ["Uranus", "Venus", "Neptune", "Saturn"], "Uranus"),
        ("What is the capital city of the Philippines?", ["Manila", "Quezon City", "Cebu City", "Davao City"], "Manila"),
        ("What is the largest species of shark?", ["Great White", "Hammerhead", "Whale Shark", "Tiger Shark"], "Whale Shark"),
        ("What is the capital of Libya?", ["Tripoli", "Cairo", "Algiers", "Tunis"], "Tripoli"),
        ("What is the study of fungi called?", ["Mycology", "Botany", "Zoology", "Entomology"], "Mycology"),
        ("What is the most populous city in the world?", ["Tokyo", "Shanghai", "Beijing", "Delhi"], "Tokyo"),
        ("What is the national flower of Japan?", ["Rose", "Cherry Blossom", "Lotus", "Tulip"], "Cherry Blossom"),
        ("What is the rarest type of diamond?", ["Pink", "Yellow", "Blue", "Green"], "Blue"),
        ("What is the currency of Sweden?", ["Krona", "Euro", "Dollar", "Pound"], "Krona"),
        ("What is the main ingredient in hummus?", ["Chickpeas", "Lentils", "Beans", "Peas"], "Chickpeas"),
        ("What is the capital of Serbia?", ["Belgrade", "Zagreb", "Budapest", "Sarajevo"], "Belgrade"),
        ("What is the most expensive spice in the world?", ["Saffron", "Vanilla", "Cinnamon", "Pepper"], "Saffron"),
        ("What is the longest river in Asia?", ["Yangtze", "Mekong", "Ganges", "Indus"], "Yangtze"),
        ("What is the capital of Kazakhstan?", ["Astana", "Almaty", "Tashkent", "Bishkek"], "Astana"),
        ("What is the official language of Iran?", ["Persian", "Arabic", "Turkish", "Kurdish"], "Persian")
    ]
}

# Type-in questions
type_in_questions = [
    ("What is your name?", "Any"),
    ("What is the capital of Spain?", "Madrid"),
    ("What color is an orange?", "Orange"),
    ("How many days are in a leap year?", "366"),
    ("What is the first element in the periodic table?", "Hydrogen"),
    ("What is the largest organ in the human body?", "Skin"),
    ("How many states are there in the USA?", "50"),
    ("What is the speed of light in a vacuum?", "299792458"),
    ("What is the main ingredient in chocolate?", "Cocoa"),
    ("What is the capital of Italy?", "Rome"),
    ("How many teeth does an adult human have?", "32"),
    ("What is the longest word in the English language?", "Pneumonoultramicroscopicsilicovolcanoconiosis"),
    ("What is the currency of the United Kingdom?", "Pound"),
    ("What is the largest continent?", "Asia"),
    ("What is the capital of Australia?", "Canberra"),
    ("What is the most spoken language in the world?", "Mandarin"),
    ("What is the highest mountain in Africa?", "Kilimanjaro"),
    ("What is the capital of Canada?", "Ottawa"),
    ("What is the chemical symbol for gold?", "Au"),
    ("What is the largest ocean?", "Pacific Ocean")
]

# Leaderboard
leaderboard = []

# Game functions
def welcome_message():
    print("\033[5mWELCOME TO ALEX HARWOOD'S CLI TRIVIA GAME\033[0m")

def ask_question(question, options, correct_answer):
    print("\n" + question)
    for index, option in enumerate(options):
        print(f"{index + 1}. {option}")
    answer = input("Your answer (1-4): ")
    return options[int(answer) - 1] == correct_answer

def ask_type_in_question(question, correct_answer):
    answer = input(question + " ")
    return answer.strip().lower() == correct_answer.strip().lower()

def play_game(difficulty, question_set):
    score = 0
    total_questions = 30 if difficulty != "type" else len(type_in_questions)

    for i in range(total_questions):
        if difficulty == "type":
            question, correct_answer = random.choice(type_in_questions)
            correct = ask_type_in_question(question, correct_answer)
        else:
            question, options, correct_answer = random.choice(question_set)
            correct = ask_question(question, options, correct_answer)

        if correct:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {correct_answer}")

    return score

def update_leaderboard(name, score):
    leaderboard.append((name, score))
    leaderboard.sort(key=lambda x: x[1], reverse=True)

def show_leaderboard():
    print("\n--- Leaderboard ---")
    for index, (name, score) in enumerate(leaderboard):
        print(f"{index + 1}. {name}: {score} points")

def main():
    welcome_message()

    while True:
        name = input("Enter your name: ")
        difficulty = input("Choose difficulty (easy, medium, hard, type): ").lower()

        if difficulty == "easy":
            score = play_game("easy", questions["easy"])
        elif difficulty == "medium":
            score = play_game("medium", questions["medium"])
        elif difficulty == "hard":
            score = play_game("hard", questions["hard"])
        elif difficulty == "type":
            score = play_game("type", None)
        else:
            print("Invalid difficulty level. Please try again.")
            continue

        print(f"\nYour score: {score}/{30}")
        update_leaderboard(name, score)
        show_leaderboard()

        play_again = input("Do you want to play another round? (y/n): ").lower()
        if play_again != 'y':
            break

if __name__ == "__main__":
    main()
