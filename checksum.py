import json
import hashlib
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
    to_json = {
        "variant": variant,
        "checksum": checksum
    }
    
    with open('result.json', 'w') as jsonfile:
        json.dump(to_json, jsonfile, indent=2)
    pass


valid_dict = {
    'telephone': re.compile(r'\+7-\([0-9]{3}\)-[0-9]{3}(?:-[0-9]{2}){2}'),
    'height': re.compile(r'[1, 2]\.[0-9]{2}'),
    'inn': re.compile(r'[0-9]{12}'),
    'identifier': re.compile(r'[0-9]{2}-[0-9]{2}\/[0-9]{2}'),
    'occupation': re.compile(r'(?:[а-яА-Яa-zA-Z]+[-|\s]?)+'),
    'latitude': re.compile(r"""(?x)(?:\-?[0-8]\d?\.\d{2,6})| #numbers 0-8.xxxxx, 10-80.xxxxx
                           (?:\-?90\.[0]{6})| #number 90.000000
                           (?:\-?9\.\d{2,6}) #number 9.xxxxxx
                           """),
    'blood_type': re.compile(r"""(?x)(?:[ABO][+|\u2122|−])| #type A, B, O
                             (?:AB[+|\u2122|−] # type AB
                             )""", re.UNICODE),
    'issn': re.compile(r'\d{4}\-\d{4}'),
    'uuid': re.compile(r'[\da-fA-f]{8}(?:-[\da-fA-f]{4}){3}-[\da-fA-f]{12}'),
    'date': re.compile(r"""(?x)(?:18|19|20)\d\d- # year - 18xx, 19xx, 20xx
                       (?:1[0-2]|0[1-9])- #month 1 - 12
                       (?:3[01]|[12]\d|0[1-9]) # day 1 - 31
                       """)
}
    
    
def match_data(research_data :list, names :list) -> tuple:
    """эта функция проверяет данные на корректность

    Args:
        research_data (list): данные для ислледования
        names (list): массив с именами столбцов для доступа к словарю с регулярными выражениями

    Returns:
        tuple(dict, dict): возврощается массив с номерами строк, где были найдены неверные данные
                            и словарь с данными, которые подходят для дальнйшей обработки
    """
    count_not_valid_data = []
    valid_data = {}
    for n in names:
        valid_data[n] = []
    k = 0
    for row in research_data:
        for i in range(10):
            if re.fullmatch(valid_dict[names[i]], row[i]) == None:
                count_not_valid_data.append(k)
            else:
                valid_data[names[i]].append(row[i])
        k += 1
    return count_not_valid_data, valid_data
            
            