import re
import json
import logging
import pandas as pd
from checksum import calculate_checksum, serialize_result
from typing import List, Callable

logger = logging.getLogger()
logger.setLevel('INFO')

VARIANT = 62
CSV_FILE = '62.csv'
PATTERNS_FILE = 'patterns.json'


def is_correct_ip(ip: str) -> bool:
    """
    Функция проверяет корректность чисел в IP.

    :param ip: IP в формате "[0-999].[0-999].[0-999].[0-999]".
    :return: Корректен ли IP.
    """
    numbers = list(map(int, re.findall(r'\d{1,3}', ip)))
    for number in numbers:
        if number > 255:
            return False
    return True


def is_correct_latitude(latitude: str) -> bool:
    """
    Функция проверяет корректность широты.

    :param latitude: широта.
    :return: Корректна ли широта.
    """
    latitude = float(latitude)
    return -90 < latitude < 90


def is_correct_date(date: str) -> bool:
    """
    Функция проверяет корректность даты.

    :param date: дата в формате yyyy-mm-dd.
    :return: Корректна ли дата.
    """
    date = list(map(int, re.findall(r'\d+', date)))
    return 0 < date[0] < 2025 and 0 < date[1] < 13 and 0 < date[2] < 32


def find_invalid_entries(dataframe: pd.DataFrame, column: str, pattern: str,
                         is_correct: Callable[[str], bool] = lambda x: True) -> List[int]:
    """
    Функция находит все неподходящие заданному шаблону записи в некотором столбце датафрейма.

    :param dataframe: датафрейм с данными.
    :param column: идентификатор столбца датафрейма, по записям которого происходит поиск.
    :param pattern: шаблон, определяющий корректную запись.
    :param is_correct: Дополнительная функция проверки.
    :return: список с номерами всех записей, неудовлетворяющих шаблону.
    """
    if not (column in dataframe.keys()):
        raise KeyError(f'Dataframe contains columns {", ".join(list(dataframe.keys()))}, but given column {column}')
    invalid_entries = []
    for i in range(len(dataframe[column])):
        if not re.fullmatch(pattern, dataframe[column][i], re.X) or not is_correct(dataframe[column][i]):
            invalid_entries.append(i)
    logging.info(f'Column {column}: {len(invalid_entries)} invalid entries was found')
    return invalid_entries


if __name__ == '__main__':
    dataset = pd.read_csv(CSV_FILE, sep=';', quotechar='"', encoding='utf-16')
    with open(PATTERNS_FILE, 'r') as fp:
        patterns = json.load(fp)
    row_numbers = set()
    try:
        row_numbers.update(find_invalid_entries(dataset, 'telephone', patterns['telephone']))
        row_numbers.update(find_invalid_entries(dataset, 'http_status_message', patterns['http_status_message']))
        row_numbers.update(find_invalid_entries(dataset, 'inn', patterns['inn']))
        row_numbers.update(find_invalid_entries(dataset, 'identifier', patterns['identifier']))
        row_numbers.update(find_invalid_entries(dataset, 'ip_v4', patterns['ip_v4'], is_correct_ip))
        row_numbers.update(find_invalid_entries(dataset, 'latitude', patterns['latitude'], is_correct_latitude))
        row_numbers.update(find_invalid_entries(dataset, 'blood_type', patterns['blood_type']))
        row_numbers.update(find_invalid_entries(dataset, 'isbn', patterns['isbn']))
        row_numbers.update(find_invalid_entries(dataset, 'uuid', patterns['uuid']))
        row_numbers.update(find_invalid_entries(dataset, 'date', patterns['date'], is_correct_date))
        checksum = calculate_checksum(list(row_numbers))
        serialize_result(VARIANT, checksum)
        logging.info('Checksum was successfully calculated and serialized')
    except KeyError as error:
        logging.error(error)
