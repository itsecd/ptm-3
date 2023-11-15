import csv
import os
import re

from checksum import serialize_result, calculate_checksum

PATTERNS = {
    "email": "[a-zA-Z0-9._%+-]+@+[a-zA-Z0-9._%+-]+.[a-z]",
    "http_status_message": "\\d{3} +[a-zA-Z ]{1,}",
    "inn": "\\d{12}",
    "passport": "\\d{2}\\s\\d{2}\\s\\d{6}",
    "ip_v4": "\\d{1,3}(\\.+\\d{1,3}){3}",
    "latitude": "-?\\d{1,2}\\.\\d{4,}",
    "hex_color": "#[a-f0-9]{6}",
    "isbn": "(\\d+-){4}\\d+",
    "uuid": "[a-f0-9]{8}([-a-f0-9]{4}){4}[a-f0-9]{12}",
    "time": "([01]\\d|2[0-3]):([0-5]\\d):([0-5]\\d)\\.(\\d{1,6})"
}


def is_valid_line(row: list[str]) -> bool:
    """
    функция которая проверяет: соответствует ли каждое значение в строке
    шаблону в PATTERNS.
    :param row: list[str]
    :return: bool
    """
    flag = True
    for k, v in zip(PATTERNS.keys(), row):
        if not re.match(PATTERNS[k], v):
            flag = False
            return flag
    return flag


def get_invalid_lines(csv_file: str) -> list[int]:
    """
    функция, которая возвращает список индексов строк CSV-файла, не соответствующих ожидаемым шаблонам.
    :param csv_file: str
    :return: list[int]
    """
    lst = []
    data = []
    with open(csv_file, "r", newline="", encoding="utf-16") as file:
        read_data = csv.reader(file, delimiter=";")
        for row in read_data:
            data.append(row)
    data.pop(0)
    for i, row in enumerate(data):
        if not is_valid_line(row):
            lst.append(i)
    return lst


if __name__ == "__main__":
    csv_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "53.csv")
    erroneous_lines = get_invalid_lines(csv_file)
    print(erroneous_lines)
    serialize_result(53, calculate_checksum(erroneous_lines))

