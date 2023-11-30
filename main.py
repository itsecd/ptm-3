import csv
import json
import re

from checksum import serialize_result, calculate_checksum


def csv_reader(path: str) -> list:
    """Читаем из csv-файла и записываем в list

        path (str): путь к файлу

        list: список с прочитанными строками файла
    """
    data = []
    with open(path, "r", encoding="utf16") as file:
        reader = csv.reader(file, delimiter=";")
        for row in reader:
            data.append(row)
        data.pop(0)
    return data


def json_reader(path: str) -> dict:
    """Читаем из json-файла и записываем в словарь

        path (str): путь к файлу

        dict: словарь с данными из файла
    """
    with open(path, 'r') as fp:
        patterns = json.load(fp)
    return patterns


def is_valid_row(row: list, patterns: dict) -> bool:
    """Функция, проверяющая каждый элемент строки на вадидность

        row (list): строка из таблицы
        patterns (dict): словарь с паттернами регулярных выражений

        bool: валидно/невалидно
    """
    for key, value in zip(patterns.keys(), row):
        if not re.fullmatch(patterns[key], value):
            return False
    return True


def is_valid_data(path_json: str, path_csv: str) -> None:
    """Функция, проходящаяся по строкам списка и записывающая номера невалидных.
    После передает список невалидных в функцию сериализации

        path_json (str): путь к json файлу
        path_csv (str): путь к csv файлу
    """
    patterns = json_reader(path_json)
    data = csv_reader(path_csv)
    invalid_rows = []
    for i in range(len(data)):
        if not is_valid_row(data[i], patterns):
            invalid_rows.append(i)
    serialize_result(14, calculate_checksum(invalid_rows))


if __name__ == "__main__":
    is_valid_data("patterns.json", "data.csv")
