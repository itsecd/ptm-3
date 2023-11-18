import re
import json
import pandas as pd
import os
from checksum import calculate_checksum, serialize_result
from check_cols_func import check_data_col, check_ipv4, check_longitude
from typing import Callable

VARIANT = 10
CSV_PATH = f"{VARIANT}.csv"
PATTERNS_PATH = "patterns.json"


def read_patterns(path_to_file: str) -> json:
    '''
    Считывание паттернов из файла path_to_file
    :params path_to_file: path to file with patterns
    :return: json file with patterns
    '''
    patterns = []
    with open(path_to_file, 'r') as fp:
        patterns = json.load(fp)
    return patterns


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
    print(result)
    return result


def start_check(dataset: pd.DataFrame) -> set:
    '''
    Начало проверки dataset
    :params dataset: dataset to check
    :return: set of list with found indexes
    '''
    patterns = []
    patterns = read_patterns(PATTERNS_PATH)
    result = set()
    for col in dataset.columns:
        if col == "date":
            result.update(check_column(
                dataset, col, patterns[col], check_data_col))
        if col == "ip_v4":
            result.update(check_column(
                dataset, col, patterns[col], check_ipv4))
        if col == "longitude":
            result.update(check_column(
                dataset, col, patterns[col], check_longitude))
        else:
            result.update(check_column(dataset, col, patterns[col]))
    return result


if __name__ == "__main__":
    os.system("cls")
    dataset = pd.read_csv(CSV_PATH, sep=";", encoding="utf-16")
    result = start_check(dataset)
    print(calculate_checksum(list(result)))
    serialize_result(VARIANT, calculate_checksum(list(result)))
