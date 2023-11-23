import csv
import json
import re
from checksum import serialize_result, calculate_checksum

CSV_PATH = "9.csv"
JSON_PATH = "regexps.json"


def read_csv(path: str) -> list:
    """ Читает данные из csv файла и записывает в список.

    Аргументы:
        path(str): путь csv файла
    
    Возвращаемое значение:
        list: список данных из csv файла
    """
    data = []
    try: 
        with open(path, "r", encoding="utf16") as file:
            reader = csv.reader(file, delimiter=";")
            for row in reader:
                data.append(row)
            data.pop(0)
    except Exception as err:
        print(f"Error reading of file:{err}")
    return data


def read_exps(path: str) -> dict:
    """ Читает json файл с регулярками и записывает в словарь.

    Аргументы:
        path(str): путь до регулярок

    Возвращаемое значение: 
        dict: прочитанные в словарь регулярки
    """
    data = {}
    try: 
        with open(path, "r") as file:
            data = json.load(file)
    except Exception as err:
        print(f"Error reading of file:{err}")
    return data 


def chek_row(row: list, exps: dict) -> bool:
    """ Проверяет соответствие строки данных ругулярному выражению.

    Аргументы: 
        row(list): строка из датасета
        exps(dict): словарь регулярок

    Возвращаемое значение:
        bool: True, если строка соотвествует выражению. False - иначе
    """
    for key, value in zip(exps.keys(), row):
        if not re.match(exps[key], value):
            return False
    return True


def validate_data(path_csv: str, path_json: str) -> list:
    """ Записывает номера строк, которые не соотвествуют регулярным выражениям. 
    
    Аргументы: 
        path_csv(str): путь до датасета
        path_json(str): путь до регулярок

    Возвращаемое значение:
        list: список с номерами невалидных строк
    """
    rows_numbers = []
    data = read_csv(path_csv)
    regexps = read_exps(path_json)
    for i in range(len(data)):
        if not chek_row(data[i], regexps):
            rows_numbers.append(i)
    return rows_numbers


if __name__ == "__main__":
    invalid_rows = validate_data(CSV_PATH, JSON_PATH)
    hash_sum = calculate_checksum(invalid_rows)
    serialize_result(9, hash_sum)
    