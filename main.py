import random
import re
from ca import interactive_quiz
from ca_award import CAQuiz
from CA_scheme import QuizGenerator
from operations import OperationsQuiz
from defence_loc import AutomatedQuiz

print("🙏WELCOME🙏 to Ask_GK 😃\n")
print("-------------------------------\n")
print("1. Environment\n")
print('2. India\n')
print('3. Tissues\n')
print('4. polity\n')
print('5. Defence\n')
print('6. History\n')
print('7. Current Affairs\n')

filename = ''
file_input = int(
    input('Choose any one from the given fields you want me to ask from: '))
print('---------------------------------------------------\n')
if file_input > 0 and file_input < 10:
    if file_input == 1:
        print('ip: Important protocols\n')
        print('sc: Shifting cultivations\n')
        print('gl: Grasslands\n')
        print('lake: lakes\n')
        print('np: National parks\n')
        print('rp: Important revolutions and its purpose\n')
        print('rf: Importand revolutions and their fathers\n')
        print('ied: Important days related to environment\n')
        print('iy: Importand years related to environment\n')
        
        env_input = input('choose one: ')
        if env_input == 'ip':
            filename = './protocol.txt'
        elif env_input=='sc':
            filename = './shifting_cultivation.txt'
        elif env_input=='np':
            filename = './nationalparks.txt' 
        elif env_input=='rp':
            filename = './revolution_purpose.txt'  
        elif env_input=='rf':
            filename = './revolution_father.txt'
        elif env_input=='ied':
            filename = './imp_envdays.txt' 
        elif env_input=='iy':
            filename = './imp_envyears.txt'  
        else:
            filename = './grassland.txt'
    elif file_input == 2:
        print('cnn: Indian cities and their nicknames\n')
        print('itb: Indian tribes\n')
        ind_input = input('choose one: ')
        if(ind_input=='cnn'):
            filename = './city_nicknames.txt'
        elif(ind_input == 'itb'):
            filename = './tribes.txt'
    elif file_input == 3:
        print('pt: plant tissue\n')
        print('at: animal tissue\n')
        tissue_input = input('choose one: ')
        if tissue_input == 'pt':
            filename = './planttissue.txt'
        else:
            filename = './animaltissue.txt'
    elif file_input == 4:
        print('bf: borrowed features\n')
        print('pts: constitutional parts\n')
        print('sl: schedules\n')
        print('amd: amendments\n')

        polity_input = input('choose one: ')
        if polity_input == 'bf':
            filename = './borrowedfeatures.txt'
        elif polity_input == 'pts':
            filename = './part.txt'
        elif polity_input == 'amd':
            amd_input = input('amd1, amd2, amd3, amd4(choose one): ')
            if(amd_input == 'amd1'):
                filename = './amendments.txt'
            elif(amd_input == 'amd2'):
                filename = './amendments2.txt'
            elif(amd_input == 'amd3'):
                filename = './amendments3.txt'
            elif(amd_input == 'amd4'):
                filename = './amendments4.txt'
        else:
            filename = './schedules.txt'

    elif file_input == 5:
        print('opt: operations\n')
        print("loc: Defence Institutes and locations")
        op_input = input('choose one from above: ')
        if op_input == 'opt':
            OperationsQuiz().start_quiz()
            exit()
        if op_input == 'loc':
            AutomatedQuiz().start_quiz()
            exit()
    elif file_input == 6:
        print('srmi: Social and religious movements in India\n')
        print('fih: first in History\n')

        history_input = input('choose one: ')
        if history_input == 'srmi':
            filename = './socio_religious.txt'
            print("🍁 for the questions(who started the Religious movement) below- options will be given for the names.🍁\n")
        elif history_input=='fih':
            fih_input = input('choose one: fih1, fih2, fih3: ')
            if fih_input=='fih1':
                filename = './firstIn_history.txt'
            if fih_input=='fih2':
                filename = './firstIn_history2.txt'
            if fih_input=='fih3':
                filename = './firstIn_history3.txt'


    elif file_input == 7:
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

    elif filename == './part.txt' or filename == './schedules.txt' or filename=='./amendments.txt' or filename =='./city_nicknames.txt':
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
