import random
import time

def print_with_blinking_effect(text):
    for _ in range(5):
        print(f"\033[1;37;41m{text}\033[0m", flush=True)  # Red background
        time.sleep(0.5)
        print("\033[0m", flush=True)  # Clear line
        time.sleep(0.5)

def get_questions():
    return {
        'easy': [
            
    ("What is 2 + 2?", ["3", "4", "5", "6"], "4"),
    ("What color is the sky?", ["Blue", "Green", "Red", "Yellow"], "Blue"),
    ("What is the capital of France?", ["Berlin", "Madrid", "Paris", "Rome"], "Paris"),
    ("How many legs does a spider have?", ["6", "8", "10", "12"], "8"),
    ("What is the largest mammal?", ["Elephant", "Blue Whale", "Giraffe", "Hippo"], "Blue Whale"),
    ("What is 10 - 5?", ["2", "3", "5", "7"], "5"),
    ("What is the opposite of hot?", ["Cold", "Warm", "Cool", "Freezing"], "Cold"),
    ("How many days are in a leap year?", ["364", "365", "366", "367"], "366"),
    ("What shape has 4 equal sides?", ["Rectangle", "Square", "Triangle", "Circle"], "Square"),
    ("What is the boiling point of water?", ["90°C", "100°C", "110°C", "120°C"], "100°C"),
    ("What is the name of the fairy in Peter Pan?", ["Tinker Bell", "Wendy", "Cinderella", "Aurora"], "Tinker Bell"),
    ("Which planet is known as the Red Planet?", ["Earth", "Mars", "Jupiter", "Venus"], "Mars"),
    ("What is 5 + 3?", ["5", "6", "7", "8"], "8"),
    ("What is the currency used in Japan?", ["Yen", "Dollar", "Euro", "Pound"], "Yen"),
    ("How many colors are in a rainbow?", ["5", "6", "7", "8"], "7"),
    ("What is the main ingredient in guacamole?", ["Tomato", "Avocado", "Pepper", "Onion"], "Avocado"),
    ("What do bees make?", ["Honey", "Wax", "Nectar", "Pollen"], "Honey"),
    ("How many hours are in a day?", ["12", "24", "36", "48"], "24"),
    ("What is the name of the main character in Harry Potter?", ["Hermione", "Harry", "Ron", "Draco"], "Harry"),
    ("What is the fastest land animal?", ["Cheetah", "Lion", "Horse", "Elephant"], "Cheetah"),
    ("What is the smallest continent?", ["Asia", "Africa", "Antarctica", "Australia"], "Australia"),
    ("What is the largest ocean?", ["Atlantic", "Indian", "Arctic", "Pacific"], "Pacific"),
    ("What do you call a baby cat?", ["Kitten", "Pup", "Cub", "Calf"], "Kitten"),
    ("What is the largest organ in the human body?", ["Heart", "Liver", "Skin", "Lungs"], "Skin"),
    ("How many planets are in the solar system?", ["7", "8", "9", "10"], "8"),
    ("What is the primary language spoken in Brazil?", ["Spanish", "English", "Portuguese", "French"], "Portuguese"),
    ("Which animal is known as the king of the jungle?", ["Tiger", "Lion", "Elephant", "Bear"], "Lion"),
    ("What is the freezing point of water?", ["0°C", "-1°C", "32°F", "100°F"], "0°C"),
    ("What is the main ingredient in pasta?", ["Flour", "Rice", "Corn", "Oats"], "Flour"),
    ("What do you call the person who writes books?", ["Author", "Editor", "Publisher", "Writer"], "Author"),
    ("What is 12 divided by 4?", ["1", "2", "3", "4"], "3"),
    ("What is the tallest mountain in the world?", ["K2", "Kangchenjunga", "Mount Everest", "Lhotse"], "Mount Everest"),
    ("What do you use to write on a blackboard?", ["Chalk", "Marker", "Pen", "Pencil"], "Chalk"),
]

        ],
        'medium': [
            
    ("What is the capital of Australia?", ["Sydney", "Canberra", "Melbourne", "Brisbane"], "Canberra"),
    ("Which element has the chemical symbol O?", ["Osmium", "Oxygen", "Gold", "Silver"], "Oxygen"),
    ("Who wrote 'Romeo and Juliet'?", ["Charles Dickens", "Mark Twain", "William Shakespeare", "Jane Austen"], "William Shakespeare"),
    ("What is the longest river in the world?", ["Amazon", "Nile", "Yangtze", "Mississippi"], "Nile"),
    ("What is the process of converting a liquid into a gas?", ["Condensation", "Evaporation", "Sublimation", "Melting"], "Evaporation"),
    ("Which planet is known for its rings?", ["Earth", "Mars", "Jupiter", "Saturn"], "Saturn"),
    ("What is the capital of Canada?", ["Ottawa", "Toronto", "Vancouver", "Montreal"], "Ottawa"),
    ("What is the hardest natural substance on Earth?", ["Gold", "Diamond", "Iron", "Copper"], "Diamond"),
    ("What is the largest desert in the world?", ["Sahara", "Arabian", "Gobi", "Antarctic"], "Antarctic"),
    ("What year did World War II end?", ["1945", "1944", "1943", "1942"], "1945"),
    ("Who painted the Mona Lisa?", ["Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Claude Monet"], "Leonardo da Vinci"),
    ("What is the main ingredient in hummus?", ["Chickpeas", "Lentils", "Beans", "Rice"], "Chickpeas"),
    ("Which gas do plants absorb from the atmosphere?", ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"], "Carbon Dioxide"),
    ("What is the formula for calculating the area of a circle?", ["πr^2", "2πr", "πd", "πr"], "πr^2"),
    ("What is the smallest prime number?", ["1", "2", "3", "5"], "2"),
    ("In which country is the Great Pyramid of Giza located?", ["Egypt", "Greece", "Mexico", "India"], "Egypt"),
    ("What is the term for animals that only eat plants?", ["Carnivores", "Herbivores", "Omnivores", "Insectivores"], "Herbivores"),
    ("What is the speed of light?", ["299,792 km/s", "150,000 km/s", "3,000 km/s", "300,000 km/s"], "299,792 km/s"),
    ("Which country gifted the Statue of Liberty to the United States?", ["Germany", "France", "Italy", "England"], "France"),
    ("What is the currency of Russia?", ["Ruble", "Dollar", "Euro", "Pound"], "Ruble"),
    ("What is the largest internal organ in the human body?", ["Heart", "Liver", "Lungs", "Kidneys"], "Liver"),
    ("What is the capital of Italy?", ["Rome", "Milan", "Venice", "Florence"], "Rome"),
    ("Who is known as the Father of Geometry?", ["Isaac Newton", "Euclid", "Pythagoras", "Archimedes"], "Euclid"),
    ("What does DNA stand for?", ["Deoxyribonucleic Acid", "Dioxyribonucleic Acid", "Deoxyribonucleus Acid", "Dioxyribonucleus Acid"], "Deoxyribonucleic Acid"),
    ("Which ocean is the largest?", ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"], "Pacific Ocean"),
    ("What year did the Titanic sink?", ["1912", "1910", "1905", "1915"], "1912"),
    ("Who discovered penicillin?", ["Marie Curie", "Alexander Fleming", "Louis Pasteur", "Isaac Newton"], "Alexander Fleming"),
    ("What is the largest island in the world?", ["Australia", "Greenland", "New Guinea", "Borneo"], "Greenland"),
]

        ],
        'hard': [
        
    ("What is the capital of Bhutan?", ["Thimphu", "Kathmandu", "Dhaka", "Colombo"], "Thimphu"),
    ("Who is the author of 'The Hitchhiker's Guide to the Galaxy'?", ["Douglas Adams", "Isaac Asimov", "Philip K. Dick", "Arthur C. Clarke"], "Douglas Adams"),
    ("What is the principle behind the operation of a refrigerator?", ["Thermodynamics", "Electromagnetism", "Optics", "Kinematics"], "Thermodynamics"),
    ("What is the first element on the periodic table?", ["Hydrogen", "Helium", "Lithium", "Beryllium"], "Hydrogen"),
    ("Who invented the telephone?", ["Thomas Edison", "Alexander Graham Bell", "Nikola Tesla", "Graham Bell"], "Alexander Graham Bell"),
    ("What is the longest bone in the human body?", ["Femur", "Tibia", "Fibula", "Humerus"], "Femur"),
    ("What is the capital of Norway?", ["Oslo", "Stockholm", "Copenhagen", "Helsinki"], "Oslo"),
    ("What is the currency of South Africa?", ["Rand", "Dollar", "Euro", "Pound"], "Rand"),
    ("What is the smallest country in the world?", ["Monaco", "Nauru", "Vatican City", "Malta"], "Vatican City"),
    ("What is the chemical formula for table salt?", ["NaCl", "KCl", "CaCO3", "MgCl2"], "NaCl"),
    ("Who painted the ceiling of the Sistine Chapel?", ["Raphael", "Michelangelo", "Leonardo da Vinci", "Botticelli"], "Michelangelo"),
    ("What is the rarest blood type?", ["A+", "O-", "AB-", "B+"], "AB-"),
    ("In which year did the Berlin Wall fall?", ["1987", "1989", "1990", "1991"], "1989"),
    ("What is the most abundant gas in the Earth's atmosphere?", ["Oxygen", "Nitrogen", "Carbon Dioxide", "Argon"], "Nitrogen"),
    ("Who wrote the 'Iliad' and the 'Odyssey'?", ["Homer", "Virgil", "Ovid", "Sophocles"], "Homer"),
    ("What is the second most spoken language in the world?", ["Mandarin", "Spanish", "English", "Hindi"], "Spanish"),
    ("What is the most common isotope of carbon?", ["C-12", "C-13", "C-14", "C-11"], "C-12"),
    ("What is the capital of Kazakhstan?", ["Astana", "Almaty", "Tashkent", "Bishkek"], "Astana"),
    ("What is the tallest building in the world?", ["Burj Khalifa", "Shanghai Tower", "One World Trade Center", "Taipei 101"], "Burj Khalifa"),
    ("Which planet has the most moons?", ["Earth", "Mars", "Jupiter", "Saturn"], "Jupiter"),
    ("What is the main ingredient in traditional Japanese sake?", ["Rice", "Wheat", "Barley", "Corn"], "Rice"),
    ("What is the term for a group of lions?", ["Pack", "Herd", "Pride", "Flock"], "Pride"),
    ("What is the name of the largest volcano in the solar system?", ["Mauna Kea", "Kilimanjaro", "Olympus Mons", "Mount Everest"], "Olympus Mons"),
    ("What is the common name for the condition hypermetropia?", ["Nearsightedness", "Farsightedness", "Color blindness", "Astigmatism"], "Farsightedness"),
    ("What is the largest bone in the human body?", ["Humerus", "Tibia", "Femur", "Pelvis"], "Femur"),
    ("What was the first country to grant women the right to vote?", ["New Zealand", "Australia", "United States", "Finland"], "New Zealand"),
    ("What is the primary ingredient in tofu?", ["Soybeans", "Peas", "Wheat", "Rice"], "Soybeans"),
]

        ]
    }

def ask_question(question, options, correct_answer):
    print(question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    
    while True:
        try:
            answer = int(input("Your answer (1-4): ")) - 1
            if answer < 0 or answer >= len(options):
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")

    if options[answer] == correct_answer:
        print("Correct!\n")
        return True
    else:
        print(f"Wrong! The correct answer was: {correct_answer}\n")
        return False

def play_game():
    questions = get_questions()
    difficulty = input("Choose difficulty (easy, medium, hard): ").lower()

    if difficulty not in questions:
        print("Invalid difficulty. Please choose from easy, medium, or hard.")
        return

    score = 0
    total_questions = len(questions[difficulty])

    for question_data in random.sample(questions[difficulty], total_questions):
        question, options, correct_answer = question_data
        if ask_question(question, options, correct_answer):
            score += 1

    print(f"Your final score is: {score}/{total_questions}")

def main():
    print_with_blinking_effect("WELCOME TO ALEX HARWOOD'S CLI TRIVIA GAME")
    print("\033[1;31mWARNING: Please turn on Caps Lock for better experience!\033[0m")  # Red warning
    play_game()

if __name__ == "__main__":
    main()
