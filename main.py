import csv
import re

from checksum import calculate_checksum, serialize_result

VARIANT = 6
PATH_TO_CSV = "6.csv"

PATTERNS = {
    "telephone": "^\\+7-\\(\\d{3}\\)-\\d{3}-\\d{2}-\\d{2}$",
    "http_status_message" : "^\\d{3}\\s[^\n\r]+$",
    "inn": "^\\d{12}$",
    "identifier": "^\\d{2}-\\d{2}/\\d{2}$",
    "ip_v4": "^((25[0-5]|(2[0-4]|1\\d|[1-9]|)\\d)\\.?\\b){4}$",
    "latitude": "^(?:\\+|-|)(90\\.0+|[0-8]\\d\\.\\d+|\\d\\.\\d+|0+\\d\\.\\d+)$",
    "blood_type": "^(?:O|A|B|AB)[\\+\u2212]$",
    "isbn": "\\d+-\\d+-\\d+-\\d+(:?-\\d+)?$",
    "uuid": "^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$",
    "date": "^(?:19|20)\\d\\d-(?:0[1-9]|1[012])-(?:0[1-9]|[12]\\d|3[01])$"
}

def read_csv(path: str) -> list:
    data = []
    with open("6.csv", "r", newline="", encoding="utf-16") as file:
        read_data = csv.reader(file, delimiter=";")
        for row in read_data:
            data.append(row)
    data.pop(0)
    return data


def check_invalid_row(row: list) -> bool:
    '''
        Функция проверки каждой строки на валидность
    '''
    for patterns, item in zip(PATTERNS.keys(), row):
        if not re.search(PATTERNS[patterns], item):
            return False
    return True


def get_no_invalid_data_index(data: list) -> list:
    '''
        Функция находит невалидные строки и записывает их индексы 
    '''
    data_index = []
    index = 0
    for row in data:
        if not check_invalid_row(row):
            data_index.append(index)
        index += 1
    return data_index


if __name__ == "__main__":
    '''
        Запись checksum
    '''
    data = read_csv(PATH_TO_CSV)
    serialize_result(VARIANT, calculate_checksum(
        get_no_invalid_data_index(data)))



