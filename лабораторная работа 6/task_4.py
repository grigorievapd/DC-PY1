import json

INPUT_FILE = "input_1.csv"
OUTPUT_FILE = "output.json"

def csv_to_list_dict(filename, delimiter=',', new_line='\n') -> list[dict]:
    with open(filename) as f:
        list_ = []
        for ind, line in enumerate(f):
            rows = line.strip(new_line).split(delimiter)
            if ind == 0:
                headers = rows
                continue
            list_.append({})
            for i, _ in enumerate(headers):
                list_[-1][headers[i]] = rows[i]

    return list_
    ...  # TODO реализовать конвертер из csv в json


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
