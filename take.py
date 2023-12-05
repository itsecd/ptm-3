import csv
import re
from checksum import serialize_result, calculate_checksum
from check_func import check_longitude, check_ip, check_date

PATTERN = {
    "telephone": r"^\+7-\(\d{3}\)-\d{3}-\d{2}-\d{2}$",
    "http_status_message": r"^\d{3}\s[a-zA-Z0-9_ ]{1,}$",
    "shils": r"^\d{11}$",
    "identifier": r"^\d{2}-\d{2}/\d{2}$",
    "ip_v4": r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$",
    "longitude": r"^-? \d{1,3} \. \d+$",
    "blood_type": r"^(?: AB | A | B | O) [+\u2212]$",
    "isbn": r"^\d+-\d+-\d+-\d+(:?-\d+)?$",
    "locale_code": r"^[a-z]{2} (-[a-z]{2})?$",
    "date": r"^\d{4}-\d{2}-\d{2}$"
}


def check_row(row_str: str) -> bool:
    """
    A function that checks the string for validity
    :param row_str: string to be checked for validity
    ::return: returns True if the string has passed validation, False - otherwise
    """
    for key, value in zip(PATTERN.keys(), row_str):
        if not re.match(PATTERN[key], value, re.X):
            return False

    return True

def get_invalid_indexs(data: list[list[str]]) -> list[int]:
    """
    Function for counting and writing to the list of invalid indexes
    :param data: source list of strings
    ::return invalid_index s: list with invalid indexes
    """
    invalid_indexs = []

    for row in data:
        if not check_row(row):
            invalid_indexs.append(data.index(row))
    return invalid_indexs


def read_csv(file_name) -> list:
    '''Читаем csv-файл и записываем его в список'''
    data = []
    with open(file_name, "r", newline="", encoding="utf-16") as file:
        reader = csv.reader(file, delimiter=";")
        for i in reader:
            data.append(i)
        data.pop(0)
        return data


if __name__ == "__main__":
    var = 42
    file_name = "42.csv"
    data = read_csv(file_name)
    invalid_indexs = get_invalid_indexs(data)
    print(len(invalid_indexs))
    print(calculate_checksum(invalid_indexs))
    serialize_result(var, calculate_checksum(list(invalid_indexs)))