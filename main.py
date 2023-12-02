import re
import csv
import pandas as pd
from checksum import calculate_checksum, serialize_result
from check_func import check_longitude, check_ip, check_date

PATTERNS = {
    "telephone": "^\+7-\(\d{3}\)-\d{3}-\d{2}-\d{2}$",
    "http_status_message": "^\d{3}\s[a-zA-Z0-9_ ]{1,}",
    "snils": "^\d{11}$",
    "identifier": "^\d{2}-\d{2}/\d{2}$",
    "ip_v4": "^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$",
    "longitude": "^-? \d{1,3} \. \d+$",
    "blood_type": "^(?: AB | A | B | O) [+\u2212]$",
    "isbn": "^\d+-\d+-\d+-\d+(:?-\d+)?$",
    "locale_code": "^[a-z]{2} (-[a-z]{2})?$",
    "date": "^\d{4}-\d{2}-\d{2}$",
}


def check_row(row_str: str) -> bool:
    """
    A function that checks the string for validity

    :param row_str: string to be checked for validity
    ::return: returns True if the string has passed validation, False - otherwise
    """
    for key, value in zip(PATTERNS.keys(), row_str):
        if not re.match(PATTERNS[key], value, re.X):
            return False
        if key == "longitude":
            if check_longitude(value) == False:
                return False
        if key == "ip_v4":
            if check_ip(value) == False:
                return False
        if key == "date":
            if check_date(value) == False:
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


if __name__ == "__main__":
    var = 34
    data = []
    with open("34.csv", "r", newline="", encoding="utf-16") as file:
        read_data = csv.reader(file, delimiter=";")
        for row in read_data:
            data.append(row)
    data.pop(0)
    invalid_indexs = get_invalid_indexs(data)
    print(len(invalid_indexs))
    print(calculate_checksum(invalid_indexs))
    serialize_result(var, calculate_checksum(list(invalid_indexs)))
