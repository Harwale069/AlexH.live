import random

class TriviaGame:
    def __init__(self):
        self.categories = {
            "Easy": self.get_easy_questions(),
            "Medium": self.get_medium_questions(),
            "Hard": self.get_hard_questions(),
            "Extreme": self.get_extreme_questions(),
            "Math": self.get_math_questions(),
        }
        self.player_score = 0

    def get_easy_questions(self):
        return [
            {"question": "What is the capital of France?", "answer": "paris"},
            {"question": "What is 2 + 2?", "answer": "4"},
            {"question": "What color do you get when you mix red and white?", "answer": "pink"},
            {"question": "What is the largest ocean on Earth?", "answer": "pacific"},
            {"question": "What is the smallest planet in our solar system?", "answer": "mercury"},
            {"question": "What is the chemical symbol for water?", "answer": "h2o"},
            {"question": "What is the hardest natural substance on Earth?", "answer": "diamond"},
            {"question": "In which continent is Egypt located?", "answer": "africa"},
            {"question": "What is the main ingredient in guacamole?", "answer": "avocado"},
            {"question": "How many continents are there?", "answer": "7"},
            {"question": "What is the longest river in the world?", "answer": "nile"},
            {"question": "What planet is known as the Red Planet?", "answer": "mars"},
            {"question": "What is the capital of Japan?", "answer": "tokyo"},
            {"question": "How many days are in a leap year?", "answer": "366"},
            {"question": "What is the currency of the United States?", "answer": "dollar"},
            {"question": "What is the largest mammal in the world?", "answer": "blue whale"},
            {"question": "What is the tallest mountain in the world?", "answer": "everest"},
            {"question": "What is the primary language spoken in Brazil?", "answer": "portuguese"},
            {"question": "What is the most widely spoken language in the world?", "answer": "mandarin"},
            {"question": "What fruit is known as the king of fruits?", "answer": "durian"},
        ]

    def get_medium_questions(self):
        return [
            {"question": "What is the powerhouse of the cell?", "answer": "mitochondria"},
            {"question": "What is the capital of Australia?", "answer": "canberra"},
            {"question": "What is the boiling point of water?", "answer": "100"},
            {"question": "What is the chemical symbol for gold?", "answer": "au"},
            {"question": "Who wrote 'Romeo and Juliet'?", "answer": "shakespeare"},
            {"question": "What year did World War II end?", "answer": "1945"},
            {"question": "What is the square root of 64?", "answer": "8"},
            {"question": "What is the main gas found in the air we breathe?", "answer": "nitrogen"},
            {"question": "Who painted the Mona Lisa?", "answer": "da vinci"},
            {"question": "What is the largest planet in our solar system?", "answer": "jupiter"},
            {"question": "What is the freezing point of water?", "answer": "0"},
            {"question": "In which year did the Titanic sink?", "answer": "1912"},
            {"question": "What is the capital of Italy?", "answer": "rome"},
            {"question": "What is the hardest rock?", "answer": "diamond"},
            {"question": "What is the main ingredient in bread?", "answer": "flour"},
            {"question": "What is the largest desert in the world?", "answer": "sahara"},
            {"question": "What is the smallest continent?", "answer": "australia"},
            {"question": "Who discovered penicillin?", "answer": "fleming"},
            {"question": "What is the currency of Japan?", "answer": "yen"},
            {"question": "What is the capital of Canada?", "answer": "ottawa"},
            {"question": "What is the primary ingredient in hummus?", "answer": "chickpeas"},
        ]

    def get_hard_questions(self):
        return [
            {"question": "What is the theory of relativity?", "answer": "theory"},
            {"question": "What is the capital of Iceland?", "answer": "reykjavik"},
            {"question": "What is the largest organ in the human body?", "answer": "skin"},
            {"question": "What is the main ingredient in tofu?", "answer": "soybeans"},
            {"question": "Who is known as the father of modern physics?", "answer": "einstein"},
            {"question": "What is the currency of the European Union?", "answer": "euro"},
            {"question": "What is the smallest bone in the human body?", "answer": "stapes"},
            {"question": "What is the capital of South Korea?", "answer": "seoul"},
            {"question": "What is the largest volcano in the world?", "answer": "mauna loa"},
            {"question": "What is the most spoken language in South America?", "answer": "portuguese"},
            {"question": "What is the capital of Turkey?", "answer": "ankara"},
            {"question": "What is the longest bone in the human body?", "answer": "femur"},
            {"question": "Who is the author of '1984'?", "answer": "orwell"},
            {"question": "What is the main ingredient in mayonnaise?", "answer": "egg"},
            {"question": "What is the most expensive painting ever sold?", "answer": "salvator mundi"},
            {"question": "What is the only planet that rotates on its side?", "answer": "uranus"},
            {"question": "What is the most widely spoken language in Africa?", "answer": "arabic"},
            {"question": "Who painted the ceiling of the Sistine Chapel?", "answer": "michelangelo"},
            {"question": "What is the chemical symbol for iron?", "answer": "fe"},
            {"question": "What is the largest island in the world?", "answer": "greenland"},
            {"question": "Who wrote 'Pride and Prejudice'?", "answer": "austen"},
        ]

    def get_extreme_questions(self):
        return [
            {"question": "What is the Riemann Hypothesis?", "answer": "hypothesis"},
            {"question": "What is the capital of Kazakhstan?", "answer": "nur-sultan"},
            {"question": "What is the process of photosynthesis?", "answer": "photosynthesis"},
            {"question": "Who developed the theory of evolution?", "answer": "darwin"},
            {"question": "What is the capital of Bhutan?", "answer": "thimphu"},
            {"question": "What is Schrödinger's cat?", "answer": "thought experiment"},
            {"question": "What is the capital of Vanuatu?", "answer": "port vila"},
            {"question": "What is the Mandelbrot set?", "answer": "set"},
            {"question": "What is the capital of Mozambique?", "answer": "maputo"},
            {"question": "What is the main gas in Earth's atmosphere?", "answer": "nitrogen"},
            {"question": "What is the capital of Eritrea?", "answer": "asmara"},
            {"question": "What is the Uncertainty Principle?", "answer": "principle"},
            {"question": "What is the capital of Malta?", "answer": "valletta"},
            {"question": "What is the most common isotope of hydrogen?", "answer": "protium"},
            {"question": "What is the capital of Eswatini?", "answer": "mbabane"},
            {"question": "What is quantum entanglement?", "answer": "entanglement"},
            {"question": "What is the capital of Timor-Leste?", "answer": "dili"},
            {"question": "What is the Higgs boson?", "answer": "boson"},
            {"question": "What is the capital of Seychelles?", "answer": "victoria"},
            {"question": "What is the black hole information paradox?", "answer": "paradox"},
            {"question": "What is the capital of Djibouti?", "answer": "djibouti"},
        ]

    def get_math_questions(self):
        return [
            {"question": "What is 5 * 6?", "answer": "30"},
            {"question": "What is 12 / 4?", "answer": "3"},
            {"question": "What is 9 + 10?", "answer": "19"},
            {"question": "What is the square of 7?", "answer": "49"},
            {"question": "What is 15 - 8?", "answer": "7"},
            {"question": "What is the value of π (pi) to two decimal places?", "answer": "3.14"},
            {"question": "What is the result of 4^3?", "answer": "64"},
            {"question": "What is the area of a circle with radius 3?", "answer": "28.26"},
            {"question": "What is the sum of the first 10 positive integers?", "answer": "55"},
            {"question": "What is 100 factorial mod 11?", "answer": "0"},
        ]

    def select_category(self):
        print("Choose a category:")
        for i, category in enumerate(self.categories.keys()):
            print(f"{i + 1}. {category}")
        category_choice = int(input()) - 1
        return list(self.categories.keys())[category_choice]

    def ask_question(self, question_data):
        print(f"Question: {question_data['question']}")
        answer = input("Your answer: ").strip().lower()
        if answer == question_data['answer']:
            print("Correct!")
            self.player_score += 1
        else:
            print(f"Wrong! The correct answer was {question_data['answer']}.")

    def play(self):
        rounds = int(input("How many rounds would you like to play? "))
        while rounds > 0:
            rounds -= 1
            category = self.select_category()
            questions = random.sample(self.categories[category], k=5)
            for question_data in questions:
                self.ask_question(question_data)
            print(f"Your final score: {self.player_score}")

# Create an instance of the game
game = TriviaGame()
game.play()

