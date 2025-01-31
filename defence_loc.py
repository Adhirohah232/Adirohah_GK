import random

class AutomatedQuiz:
    def __init__(self):
        self.locations = {}  # Dictionary to store locations data
        self.num_questions = 0  # Number of questions for the quiz
        self.load_data("cmndsInstLOC.txt")  # Automatically load data on initialization

    def load_data(self, filename):
        """Load data from the text file and parse it into a dictionary."""
        try:
            with open(filename, "r") as file:
                data = file.read()

            # Extract the dictionary part from the file and convert it into Python dictionary
            data = data.strip().removeprefix('"locations"=').replace("{", "").replace("}", "").strip()
            lines = data.split("\n")

            for line in lines:
                line = line.strip()
                if not line or ":" not in line:
                    continue
                try:
                    key, value = map(str.strip, line.replace('"', "").split(":"))
                    self.locations[key] = value
                except ValueError:
                    continue  # Skip invalid lines

            if not self.locations:
                raise ValueError("No data available in the file.")

        except FileNotFoundError:
            print(f"File '{filename}' not found. Please ensure the file exists.")
            exit(1)
        except Exception as e:
            print(f"An error occurred while loading data: {e}")
            exit(1)

    def generate_question(self):
        """Generate a random question from the loaded data."""
        if not self.locations:
            raise ValueError("No data available for the quiz. Please load data first.")
        question, correct_answer = random.choice(list(self.locations.items()))
        options = random.sample(list(self.locations.values()), 3)
        if correct_answer not in options:
            options.append(correct_answer)
        random.shuffle(options)
        return question, correct_answer, options

    def start_quiz(self):
        """Start the quiz."""
        try:
            if not self.locations:
                raise ValueError("No data available for the quiz. Please load data first.")
            
            # Get the number of questions from the user
            self.num_questions = int(input("Enter the number of questions for the quiz: "))
            if self.num_questions <= 0:
                print("Number of questions must be greater than zero.")
                return
            
            score = 0
            for i in range(1, self.num_questions + 1):
                print(f"\nQuestion {i}:")
                question, correct_answer, options = self.generate_question()
                print(f"📍 Where is '{question}' located? 📍")
                for idx, option in enumerate(options, 1):
                    # Strip unnecessary trailing commas or whitespace from options
                    clean_option = option.strip(", ")
                    print(f"{idx}. {clean_option}")
                
                # Get user input
                try:
                    user_answer = int(input("Enter your choice (1-4): "))
                    if user_answer < 1 or user_answer > 4:
                        print("Invalid choice. Moving to next question.")
                        continue
                except ValueError:
                    print("Invalid input. Please enter a number between 1 and 4.")
                    continue

                # Check answer
                if options[user_answer - 1] == correct_answer:
                    print("✅Correct!")
                    score += 1
                else:
                    print(f"❌Wrong! The correct answer is: {correct_answer}")

            # Display the final score
            print(f"\nQuiz completed! Your score: {score}/{self.num_questions}")

        except ValueError as e:
            print(e)
        except Exception as e:
            print(f"An error occurred: {e}")