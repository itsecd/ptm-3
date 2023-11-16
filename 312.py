import csv
import logging
import re

TABLE_PATH = "12.CSV"
PATTERNS = {
    "telephone": "^\\+7-\\(\\d{3}\\)-\\d{3}-\\d{2}-\\d{2}$",
    "height": "^\\d\\.\\d{2}$",
    "snils": "^\\d{11}$",
    "identifier": "^\\d{2}-\\d{2}/\\d{2}$",
    "occupation": "^[a-zA-Zа-яА-ЯёЁ\\s-]+$",
    "longitude": "^-?((180(\\.0+)?|1[0-7]?\\d(\\.\\d+)?|\\d{1,2}(\\.\\d+)?)|0(\\.\\d+)?)$",
    "blood_type": "^(?:O|A|B|AB)[\\+\u2212]$",
    "issn": "^\\d{4}-\\d{4}$",
    "locale_code": "^([a-z]{2,3})(?:-([a-zA-Z]{2,4}))?(?:-([a-zA-Z0-9-]+))?$",
    "date": "^(?:19|20)\\d\\d-(?:0[1-9]|1[012])-(?:0[1-9]|[12]\\d|3[01])$"
}


def read_csv(path: str) -> list:
    rows = []
    try:
        with open(path, "r", encoding="utf-16") as file:
            reader = csv.reader(file, delimiter=";")
            for row in reader:
                rows.append(row)
        rows.pop(0)
    except OSError as err:
        logging.warning(f'{err} during reading from {path}')
    return rows


def check_row(row: list) -> bool:
    keys = list(PATTERNS.keys())
    for i in range(len(keys)):
        flag = bool(re.match(PATTERNS[keys[i]], row[i]))
        if not flag:
            return flag
    return True


def find_invalid_rows(path: str) -> list[int]:
    invalid_rows = []
    data = read_csv(path)
    for i in range(len(data)):
        if not check_row(data[i]):
            invalid_rows.append(i)
    return invalid_rows
if __name__ == "__main__":
    array = find_invalid_rows(TABLE_PATH)
    print(len(array))