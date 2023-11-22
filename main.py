import os
import csv
import re

from checksum import calculate_checksum, serialize_result

VARIANT = 60

PATTERNS = {
    "telephone": "^\+7-\(\d{3}\)-\d{3}-\d{2}-\d{2}$",
    "height": "^(?:0|1|2)\.\d{2}$",
    "snils": "^\d{11}$",
    "identifier": "^\d{2}-\d{2}/\d{2}$",
    "occupation": "^[a-zA-Zа-яА-ЯёЁ\s-]+$",
    "longitude": "^-?\d{1,3}\.\d+$",
    "blood_type": "^(AB|A|B|O)[−+-]?$",
    "issn": "^\d{4}\-\d{4}$",
    "locale_code": "^[a-z]{2}(-[a-z]{2})?$",
    "date": "^\d{4}-\d{2}-\d{2}$"
}

row_example = [
    "+7-(925)-245-54-22",
    "1.23",
    "12345678901",
    "12-34/56",
    "Математик",
    "123.456",
    "AB+",
    "1234-5678",
    "en-il",
    "2023-11-22"
]

def check_row(row: list) -> bool:
    """
        Проверка строки на валидность
        :param row: list
        :return: bool
    """
    for patterns, item in zip(PATTERNS.keys(), row):
        if not re.search(PATTERNS[patterns], item):
            print(patterns, item)
            return False
    return True

result = check_invalid_row(row_example)
print(result) 