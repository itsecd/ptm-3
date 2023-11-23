import csv
import re

from checksum import calculate_checksum, serialize_result

VARIANT = 27


PATTERNS = {
    "email": "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$",
    "height": "^(?:0|1|2)\.\d{2}$",
    "snils": "^\d{11}$",
    "passport": "^\d{2} \d{2} \d{6}$",
    "occupation": "^[a-zA-Zа-яА-ЯёЁ\s-]+$",
    "longitude": "^-?((1[0-7]\d)|([1-9]\d?)|180)(?:\.\d+)$",
    "hex_color": "^#[0-9a-fA-F]{6}$",
    "issn": "^\d{4}-\d{4}$",
    "locale_code": "^[a-z]{2}(-[a-z]{2})?$",
    "time": "^([01]\d|2[0-3]):([0-5]\d):([0-5]\d)\.(\d{1,6})$"
}


def check_invalid_row(row: list) -> bool:
    """
        Функция принимает на вход список row и проверяет, 
        соответствует ли каждый элемент списка определенному шаблону. 
        Для этого используются регулярные выражения из словаря PATTERNS. 
        Если хотя бы один элемент не соответствует своему шаблону, 
        функция возвращает False, иначе возвращает True.
    """
    for patterns, item in zip(PATTERNS.keys(), row):
        if not re.search(PATTERNS[patterns], item):
            return False
    return True


def get_no_invalid_data_index(data: list) -> list:
    """
        Функция принимает на вход список data, который представляет
        собой список списков. Она проходит по каждой строке в списке data
        и вызывает функцию check_invalid_row для проверки каждого элемента в строке. 
        Если хотя бы один элемент не соответствует своему шаблону, индекс этой 
        строки добавляется в список data_index. В конце функция возвращает список
        индексов невалидных строк. Таким образом, функция находит и записывает индексы
        невалидных строк в исходном списке данных.
    """
    data_index = []
    index = 0
    for row in data:
        if not check_invalid_row(row):
            data_index.append(index)
        index += 1
    return data_index


if __name__ == "__main__":
    '''
        Считывание csv файла и запись checksum
    '''
    data = []
    with open("27.csv", "r", newline="", encoding="utf-16") as file:
        read_data = csv.reader(file, delimiter=";")
        for row in read_data:
            data.append(row)
    data.pop(0)
    serialize_result(VARIANT, calculate_checksum(
        get_no_invalid_data_index(data)))