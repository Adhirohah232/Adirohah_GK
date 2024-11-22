import random


class QuizGenerator:

    def __init__(self):
        self.data = []
        self.load_data()

    def load_data(self):
        """Load and parse the CA_schemes.txt file."""
        try:
            with open("CA_schemes.txt", "r") as file:
                content = file.read()
                self.parse_data(content)
        except FileNotFoundError:
            print("Error: CA_schemes.txt file not found.")

    def parse_data(self, content):
        """Parse the content of the file and structure it into a usable format."""
        raw_schemes = eval(content.replace(
            '\\n', ''))  # Convert the text content into a Python dictionary
        self.data = raw_schemes.get("schemes", [])

    def generate_question(self, scheme):
        """Generate a question from a given scheme."""
        statements = "\n> " + "\n> ".join(scheme.get("statements", []))
        if scheme.get('whatItis') in ['scheme', 'policy']:
            question = f"Consider the following statements:\n{statements}\n\n - related to which scheme/policy/ministry?"
        else:
            question = f"Consider the following statements:\n{statements}\n\n -  related to which {scheme.get('whatItis')}?"

        correct_option = scheme.get("scheme_name", "")

        # Generate 3 random options + the correct option
        options = [
            s.get("scheme_name", "") for s in self.data
            if s.get("scheme_name", "") != correct_option
        ]
        random.shuffle(options)
        options = options[:3] + [correct_option]
        random.shuffle(options)

        return question, options, correct_option, scheme.get(
            "description", "No description available.")

    def start_quiz(self):
        """Start the quiz based on user input."""
        month = input("Enter the month (e.g., August): ").strip() or 'August'
        year = input("Enter the year (e.g., 2024): ").strip() or '2024'
        num_questions = int(input("Enter the number of questions: ").strip())

        filtered_schemes = [
            scheme for scheme in self.data if scheme.get("month", "") == month
            and scheme.get("year", "") == year
        ]

        if not filtered_schemes:
            print(f"No data available for {month} {year}.")
            return

        random.shuffle(filtered_schemes)
        selected_schemes = filtered_schemes[:num_questions]

        score = 0

        for idx, scheme in enumerate(selected_schemes, start=1):
            question, options, correct_option, description = self.generate_question(
                scheme)
            print(f"\n🌱 Question {idx}:")
            print(question)
            print('\n')
            for i, option in enumerate(options, start=1):
                print(f"{i}. {option}")

            user_answer = int(input("Your answer (1-4): ").strip())
            if options[user_answer - 1] == correct_option:
                print("✅Correct!")
                score += 1
            else:
                print(f"❌Wrong! The correct answer is: {correct_option}")

            print(f"Description: {description}\n")

        print(f"Your final score: {score}/{num_questions}")


# To use the QuizGenerator class, create an instance and call start_quiz().
if __name__ == "__main__":
    quiz = QuizGenerator()
    quiz.start_quiz()
