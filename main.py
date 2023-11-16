import csv
import os
import re

from checksum import serialize_result, calculate_checksum

PATTERNS = {
    "email": r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
    "http_status_message": r'\b\d{3}\b',
    "inn": r'\d{12}',
    "passport": r'\b\d+\s\d+\s\d+\b',
    "ip_v4": r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b',
    "latitude": r'[-+]?\d+\.\d+',
    "hex_color": r'#[a-fA-F0-9]{6}\b',
    "isbn":  r'\b\d{1,3}(?:-?\d){1,5}-?\d{1,7}-?\d\b',
    "uuid": r'\b[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}\b',
    "time": r'\b(?:[01]\d|2[0-3]):[0-5]\d:[0-5]\d\b'
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
            print(k)
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
    print(len(erroneous_lines))
    serialize_result(53, calculate_checksum(erroneous_lines))

