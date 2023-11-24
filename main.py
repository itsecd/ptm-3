import json
import re
import pandas as pd
from checksum import calculate_checksum, serialize_result
from typing import List, Callable


def check_corect_latitude(latitude_tmp: str) -> bool:
    """
        Проверка широты на корректность
        :param latitude_tmp: str
        :return: true or false
    """
    value = float(latitude_tmp)
    return -90 < value < 90


def check_correct_ip(ip: str) -> bool:
    """
        Проверка корректности чисел в IP.
        :param ip: str
        :return: true or false
    """
    numbers = list(map(int, re.findall(r'\d{1,3}', ip)))
    for number in numbers:
        if number > 255:
            return False
    return True


def check_correct_date(date: str) -> bool:
    """
    Функция проверяет корректность даты.
    :param date: дата в формате yyyy-mm-dd.
    :return: true or false
    """
    date = list(map(int, re.findall(r'\d+', date)))
    return 0 < date[0] < 2025 and 0 < date[1] < 13 and 0 < date[2] < 32


def read_csv(file_name: str) -> pd.DataFrame:
    """
        Считывает данные из файла csv
    """
    dataset = pd.read_csv(file_name, sep=';', quotechar='"', encoding='utf-16')
    return dataset


def find_invalid_entries(dataframe: list, column: str, pattern: str,
                         is_correct: Callable[[str], bool] = lambda x: True) -> List[int]:
    """
        Функция находит все неподходящие заданному шаблону записи в некотором столбце датафрейма.
    """
    if not (column in dataframe.keys()):
        return None
    invalid_entries = []
    for i in range(len(dataframe[column])):
        if not re.fullmatch(pattern, dataframe[column][i], re.X) or not is_correct(dataframe[column][i]):
            invalid_entries.append(i)
    return invalid_entries


if __name__ == "__main__":
    VARIANT = 54
    data = read_csv("54.csv")
    with open("regespx.json", 'r') as fp:
        patterns = json.load(fp)
    row_numbers = set()
    row_numbers.update(find_invalid_entries(data, 'telephone', patterns['telephone']))
    row_numbers.update(find_invalid_entries(data, 'http_status_message', patterns['http_status_message']))
    row_numbers.update(find_invalid_entries(data, 'inn', patterns['inn']))
    row_numbers.update(find_invalid_entries(data, 'identifier', patterns['identifier']))
    row_numbers.update(find_invalid_entries(data, 'ip_v4', patterns['ip_v4'], check_correct_ip))
    row_numbers.update(find_invalid_entries(data, 'latitude', patterns['latitude'], check_corect_latitude))
    row_numbers.update(find_invalid_entries(data, 'blood_type', patterns['blood_type']))
    row_numbers.update(find_invalid_entries(data, 'isbn', patterns['isbn']))
    row_numbers.update(find_invalid_entries(data, 'uuid', patterns['uuid']))
    row_numbers.update(find_invalid_entries(data, 'date', patterns['date'], check_correct_date))
    checksum = calculate_checksum(list(row_numbers))
    serialize_result(VARIANT, checksum)

