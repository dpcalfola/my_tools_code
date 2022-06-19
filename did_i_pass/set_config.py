# Import for making json
import json
from collections import OrderedDict

# CONFIG
# acceptance_score : 합격 기준 (%)
# subject_fail_score : 과락 기준 (%)
# 아래의 값을 변경 후 현재 파일(set_config.py)을 실행하면 변경된 값이 config.json 파일로 저장됩니다.
acceptance_score: int = 60
subject_fail_score: int = 40

# Make config.json
config_data = OrderedDict()
config_data["acceptance_score"] = acceptance_score
config_data["subject_fail_score"] = subject_fail_score

with open('config.json', 'w', encoding="utf-8") as make_file:
    json.dump(config_data, make_file, ensure_ascii=False, indent="\t")