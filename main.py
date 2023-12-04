import re
import os
import pandas as pd
from checksum import calculate_checksum, serialize_result
from func_for_check import check_latitude, check_ip, check_time
from typing import Callable

PATTERNS = {
    "email": "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$",
    "http_status_message": "^\\d{3}\\s[^\n\r]+$",
    "inn": "^\\d{12}$",
    "passport": "^\\d{2} \\d{2} \\d{6}$",
    "ip_v4": "^(\\d{1,3}\\.){3}\\d{1,3}$",
    "latitude": "^(-?[1-8]?\\d(?:\\.\\d{1,})?|90(?:\\.0{1,})?)$",
    "hex_color": "^#[0-9a-fA-F]{6}$",
    "isbn": "\\d+-\\d+-\\d+-\\d+(:?-\\d+)?$",
    "uuid": "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$",
    "time": "^([01][0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9])\\.([0-9]{6})$"
}


def check_column(dataset: pd.DataFrame, column: str, pattern: str, check_correct: Callable[[str], bool] = lambda x: True) -> list[int]:
    '''
    Проверка конкретного column в dataset на соответствие pattern, при необходимости проверяется значение ф-цией check_correct
    :params dataset: dataset to search incorrect cells
    :params column: column of dataset's
    :params pattern: pattern that use to search
    :params check_correct: function needed to check some value like date or degree
    :return: found indexes
    '''
    result = []
    for i in range(len(dataset[column])):
        if not re.fullmatch(pattern, dataset[column][i], re.X) or not check_correct(dataset[column][i]):
            result.append(i)
    print(f"In '{column}' find {len(result)} incorrect cells")
    return result


def start_check(dataset: pd.DataFrame) -> set:
    '''
    Начало проверки dataset
    :params dataset: dataset to check
    :return: set of list with found indexes
    '''
    result = set()
    for col in dataset.columns:
        if col == "time":
            result.update(check_column(
                dataset, col, PATTERNS[col], check_time))
        elif col == "ip_v4":
            result.update(check_column(
                dataset, col, PATTERNS[col], check_ip))
        elif col == "latitude":
            result.update(check_column(
                dataset, col, PATTERNS[col], check_latitude))
        else:
            result.update(check_column(dataset, col, PATTERNS[col]))
    return result


if __name__ == "__main__":
    os.system("cls")
    variant = 13
    dataset = pd.read_csv(f"{variant}.csv", sep=";", encoding="utf-16")
    result = start_check(dataset)
    print(len(result))
    print(calculate_checksum(list(result)))
    serialize_result(variant, calculate_checksum(list(result)))
