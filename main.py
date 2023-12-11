import csv
import re
from checksum import serialize_result, calculate_checksum

ROW_PATTERN = {
    "telephone": r"^\+7-\(\d{3}\)-\d{3}-\d{2}-\d{2}$",
    "http_status_message": r"^\d{3}\s[a-zA-Z0-9_ ]{1,}$",
    "shils": r"^[0-9]{11}$",
    "identifier": r"^[0-9]{2}\-[0-9]{2}\/[0-9]{2}$",
    "ip_v4": r"^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$",
    "longitude": r"^-?((1[0-7]\d|\d?\d)(?:\.\d{1,})?|180(\.0{1,})?)$",
    "blood_type": r"^(?: AB | A | B | O) [+\u2212]$",
    "isbn": r"^\d+-\d+-\d+-\d+(:?-\d+)?$",
    "locale_code": r"^[a-z]{2} (-[a-z]{2})?$",
    "date": r"^\d{4}-\d{2}-\d{2}$"
}


def read_csv(file_name) -> list:
    """
    Функция для чтения данных из csv-файла и сохранения их в список

    :param file_name: Название csv-файла
    :return: Список данных
    """
    data = []
    with open(file_name, "r", newline="", encoding="utf-16") as file:
        reader = csv.reader(file, delimiter=";")
        for i in reader:
            data.append(i)
        data.pop(0)
        return data


def row_valid_check(row: list) -> bool:
    """
    Функция проверки строки на валидность

    :param row: Строка данных
    :return: True/False
    """
    for key, value in zip(ROW_PATTERN.keys(), row):
        if not re.search(ROW_PATTERN[key], value, re.X):
            return False
    return True


def get_invalid_numbers(data: list) -> list:
    """
    Функция поиска невалидных строк

    :param data: Список данных
    :return: Список номеров невалидных строк
    """
    numbers = []
    i = 0
    for row in data:
        if not row_valid_check(row):
            numbers.append(i)
        i += 1
    return numbers


if __name__ == "__main__":
    data = read_csv("58.csv")
    invalid_numbers = get_invalid_numbers(data)
    serialize_result(58, calculate_checksum(list(invalid_numbers)))
