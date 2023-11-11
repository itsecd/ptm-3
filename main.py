import re
import logging
import pandas as pd
from checksum import calculate_checksum, serialize_result
from typing import List

CSV_FILE = '62.csv'


def find_invalid_entries(dataframe: pd.DataFrame, column: str, pattern: str) -> List[int]:
    """
    Функция находит все неподходящие заданному шаблону записи в некотором столбце датафрейма.

    :param dataframe: датафрейм с данными.
    :param column: идентификатор столбца датафрейма, по записям которого происходит поиск.
    :param pattern: шаблон, определяющий корректную запись.
    :return: список с номерами всех записей, неудовлетворяющих шаблону.
    """
    if not (column in dataframe.keys()):
        raise KeyError(f'Dataframe contains columns {", ".join(list(dataframe.keys()))}, but given column {column}')
    invalid_entries = []
    for i in range(len(dataframe[column])):
        if not re.fullmatch(pattern, dataframe[column][i], re.X):
            invalid_entries.append(i)
    return invalid_entries


if __name__ == '__main__':
    dataset = pd.read_csv(CSV_FILE, sep=';', quotechar='"', encoding='utf-16')
    row_numbers = []
    try:
        row_numbers += (find_invalid_entries(dataset, 'telephone', r'\+7-'
                                                                   r'\(\d{3}\)-'
                                                                   r'\d{3}-'
                                                                   r'\d{2}-'
                                                                   r'\d{2}'))
        row_numbers += (find_invalid_entries(dataset, 'http_status_message', r'\d{3}'
                                                                             r'\s'
                                                                             r'.+'))
        row_numbers += (find_invalid_entries(dataset, 'inn', r'\d{12}'))
        row_numbers += (find_invalid_entries(dataset, 'identifier', r'\d{2}-'
                                                                    r'\d{2}/'
                                                                    r'\d{2}'))
        row_numbers += (find_invalid_entries(dataset, 'ip_v4', r'(?: (?: 25[0-5]) | (?: 2[0-4]\d) | (?: 1?\d{,2}) )\.'
                                                               r'(?: (?: 25[0-5]) | (?: 2[0-4]\d) | (?: 1?\d{,2}) )\.'
                                                               r'(?: (?: 25[0-5]) | (?: 2[0-4]\d) | (?: 1?\d{,2}) )\.'
                                                               r'(?: (?: 25[0-5]) | (?: 2[0-4]\d) | (?: 1?\d{,2}) )'))
        # row_numbers += (find_invalid_entries(dataset, 'latitude', r'\d{2}-\d{2}/\d{2}'))
        # row_numbers += (find_invalid_entries(dataset, 'blood_type', r'\d{2}-\d{2}/\d{2}'))
        # row_numbers += (find_invalid_entries(dataset, 'isbn', r'\d{2}-\d{2}/\d{2}'))
        # row_numbers += (find_invalid_entries(dataset, 'uuid', r'\d{2}-\d{2}/\d{2}'))
        # row_numbers += (find_invalid_entries(dataset, 'date', r'\d{2}-\d{2}/\d{2}'))
        print(len(row_numbers))
    except KeyError as error:
        logging.error(error)

