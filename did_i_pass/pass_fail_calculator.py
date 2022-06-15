import sys

# Import for making json
import json
from collections import OrderedDict

# Import modes
from modes.total_score_mode import total_score_mode_exec
from modes.subject_score_mode import subject_score_mode_exec

# CONFIG : 합격 기준 & 과락 기준
acceptance_score: int = 60
subject_fail_score: int = 40

# Make config.json
config_data = OrderedDict()
config_data["acceptance_score"] = acceptance_score
config_data["subject_fail_score"] = subject_fail_score

with open('config.json', 'w', encoding="utf-8") as make_file:
    json.dump(config_data, make_file, ensure_ascii=False, indent="\t")

# Program start
print('1. Calculate pass/fail from total score')
print('2. Calculate failure of each subject and pass/fail')

# Get mode
mode_num = sys.stdin.readline().rstrip()

if mode_num == '1':
    total_score_mode_exec()
elif mode_num == '2':
    subject_score_mode_exec()
else:
    print('\nGoodbye')
