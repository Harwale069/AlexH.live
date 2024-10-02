import random
import os
import time

def blink_text(text, blink_times=5, blink_speed=0.5):
    for _ in range(blink_times):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(text)
        time.sleep(blink_speed)
        os.system('cls' if os.name == 'nt' else 'clear')
        time.sleep(blink_speed)

class TriviaGame:
    def __init__(self):
        self.score = 0
        self.rounds = 0
        self.correct_answers = 0
        self.incorrect_answers = 0
        self.extreme_unlocked = False

        # Questions for each category (25 fully written questions for each difficulty)
        self.questions = {
            'Easy': [
                ("What is the hardest natural substance on Earth?", ["Diamond", "Gold", "Iron", "Platinum"], "Diamond"),
                ("What is the capital of France?", ["Berlin", "Madrid", "Paris", "Lisbon"], "Paris"),
                ("What is 2 + 2?", ["3", "4", "5", "6"], "4"),
                ("Which planet is known as the Red Planet?", ["Earth", "Mars", "Jupiter", "Venus"], "Mars"),
                ("What is the largest mammal?", ["Elephant", "Blue Whale", "Giraffe", "Shark"], "Blue Whale"),
                ("What color are bananas?", ["Green", "Blue", "Yellow", "Red"], "Yellow"),
                ("What is the freezing point of water?", ["32°F", "0°C", "100°C", "50°F"], "0°C"),
                ("Which animal barks?", ["Cat", "Cow", "Dog", "Bird"], "Dog"),
                ("How many days are in a week?", ["5", "6", "7", "8"], "7"),
                ("What is the chemical symbol for water?", ["H2", "O2", "H2O", "CO2"], "H2O"),
                ("Which shape has 4 equal sides?", ["Triangle", "Square", "Circle", "Hexagon"], "Square"),
                ("Which fruit is known for having a crown?", ["Banana", "Pineapple", "Mango", "Orange"], "Pineapple"),
                ("Which ocean is the largest?", ["Atlantic", "Indian", "Pacific", "Southern"], "Pacific"),
                ("How many colors are in the rainbow?", ["5", "6", "7", "8"], "7"),
                ("Which holiday is celebrated on December 25?", ["Halloween", "Thanksgiving", "Christmas", "Easter"], "Christmas"),
                ("What is the smallest prime number?", ["1", "2", "3", "4"], "2"),
                ("Which animal is known for having a long neck?", ["Horse", "Giraffe", "Dog", "Elephant"], "Giraffe"),
                ("Which bird is the symbol of the United States?", ["Eagle", "Owl", "Dove", "Crow"], "Eagle"),
                ("What is the first letter of the alphabet?", ["B", "A", "C", "D"], "A"),
                ("Which month has 28 or 29 days?", ["January", "February", "March", "April"], "February"),
                ("How many wheels does a tricycle have?", ["2", "3", "4", "5"], "3"),
                ("Which insect makes honey?", ["Bee", "Ant", "Butterfly", "Spider"], "Bee"),
                ("What is the primary color of grass?", ["Yellow", "Red", "Green", "Blue"], "Green"),
                ("Which planet is closest to the sun?", ["Venus", "Mercury", "Earth", "Mars"], "Mercury"),
                ("How many legs does a spider have?", ["6", "7", "8", "10"], "8")
            ],
            'Medium': [
                ("What is the smallest country in the world?", ["Vatican City", "Monaco", "San Marino", "Liechtenstein"], "Vatican City"),
                ("What is the largest desert on Earth?", ["Sahara", "Gobi", "Arctic", "Antarctic"], "Antarctic"),
                ("Which element does 'O' represent on the periodic table?", ["Oxygen", "Osmium", "Oganesson", "Oxide"], "Oxygen"),
                ("Who wrote 'Romeo and Juliet'?", ["Charles Dickens", "Jane Austen", "William Shakespeare", "Leo Tolstoy"], "William Shakespeare"),
                ("What is the square root of 144?", ["10", "11", "12", "13"], "12"),
                ("Which country is famous for the Eiffel Tower?", ["Germany", "France", "Italy", "Spain"], "France"),
                ("Which organ in the human body pumps blood?", ["Liver", "Lungs", "Brain", "Heart"], "Heart"),
                ("Which war was fought between the North and South regions of the United States?", ["World War I", "World War II", "Civil War", "Revolutionary War"], "Civil War"),
                ("What is the largest bone in the human body?", ["Femur", "Skull", "Humerus", "Tibia"], "Femur"),
                ("What is the capital of Japan?", ["Beijing", "Seoul", "Tokyo", "Bangkok"], "Tokyo"),
                ("Which continent is Australia in?", ["Asia", "Europe", "Africa", "Australia"], "Australia"),
                ("Which gas do plants absorb from the atmosphere?", ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"], "Carbon Dioxide"),
                ("Which instrument has 88 keys?", ["Guitar", "Violin", "Drum", "Piano"], "Piano"),
                ("How many bones are in the adult human body?", ["200", "206", "212", "220"], "206"),
                ("Which planet is known for its rings?", ["Mars", "Jupiter", "Saturn", "Uranus"], "Saturn"),
                ("Who invented the telephone?", ["Alexander Graham Bell", "Thomas Edison", "Nikola Tesla", "Henry Ford"], "Alexander Graham Bell"),
                ("What is the hottest planet in the solar system?", ["Venus", "Mars", "Jupiter", "Mercury"], "Venus"),
                ("Which is the longest river in the world?", ["Amazon", "Nile", "Yangtze", "Mississippi"], "Nile"),
                ("Which artist painted the Mona Lisa?", ["Van Gogh", "Michelangelo", "Leonardo da Vinci", "Raphael"], "Leonardo da Vinci"),
                ("Which metal is the best conductor of electricity?", ["Gold", "Copper", "Aluminum", "Silver"], "Silver"),
                ("How many teeth does an adult human have?", ["28", "30", "32", "34"], "32"),
                ("Which vitamin is known as the sunshine vitamin?", ["Vitamin A", "Vitamin C", "Vitamin D", "Vitamin E"], "Vitamin D"),
                ("Which U.S. state is known as the 'Sunshine State'?", ["California", "Hawaii", "Texas", "Florida"], "Florida"),
                ("Which element is the main component of diamonds?", ["Carbon", "Nitrogen", "Oxygen", "Sulfur"], "Carbon"),
                ("Which country is home to the kangaroo?", ["New Zealand", "Australia", "Indonesia", "Papua New Guinea"], "Australia")
            ],
            'Hard': [
                ("What is the heaviest naturally occurring element?", ["Lead", "Uranium", "Gold", "Plutonium"], "Uranium"),
                ("Which planet is closest to the sun?", ["Earth", "Mercury", "Venus", "Mars"], "Mercury"),
                ("Who developed the theory of relativity?", ["Isaac Newton", "Albert Einstein", "Galileo Galilei", "Nikola Tesla"], "Albert Einstein"),
                ("What is the chemical symbol for lead?", ["Pb", "Li", "Fe", "Hg"], "Pb"),
                ("Which scientist is known for the laws of motion?", ["Newton", "Einstein", "Bohr", "Curie"], "Newton"),
                ("What is the atomic number of gold?", ["78", "79", "80", "81"], "79"),
                ("Which river is the longest in Africa?", ["Congo", "Nile", "Zambezi", "Limpopo"], "Nile"),
                ("What is the smallest unit of matter?", ["Atom", "Molecule", "Electron", "Neutron"], "Atom"),
                ("Which country won the first World Cup in 1930?", ["Brazil", "Germany", "Argentina", "Uruguay"], "Uruguay"),
                ("Which civilization built the pyramids?", ["Romans", "Egyptians", "Mayans", "Incas"], "Egyptians"),
                ("What is the most abundant gas in Earth's atmosphere?", ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"], "Nitrogen"),
                ("Who discovered penicillin?", ["Marie Curie", "Louis Pasteur", "Alexander Fleming", "Albert Sabin"], "Alexander Fleming"),
                ("What is the capital of Iceland?", ["Reykjavik", "Helsinki", "Oslo", "Stockholm"], "Reykjavik"),
                ("Which metal has the highest melting point?", ["Iron", "Tungsten", "Platinum", "Gold"], "Tungsten"),
                ("Who wrote 'The Odyssey'?", ["Plato", "Homer", "Aristotle", "Socrates"], "Homer"),
                ("Which continent has the most countries?", ["Asia", "Africa", "Europe", "South America"], "Africa"),
                ("What is the largest country by area?", ["China", "Canada", "Russia", "United States"], "Russia"),
                ("Which is the most populous city in the world?", ["Tokyo", "New York", "Shanghai", "Mumbai"], "Tokyo"),
                ("What is the most spoken language in the world?", ["English", "Mandarin", "Spanish", "Hindi"], "Mandarin"),
                ("Which scientist is known for the law of gravitation?", ["Isaac Newton", "Albert Einstein", "Galileo Galilei", "Marie Curie"], "Isaac Newton"),
                ("What is the capital of Brazil?", ["Buenos Aires", "Brasilia", "Lima", "Santiago"], "Brasilia"),
                ("What is the world's largest ocean?", ["Atlantic", "Indian", "Pacific", "Southern"], "Pacific"),
                ("Which U.S. state is the largest by area?", ["Texas", "California", "Alaska", "Montana"], "Alaska"),
                ("Which famous musician was known as 'The King of Pop'?", ["Elvis Presley", "Michael Jackson", "Prince", "Freddie Mercury"], "Michael Jackson"),
                ("Which organ in the human body is responsible for filtering blood?", ["Liver", "Heart", "Kidneys", "Lungs"], "Kidneys"),
                ("Which country is known for the maple leaf?", ["United States", "Canada", "Australia", "New Zealand"], "Canada")
            ],
            'Extreme': [
                ("What is the most abundant gas in the universe?", ["Hydrogen", "Oxygen", "Nitrogen", "Helium"], "Hydrogen"),
                ("What is the speed of light in a vacuum?", ["299,792,458 m/s", "300,000,000 m/s", "280,000,000 m/s", "315,000,000 m/s"], "299,792,458 m/s"),
                ("Which mathematical conjecture is one of the greatest unsolved problems?", ["Goldbach Conjecture", "Riemann Hypothesis", "Fermat's Last Theorem", "Poincaré Conjecture"], "Riemann Hypothesis"),
                ("Who was the first person to reach the South Pole?", ["Roald Amundsen", "Robert Falcon Scott", "Ernest Shackleton", "Henry Hudson"], "Roald Amundsen"),
                ("What is the chemical formula of table sugar?", ["C12H22O11", "C6H12O6", "C2H5OH", "CH4"], "C12H22O11"),
                ("Which disease was eradicated in 1980?", ["Smallpox", "Polio", "Malaria", "Cholera"], "Smallpox"),
                ("Which particle is known as the 'God Particle'?", ["Higgs boson", "Photon", "Neutrino", "Quark"], "Higgs boson"),
                ("Which theory is related to black holes?", ["General Relativity", "Quantum Mechanics", "Special Relativity", "Newtonian Mechanics"], "General Relativity"),
                ("Which scientist formulated the laws of planetary motion?", ["Kepler", "Copernicus", "Galileo", "Newton"], "Kepler"),
                ("What is the highest mountain in the solar system?", ["Mount Everest", "Olympus Mons", "K2", "Mauna Kea"], "Olympus Mons"),
                ("Who developed the first polio vaccine?", ["Albert Sabin", "Edward Jenner", "Louis Pasteur", "Jonas Salk"], "Jonas Salk"),
                ("What is the rarest blood type?", ["A", "B", "O", "AB negative"], "AB negative"),
                ("Which country has won the most Olympic medals?", ["United States", "China", "Russia", "Germany"], "United States"),
                ("What is the coldest place in the universe?", ["Boomerang Nebula", "Black Hole", "Andromeda Galaxy", "Antarctica"], "Boomerang Nebula"),
                ("What is the only metal that is liquid at room temperature?", ["Mercury", "Iron", "Aluminum", "Gold"], "Mercury"),
                ("What is the smallest unit of life?", ["Cell", "Molecule", "Atom", "Tissue"], "Cell"),
                ("What is the process by which plants make their own food?", ["Photosynthesis", "Respiration", "Fermentation", "Osmosis"], "Photosynthesis"),
                ("Which is the closest galaxy to the Milky Way?", ["Andromeda", "Sombrero", "Triangulum", "Whirlpool"], "Andromeda"),
                ("Who was the first woman to win a Nobel Prize?", ["Marie Curie", "Rosalind Franklin", "Dorothy Hodgkin", "Ada Lovelace"], "Marie Curie"),
                ("Which famous battle took place in 1066?", ["Battle of Hastings", "Battle of Waterloo", "Battle of Gettysburg", "Battle of Agincourt"], "Battle of Hastings"),
                ("What is the longest river in Asia?", ["Yangtze", "Ganges", "Indus", "Yellow River"], "Yangtze"),
                ("Which planet has the most moons?", ["Jupiter", "Saturn", "Mars", "Neptune"], "Saturn"),
                ("Which dinosaur is known for having three horns?", ["Tyrannosaurus", "Stegosaurus", "Triceratops", "Velociraptor"], "Triceratops"),
                ("What is the scientific name for the human species?", ["Homo erectus", "Homo habilis", "Homo sapiens", "Homo neanderthalensis"], "Homo sapiens"),
                ("What is the highest-grossing film of all time?", ["Avatar", "Avengers: Endgame", "Titanic", "Star Wars"], "Avatar")
            ]
        }

    def ask_question(self, difficulty):
        question, options, answer = random.choice(self.questions[difficulty])
        print(f"Question: {question}")
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        user_answer = input("Enter the number of your answer: ")

        if options[int(user_answer) - 1] == answer:
            print("Correct!")
            self.score += 10 if difficulty == 'Easy' else 20 if difficulty == 'Medium' else 30
            self.correct_answers += 1
        else:
            print(f"Wrong! The correct answer was {answer}.")
            self.incorrect_answers += 1

    def play_round(self, difficulty):
        for _ in range(5):  # 5 questions per round
            self.ask_question(difficulty)

    def play_game(self):
        blink_text("WELCOME TO ALEX HARWOOD'S CLI TRIVIA GAME", blink_speed=0.3)

        while True:
            print("\nSelect difficulty:")
            if self.extreme_unlocked:
                print("1. Easy\n2. Medium\n3. Hard\n4. Extreme")
            else:
                print("1. Easy\n2. Medium\n3. Hard")

            choice = input("Enter your choice: ")

            if choice == '1':
                difficulty = 'Easy'
            elif choice == '2':
                difficulty = 'Medium'
            elif choice == '3':
                difficulty = 'Hard'
            elif choice == '4' and self.extreme_unlocked:
                difficulty = 'Extreme'
            else:
                print("Invalid choice. Please try again.")
                continue

            self.play_round(difficulty)

            if difficulty == 'Hard' and self.correct_answers >= 2.5:  # At least 50% of 5 questions correct
                print("You've unlocked Extreme mode!")
                self.extreme_unlocked = True

            play_again = input("Do you want to play another round? (yes/no): ").lower()
            if play_again != 'yes':
                break

        print(f"Game over! Your final score is: {self.score}")

if __name__ == "__main__":
    game = TriviaGame()
    game.play_game()

