import sys
from did_i_pass.modes.snippets import non_integer_filter


def total_score_mode_exec(acceptance_score: int):
    # Declare variables
    total_questions: int = -9999
    answers: int = -9999
    correct: int = -9999
    incorrect: int = -9999
    escape: bool = False
    converted_score: float = 0.0
    is_passed: bool = False

    # Get total number of questions
    while not escape:
        print('\nEnter total number of questions')
        get_input = sys.stdin.readline().rstrip()
        escape, total_questions = non_integer_filter(get_input)

    escape = False

    # Get the number of correct answers or incorrect answers
    while not escape:
        print('\nEnter the number of correct answers or incorrect answers')
        print('(Correct: positive / Incorrect: negative)')
        get_input = sys.stdin.readline().rstrip()
        escape, answers = non_integer_filter(get_input)

    escape = False

    # Process
    if answers >= 0:
        correct = answers
        incorrect = total_questions - correct
    else:
        correct = total_questions + answers
        incorrect = -1 * answers

    converted_score = correct / total_questions * 100

    if converted_score >= acceptance_score:
        is_passed = True
    else:
        is_passed = False

    # Print result
    print(f'''
=========== RESULT ===========
total_questions: {total_questions}
your_input: {answers}
correct: {correct}
incorrect: {incorrect}
==============================
acceptance_score: {acceptance_score}
converted_score: {converted_score}
is_passed?: {is_passed}
    ''')
