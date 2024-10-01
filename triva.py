import random

# Define the trivia questions and answers for each difficulty level
trivia_questions = {
    "Easy": [
        {"question": "What is the capital of France?", "answer": "paris"},
        {"question": "What color is the sky on a clear day?", "answer": "blue"},
        {"question": "What is 2 + 2?", "answer": "4"},
        {"question": "What is the largest mammal?", "answer": "blue whale"},
        {"question": "What fruit is known for having seeds on the outside?", "answer": "strawberry"},
        {"question": "How many continents are there?", "answer": "7"},
        {"question": "What is the name of the fairy in Peter Pan?", "answer": "tinkerbell"},
        {"question": "What is the main ingredient in guacamole?", "answer": "avocado"},
        {"question": "What do bees produce?", "answer": "honey"},
        {"question": "What is the chemical symbol for water?", "answer": "h2o"},
        {"question": "What animal is known as the king of the jungle?", "answer": "lion"},
        {"question": "What is the currency used in Japan?", "answer": "yen"},
        {"question": "What planet is known as the Red Planet?", "answer": "mars"},
        {"question": "What is the first letter of the alphabet?", "answer": "a"},
        {"question": "What is the largest ocean on Earth?", "answer": "pacific"},
        {"question": "In which month is Christmas celebrated?", "answer": "december"},
        {"question": "How many legs does a spider have?", "answer": "8"},
        {"question": "What is the name of Harry Potter's pet owl?", "answer": "hedwig"},
        {"question": "What is the smallest prime number?", "answer": "2"},
        {"question": "What is the main ingredient in bread?", "answer": "flour"},
        {"question": "Which planet is known for its rings?", "answer": "saturn"},
        {"question": "What is the capital of Italy?", "answer": "rome"},
        {"question": "What is the boiling point of water?", "answer": "100"},
        {"question": "Which month comes after June?", "answer": "july"},
        {"question": "How many sides does a triangle have?", "answer": "3"},
        {"question": "What animal is known for its ability to change colors?", "answer": "chameleon"},
        {"question": "What is the main language spoken in Brazil?", "answer": "portuguese"},
        {"question": "What is the tallest mountain in the world?", "answer": "everest"},
        {"question": "What is the name of the longest river in the world?", "answer": "nile"},
        {"question": "What gas do plants absorb from the atmosphere?", "answer": "carbon dioxide"},
        {"question": "What is the hardest natural substance on Earth?", "answer": "diamond"},
        {"question": "What is the process by which plants make their food called?", "answer": "photosynthesis"},
        {"question": "What is the primary language spoken in Canada?", "answer": "english"},
        {"question": "What is the name of the largest desert in the world?", "answer": "sahara"},
        {"question": "What is the capital of Australia?", "answer": "canberra"},
    ],
    "Medium": [
        {"question": "What is the currency used in the United Kingdom?", "answer": "pound"},
        {"question": "What is the name of the largest planet in our solar system?", "answer": "jupiter"},
        {"question": "What chemical element has the symbol 'O'?", "answer": "oxygen"},
        {"question": "Who wrote 'Romeo and Juliet'?", "answer": "shakespeare"},
        {"question": "What is the capital city of Canada?", "answer": "ottawa"},
        {"question": "In what year did the Titanic sink?", "answer": "1912"},
        {"question": "What is the hardest rock?", "answer": "diamond"},
        {"question": "What is the largest land animal?", "answer": "elephant"},
        {"question": "How many bones are in the adult human body?", "answer": "206"},
        {"question": "What is the longest river in South America?", "answer": "amazon"},
        {"question": "What is the most spoken language in the world?", "answer": "mandarin"},
        {"question": "What element does 'Na' represent on the periodic table?", "answer": "sodium"},
        {"question": "In which city is the famous landmark the Eiffel Tower located?", "answer": "paris"},
        {"question": "What is the name of the largest volcano in the world?", "answer": "mauna loa"},
        {"question": "What planet is known as the Morning Star?", "answer": "venus"},
        {"question": "What is the most common blood type?", "answer": "o"},
        {"question": "Which planet is closest to the sun?", "answer": "mercury"},
        {"question": "Who painted the Mona Lisa?", "answer": "da vinci"},
        {"question": "What is the capital of Egypt?", "answer": "cairo"},
        {"question": "What is the speed of light?", "answer": "299792458"},
        {"question": "What is the name of the fictional wizarding school in Harry Potter?", "answer": "hogwarts"},
        {"question": "What is the largest island in the world?", "answer": "greenland"},
        {"question": "What is the main ingredient in sushi?", "answer": "rice"},
        {"question": "Which animal is known as a 'panda bear'?", "answer": "giant panda"},
        {"question": "What is the primary gas in the Earth's atmosphere?", "answer": "nitrogen"},
        {"question": "What is the chemical symbol for gold?", "answer": "au"},
        {"question": "Who is known as the 'Father of Geometry'?", "answer": "euclid"},
        {"question": "What is the capital city of Thailand?", "answer": "bangkok"},
        {"question": "What is the largest ocean on Earth?", "answer": "pacific"},
        {"question": "What type of animal is a seahorse?", "answer": "fish"},
        {"question": "What year did World War II end?", "answer": "1945"},
        {"question": "What is the tallest building in the world?", "answer": "burj khalifa"},
        {"question": "What is the main ingredient in chocolate?", "answer": "cocoa"},
    ],
    "Hard": [
        {"question": "What is the square root of 144?", "answer": "12"},
        {"question": "What is the capital of Iceland?", "answer": "reykjavik"},
        {"question": "Who discovered penicillin?", "answer": "fleming"},
        {"question": "What is the chemical formula for table salt?", "answer": "nacl"},
        {"question": "What is the largest organ in the human body?", "answer": "skin"},
        {"question": "What is the name of the longest river in Asia?", "answer": "yangtze"},
        {"question": "What is the process by which plants absorb water called?", "answer": "osmosis"},
        {"question": "What is the most abundant element in the universe?", "answer": "hydrogen"},
        {"question": "What is the formula for calculating the area of a circle?", "answer": "pi*r^2"},
        {"question": "Who wrote 'The Odyssey'?", "answer": "homer"},
        {"question": "What is the capital of Nigeria?", "answer": "abuja"},
        {"question": "What is the chemical symbol for potassium?", "answer": "k"},
        {"question": "What is the main ingredient in hummus?", "answer": "chickpeas"},
        {"question": "What is the largest continent?", "answer": "asia"},
        {"question": "What is the unit of currency in Russia?", "answer": "ruble"},
        {"question": "What is the capital of Mongolia?", "answer": "ulaanbaatar"},
        {"question": "What is the primary component of the sun?", "answer": "hydrogen"},
        {"question": "What is the largest bird in the world?", "answer": "ostrich"},
        {"question": "Who is the author of 'Pride and Prejudice'?", "answer": "austen"},
        {"question": "What is the chemical formula for glucose?", "answer": "c6h12o6"},
        {"question": "What is the capital of Sri Lanka?", "answer": "sri jayawardenepura kotte"},
        {"question": "What is the primary gas released by plants during photosynthesis?", "answer": "oxygen"},
        {"question": "What is the most populated country in the world?", "answer": "china"},
        {"question": "What is the capital of Switzerland?", "answer": "bern"},
        {"question": "What is the currency used in South Africa?", "answer": "rand"},
        {"question": "What is the highest waterfall in the world?", "answer": "angel falls"},
        {"question": "Who painted 'The Starry Night'?", "answer": "van gogh"},
        {"question": "What is the currency of India?", "answer": "rupee"},
        {"question": "What is the fastest land animal?", "answer": "cheetah"},
        {"question": "What is the primary component of natural gas?", "answer": "methane"},
        {"question": "What is the name of the longest mountain range in the world?", "answer": "andes"},
        {"question": "What is the scientific study of insects called?", "answer": "entomology"},
        {"question": "What is the name of the galaxy that contains our solar system?", "answer": "milky way"},
        {"question": "What is the capital of Finland?", "answer": "helsinki"},
        {"question": "What is the main ingredient in traditional Japanese sake?", "answer": "rice"},
    ],
    "Extreme": [
        {"question": "What is the name of the first artificial Earth satellite?", "answer": "sputnik"},
        {"question": "What is the chemical formula for ammonia?", "answer": "nh3"},
        {"question": "Who developed the theory of relativity?", "answer": "einstein"},
        {"question": "What is the speed of sound?", "answer": "343"},
        {"question": "What is the only planet in our solar system that rotates on its side?", "answer": "uranus"},
        {"question": "What is the main ingredient in traditional pesto?", "answer": "basil"},
        {"question": "What is the name of the first human to journey into outer space?", "answer": "gagarin"},
        {"question": "What is the capital of Bhutan?", "answer": "thimphu"},
        {"question": "What is the hardest natural substance on Earth?", "answer": "diamond"},
        {"question": "What is the chemical symbol for silver?", "answer": "ag"},
        {"question": "What is the world's longest river?", "answer": "nile"},
        {"question": "What is the capital city of Azerbaijan?", "answer": "baku"},
        {"question": "What is the scientific name for the common cold?", "answer": "rhinovirus"},
        {"question": "What is the main ingredient in traditional tzatziki sauce?", "answer": "yogurt"},
        {"question": "What is the name of the first woman to win a Nobel Prize?", "answer": "curie"},
        {"question": "What is the capital city of Kazakhstan?", "answer": "nursultan"},
        {"question": "What is the chemical symbol for iron?", "answer": "fe"},
        {"question": "What is the largest planet in our solar system?", "answer": "jupiter"},
        {"question": "What is the primary language spoken in Egypt?", "answer": "arabic"},
        {"question": "What is the tallest mountain in North America?", "answer": "denali"},
        {"question": "What is the name of the world's largest desert?", "answer": "antarctica"},
        {"question": "What is the name of the first manned mission to land on the moon?", "answer": "apollo 11"},
        {"question": "What is the chemical formula for table sugar?", "answer": "c12h22o11"},
        {"question": "What is the main ingredient in traditional kimchi?", "answer": "cabbage"},
        {"question": "What is the capital of Turkmenistan?", "answer": "ashgabat"},
        {"question": "What is the primary gas found in the Earth's atmosphere?", "answer": "nitrogen"},
        {"question": "What is the name of the largest volcano in the solar system?", "answer": "olympus mons"},
        {"question": "What is the smallest country in the world?", "answer": "vatican city"},
        {"question": "What is the capital of Paraguay?", "answer": "asuncion"},
        {"question": "What is the name of the first cloned sheep?", "answer": "dolly"},
        {"question": "What is the longest river in Europe?", "answer": "volga"},
        {"question": "What is the largest organ inside the human body?", "answer": "liver"},
    ],
}

