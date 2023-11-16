import csv
import os
import re

from checksum import serialize_result, calculate_checksum

PATTERNS = {
    "email": "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$",
    "http_status_message": "\\d{3}\\s[a-zA-Z]{1,}",
    "inn": r'^\b\d{12}\b$',
    "passport": "^\\d{2}\\s\\d{2}\\s\\d{6}$",
    "ip_v4": "^\\d{1,3}\\.+\\d{1,3}\\.+\\d{1,3}\\.+\\d{1,3}$",  # yes
    "latitude": "^-?(?:90(?:\\.0+)?|[1-8]?\\d(?:\\.\\d+)?)$", # yes
    "hex_color": "^#([a-f0-9]{6}|[a-f0-9]{3})$",#yes
    "isbn":  "\\d+-\\d+-\\d+-\\d+(:?-\\d+)?", #yes
    "uuid": r'^\b[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\b$', #yes
    "time": "^([01]\\d|2[0-3]):([0-5]\\d):([0-5]\\d)\\.(\\d{1,6})$" #yes
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
            print(k + " : " + v)
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

