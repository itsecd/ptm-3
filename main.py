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
        if not re.fullmatch(pattern, dataframe[column][i]):
            invalid_entries.append(i)
    return invalid_entries


if __name__ == '__main__':
    dataset = pd.read_csv(CSV_FILE, sep=';', quotechar='"', encoding='utf-16')
    try:
        row_numbers = find_invalid_entries(dataset, 'telephone', r'\+7-\(\d{3}\)-\d{3}-\d{2}-\d{2}')
        print(calculate_checksum(row_numbers))
    except KeyError as error:
        logging.error(error)

