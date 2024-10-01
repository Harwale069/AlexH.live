\import random

# Questions categorized by difficulty
questions = {
    "easy": [
        ("What is the capital of France?", ["Paris", "London", "Rome", "Berlin"], "Paris"),
        ("What is 2 + 2?", ["3", "4", "5", "6"], "4"),
        ("What color is the sky?", ["Blue", "Green", "Red", "Yellow"], "Blue"),
        ("What is the largest mammal?", ["Elephant", "Blue Whale", "Giraffe", "Rhino"], "Blue Whale"),
        ("What is the first letter of the alphabet?", ["A", "B", "C", "D"], "A"),
        ("How many colors are in a rainbow?", ["5", "6", "7", "8"], "7"),
        ("What is the name of the fairy in Peter Pan?", ["Tinkerbell", "Cinderella", "Aurora", "Snow White"], "Tinkerbell"),
        ("What is the boiling point of water?", ["100°C", "90°C", "80°C", "110°C"], "100°C"),
        ("Which animal is known as the King of the Jungle?", ["Lion", "Tiger", "Elephant", "Bear"], "Lion"),
        ("What is the capital of Japan?", ["Tokyo", "Seoul", "Beijing", "Bangkok"], "Tokyo"),
        ("What is the shape of the Earth?", ["Flat", "Cube", "Sphere", "Cylinder"], "Sphere"),
        ("What gas do plants absorb?", ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"], "Carbon Dioxide"),
        ("What is the color of an emerald?", ["Red", "Green", "Blue", "Yellow"], "Green"),
        ("What is the capital of Italy?", ["Rome", "Paris", "Madrid", "Lisbon"], "Rome"),
        ("Which planet is known as the Red Planet?", ["Earth", "Mars", "Jupiter", "Venus"], "Mars"),
        ("What is the main ingredient in guacamole?", ["Avocado", "Tomato", "Onion", "Pepper"], "Avocado"),
        ("Which country is known for the Eiffel Tower?", ["Spain", "Italy", "France", "Germany"], "France"),
        ("What is the largest ocean on Earth?", ["Atlantic", "Indian", "Arctic", "Pacific"], "Pacific"),
        ("What is the capital of Canada?", ["Toronto", "Ottawa", "Vancouver", "Montreal"], "Ottawa"),
        ("How many continents are there?", ["5", "6", "7", "8"], "7"),
        ("What is the fastest land animal?", ["Cheetah", "Lion", "Horse", "Elephant"], "Cheetah"),
    ],
    "medium": [
        ("What is the capital of Australia?", ["Sydney", "Canberra", "Melbourne", "Brisbane"], "Canberra"),
        ("What is the chemical symbol for gold?", ["Au", "Ag", "Pb", "Fe"], "Au"),
        ("Which planet is closest to the sun?", ["Earth", "Mars", "Mercury", "Venus"], "Mercury"),
        ("What is the largest organ in the human body?", ["Heart", "Liver", "Skin", "Lungs"], "Skin"),
        ("What is the smallest prime number?", ["1", "2", "3", "4"], "2"),
        ("Who wrote 'Romeo and Juliet'?", ["Mark Twain", "Charles Dickens", "William Shakespeare", "Jane Austen"], "William Shakespeare"),
        ("What is the main ingredient in pesto?", ["Basil", "Parsley", "Cilantro", "Mint"], "Basil"),
        ("What is the hardest natural substance?", ["Gold", "Iron", "Diamond", "Quartz"], "Diamond"),
        ("What year did the Titanic sink?", ["1910", "1912", "1914", "1916"], "1912"),
        ("What is the capital of Egypt?", ["Cairo", "Alexandria", "Giza", "Luxor"], "Cairo"),
        ("Which organ is responsible for pumping blood?", ["Liver", "Heart", "Lungs", "Kidneys"], "Heart"),
        ("What is the longest river in the world?", ["Amazon", "Nile", "Yangtze", "Mississippi"], "Nile"),
        ("Which country is known as the Land of the Rising Sun?", ["China", "Japan", "Thailand", "Korea"], "Japan"),
        ("What is the main language spoken in Brazil?", ["Spanish", "Portuguese", "English", "French"], "Portuguese"),
        ("What is the currency of Japan?", ["Yen", "Won", "Dollar", "Euro"], "Yen"),
        ("Who painted the Mona Lisa?", ["Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Claude Monet"], "Leonardo da Vinci"),
        ("What is the capital city of Canada?", ["Ottawa", "Toronto", "Montreal", "Vancouver"], "Ottawa"),
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
        ("What is the official language of Iran?", ["Persian", "Arabic", "Turkish", "Kurdish"], "Persian"),
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
    ("What is the main ingredient in sushi?", "Rice"),
    ("What is the capital of India?", "New Delhi"),
    ("How many bones are in the adult human body?", "206"),
    ("What is the hardest natural substance?", "Diamond"),
    ("What is the chemical formula for water?", "H2O")
]

def get_difficulty():
    while True:
        difficulty = input("Choose difficulty (easy, medium, hard, extreme, or type-in): ").lower()
        if difficulty in questions or difficulty == "type-in":
            return difficulty
        else:
            print("Invalid difficulty. Please try again.")

def select_questions(difficulty, num_questions):
    if difficulty == "type-in":
        return random.sample(type_in_questions, min(len(type_in_questions), num_questions))
    else:
        return random.sample(questions[difficulty], min(len(questions[difficulty]), num_questions))

def ask_question(question, options):
    print("\n" + question)
    for idx, option in enumerate(options):
        print(f"{idx + 1}. {option}")

def check_answer(user_answer, correct_answer, question_type):
    if question_type == "multiple-choice":
        return user_answer.strip().lower() in [correct_answer.lower(), str(options.index(correct_answer) + 1)]
    elif question_type == "type-in":
        return user_answer.strip().lower() == correct_answer.lower()

def trivia_game():
    print("\nWELCOME TO ALEX HARWOOD'S CLI TRIVIA GAME")
    total_score = 0
    rounds = 1
    global_leaderboard = []

    while True:
        difficulty = get_difficulty()
        num_questions = int(input("How many questions per round? (max 30): "))
        selected_questions = select_questions(difficulty, num_questions)

        for question in selected_questions:
            if difficulty == "type-in":
                question_text, correct_answer = question
                user_answer = input(question_text + " ")
                if check_answer(user_answer, correct_answer, "type-in"):
                    print("Correct!")
                    total_score += 1
                else:
                    print(f"Wrong! The correct answer was: {correct_answer}")
            else:
                question_text, options, correct_answer = question
                ask_question(question_text, options)
                user_answer = input("Your answer (type the option number or the answer): ")
                if check_answer(user_answer, correct_answer, "multiple-choice"):
                    print("Correct!")
                    total_score += 1
                else:
                    print(f"Wrong! The correct answer was: {correct_answer}")

        print(f"\nYour total score: {total_score} out of {len(selected_questions)}")
        rounds += 1

        play_again = input("Do you want to play another round? (yes/no): ").lower()
        if play_again != "yes":
            break

    print("Thank you for playing!")
    player_name = input("Enter your name for the leaderboard: ")
    global_leaderboard.append((player_name, total_score))
    print("Global Leaderboard:")
    for name, score in sorted(global_leaderboard, key=lambda x: x[1], reverse=True):
        print(f"{name}: {score}")

if __name__ == "__main__":
    trivia_game()
