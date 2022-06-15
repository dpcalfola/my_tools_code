import sys

# json
import json

# Load snippet
from did_i_pass.modes.snippets import non_integer_filter

# Load config.json
config_path = sys.path[1] + "/did_i_pass/config.json"
with open(config_path, "r") as json_file:
    config_data = json.load(json_file)


def total_score_mode_exec():
    # Set config variable
    acceptance_score = config_data['acceptance_score']

    # Declare variables
    total_questions: int = -9999
    answers_num: int = -9999
    correct: int = -9999
    incorrect: int = -9999
    escape_flag: bool = False
    converted_score: float = 0.0
    result_message: str = ''

    # Get total number of questions
    while not escape_flag:
        print('\n< Enter total number of questions >')
        get_input = sys.stdin.readline().rstrip()
        escape_flag, total_questions = non_integer_filter(get_input)

    escape_flag = False

    # Get the number of correct answers or incorrect answers
    while not escape_flag:
        print(f'\n< Enter your score >')
        print('Correct(positive integer) or incorrect(negative integer)')
        get_input = sys.stdin.readline().rstrip()
        escape_flag, answers_num = non_integer_filter(get_input)

    escape_flag = False

    # Process
    if answers_num >= 0:
        correct = answers_num
        incorrect = total_questions - correct
    else:
        correct = total_questions + answers_num
        incorrect = -1 * answers_num

    converted_score = correct / total_questions * 100

    if converted_score >= acceptance_score:
        result_message = 'PASSED'
    else:
        result_message = 'FAILED'

    # Print result
    print()
    print('====================== SCORES ======================')
    print(f'total_questions: {total_questions}')
    print(f'your_input: {answers_num}')
    print(f'correct: {correct}')
    print(f'incorrect: {incorrect}')
    print('====================================================')
    print(f'acceptance_score: {acceptance_score}')
    print(f'your_score: {converted_score}')
    print('====================== RESULT ======================')
    print(f'DID I PASSED ?: {result_message}')
    print('====================================================')
