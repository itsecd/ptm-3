import json
import hashlib
import csv
import re
from typing import List

"""
В этом модуле обитают функции, необходимые для автоматизированной проверки результатов ваших трудов.
"""


def calculate_checksum(row_numbers: List[int]) -> str:
    """
    Вычисляет md5 хеш от списка целочисленных значений.

    ВНИМАНИЕ, ВАЖНО! Чтобы сумма получилась корректной, считать, что первая строка с данными csv-файла имеет номер 0
    Другими словами: В исходном csv 1я строка - заголовки столбцов, 2я и остальные - данные.
    Соответственно, считаем что у 2 строки файла номер 0, у 3й - номер 1 и так далее.

    Надеюсь, я расписал это максимально подробно.
    Хотя что-то мне подсказывает, что обязательно найдется человек, у которого с этим возникнут проблемы.
    Которому я отвечу, что все написано в докстринге ¯\_(ツ)_/¯

    :param row_numbers: список целочисленных номеров строк csv-файла, на которых были найдены ошибки валидации
    :return: md5 хеш для проверки через github action
    """
    row_numbers.sort()
    return hashlib.md5(json.dumps(row_numbers).encode('utf-8')).hexdigest()


def serialize_result(variant: int, checksum: str) -> None:
    """
    Метод для сериализации результатов лабораторной пишите сами.
    Вам нужно заполнить данными - номером варианта и контрольной суммой - файл, лежащий в корне репозитория.
    Файл называется, очевидно, result.json.

    ВНИМАНИЕ, ВАЖНО! На json натравлен github action, который проверяет корректность выполнения лабораторной.
    Так что не перемещайте, не переименовывайте и не изменяйте его структуру, если планируете успешно сдать лабу.

    :param variant: номер вашего варианта
    :param checksum: контрольная сумма, вычисленная через calculate_checksum()
    """
    with open("result.json", "w") as f:
        json.dump({"variant" : str(variant), "checksum": checksum}, f, indent=2)
    
right_str = {
    "telephone": re.compile(r"^\+7-\(9\d{2}\)-\d{3}-\d{2}-\d{2}$"),
    "height": re.compile(r"^[1-2]\.\d{1,2}$"),
    "snils": re.compile(r"^\d{11}$"),
    "identifier": re.compile(r"\d{2}-\d{2}/\d{2}"),
    "occupation": re.compile(r"[А-ЯA-Z-][\w]*"),
    "longitude": re.compile(r"^-?((1[0-7]\d)|([0-9]\d?)|180)(?:\.\d+)$"),
    "blood_type": re.compile(r"(B|A|O|AB)(\+|\u2212)"),
    "issn": re.compile(r"\d{4}-\d{4}"),
    "locale_code": re.compile(r"^[a-z]{2}(-[a-z]{2})?$"),
    "date": re.compile(r"20\d{2}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])")
}
    
def check_string(string):
  
    for title, value in string.items():
        if not re.match(right_str[title], value):
            return True
    return False

    
def get_wrong_indexes():
    indexes = []
    index = 0
    with open("52.csv", 'r', encoding="utf-16") as f:
        data = csv.reader(f, delimiter=";")
        for row in data:
            headers = row
            break
        for row in data:
            row_data = dict(zip(headers, row))
            if check_string(row_data):
                indexes.append(index)
            index +=1
    return indexes


if __name__ == "__main__":
    wrong_string_indexes = get_wrong_indexes()
    print(len(wrong_string_indexes))
    hash = calculate_checksum(wrong_string_indexes)
    serialize_result(52, hash)