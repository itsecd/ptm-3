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


def check_row(row: list) -> bool:
    """
        Проверка строки на валидность
        :param row: list
        :return: bool
    """
    for patterns, item in zip(PATTERNS.keys(), row):
        if not re.search(PATTERNS[patterns], item):
            return False
    return True


def read_csv(file_name: str) -> list:
    """
        Считывает данные из файла csv и возвращает список строк
        :param file_name: str
        :return: list
    """
    data_rows = []
    with open(file_name, "r", newline="", encoding="utf-16") as file:
        reader = csv.reader(file, delimiter=";")
        for elem in reader:
            data_rows.append(elem)
    data_rows.pop(0)
    return data_rows


def find_invalid_check(data: list) -> None:
    """
        Нахождение индексов неверных данных и вызов 
        функций автоматической проверки результатов
        :param data: list
        :return: None
    """
    list_index = []
    index = 0
    for elem in data:
        if not check_row(elem):
            list_index.append(index)
        index += 1
    # print(list_index)
    # print(len(list_index))
    serialize_result(VARIANT, calculate_checksum(list_index))

if __name__ == "__main__":
    find_invalid_check(read_csv("60.csv"))