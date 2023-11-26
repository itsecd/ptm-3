import csv
import re
import json
import hashlib
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

def validation(str):
    global k
    regex_str = {
        "email": re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"),
        "height": re.compile(r"^(1|2)\.\d{2}$"),
        "snils": re.compile(r"^\d{11}$"),
        "passport": re.compile(r"\d{2} \d{2} \d{6}", re.ASCII),
        "occupation": re.compile(r"[А-ЯA-Z-][\w]*"),
        "longitude": re.compile(r"^[-]?\d{1,3}\.\d{1,6}$"),
        "hex_color": re.compile(r"^#[a-f0-9]{6}$", re.IGNORECASE),
        "issn": re.compile(r"\b\d{4}-[\dX]{4}"),
        "locale_code": re.compile(r"^\w{2}(?:-\w{2})?$", re.IGNORECASE | re.ASCII),
        "time": re.compile(r"\d{2}:\d{2}:\d{2}\.\d{6}", re.ASCII)
    }

    for title, value in str.items():
        if not re.match(regex_str[title], value):
            print(f"{title}")
            return True
    return False

def indexes():
    indexes = []
    index = 0
    with open("51.csv", 'r', encoding="utf-16") as f:
        data = csv.reader(f, delimiter=";")
        for row in data:
            headers = row
            break
        for row in data:
            if validation(dict(zip(headers, row))):
                indexes.append(index)
                print(index)
            index +=1
    return indexes

if __name__ == "__main__":
    neded_indexes = indexes()
    print('len: ',len(neded_indexes))
    hash = calculate_checksum(neded_indexes)
    serialize_result(51, hash)