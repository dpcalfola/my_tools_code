import sys

# Import modes
from modes.total_score_mode import total_score_mode_exec
from modes.subject_score_mode import subject_score_mode_exec

# json library
import json

# Load config.json
config_path = sys.path[1] + "/did_i_pass/config.json"
with open(config_path, "r") as json_file:
    config_data = json.load(json_file)

acceptance_score = config_data['acceptance_score']
subject_fail_score = config_data['subject_fail_score']

# Program start
print('1. Calculate pass/fail from total score')
print('2. Calculate failure of each subject and pass/fail')
print(f'(acceptance_score: {acceptance_score}% / subject_fail_score: {subject_fail_score}%)')

# Get mode
mode_num = sys.stdin.readline().rstrip()

if mode_num == '1':
    total_score_mode_exec()
elif mode_num == '2':
    subject_score_mode_exec()
else:
    print('\nGoodbye')
