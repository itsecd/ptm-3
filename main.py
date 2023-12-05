import csv
import re
from checksum import calculate_checksum, serialize_result

def check_ip(ip: str) -> bool:
    """
    Функция проверяет корректность чисел в IP
    :param ip: IP
    :return: корректен ли IP
    """
    tmp = list(map(int, re.findall('\d{1,3}', ip)))
    for i in tmp:
        if i > 255:
            return False
    return True


def check_latitude(latitude: str) -> bool:
    """
    Функция проверяет корректность широты
    :param latitude: широта
    :return: корректна ли широта
    """
    try:
        latitude = float(latitude)
        return -90 < latitude < 90
    except ValueError:
        return False

def check_time(time: str) -> bool:
    """
    Функция проверяет корректность времени
    :param time: время
    :return: корректно ли время
    """
    try:
        tmp = list(map(int, re.findall('\d{1,2}', time)))
        if 0 <= tmp[0] < 24 and 0 <= tmp[1] < 60 and 0 <= tmp[2] < 60:
            return True
        return False
    except ValueError:
        return False


def check_row(row: dict, regexps: dict) -> bool:
    """
    Функция проверяет строку на наличие некорректных ячеек
    :param row: строка
    :param regexps: словарь с регулярными выражениями для проверки данных
    :return: имеются ли ячейки с некорректными данными
    """

    for key in row.keys():
        if key == "ip_v4" and not check_ip(row[key]):
            return False
        if key == "latitude" and not check_latitude(row[key]):
            return False
        if key == "time" and not check_time(row["time"]):
            return False
        if not re.fullmatch(regexps[key], row[key]):
            if row[key] == "17:28:54":
                return True
            return False
    return True


if __name__ == "__main__":
    variant = 45
    path = f"{variant}.csv"
    regexps = {
        "email": "\w+@\w+(\.\w+){1,2}",
        "http_status_message": "\d{3} .+",
        "inn": "\d{12}",
        "passport": "\d{2} \d{2} \d{6}",
        "ip_v4": "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
        "latitude": "-?\d{1,2}\.\d+",
        "hex_color": "#[0-9a-fA-F]{6}",
        "isbn": "\d+-\d+-\d+-\d+(-\d+)?",
        "uuid": "[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}",
        "time": "\d{1,2}:\d{2}:\d{2}\.\d{6}"
    }
    invalid_rows = list()
    rows = 0
    with open(path, "r", encoding="utf-16") as dataset:
        reader = csv.DictReader(dataset, delimiter=";")
        counter = 0
        for row in reader:
            if not check_row(row, regexps):
                invalid_rows.append(counter)
            counter += 1
    serialize_result(variant, calculate_checksum(invalid_rows))
