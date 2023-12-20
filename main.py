import csv
import re
from checksum import calculate_checksum, serialize_result
import os

EXAMPLES = {
    "telephone": "^\+7|8 \(\d{3}\) \d{3}-\d{2}-\d{2}$",
    "http_status_message": "(\d{3}) [A-Za-z\s]+$",
    "snils": "^\\d{11}$",
    "identifier": "^\d{2}-\d{2}/\d{2}$",
    "ip_v4": "^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$",
    "longitude": "^-?((\d|[1-9]\d|1[0-7]\d)(\.\d+)?|180(\.0+)?)$",
    "blood_type": "^(A|B|AB|O)[\+-]$'",
    "isbn": "^\d{3}-\d{1,5}-\d{1,7}-\d{1,7}-\d$",
    "locale_code": "^[a-z]{2}-[a-z]{2}$",
    "date": "^\d{4}-\d{2}-\d{2}$"
}

def valid_check(line: list[str]):
    """
    Проверяет на соответствие значение в строках с примерами из EXAMPLES

            Параметры:
                    line(list[str]): строка значений из csv-файла
    """

    for key, value in zip(EXAMPLES.keys(), line):
        if not re.match(EXAMPLES[key], value):
            return False
    return True

def invalid_line(path: str):
    """
    Возвращает список строк csv-файла, значения которых не совпадают с примерами

            Параметры:
                    path(str): путь к csv-файлу
    """

    index_list = []
    values = []
    with open(path, "r", newline="", encoding="utf-16") as file:
        data = csv.reader(file, delimiter=";")
        for line in data:
            values.append(line)
    values.pop(0)
    for i, line in enumerate(values):
        if not valid_check(line):
            index_list.append(i)
    return index_list

if __name__ == "__main__":
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "50.csv")
    invalid_lines = invalid_line(path)
    serialize_result(50, calculate_checksum(invalid_lines))
