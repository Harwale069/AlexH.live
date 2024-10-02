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
                ("What is 2 + 2?", ["3", "4", "5", "6"], "4"),
                ("What is 5 - 3?", ["1", "2", "3", "4"], "2"),
                ("What is 10 divided by 2?", ["4", "5", "6", "7"], "5"),
                ("What is 3 times 3?", ["6", "8", "9", "12"], "9"),
                ("What is 7 + 2?", ["8", "9", "10", "11"], "9"),
                ("How many sides does a square have?", ["3", "4", "5", "6"], "4"),
                ("What is 10 + 15?", ["20", "25", "30", "35"], "25"),
                ("What is the value of pi?", ["3.12", "3.14", "3.16", "3.18"], "3.14"),
                ("How many days are in a leap year?", ["365", "366", "367", "364"], "366"),
                ("What is 1 + 1?", ["0", "1", "2", "3"], "2")
            ],
            'Medium': [
                ("What is the square root of 144?", ["10", "11", "12", "13"], "12"),
                ("What is 15 * 3?", ["40", "45", "50", "55"], "45"),
                ("If a triangle has two sides of 5 cm and 10 cm, what is the perimeter?", ["15 cm", "20 cm", "25 cm", "30 cm"], "30 cm"),
                ("What is the area of a rectangle with a length of 4 and width of 5?", ["20", "10", "25", "30"], "20"),
                ("What is 81 / 9?", ["7", "8", "9", "10"], "9"),
                ("What is 3 raised to the power of 3?", ["9", "27", "18", "30"], "27"),
                ("If 6x = 18, what is x?", ["1", "2", "3", "4"], "3"),
                ("How many degrees are in a triangle?", ["90", "180", "270", "360"], "180"),
                ("What is 144 divided by 12?", ["10", "11", "12", "13"], "12"),
                ("What is 50% of 100?", ["20", "50", "25", "10"], "50")
            ],
            'Hard': [
                ("What is the derivative of x^2?", ["x", "2x", "x^2", "1"], "2x"),
                ("What is the value of sin(90°)?", ["0", "1", "0.5", "-1"], "1"),
                ("Solve for x: 2x + 3 = 7.", ["1", "2", "3", "4"], "2"),
                ("What is the integral of 2x dx?", ["x^2", "2x^2", "2x", "x"], "x^2"),
                ("What is the formula for the area of a circle?", ["2πr", "πr^2", "πd", "2r"], "πr^2"),
                ("What is the value of 7 factorial (7!)?", ["5040", "40320", "720", "120"], "5040"),
                ("What is the square root of 169?", ["12", "13", "14", "15"], "13"),
                ("What is the equation for the Pythagorean Theorem?", ["a^2 + b^2 = c^2", "a^2 + b = c", "a + b^2 = c^2", "a + b + c = 0"], "a^2 + b^2 = c^2"),
                ("Solve for x: 4x - 5 = 11.", ["2", "3", "4", "5"], "4"),
                ("What is the cube root of 27?", ["2", "3", "4", "5"], "3")
            ],
            'Extreme': [
                ("What is the value of Euler's number e (approximately)?", ["2.7", "2.71", "2.718", "2.71828"], "2.71828"),
                ("Solve the equation: ln(e^5) = ?", ["1", "5", "0", "10"], "5"),
                ("What is the value of the golden ratio?", ["1.6", "1.618", "1.62", "1.61803"], "1.61803"),
                ("What is the derivative of sin(x)?", ["cos(x)", "-cos(x)", "sin(x)", "-sin(x)"], "cos(x)"),
                ("What is the sum of the infinite geometric series 1 + 1/2 + 1/4 + 1/8 + ... ?", ["2", "3", "1.5", "2.5"], "2"),
                ("What is the probability of rolling a 6 on a fair six-sided die?", ["1/2", "1/3", "1/6", "1/12"], "1/6"),
                ("Solve for x: log10(x) = 2.", ["1", "10", "100", "1000"], "100"),
                ("What is the limit of (1 + 1/n)^n as n approaches infinity?", ["e", "1", "0", "infinity"], "e"),
                ("What is the Riemann Hypothesis concerned with?", ["Prime numbers", "Geometric shapes", "Calculus", "Probability"], "Prime numbers"),
                ("What is the formula for the circumference of a circle?", ["πr^2", "2πr", "πd", "r^2"], "2πr")
            ],
            'Type': [
                ("Solve for x: x^2 - 4 = 0.", "x = 2 or x = -2"),
                ("What is the area of a triangle with base 5 and height 12?", "30"),
                ("What is the slope of the line y = 3x + 4?", "3"),
                ("Find the derivative of 3x^3.", "9x^2"),
                ("What is the value of log base 2 of 8?", "3")
            ]
        }

    # Other methods and gameplay logic...
