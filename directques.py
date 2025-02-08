import random
import sys
import os


class QuizGeneratordirect:
    def __init__(self, filename):
        """Initialize and start quiz automatically"""
        try:
            # Check if file exists
            if not os.path.exists(filename):
                print(f"Error: File '{filename}' not found!")
                sys.exit(1)

            self.questions = []
            self.load_questions(filename)

            # Only start quiz if questions were loaded successfully
            if self.questions:
                self.run_quiz()
            else:
                print("Error: No valid questions found in the file!")
                sys.exit(1)

        except Exception as e:
            print(f"Error initializing quiz: {str(e)}")
            sys.exit(1)

    def load_questions(self, filename):
        """Load and parse questions from the text file."""
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                content = file.read()
                # Split questions by double newlines to handle multi-line blocks
                raw_questions = content.strip().split("\n\n")

                for block in raw_questions:
                    try:
                        lines = block.strip().split("\n")
                        if len(lines) >= 3:  # Ensure block contains question, options, and answer
                            question_text = lines[0].strip()
                            options_line = lines[1].strip().lstrip('[').rstrip(']')
                            options = [opt.strip() for opt in options_line.split(',')]
                            answer_line = lines[2].strip().replace('Ans:', '').strip()

                            if answer_line in options:  # Ensure the correct answer is valid
                                self.questions.append({
                                    'question': question_text,
                                    'options': options,
                                    'answer': answer_line
                                })
                            else:
                                print(f"Warning: Skipping question due to invalid answer: '{answer_line}' not in options.")
                    except Exception as e:
                        print(f"Warning: Skipping invalid block: {str(e)}")

        except Exception as e:
            print(f"Error reading file: {str(e)}")
            sys.exit(1)

    def run_quiz(self):
        """Run the quiz automatically"""
        print("\n=== Quiz Started ===\n")

        # Ask for number of questions
        while True:
            try:
                num_questions = int(input(f"🌱 How many questions would you like to attempt? (max {len(self.questions)}): 🌱"))
                if num_questions <= 0:
                    print("Please enter a positive number.")
                elif num_questions > len(self.questions):
                    print(f"Warning: Only {len(self.questions)} questions available. Using all questions.")
                    num_questions = len(self.questions)
                    break
                else:
                    break
            except ValueError:
                print("Please enter a valid number.")
            except KeyboardInterrupt:
                print("\nQuiz cancelled by user.")
                sys.exit(0)

        # Select random questions
        selected_questions = random.sample(self.questions, num_questions)
        score = 0

        try:
            for i, q in enumerate(selected_questions, 1):
                print(f"\n🍁 Question {i}:")
                print(q['question'])

                # Randomize options
                options = q['options'].copy()
                random.shuffle(options)

                # Display options
                for j, opt in enumerate(options, 1):
                    print(f"{j}. {opt}")

                # Get user input
                while True:
                    try:
                        answer = input("\nYour answer (enter the number): ")
                        if answer.lower() in ['q', 'quit', 'exit']:
                            print("\nQuiz cancelled by user.")
                            sys.exit(0)

                        answer_idx = int(answer) - 1
                        if 0 <= answer_idx < len(options):
                            user_answer = options[answer_idx]
                            break
                        else:
                            print(f"Please enter a number between 1 and {len(options)}")
                    except ValueError:
                        print("Invalid input! Please enter a number.")
                    except KeyboardInterrupt:
                        print("\nQuiz cancelled by user.")
                        sys.exit(0)

                # Check answer
                if user_answer == q['answer']:
                    print("Correct! ✅")
                    score += 1
                else:
                    print(f"Wrong! ❌ The correct answer was: {q['answer']}")

            # Display final score
            print("\n" + "=" * 40)
            print(f"\nQuiz completed! Your score: {score}/{num_questions}")
            percentage = (score / num_questions) * 100
            print(f"Percentage: {percentage:.2f}%\n")

        except Exception as e:
            print(f"\nAn error occurred during the quiz: {str(e)}")
            sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        QuizGeneratordirect(sys.argv[1])
    else:
        print("Please provide a filename as argument!")
        print("Usage: python quiz_generator.py <filename>")