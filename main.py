import csv
import re
from checksum import serialize_result, calculate_checksum

PATTERNS = {
    "telephone": "^\+7-\(\d{3}\)-\d{3}-\d{2}-\d{2}$",
    "height": "^(?:0|1|2)\.\d{2}$",
    "inn": "^\d{12}$",
    "identifier": "^\d{2}-\d{2}/\d{2}$",
    "occupation": "^[a-zA-Zа-яА-ЯёЁ\s-]+$",
    "latitude": "^(-?[1-8]?\d(?:\.\d{1,})?|90(?:\.0{1,})?)$",
    "blood_type": "^(AB|A|B|O)[−+-]?$",
    "issn": "^\d{4}-\d{4}$",
    "uuid": "^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$",
    "date": "^\d{4}-\d{2}-\d{2}$"
}


def get_data(filename: str) -> list:
    """
    Получение данных из csv файла.
    :param filename: Имя файла.
    """
    data = []
    with open(filename, "r", newline="", encoding="utf-16") as file:
        read_data = csv.reader(file, delimiter=";")
        for row in read_data:
            data.append(row)
    return data


def data_check(data: list) -> list:
    """
    Проверяет валидность данных.
    :param data: Проверяемые данные.
    """
    data.pop(0)
    invalid_lines = []
    for index, row in enumerate(data):
        for key, value in zip(PATTERNS.keys(), row):
            if not re.match(PATTERNS[key], value):
                invalid_lines.append(index)
    return invalid_lines


if __name__ == '__main__':
    data = get_data("56.csv")
    invalid_lines = data_check(data)
    serialize_result(56, calculate_checksum(invalid_lines))