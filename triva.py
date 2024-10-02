import random

class TriviaGame:
    def play(self):
        while True:
            try:
                rounds = int(input("How many rounds would you like to play? "))
                break
            except ValueError:
                print("Please enter a valid number.")

        category = self.select_category()
        # Add remaining logic for playing the game

    def select_category(self):
        print("Choose a category:")
        print("1. Easy\n2. Medium\n3. Hard\n4. Extreme\n5. Math")
        while True:
            try:
                category_choice = int(input()) - 1
                if 0 <= category_choice < 5:
                    return self.categories[category_choice]
                else:
                    print("Please select a number between 1 and 5.")
            except ValueError:
                print("Please enter a valid number.")

    # Ensure this is defined somewhere in your class
    def some_method(self, difficulty):
        if difficulty in self.difficulties:
            # Your logic here

            "Easy": [
                ("What is 2 + 2?", "4", ["3", "4", "5", "6"]),
                ("How many legs does a spider have?", "8", ["6", "7", "8", "10"]),
                ("What is the capital of France?", "Paris", ["Paris", "Rome", "Berlin", "Madrid"]),
                ("What is the color of the sky?", "Blue", ["Blue", "Green", "Red", "Yellow"]),
                ("What is the currency of the United States?", "Dollar", ["Yen", "Dollar", "Euro", "Rupee"]),
                ("How many colors are in a rainbow?", "7", ["5", "6", "7", "8"]),
                ("What is the name of the planet we live on?", "Earth", ["Earth", "Mars", "Venus", "Jupiter"]),
                ("What is 10 - 3?", "7", ["6", "7", "8", "9"]),
                ("Which animal is known as the king of the jungle?", "Lion", ["Lion", "Tiger", "Bear", "Elephant"]),
                ("How many hours are in a day?", "24", ["12", "24", "36", "48"]),
                ("What is the largest mammal in the world?", "Blue Whale", ["Blue Whale", "Elephant", "Giraffe", "Shark"]),
                ("What fruit is known as the king of fruits?", "Mango", ["Apple", "Banana", "Mango", "Orange"]),
                ("What shape is a stop sign?", "Octagon", ["Circle", "Square", "Triangle", "Octagon"]),
                ("How many days are in a week?", "7", ["5", "6", "7", "8"]),
                ("What is the opposite of hot?", "Cold", ["Warm", "Hot", "Cold", "Cool"]),
                ("Which month has Halloween?", "October", ["September", "October", "November", "December"]),
                ("What color is a ripe banana?", "Yellow", ["Red", "Yellow", "Green", "Blue"]),
                ("How many sides does a triangle have?", "3", ["2", "3", "4", "5"]),
                ("What is the name of the fairy in Peter Pan?", "Tinkerbell", ["Tinkerbell", "Cinderella", "Ariel", "Belle"]),
                ("What is the first letter of the English alphabet?", "A", ["A", "B", "C", "D"]),
                ("What is the boiling point of water in degrees Celsius?", "100", ["90", "100", "110", "120"]),
                ("What is the capital of Italy?", "Rome", ["Rome", "Paris", "Berlin", "Madrid"]),
                ("How many continents are there?", "7", ["5", "6", "7", "8"]),
                ("What is the largest planet in our solar system?", "Jupiter", ["Earth", "Mars", "Jupiter", "Saturn"]),
                ("What is the tallest mountain in the world?", "Mount Everest", ["K2", "Mount Everest", "Kilimanjaro", "Denali"]),
                ("Which gas do plants absorb from the atmosphere?", "Carbon Dioxide", ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"]),
            ],
            "Medium": [
                ("What is the primary ingredient in hummus?", "Chickpeas", ["Chickpeas", "Lentils", "Peas", "Beans"]),
                ("What is the smallest continent?", "Australia", ["Africa", "Asia", "Australia", "Europe"]),
                ("What is the boiling point of water?", "100", ["90", "100", "120", "110"]),
                ("What is the hardest natural substance on Earth?", "Diamond", ["Gold", "Diamond", "Iron", "Silver"]),
                ("What is the capital of Japan?", "Tokyo", ["Tokyo", "Beijing", "Seoul", "Bangkok"]),
                ("What is the tallest building in the world?", "Burj Khalifa", ["Burj Khalifa", "Eiffel Tower", "Empire State Building", "One World Trade Center"]),
                ("What is the capital of Australia?", "Canberra", ["Sydney", "Melbourne", "Canberra", "Brisbane"]),
                ("What is the largest ocean on Earth?", "Pacific Ocean", ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"]),
                ("Who wrote the play 'Romeo and Juliet'?", "William Shakespeare", ["Charles Dickens", "Mark Twain", "William Shakespeare", "Jane Austen"]),
                ("What is the chemical symbol for gold?", "Au", ["Ag", "Au", "Pb", "Fe"]),
                ("What planet is known as the Red Planet?", "Mars", ["Earth", "Mars", "Jupiter", "Saturn"]),
                ("What is the capital city of Canada?", "Ottawa", ["Toronto", "Ottawa", "Vancouver", "Montreal"]),
                ("What is the main language spoken in Brazil?", "Portuguese", ["Spanish", "Portuguese", "English", "French"]),
                ("What is the currency used in Japan?", "Yen", ["Dollar", "Yen", "Euro", "Won"]),
                ("What is the largest desert in the world?", "Sahara Desert", ["Gobi Desert", "Sahara Desert", "Kalahari Desert", "Arabian Desert"]),
                ("What does DNA stand for?", "Deoxyribonucleic Acid", ["Deoxyribonucleic Acid", "Dioxyribonucleic Acid", "Deoxyribose Acid", "Dinitrogen Acid"]),
                ("What is the freezing point of water in degrees Celsius?", "0", ["0", "32", "100", "212"]),
                ("What is the capital of Egypt?", "Cairo", ["Cairo", "Alexandria", "Luxor", "Giza"]),
                ("What is the name of the largest land animal?", "Elephant", ["Giraffe", "Elephant", "Hippo", "Rhino"]),
                ("Which gas is most abundant in the Earth's atmosphere?", "Nitrogen", ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"]),
                ("What is the term for an animal that only eats plants?", "Herbivore", ["Carnivore", "Omnivore", "Herbivore", "Insectivore"]),
                ("What is the primary function of red blood cells?", "Transport Oxygen", ["Fight Infection", "Transport Oxygen", "Clot Blood", "Digest Food"]),
                ("Who was the first man on the moon?", "Neil Armstrong", ["Buzz Aldrin", "Yuri Gagarin", "Neil Armstrong", "Michael Collins"]),
                ("What is the capital of Greece?", "Athens", ["Rome", "Athens", "Paris", "Berlin"]),
            ],
            "Hard": [
                ("What is Schrödinger's cat?", "Thought experiment", ["Animal", "Thought experiment", "Quantum cat", "Experiment"]),
                ("What is the black hole information paradox?", "Paradox", ["Theory", "Paradox", "Experiment", "Thought"]),
                ("What is the Uncertainty Principle?", "Principle", ["Law", "Principle", "Theory", "Concept"]),
                ("What is the capital of Mozambique?", "Maputo", ["Maputo", "Lagos", "Nairobi", "Johannesburg"]),
                ("What is the capital of Eswatini?", "Mbabane", ["Mbabane", "Pretoria", "Harare", "Gaborone"]),
                ("What is the speed of light in vacuum?", "299,792 km/s", ["299,792 km/s", "300,000 km/s", "150,000 km/s", "400,000 km/s"]),
                ("Who developed the theory of general relativity?", "Albert Einstein", ["Isaac Newton", "Albert Einstein", "Galileo Galilei", "Nikola Tesla"]),
                ("What is the rarest blood type?", "AB negative", ["A positive", "O negative", "AB negative", "B positive"]),
                ("What is the first element on the periodic table?", "Hydrogen", ["Helium", "Oxygen", "Hydrogen", "Carbon"]),
                ("What is the hardest known natural material?", "Diamond", ["Diamond", "Ruby", "Sapphire", "Emerald"]),
                ("What is the largest internal organ in the human body?", "Liver", ["Heart", "Liver", "Kidney", "Lung"]),
                ("What is the most abundant element in the universe?", "Hydrogen", ["Oxygen", "Hydrogen", "Carbon", "Nitrogen"]),
                ("What is the smallest bone in the human body?", "Stapes", ["Stapes", "Incus", "Malleus", "Femur"]),
                ("Who is known as the father of modern physics?", "Albert Einstein", ["Isaac Newton", "Albert Einstein", "Galileo Galilei", "Stephen Hawking"]),
                ("What is the capital of Bhutan?", "Thimphu", ["Thimphu", "Kathmandu", "Lhasa", "Dhaka"]),
                ("What is the formula for calculating the area of a circle?", "πr²", ["πr", "2πr", "πr²", "πd"]),
                ("What is the capital of Fiji?", "Suva", ["Nadi", "Suva", "Lautoka", "Levuka"]),
                ("What is the most spoken language in the world?", "Mandarin Chinese", ["English", "Mandarin Chinese", "Spanish", "Hindi"]),
                ("What is the capital of Latvia?", "Riga", ["Tallinn", "Vilnius", "Riga", "Minsk"]),
                ("What is the longest river in the world?", "Nile", ["Amazon", "Nile", "Yangtze", "Mississippi"]),
                ("What is the main ingredient in traditional Japanese miso soup?", "Miso", ["Soy", "Miso", "Seaweed", "Fish"]),
                ("What year did World War II end?", "1945", ["1944", "1945", "1946", "1947"]),
                ("What is the most widely practiced religion in the world?", "Christianity", ["Buddhism", "Hinduism", "Christianity", "Islam"]),
            ],
            "Extreme": [
                ("What is the theoretical temperature at which all molecular motion ceases?", "Absolute Zero", ["Absolute Zero", "Freezing Point", "Boiling Point", "Room Temperature"]),
                ("What is the Pythagorean theorem?", "a² + b² = c²", ["a² + b² = c²", "a + b = c", "c = 2πr", "F = ma"]),
                ("What is the name of the longest muscle in the human body?", "Sartorius", ["Sartorius", "Biceps", "Triceps", "Rectus"]),
                ("What is the most common isotope of Uranium?", "Uranium-238", ["Uranium-235", "Uranium-238", "Uranium-234", "Plutonium-239"]),
                ("What is the term for the fear of heights?", "Acrophobia", ["Acrophobia", "Claustrophobia", "Agoraphobia", "Xenophobia"]),
                ("What is the only planet in the solar system that rotates on its side?", "Uranus", ["Earth", "Mars", "Uranus", "Venus"]),
                ("What is the main ingredient in traditional Italian pesto?", "Basil", ["Oregano", "Basil", "Parsley", "Thyme"]),
                ("What is the mathematical constant known as Euler's number?", "e", ["e", "π", "i", "φ"]),
                ("What is the capital of Iceland?", "Reykjavik", ["Reykjavik", "Oslo", "Stockholm", "Copenhagen"]),
                ("What is the main gas found in the sun?", "Hydrogen", ["Oxygen", "Hydrogen", "Carbon Dioxide", "Nitrogen"]),
                ("What is the capital of Mongolia?", "Ulaanbaatar", ["Beijing", "Ulaanbaatar", "Seoul", "Tokyo"]),
                ("What is the most abundant protein in the human body?", "Collagen", ["Actin", "Myosin", "Collagen", "Keratin"]),
                ("What is the square root of 144?", "12", ["10", "11", "12", "13"]),
                ("What is the name of the largest volcano in the solar system?", "Olympus Mons", ["Mount Everest", "Olympus Mons", "Mauna Kea", "Kilimanjaro"]),
                ("What is the most famous equation in physics?", "E=mc²", ["F=ma", "E=mc²", "a² + b² = c²", "PV=nRT"]),
                ("What is the only country that is also a continent?", "Australia", ["Australia", "Antarctica", "Greenland", "South America"]),
                ("What is the most common type of star in the universe?", "Red Dwarf", ["Red Dwarf", "White Dwarf", "Supernova", "Giant"]),
                ("What is the main ingredient in a traditional Spanish paella?", "Rice", ["Rice", "Noodles", "Beans", "Lentils"]),
                ("What is the capital of Kazakhstan?", "Nur-Sultan", ["Astana", "Almaty", "Nur-Sultan", "Tashkent"]),
                ("What is the process by which plants make their food called?", "Photosynthesis", ["Digestion", "Respiration", "Photosynthesis", "Fermentation"]),
                ("What is the main component of the cell membrane?", "Phospholipid", ["Cholesterol", "Phospholipid", "Carbohydrate", "Protein"]),
                ("What is the capital of Cyprus?", "Nicosia", ["Nicosia", "Athens", "Beirut", "Damascus"]),
                ("What is the largest known structure in the universe?", "Hercules-Corona Borealis Great Wall", ["Milky Way", "Hercules-Corona Borealis Great Wall", "Andromeda", "Virgo Cluster"]),
                ("What is the main organ involved in the circulatory system?", "Heart", ["Lung", "Heart", "Liver", "Kidney"]),
            ],
            "Math": [
                ("What is 5 + 7?", "12", ["11", "12", "13", "14"]),
                ("What is 15 ÷ 3?", "5", ["4", "5", "6", "7"]),
                ("What is the area of a rectangle with length 4 and width 5?", "20", ["18", "19", "20", "21"]),
                ("What is 9 × 6?", "54", ["52", "53", "54", "55"]),
                ("What is the value of π (pi) rounded to two decimal places?", "3.14", ["3.12", "3.14", "3.16", "3.18"]),
                ("What is 100 - 37?", "63", ["62", "63", "64", "65"]),
                ("What is the square of 8?", "64", ["56", "62", "64", "66"]),
                ("What is the circumference of a circle with a radius of 3?", "18.84", ["18.28", "18.84", "19.10", "19.58"]),
                ("What is 25% of 200?", "50", ["40", "50", "60", "70"]),
                ("What is the sum of angles in a triangle?", "180", ["90", "180", "270", "360"]),
                ("What is 12 - 5 + 3?", "10", ["9", "10", "11", "12"]),
                ("What is the value of 3²?", "9", ["6", "7", "8", "9"]),
                ("What is the formula for the area of a triangle?", "1/2 × base × height", ["base × height", "base²", "1/2 × base × height", "base + height"]),
                ("What is 14 ÷ 2?", "7", ["6", "7", "8", "9"]),
                ("What is the square root of 64?", "8", ["6", "7", "8", "9"]),
                ("What is 7 × 7?", "49", ["48", "49", "50", "51"]),
                ("What is the value of 2 + 2 × 2?", "6", ["5", "6", "7", "8"]),
                ("What is 10 + 20 ÷ 4?", "15", ["14", "15", "16", "17"]),
                ("What is the value of 15 - 6 + 2?", "11", ["10", "11", "12", "13"]),
                ("What is 100 ÷ 10 × 2?", "20", ["10", "20", "30", "40"]),
                ("What is the area of a circle with a diameter of 10?", "78.54", ["75.36", "78.54", "79.78", "80.00"]),
                ("What is 5 × 5 - 5?", "20", ["19", "20", "21", "22"]),
                ("What is the value of 100 - (3 × 25)?", "25", ["20", "25", "30", "35"]),
                ("What is 11 × 12?", "132", ["120", "130", "132", "134"]),
                ("What is the value of 2 × (3 + 4)?", "14", ["12", "14", "16", "18"]),
                ("What is 8 - (3 + 2)?", "3", ["1", "2", "3", "4"]),
                ("What is 50% of 80?", "40", ["30", "40", "50", "60"]),
            ],
        }
        self.scores = {}

    def display_welcome(self):
        print("\033[5mWELCOME TO ALEX HARWOOD'S CLI TRIVIA GAME\033[0m")

    def select_difficulty(self):
        while True:
            difficulty = input("Select difficulty (Easy, Medium, Hard, Extreme, Math): ").capitalize()
            if difficulty in self
