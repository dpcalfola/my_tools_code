import sys

# json library
import json

# Load snippets
from did_i_pass.modes import snippets

# Load config.json
config_path = sys.path[1] + "/did_i_pass/config.json"
with open(config_path, "r") as json_file:
    config_data = json.load(json_file)


class Subject:
    # Set config variable
    subject_fail_score: int = config_data['subject_fail_score']

    # Fields
    num: int
    subject_questions: int
    input_score: int
    correct: int
    incorrect: int
    converted_subject_score: float
    is_pass: bool
    fail_message: str

    # All field is going to set when obj is constructed
    def __init__(self, num: int, subject_questions: int, input_score: int):
        self.num = num
        self.subject_questions = subject_questions
        self.input_score = input_score

        # Set other fields from calling calculating method
        self.calculate_subject()

    # Calculating method
    def calculate_subject(self):

        # Set correct and incorrect
        if self.input_score >= 0:
            self.correct = self.input_score
            self.incorrect = self.subject_questions - self.input_score
        else:
            self.correct = self.subject_questions + self.input_score
            self.incorrect = -1 * self.input_score

        #
        self.converted_subject_score = self.correct / self.subject_questions * 100

        #
        if self.converted_subject_score < self.subject_fail_score:
            self.is_pass = False
            self.fail_message = 'failed'
        else:
            self.is_pass = True
            self.fail_message = 'passed'
