import csv
import re
from checksum import calculate_checksum, serialize_result


PATTERNS = {
    'telephone': r'\+7 - \(\d{3}\) - \d{3} - \d{2} - \d{2}',
    "height": "^(?:0|1|2)\.\d{2}$",
    "inn": "^\d{12}$",
    'identifier': r'\d{2} - \d{2} / \d{2}',
    "occupation": "^[a-zA-Zа-яА-ЯёЁ\s-]+$",
    "latitude": "^(-?[1-8]?\d(?:\.\d{1,})?|90(?:\.0{1,})?)$",
    'blood_type': r'(?: AB | A | B | O) [+−]',
    "issn": "^\d{4}-\d{4}$",
    "uuid": "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$",
    'date': r'\d{4} - \d{2} - \d{2}'
}


def check_invalid_row(row: list) -> bool:
    """
        Функция проверки каждой строки на валидность
    """
    flag = True
    for key, item in zip(PATTERNS.keys(), row):
        if not re.match(PATTERNS[key], item):
            flag = False
            return flag
    return flag


def get_no_invalid_data_index(data: list) -> list:
    """
        Функция находит невалидные строки и записывает их индексы
    """
    data_index = []
    index = 0
    for row in data:
        if not check_invalid_row(row):
            data_index.append(index)
        index += 1
    return data_index


if __name__ == "__main__":
    data = []
    with open("48.csv", "r", newline="", encoding="utf-16") as file:
        read_data = csv.reader(file, delimiter=";")
        for row in read_data:
            data.append(row)
    data.pop(0)
    serialize_result(48, calculate_checksum(get_no_invalid_data_index(data)))