# Type-in questions
type_in_questions = [
    {"question": "What is your name?", "answer": "your name"},
    {"question": "What is your favorite color?", "answer": "any color"},
    {"question": "What is your favorite food?", "answer": "any food"},
    {"question": "What is your hometown?", "answer": "any town"},
    {"question": "What is your dream job?", "answer": "any job"},
    {"question": "What is your favorite hobby?", "answer": "any hobby"},
    {"question": "What is your favorite movie?", "answer": "any movie"},
    {"question": "What is your favorite book?", "answer": "any book"},
    {"question": "What is your favorite sport?", "answer": "any sport"},
    {"question": "What is your favorite animal?", "answer": "any animal"},
    {"question": "What is your favorite season?", "answer": "any season"},
    {"question": "What is your favorite game?", "answer": "any game"},
    {"question": "What is your favorite song?", "answer": "any song"},
    {"question": "What is your favorite TV show?", "answer": "any show"},
    {"question": "What is your favorite ice cream flavor?", "answer": "any flavor"},
    {"question": "What is your favorite dessert?", "answer": "any dessert"},
    {"question": "What is your favorite drink?", "answer": "any drink"},
    {"question": "What is your favorite holiday?", "answer": "any holiday"},
    {"question": "What is your favorite city?", "answer": "any city"},
    {"question": "What is your favorite childhood memory?", "answer": "any memory"},
]

# Function to run the trivia game
def run_trivia():
    print("WELCOME TO ALEX HARWOOD'S CLI TRIVIA GAME".center(80, '*'))
    print("\nSelect difficulty level:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    print("4. Extreme")
    print("5. Type-in")
    
    choice = input("Enter the number of your choice: ")
    
    if choice == "1":
        difficulty = "Easy"
    elif choice == "2":
        difficulty = "Medium"
    elif choice == "3":
        difficulty = "Hard"
    elif choice == "4":
        difficulty = "Extreme"
    elif choice == "5":
        difficulty = "Type-in"
    else:
        print("Invalid choice! Exiting the game.")
        return
    
    score = 0
    total_questions = 30 if difficulty != "Type-in" else 20
    questions = trivia_questions[difficulty] if difficulty != "Type-in" else type_in_questions

    random.shuffle(questions)
    questions = questions[:total_questions]

    for q in questions:
        answer = input(f"{q['question']} ").strip().lower()
        if answer == q['answer']:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {q['answer']}.")
    
    print(f"\nYour score: {score}/{total_questions}")

if __name__ == "__main__":
    run_trivia()
