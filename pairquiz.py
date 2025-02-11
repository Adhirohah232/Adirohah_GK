import random

def parse_data(file_path):
    """
    Parse the input text file and return a list of tuples (sanctuary_name, state_name).
    """
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            if line.strip():  # Ignore empty lines
                # Split on colon and strip extra spaces
                parts = line.strip().split(':')
                if len(parts) == 2:
                    sanctuary, state = parts[0].strip(), parts[1].strip()
                    data.append((sanctuary, state))
    return data


def generate_quizpair(file_path):
    """
    Generate a quiz with unique random questions from the parsed data.
    """
    data = parse_data(file_path)

    num_questions = int(input(f"How many questions do you want to answer?(limit- {len(data)}): "))
    if num_questions > len(data):
        print("Error: Number of questions exceeds available data.")
        return

    questions = random.sample(data, num_questions)
    states = list(set(state for _, state in data))  # Unique state names

    score = 0
    for idx, (sanctuary, correct_state) in enumerate(questions, 1):
        # Generate random options including the correct answer
        options = set([correct_state])
        while len(options) < 4:
            options.add(random.choice(states))
        options = list(options)
        random.shuffle(options)

        # Display the question
        print()
        print(f"🍁 Ques: {idx}.")
        print(f'{sanctuary} - \n')
        for i, option in enumerate(options, ord('a')):
            print(f"  {chr(i)}. {option}")

        # Take the user's answer
        answer = input("Your answer (a/b/c/d): ").strip().lower()
        correct_option = chr(options.index(correct_state) + ord('a'))

        if answer == correct_option:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong. The correct answer was {correct_option}. {correct_state}\n")

    print(f"Quiz Complete! Your Score: {score}/{num_questions}\n")
    exit()
