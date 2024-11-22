import random
import re
from ca import interactive_quiz
from ca_award import CAQuiz
from CA_scheme import QuizGenerator
from operations import OperationsQuiz

print("🙏WELCOME🙏 to Ask_GK 😃\n")
print('1. Important protocols\n')
print('2. Shifting cultivations\n')
print('3. Grasslands\n')
print('4. Indian Tribes\n')
print('5. Tissues\n')
print('6. polity\n')
print('7. National parks\n')
print('8. Defence\n')
print('9. Current Affairs\n')

filename = ''
file_input = int(
    input('Choose any one from the given fields you want me to ask from: '))
print('---------------------------------------------------\n')
if file_input > 0 and file_input < 10:
    if file_input == 1:
        filename = './protocols.txt'
    elif file_input == 2:
        filename = './shifting_cultivation.txt'
    elif file_input == 3:
        filename = './grassland.txt'
    elif file_input == 4:
        filename = './tribes.txt'
    elif file_input == 5:
        print('pt: plant tissue\n')
        print('at: animal tissue\n')
        tissue_input = input('choose one: ')
        if tissue_input == 'pt':
            filename = './planttissue.txt'
        else:
            filename = './animaltissue.txt'
    elif file_input == 6:
        print('bf: borrowed features\n')
        print('pts: constitutional parts\n')
        print('sl: schedules\n')

        polity_input = input('choose one: ')
        if polity_input == 'bf':
            filename = './borrowedfeatures.txt'
        elif polity_input == 'pts':
            filename = './part.txt'
        elif polity_input == 'sl':
            filename = './schedules.txt'
    elif file_input == 7:
        filename = './nationalparks.txt'
    elif file_input == 8:
        print('opt: operations\n')
        op_input = input('choose one from above: ')
        if op_input == 'opt':
            OperationsQuiz().start_quiz()
            exit()
    elif file_input == 9:
        start_again = 'n'
        repeat = True
        while (repeat):
            print('state: state related CA\n')
            print('awards: awards related CA\n')
            print('scheme: schemes related CA\n')
            ca_input = input('choose one from the above: ')
            if (ca_input == 'state'):
                interactive_quiz()
                start_again = input('want to start quiz on CA again? (y/n): ')
                print('-------------------------------------------\n')
                if (start_again == 'n'):
                    exit()
            elif (ca_input == 'awards'):
                CAQuiz().start_quiz()
                start_again = input('want to start quiz on CA again? (y/n): ')
                print('-------------------------------------------\n')

                if (start_again == 'n'):
                    exit()
            elif (ca_input == 'scheme'):
                QuizGenerator().start_quiz()
                start_again = input('want to start quiz on CA again? (y/n): ')
                print('-------------------------------------------\n')

                if (start_again == 'n'):
                    exit()

limit = int(input('How many questions do you want me to ask?: '))
score = 0


def get_random_word(terms):
    keys = list(terms.keys())
    random.shuffle(keys)
    random_index = random.randint(0, len(keys) - 1)
    return keys[random_index]


def get_anyword_forchoice(terms):
    anyword = random.choice(list(terms.values()))
    anyword_arr = anyword.split(', ')
    random_ind = random.randint(0, len(anyword_arr) - 1)
    result = anyword_arr[random_ind]
    if '(' in result and ')' in result:
        result = re.sub(r'\([^)]*\)', '', result)
    return result


with open(filename, 'r', encoding='utf-8') as file:
    result = file.readlines()

terms = {}
for line in result:
    if '. ' in line:
        parts = line.split('. ')
        serial = parts[0]
        definition = '. '.join(parts[1:])
        term, meaning = definition.split(': ')
        terms[term.strip()] = meaning.strip()

