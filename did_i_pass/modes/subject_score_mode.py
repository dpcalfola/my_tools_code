import sys

# json library
import json

# Load snippets
from did_i_pass.modes import snippets

# Load Subject class
from did_i_pass.modes.classes import Subject

# Load config.json
config_path = sys.path[1] + "/did_i_pass/config.json"
with open(config_path, "r") as json_file:
    config_data = json.load(json_file)


# Module main
def subject_score_mode_exec():
    # Declare variables
    subjects_obj_list: list = []

    # Input method
    get_information(subjects_obj_list)

    # Exit if there's no input data
    if not subjects_obj_list:
        print('\nNo data: Program exit')
        return

    # Calculating overall
    overall: dict = calculate_overall(subjects_obj_list)

    # Print result
    print_result(subjects_obj_list, overall)


# Methods

def get_information(obj_list: list) -> list:
    subject_cnt: int = 1

    # ===== Start point of the loop of getting one subject information =====
    while True:
        escape_flag: bool = False
        subject_question_number: int = -9999
        input_score: int = -9999
        subject_ordinal: str = snippets.get_ordinal(subject_cnt)[1]

        # Get subject_question_number
        while not escape_flag:
            print(f'\n< {subject_ordinal} subject questions >')
            print(f'Enter the number of {subject_ordinal} subject questions')
            print('[0]: End up and Calculate')

            get_input = sys.stdin.readline().rstrip()

            if get_input == '0':
                return obj_list

            escape_flag, subject_question_number = snippets.non_integer_filter(get_input)

        escape_flag = False

        # Get input_score
        while not escape_flag:
            print(f'\n< {subject_ordinal} subject score >')
            print(f'Enter your score')
            print('Correct(positive integer) or incorrect(negative integer)')
            print('[0]: End up and Calculate')

            get_input = sys.stdin.readline().rstrip()

            if get_input == '0':
                return obj_list

            escape_flag, input_score = snippets.non_integer_filter(get_input)

        escape_flag = False

        # Raise error : Score is lager than questions
        # Go back to current subject_cnt
        if abs(input_score) > subject_question_number:
            print('\nError : Score is lager than questions')
            continue

        # Create Subject obj and append to obj_list
        subject = Subject(subject_cnt, subject_question_number, input_score)
        obj_list.append(subject)

        subject_cnt += 1

        # Raise error: Exceeded the allowable limit of subject number
        if subject_cnt > 100:
            print('Error: Exceeded the allowable limit of subject number')
            print('Please Enter any key to progress')
            _ = sys.stdin.readline().rstrip()
            return obj_list

        # ===== End point of the loop of getting one subject information =====


def calculate_overall(subjects_obj_list: list) -> dict:
    # Load acceptance_score from config
    acceptance_score: int = config_data['subject_fail_score']

    # Declare variables
    overall: dict = {}
    total_questions: int = 0
    total_correct: int = 0
    total_converted_score: float = -1
    is_pass_overall: bool = False
    is_subject_pass: bool = True

    # Calculate
    for subject in subjects_obj_list:
        total_questions += subject.subject_questions
        total_correct += subject.correct
        # If there's any failed subject, total_is_pass changes to False
        if not subject.is_pass:
            is_subject_pass = False

    total_converted_score = total_correct / total_questions * 100

    if total_converted_score >= acceptance_score and is_subject_pass:
        is_pass_overall = True

    # Save overall result to dict
    overall = {
        'total_questions': total_questions,
        'total_correct': total_correct,
        'total_converted_score': total_converted_score,
        'is_pass_overall': is_pass_overall
    }
    return overall


def print_result(subjects_obj_list: list, overall: dict):
    # Config variable
    acceptance_score: int = config_data['acceptance_score']
    subject_fail_score: int = config_data['subject_fail_score']

    # Print config data
    print()
    print('====================== CONFIG ======================')
    print(f'acceptance_score: {acceptance_score}')
    print(f'subject_fail_score: {subject_fail_score}')

    #
    print()
    print('====================== SCORES ======================')

    # Print each subject result
    for subject in subjects_obj_list:
        subject_ordinal: str = snippets.get_ordinal(subject.num)[1]

        print()
        print(f'< {subject_ordinal} subject >')
        print(f'questions: {subject.subject_questions}')
        print(f'input_score: {subject.input_score}')
        print(f'correct: {subject.correct}')
        print(f'incorrect: {subject.incorrect}')
        print(f'converted_subject_score: {subject.converted_subject_score}')
        print(f'subject_fail: {subject.fail_message}')

    # Print overall result
    total_questions = overall['total_questions']
    total_correct = overall['total_correct']
    total_converted_score = overall['total_converted_score']
    is_pass_overall = overall['is_pass_overall']

    print()
    print('< OVERALL >')
    print(f'total_questions: {total_questions}')
    print(f'total_correct: {total_correct}')
    print(f'your_score: {total_converted_score}')
    print(f'is_pass_overall: {is_pass_overall}')

    # Print Consequence
    print()
    print('====================== RESULT ======================')
    print()
    print('DID I PASSED? : PASSED' if is_pass_overall else 'DID I PASSED? : FAILED')
    print()
    print('====================================================')
