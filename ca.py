import random
import json
from typing import Dict, List, Tuple, Optional, Any


class CurrentAffairsQuiz:

    def __init__(self, filename: str = "current_affairs.txt"):
        self.filename = filename
        self.data = None
        self.score = 0
        self.current_quiz_length = 0

    def load_data_from_file(self) -> Optional[Dict[str, Any]]:
        """Load and parse data from the text file"""
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                content = file.read()
                self.data = json.loads(content)
                return self.data
        except FileNotFoundError:
            print(f"Error: File '{self.filename}' not found.")
            return None
        except json.JSONDecodeError as e:
            print(f"Error: Invalid JSON format in '{self.filename}'. {e}")
            return None
        except Exception as e:
            print(f"Unexpected error reading file: {e}")
            return None

    def get_random_states(self,
                          correct_state: str,
                          all_states: List[str],
                          num_options: int = 3) -> List[str]:
        """Get random states for multiple choice, excluding the correct answer"""
        available_states = [
            state for state in all_states if state != correct_state
        ]
        random_states = random.sample(available_states,
                                      min(num_options, len(available_states)))
        options = [correct_state] + random_states
        random.shuffle(options)
        return options

    def generate_question(
            self, item: Dict[str, Any],
            all_states: List[str]) -> Tuple[str, List[str], str, str]:
        """Generate a question based on the item type"""
        if item["scheme"] == 1:
            question = f"Scheme - {item['term_to_ask']} is related/launched in which state?"
        else:
            question = f"{item['term_to_ask']} is {item['whatItis']} in/by which state/country?"

        options = self.get_random_states(item["state"], all_states)
        return question, options, item["state"], item["description"]

    def get_available_data(self) -> Tuple[str, int]:
        """Get available month and year from loaded data"""
        # Ensure data is loaded
        if not self.data:
            self.data = self.load_data_from_file()

        # Check if data loading was successful
        if not self.data or 'ca' not in self.data or len(self.data['ca']) == 0:
            print("No data available. Please check your JSON file.")
            return None, None

        # Use the first item's month and year
        return (self.data['ca'][0].get('month', 'Unknown'),
                int(self.data['ca'][0].get('year', 2024)))

    def get_available_questions(self, genre: str) -> List[Dict[str, Any]]:
        """Get questions available for a specific genre"""
        if not self.data:
            self.data = self.load_data_from_file()

        if not self.data or 'ca' not in self.data:
            return []

        return [
            item for item in self.data["ca"]
            if item["genre"].lower() == genre.lower()
        ]

    def get_all_states(self) -> List[str]:
        """Get list of all states from the data"""
        if not self.data:
            self.data = self.load_data_from_file()
        return list(set(item["state"] for item in self.data["ca"]))

    def validate_inputs(self, year: int, month: str) -> bool:
        """Validate year and month inputs"""
        if not self.data:
            self.data = self.load_data_from_file()

        # Check if any items match the input year and month
        return any(
            int(item["year"]) == year
            and item["month"].lower() == month.lower()
            for item in self.data["ca"])

    def process_answer(self, options: List[str], user_answer: int,
                       correct_answer: str) -> Tuple[bool, str]:
        """Process user's answer and return if it's correct and appropriate message"""
        is_correct = options[user_answer - 1] == correct_answer
        if is_correct:
            self.score += 1
            return True, "\n✅ Correct!"
        return False, f"\n❌ Wrong! The correct answer is: {correct_answer}"

    def get_final_score(self) -> Tuple[int, int, float]:
        """Get final score, total questions, and percentage"""
        percentage = (self.score / self.current_quiz_length
                      ) * 100 if self.current_quiz_length > 0 else 0
        return self.score, self.current_quiz_length, percentage

    def reset_score(self):
        """Reset the quiz score"""
        self.score = 0
        self.current_quiz_length = 0

    def run_quiz(self, year: int, month: str, genre: str,
                 num_questions: int) -> bool:
        """Run the quiz with given parameters"""
        # Reset score for new quiz
        self.reset_score()

        # Load data if not already loaded
        if not self.data:
            self.data = self.load_data_from_file()
            if not self.data:
                return False

        # Get relevant items filtered by genre, year, and month
        relevant_items = [
            item for item in self.data["ca"]
            if (item["genre"].lower() == genre.lower() and int(item["year"]) ==
                year and item["month"].lower() == month.lower())
        ]

        if not relevant_items:
            print(
                f"No questions available for genre: {genre} in {month} {year}")
            return False

        all_states = self.get_all_states()

        # Adjust number of questions if necessary
        num_questions = min(num_questions, len(relevant_items))
        self.current_quiz_length = num_questions

        # Generate and ask questions
        questions_to_ask = random.sample(relevant_items, num_questions)

        for question_num, item in enumerate(questions_to_ask, 1):
            question, options, correct_answer, description = self.generate_question(
                item, all_states)

            # Return the question data
            yield {
                'question_number': question_num,
                'question': question,
                'options': options,
                'correct_answer': correct_answer,
                'description': description
            }

        return True


# Example usage for interactive mode
def interactive_quiz():
    quiz = CurrentAffairsQuiz()

    # Get user inputs
    print("\nWelcome to the Current Affairs Quiz!")
    month_data, year_data = quiz.get_available_data()

    # Check if data was successfully retrieved
    if month_data is None or year_data is None:
        print("Could not retrieve quiz data. Exiting.")
        return

    print(f"Available data for: {month_data} {year_data}")

    year = int(input("Enter year (e.g., 2024): ") or 2024)
    month = input("Enter month (e.g., August): ") or 'August'
    genre = 'state'

    # Show available questions count
    available_questions = quiz.get_available_questions(genre)
    filtered_questions = [
        q for q in available_questions
        if int(q['year']) == year and q['month'].lower() == month.lower()
    ]
    print(f"\nAvailable questions for {genre}: {len(filtered_questions)}")

    # Check if there are any questions
    if len(filtered_questions) == 0:
        print("No questions available. Exiting.")
        return

    num_questions = int(
        input(f"Enter number of questions (1-{len(filtered_questions)}): "))

    # Run the quiz
    print("\nLet's start the quiz!\n")

    quiz_generator = quiz.run_quiz(year, month, genre, num_questions)
    for question_data in quiz_generator:
        print(f"\n🌱 Question {question_data['question_number']}:")
        print(question_data['question'])

        for i, option in enumerate(question_data['options'], 1):
            print(f"{i}. {option}")

        while True:
            try:
                user_answer = int(input("\nEnter your answer (1-4): "))
                if 1 <= user_answer <= len(question_data['options']):
                    break
                print("Please enter a number between 1 and 4")
            except ValueError:
                print("Please enter a valid number")

        is_correct, message = quiz.process_answer(
            question_data['options'], user_answer,
            question_data['correct_answer'])
        print(message)
        print("Description:", question_data['description'])
        print("\n" + "-" * 50)

    # Display final score
    score, total, percentage = quiz.get_final_score()
    print(f"\nQuiz completed! Your final score: {score} out of {total}")
    print(f"Percentage: {percentage:.2f}%")


if __name__ == "__main__":
    interactive_quiz()