for i in range(limit):
    if filename == './planttissue.txt' or filename == './animaltissue.txt':
        askword = get_random_word(terms)
        askword_values = terms[askword].split(', ')
        random.shuffle(askword_values)

        # Check if the question is about living or dead tissues
        if 'living.' in askword_values or 'dead.' in askword_values:
            is_living = 'living.' in askword_values
            print(f'.................................')
            print(
                f'{i + 1}) Which tissue is {"living." if is_living else "dead."}?'
            )
            correct_tissue = askword

            if is_living:
                wrong_choices = [
                    key for key, value in terms.items()
                    if 'dead.' in value.split(', ')
                ]
            else:
                wrong_choices = [
                    key for key, value in terms.items()
                    if 'living.' in value.split(', ')
                ]

            if len(wrong_choices) < 3:
                wrong_choices += [
                    key for key in terms.keys()
                    if key not in wrong_choices and key != correct_tissue
                ]

            choices = random.sample(wrong_choices, min(
                3, len(wrong_choices))) + [correct_tissue]
            random.shuffle(choices)

            for j in range(4):
                print(f'{j + 1}. {choices[j]}')

            user_input = int(input('Your answer: '))
            if user_input < 1 or user_input > 4:
                print(
                    'Invalid choice. Please choose a number between 1 and 4.')
                continue

            selected_choice = choices[user_input - 1]
            if selected_choice == correct_tissue:
                score += 1
                print('Remark: CORRECT!!😊')
            else:
                print(
                    f'Remark: INCORRECT🥲, the correct answer is: {correct_tissue}'
                )
            print('.................................\n')

        else:
            askword_value = random.choice(askword_values).strip()
            print('.................................')
            print(
                f'{i + 1}) > {askword_value.upper()} is related to/type of/char of:'
            )
            correct_term = askword
            terms_keys = list(terms.keys())
            terms_keys.remove(correct_term)
            choices = random.sample(terms_keys, min(
                3, len(terms_keys))) + [correct_term]
            random.shuffle(choices)

            for j in range(4):
                print(f'{j + 1}. {choices[j]}')

            user_input = int(input('Your answer: '))
            if user_input < 1 or user_input > 4:
                print(
                    'Invalid choice. Please choose a number between 1 and 4.')
                continue

            selected_choice = choices[user_input - 1]
            if selected_choice == correct_term:
                score += 1
                print('Remark: CORRECT!!😊')
            else:
                print(
                    f'Remark: INCORRECT🥲, the correct answer is: {correct_term}'
                )
            print('.................................\n')

    elif filename == './tribes.txt':
        askword = get_random_word(terms)
        askword_values = terms[askword].split(', ')
        random.shuffle(askword_values)
        ask_tribe = random.choice(askword_values).strip()

        print('.................................')
        print(f'{i + 1}) > {ask_tribe.upper()}-tribe belongs to:')
        correct_region = askword

        regions = list(terms.keys())
        regions.remove(correct_region)
        choices = random.sample(regions, 3) + [correct_region]
        random.shuffle(choices)

        for j in range(4):
            print(f'{j + 1}. {choices[j]}')

        user_input = int(input('Your answer: '))
        if user_input < 1 or user_input > 4:
            print('Invalid choice. Please choose a number between 1 and 4.')
            continue

        selected_choice = choices[user_input - 1]
        if selected_choice == correct_region:
            score += 1
            print('Remark: CORRECT!!😊')
        else:
            print(
                f'Remark: INCORRECT🥲, the correct answer is: {correct_region}')
        print('.................................\n')

    elif filename == './borrowedfeatures.txt':
        askword = get_random_word(terms)
        askword_values = terms[askword].split(', ')
        random.shuffle(askword_values)
        ask_feature = random.choice(askword_values).strip()

        print('.................................')
        print(f'{i + 1}) concept of "{ask_feature.upper()}" -taken from:')
        correct_region = askword

        regions = list(terms.keys())
        regions.remove(correct_region)
        choices = random.sample(regions, 3) + [correct_region]
        random.shuffle(choices)

        for j in range(4):
            print(f'{j + 1}. {choices[j]}')

        user_input = int(input('Your answer: '))
        if user_input < 1 or user_input > 4:
            print('Invalid choice. Please choose a number between 1 and 4.')
            continue

        selected_choice = choices[user_input - 1]
        if selected_choice == correct_region:
            score += 1
            print('Remark: CORRECT!!😊')
        else:
            print(
                f'Remark: INCORRECT🥲, the correct answer is: {correct_region}')
        print('.................................\n')

    elif filename == './part.txt' or filename == './schedules.txt':
        askword = get_random_word(terms)
        askword_values = terms[askword].split(', ')
        random.shuffle(askword_values)
        ask_feature = random.choice(askword_values).strip()

        print('.................................')
        print(f'{i + 1}). "{ask_feature.upper()}" -:')
        correct_region = askword

        regions = list(terms.keys())
        regions.remove(correct_region)
        choices = random.sample(regions, 3) + [correct_region]
        random.shuffle(choices)

        for j in range(4):
            print(f'{j + 1}. {choices[j]}')

        user_input = int(input('Your answer: '))
        if user_input < 1 or user_input > 4:
            print('Invalid choice. Please choose a number between 1 and 4.')
            continue

        selected_choice = choices[user_input - 1]
        if selected_choice == correct_region:
            score += 1
            print('Remark: CORRECT!!😊')
        else:
            print(
                f'Remark: INCORRECT🥲, the correct answer is: {correct_region}')
        print('.................................\n')

    elif filename == './nationalparks.txt':
        askword = get_random_word(terms)
        askword_values = terms[askword].split(', ')
        random.shuffle(askword_values)
        ask_feature = random.choice(askword_values).strip()

        print('.................................')
        print(
            f'{i + 1}). "{ask_feature.upper()}"- national park is situated in:'
        )
        correct_region = askword

        regions = list(terms.keys())
        regions.remove(correct_region)
        choices = random.sample(regions, 3) + [correct_region]
        random.shuffle(choices)

        for j in range(4):
            print(f'{j + 1}. {choices[j]}')

        user_input = int(input('Your answer: '))
        if user_input < 1 or user_input > 4:
            print('Invalid choice. Please choose a number between 1 and 4.')
            continue

        selected_choice = choices[user_input - 1]
        if selected_choice == correct_region:
            score += 1
            print('Remark: CORRECT!!😊')
        else:
            print(
                f'Remark: INCORRECT🥲, the correct answer is: {correct_region}')
        print('.................................\n')

    else:
        askword = get_random_word(terms)
        print('.................................')
        print(f'{i + 1}) Choose the correct answer for: {askword.upper()}')
        answord = terms[askword]

        if '(' in answord and ')' in answord:
            answord = re.sub(r'\([^)]*\)', '', answord)

        answord_arr = answord.split(', ')
        random_ind = random.randint(0, len(answord_arr) - 1)
        choice1 = answord_arr[random_ind]
        choice2 = get_anyword_forchoice(terms)
        choice3 = get_anyword_forchoice(terms)
        choice4 = get_anyword_forchoice(terms)

        print('Your choices: ')
        user_choices = [choice1, choice2, choice3, choice4]
        random.shuffle(user_choices)

        for j in range(4):
            print(f'{j + 1}. {user_choices[j]}')

        user_input = int(input('Your answer: '))
        if user_input < 1 or user_input > 4:
            print('Invalid choice. Please choose a number between 1 and 4.')
            continue

        selected_choice = user_choices[user_input - 1]
        if selected_choice in answord_arr:
            score += 1
            print('Remark: CORRECT!!😊')
            if '(' in terms[askword] and ')' in terms[askword]:
                remark = re.search(r'\((.*?)\)', terms[askword]).group(1)
                print(f'side knowledge: {remark}')
            print('.................................\n')
        else:
            common_elements = set(user_choices) & set(answord_arr)
            correct_answer = list(common_elements)[0]
            print(
                f'Remark: INCORRECT🥲, the correct answer is: {correct_answer}')
            if '(' in terms[askword] and ')' in terms[askword]:
                remark = re.search(r'\((.*?)\)', terms[askword]).group(1)
                print(f'side knowledge: {remark}')
            print('.................................\n')

if limit == 1:
    if score == limit:
        print('🎉🎉Congratulations, champion🎉🎉')
        print('You got it right😊')
    else:
        print('Sorry😔, you need to revise more')
else:
    print(f'Score: {score}/{limit}')
    if score == limit:
        print('🎉🎉Congratulations, champion🎉🎉')
        print('You got all correct😊')
    elif score >= limit / 2:
        print('You did well👍')
    else:
        print('You need to practice more😔')
print('\n')
