import json
import random


class CAQuiz:

    def __init__(self, json_file='CA_awards.txt'):
        self.json_file = json_file
        self.data = None
        self.load_data()

    def load_data(self):
        """Load data from the JSON file."""
        try:
            with open(self.json_file, 'r') as file:
                self.data = json.load(file)
        except FileNotFoundError:
            print(f"Error: File '{self.json_file}' not found.")
            exit()
        except json.JSONDecodeError:
            print("Error: Failed to decode JSON file.")
            exit()

    def get_user_inputs(self):
        """Get inputs from the user for the quiz."""
        self.month = input("Enter the month for the quiz (e.g., August): "
                           ).capitalize() or 'August'
        self.year = input(
            "Enter the year for the quiz (default is 2024): ") or "2024"
        self.num_questions = int(
            input("Enter the number of questions for the quiz: "))

    def type_1_question(self, award_name, correct_answer):
        """Generate a Type-1 question."""
        question = f"Who was awarded with '{award_name}'?"
        options = [item['who_awarded'] for item in self.data['award_section']]
        random_options = random.sample(options, 3)
        if correct_answer not in random_options:
            random_options.append(correct_answer)
        random.shuffle(random_options)
        return question, correct_answer, random_options

    def type_2_question(self, award_name, country):
        """Generate a Type-2 question."""
        question = f"Award '{award_name}' belongs to which country?"
        options = [item['country'] for item in self.data['award_section']]
        random_options = random.sample(options, 3)
        if country not in random_options:
            random_options.append(country)
        random.shuffle(random_options)
        return question, country, random_options

    def type_3_question(self, awardee, award_name, correct_designation):
        """Generate a Type-3 question."""
        question = f"Who is {awardee} who has been awarded with '{award_name}'?"
        options = [
            item['awardee_designation'] for item in self.data['award_section']
        ]
        random_options = random.sample(options, 3)
        if correct_designation not in random_options:
            random_options.append(correct_designation)
        random.shuffle(random_options)
        return question, correct_designation, random_options

    def start_quiz(self):
        """Start the quiz."""
        self.get_user_inputs()

        questions = [
            item for item in self.data['award_section']
            if item['month'] == self.month and item['year'] == self.year
        ]
        if not questions:
            print("No questions available for the selected month and year.")
            return

        score = 0
        print("\n--- Quiz Starts ---\n")
        for _ in range(self.num_questions):
            question_data = random.choice(questions)
            question_type = random.choice([1, 2, 3])

            if question_type == 1:
                question, correct_answer, options = self.type_1_question(
                    question_data['award_name'], question_data['who_awarded'])
            elif question_type == 2 and question_data['country'] != "India":
                question, correct_answer, options = self.type_2_question(
                    question_data['award_name'], question_data['country'])
            else:
                question, correct_answer, options = self.type_3_question(
                    question_data['who_awarded'], question_data['award_name'],
                    question_data['awardee_designation'])

            print(question)
            for idx, option in enumerate(options, 1):
                print(f"{idx}. {option}")

            answer = input("Enter the number of your answer: ")
            if options[int(answer) - 1] == correct_answer:
                print("✅Correct!")
                score += 1
            else:
                print(f"❌Wrong! The correct answer is '{correct_answer}'.")
            print(f"Description: {question_data['description']}\n")

        print(
            f"--- Quiz Ends ---\nYour final score: {score}/{self.num_questions}"
        )


# Main Execution Block
if __name__ == "__main__":
    quiz = CAQuiz()
    quiz.start_quiz()
