import sys

from modes.total_score_mode import total_score_mode_exec

acceptance_score = 60


# Program start
print('1. Calculate total score, 2. Calculate subject score')

# Get mode
mode_num = sys.stdin.readline().rstrip()

if mode_num == '1':
    total_score_mode_exec(acceptance_score)
else:
    print('\nGoodbye')
