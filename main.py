import csv
import re
from checksum import serialize_result, calculate_checksum

PATTERN = {
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
    '''
    Читаем csv-файл и записываем его в список
    '''
    data = []
    with open(file_name, "r", newline="", encoding="utf-16") as file:
        reader = csv.reader(file, delimiter=";")
        for i in reader:
            data.append(i)
        data.pop(0)
        return data

def check_invalid_row(row: list) -> bool:
    '''
       Проверяем каждую строку на валидность
    '''
    for key, value in zip(PATTERN.keys(), row):
        if not re.search(PATTERN[key], value, re.X):
            return False
    return True

def get_invalid_indexs(data: list) -> list:
    '''
        Находим невалидные строки и записываем их индексы 
    '''
    indexs = []
    index = 0
    for row in data:
        if not check_invalid_row(row):
            indexs.append(index)
        index += 1
    return indexs

if __name__ == "__main__":
    variant = 42
    file_name = "42.csv"
    data = read_csv(file_name)
    invalid_indexs = get_invalid_indexs(data)
    print(len(invalid_indexs))
    print(calculate_checksum(invalid_indexs))
    serialize_result(variant, calculate_checksum(list(invalid_indexs)))

