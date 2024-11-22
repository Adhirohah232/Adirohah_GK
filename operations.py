import json
import random


class OperationsQuiz:

    def __init__(self):
        """Initialize the quiz with default values"""
        self.operations = None
        self.score = 0
        self.num_questions = 0
        self.questions_asked = 0

    def load_operations_from_text(self):
        """Load operations data from the text file"""
        try:
            with open('operations.txt', 'r') as file:
                content = file.read()
                data = json.loads(content)
                self.operations = data['operations']
                return True
        except FileNotFoundError:
            print(f"Error: File 'operations.txt' not found.")
            return False
        except json.JSONDecodeError:
            print("Error: Invalid JSON format in the text file.")
            return False
        except Exception as e:
            print(f"Error: An unexpected error occurred: {str(e)}")
            return False

    def get_random_options(self, correct_answer, all_options, num_options=4):
        """Generate random options including the correct answer"""
        options = [correct_answer]
        remaining_options = [
            opt for opt in all_options if opt != correct_answer
        ]
        options.extend(
            random.sample(remaining_options,
                          min(num_options - 1, len(remaining_options))))
        random.shuffle(options)
        return options

    def ask_question(self, question, options, correct_answer):
        """Ask a question and get user input"""
        print("\n" + question)
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")

        while True:
            try:
                choice = int(input("\nEnter your answer (1-4): "))
                if 1 <= choice <= len(options):
                    break
                print("Please enter a number between 1 and 4.")
            except ValueError:
                print("Please enter a valid number.")

        user_answer = options[choice - 1]
        is_correct = user_answer == correct_answer

        if is_correct:
            print("Correct! Well done!")
            self.score += 1
        else:
            print(f"Wrong! The correct answer was: {correct_answer}")

    def generate_type1_question(self):
        """Generate a question of type 1: Match purpose to operation name"""
        operation = random.choice(self.operations)
        question = f"Consider this statement:\n\"{operation['purpose']}\"\nyear- {operation['year']}\n* is related to which operation?"
        all_names = list(set(op['name'] for op in self.operations))
        options = self.get_random_options(operation['name'], all_names)
        self.ask_question(question, options, operation['name'])

    def generate_type2_question(self):
        """Generate a question of type 2: Match purpose to year"""
        operation = random.choice(self.operations)
        question = f"Which year was operation {operation['name']}, for the purpose\n\"{operation['purpose']}\", carried out?"
        all_years = list(set(str(op['year']) for op in self.operations))
        options = self.get_random_options(str(operation['year']), all_years)
        self.ask_question(question, options, str(operation['year']))

    def generate_type3_question(self):
        """Generate a question of type 3: Match operation and year to purpose"""
        operation = random.choice(self.operations)
        question = f"What was the purpose of the operation {operation['name']} carried out by {operation['carried_by']} during year- {operation['year']}?"
        all_purposes = list(set(op['purpose'] for op in self.operations))
        options = self.get_random_options(operation['purpose'], all_purposes)
        self.ask_question(question, options, operation['purpose'])

    def get_num_questions(self):
        """Get the number of questions from user"""
        while True:
            try:
                self.num_questions = int(
                    input("How many questions would you like to answer? "))
                if self.num_questions > 0:
                    return True
                print("Please enter a positive number of questions.")
            except ValueError:
                print("Please enter a valid number.")
        return False

    def display_final_score(self):
        """Display the final score and percentage"""
        print(
            f"\nQuiz completed! Your score: {self.score} out of {self.num_questions}"
        )
        percentage = (self.score / self.num_questions) * 100
        print(f"Percentage: {percentage:.2f}%")

    def start_quiz(self):
        """Main method to start and run the quiz"""
        # Load operations data
        if not self.load_operations_from_text():
            return

        # Get number of questions
        if not self.get_num_questions():
            return

        # Reset score and questions count
        self.score = 0
        self.questions_asked = 0

        # Run quiz
        while self.questions_asked < self.num_questions:
            # Randomly choose question type (1, 2, or 3)
            question_type = random.randint(1, 3)

            if question_type == 1:
                self.generate_type1_question()
            elif question_type == 2:
                self.generate_type2_question()
            else:
                self.generate_type3_question()

            self.questions_asked += 1

        # Display final score
        self.display_final_score()


# If running this file directly
if __name__ == "__main__":
    quiz = OperationsQuiz()
    quiz.start_quiz()
