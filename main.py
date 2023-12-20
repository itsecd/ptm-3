import csv
import json
import logging
import re
from checksum import serialize_result, calculate_checksum


logger = logging.getLogger()
logger.setLevel("INFO")
CSV_PATH = "1.csv"
REGEXPS_PATH = "REGEXPS.json"
VARIANT = 1


def read_csv(path_to_csv: str) -> list:
    """Функция считывает из csv файла данные и записывает их в список
    Args:
        path_to_csv (str): путь к csv файлу
    Returns:
        list: данные из файла
    """
    data = []
    try:
        with open(path_to_csv, "r", encoding="utf16") as file:
            reader = csv.reader(file, delimiter=";")
            for row in reader:
                data.append(row)
            data.pop(0)
    except FileNotFoundError:
        logging.error(f"Файл {path_to_csv} не найден.")
    except Exception as e:
        logging.error(f"Произошла ошибка при чтении csv файла: {e}")
    return data


def read_json(path_json: str) -> dict:
    """Функция считывает из json файла данные и записывает их в кортеж
    Args:
        path_json (str): путь к файлу
    Returns:
        dict: данные
    """
    data = {}
    try:
        with open(path_json, "r") as json_file:
            data = json.load(json_file)
    except FileNotFoundError:
        logging.error(f"Файл {path_json} не найден.")
    except Exception as e:
        logging.error(f"Произошла ошибка при чтении json файла: {e}")
    return data


def validate_row(row: list, patterns: dict) -> bool:
    """Функция проверяет каждый элемент из строки массива на валидность данных
    Args:
        row (list): строка из csv таблицы
        patterns (dict): кортеж с регулярными выражениями
    Returns:
        bool: результат проверки
    """
    for key, value in zip(patterns.keys(), row):
        if not re.match(patterns[key], value):
            return False
    return True


def validate_data(path_json: str, path_csv: str) -> None:
    """Функция проходит по всему массиву данных из csv файла и 
    записывает номера невалидных строк в список. 
    Полученный список передается в функцию сериализации
    Args:
        path_json (str): путь файлу с регулярными выражениями 
        path_csv (str): путь файлу с данными
    """
    patterns = read_json(path_json)
    data = read_csv(path_csv)
    nonvalidate_rows = []
    for i in range(len(data)):
        if not validate_row(data[i], patterns):
            nonvalidate_rows.append(i)
    serialize_result(VARIANT, calculate_checksum(nonvalidate_rows))

def validation_report(path_json: str, path_csv: str) -> None:
    """Функция выводит отчет по валидации файла в консоль"""
    patterns = read_json(path_json)
    data = read_csv(path_csv)
    invalid_counts = {key: 0 for key in patterns.keys()}
    total_invalid_records = 0

    for i, row in enumerate(data, start=1):
        for key, value in zip(patterns.keys(), row):
            if not re.match(patterns[key], value):
                invalid_counts[key] += 1
                total_invalid_records += 1

    print("\n" + "=" * 40)
    print("Отчет по валидации файла:")
    print("-" * 40)

    for key, count in invalid_counts.items():
        print(f"{key}: {count} ошибочных значений")

    print("-" * 40)
    print(f"Всего невалидных записей: {total_invalid_records}")
    print("=" * 40 + "\n")

if __name__ == "__main__":
    validate_data(REGEXPS_PATH, CSV_PATH)
    validation_report(REGEXPS_PATH, CSV_PATH)