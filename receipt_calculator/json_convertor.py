import json

# Get json data
data_file = open('data_receipt_json/test_data_01.json', 'r', encoding='utf-8')
dataObject: dict = json.load(data_file)


def print_data(data: dict):
    print(json.dumps(data, indent=4, ensure_ascii=False))
