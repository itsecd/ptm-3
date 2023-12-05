import pandas as pd
import re
from checksum import calculate_checksum, serialize_result
from regular_expressions import regexps
from typing import List


def find_invalid_entries(data_column: pd.Series, regexp: str) -> List[int]:
    """
    эта функция проверяет записи в столбце на валидность
    :param data_column: столбец данных
    :param regexp: регулярное выражение для проверки данных
    :return: список строк, которые являются некорректными
    """
    invalid_rows = list()
    for i in range(len(data_column)):
        if not re.match(regexp, data_column[i]):
            invalid_rows.append(i)
    return invalid_rows


if __name__ == "__main__":
    data = pd.read_csv("47.csv", sep=";", encoding="utf-16")
    invalid_rows = list()
    invalid_rows.extend(find_invalid_entries(data["email"], regexps["email"]))
    invalid_rows.extend(find_invalid_entries(data["height"], regexps["height"]))
    invalid_rows.extend(find_invalid_entries(data["inn"], regexps["inn"]))
    invalid_rows.extend(find_invalid_entries(data["passport"], regexps["passport"]))
    invalid_rows.extend(find_invalid_entries(data["occupation"], regexps["occupation"]))
    invalid_rows.extend(find_invalid_entries(data["latitude"], regexps["latitude"]))
    invalid_rows.extend(find_invalid_entries(data["hex_color"], regexps["hex_color"]))
    invalid_rows.extend(find_invalid_entries(data["issn"], regexps["issn"]))
    invalid_rows.extend(find_invalid_entries(data["uuid"], regexps["uuid"]))
    invalid_rows.extend(find_invalid_entries(data["time"], regexps["time"]))
    calculated_sum = calculate_checksum(invalid_rows)
    serialize_result(47, calculated_sum)
