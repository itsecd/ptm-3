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
    "longitude": "^-?\d{1,3}\.\d+$",
    "hex_color": "^#[0-9a-fA-F]{6}$",
    "issn": "^\d{4}-\d{4}$",
    "locale_code": "^[a-z]{2}(-[a-z]{2})?$",
    "time": "^([01]\d|2[0-3]):([0-5]\d):([0-5]\d)\.(\d{1,6})$"
}


def longitude(longitude_tmp: str) -> bool:
    """
        Проверка долготы на корректность
        :param longitude_tmp: str
        :return: bool
    """
    value = float(longitude_tmp)
    return -180 < value < 180


def check_row(row: list) -> bool:
    """
        Проверка строки на валидность
        :param row: list
        :return: bool
    """
    for patterns, item in zip(PATTERNS.keys(), row):
        if not re.search(PATTERNS[patterns], item):
            return False
        if patterns == 'longitude':
            if longitude(item) == False:                                  
                return False
    return True


def read_csv(file_name: str) -> list:
    """
        Считывает данные из файла csv и возвращает список строк
        :param file_name: str
        :return: list
    """
    data_rows = []
    with open(file_name, "r", newline="", encoding="utf-16") as file:
        reader = csv.reader(file, delimiter=";")
        for elem in reader:
            data_rows.append(elem)
    data_rows.pop(0)
    return data_rows


def find_invalid_check(data: list) -> None:
    """
        Нахождение индексов неверных данных и вызов 
        функций автоматической проверки результатов
        :param data: list
        :return: None
    """
    list_index = []
    index = 0
    for elem in data:
        if not check_row(elem):
            list_index.append(index)
        index += 1
    serialize_result(VARIANT, calculate_checksum(list_index))


if __name__ == "__main__":
    find_invalid_check(read_csv("27.csv"))