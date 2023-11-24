import csv
import re
from checksum import calculate_checksum, serialize_result

VARIANT = 54

PATTERNS = {
    "telephone": "^\+7-\(\d{3}\)-\d{3}-\d{2}-\d{2}$",
    "http_status_message": "^\d{3} \s .+$",
    "inn": "^\d{12}$",
    "identifier": "^\d{2}-\d{2}/\d{2}$",
    "ip_v4": "^\d{1,3} \. \d{1,3} \. \d{1,3} \. \d{1,3}$",
    "latitude": "^(-?[1-8]?\d(?:\.\d{1,})?|90(?:\.0{1,})?)$",
    "blood_type": "^(AB|A|B|O)[−+-]?$",
    "isbn": "^\d{3}-\d{1}-\d{5}-\d{3}-\d{1}|\d{1}-\d{5}-\d{3}-\d{1}$",
    "uuid": "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$",
    "date": "^\d{4}-\d{2}-\d{2}$",
}


def check_corect_latitude(latitude_tmp: str) -> bool:
    """
        Проверка широты на корректность
        :param latitude_tmp: str
        :return: true or false
    """
    value = float(latitude_tmp)
    return -90 < value < 90

def check_correct_ip(ip: str) -> bool:
    """
        Проверка корректности чисел в IP.
        :param ip: str
        :return: true or false
    """
    numbers = list(map(int, re.findall(r'\d{1,3}', ip)))
    for number in numbers:
        if number > 255:
            return False
    return True


def check_invalid_row(row: list) -> bool:
    """
        Проверка строки на достоверность данных
        :param row: list
        :return: true or false
    """
    for patterns, item in zip(PATTERNS.keys(), row):
        if not re.search(PATTERNS[patterns], item):
            return False
        if patterns == 'latitude':
            if not check_corect_latitude(item):
                return False
        if patterns == 'ip_v4':
            if not check_correct_ip(item):
                return False
    return True


def find_invalid_data(data: list) -> list:
    """
        Поиск индексов недопустимых данных и вызов функции
        для автоматической проверки контрольной суммы
        :param data: list
        :return: list
    """
    list_index = []
    index = 0
    for elem in data:
        if not check_invalid_row(elem):
            list_index.append(index)
        index += 1
    return list_index


def read_csv(file_name: str) -> list:
    """
        Считывает данные из файла csv и возвращает список строк
        :param file_name: string
        :return: list
    """
    data_rows = []
    with open(file_name, "r", newline="", encoding="utf-16") as file:
        reader = csv.reader(file, delimiter=";")
        for elem in reader:
            data_rows.append(elem)
    data_rows.pop(0)
    return data_rows

if __name__ == "__main__":
    data = read_csv("54.csv")
    invalid_rows = find_invalid_data(data)
    serialize_result(VARIANT, calculate_checksum(invalid_rows))
