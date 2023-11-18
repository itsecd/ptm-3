import csv
import json
import re
from checksum import serialize_result, calculate_checksum


def read_csv(path_to_csv: str) -> list:
    """Функция, которая читает из csv файла данные и записывает их в список

    Args:
        path_to_csv (str): путь к csv файлу

    Returns:
        list: список с прочитанными строками csv
    """
    data = []
    try:
        with open(path_to_csv, "r", encoding="utf16") as file:
            reader = csv.reader(file, delimiter=";")
            for row in reader:
                data.append(row)
            data.pop(0)
    except FileNotFoundError:
        print(f"Файл {path_to_csv} не найден.")
    except Exception as e:
        print(f"Произошла ошибка при чтении файла: {e}")
    return data


def read_json(path_json: str) -> dict:
    """Функция, которая читает из json файла данные и записывает их в кортеж

    Args:
        path_json (str): путь к файлу

    Returns:
        dict: кортеж с данными из json
    """
    data_to_read = {}
    try:
        with open(path_json, "r") as json_file:
            data_to_read = json.load(json_file)
    except FileNotFoundError:
        print(f"Файл {path_json} не найден.")
    except Exception as e:
        print(f"Произошла ошибка при чтении файла: {e}")
    return data_to_read


def validate_row(row: list, patterns: dict) -> bool:
    """Функция, которая проверяет каждый элемент из строки массива данных на валидность данных

    Args:
        row (list): строка из csv таблицы
        patterns (dict): кортеж с паттернами регулярных выражений

    Returns:
        bool: результат проверки
    """
    for key, value in zip(patterns.keys(), row):
        if not re.match(patterns[key], value):
            return False
    return True


def validate_data(path_json: str, path_csv: str) -> None:
    """Функция, которая проходит по всему массиву данных из csv и 
    записывает номера невалидных строк в список; 
    полученный список передается в функцию сериализации

    Args:
        path_json (str): путь к json файлу с регулярными выражениями 
        path_csv (str): путь к csv файлу с данными
    """
    patterns = read_json(path_json)
    data = read_csv(path_csv)
    nonvalidate_rows = []
    for i in range(len(data)):
        if not validate_row(data[i], patterns):
            nonvalidate_rows.append(i)
    serialize_result(5, calculate_checksum(nonvalidate_rows))


if __name__ == "__main__":
    validate_data("REGEXPS.json", "5.csv")
