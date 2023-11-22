import re
import csv

from checksum import serialize_result, calculate_checksum


PATTERNS = {
    "telephone":"^\+7-\(\d{3}\)-\d{3}-\d{2}-\d{2}$",
    "height":"^(?:0|1|2)\.\d{2}$",
    "snils":"^\d{11}$",
    "indentifier":"^\d{2}-\d{2}/\d{2}$",
    "occupation":"^[a-zA-Zа-яА-ЯёЁ\s-]+$",
    "longitude":"^-?\d{1,3}\.\d+$",
    "blood_type":"^(?:A|B|AB|O)(?:\+|\u2212)$",
    "issn":"^\d{4}-\d{4}$",
    "locale_code":"^[a-z]{2}(-[a-z]{2})?$",
    "date":"^\d{4}-(?:0[1-9]|1[0-2])-(?:0[1-9]|1\d|2[0-9]|3[0-1])$",
}

def check_valid_data(row: list) -> bool:
    """Check string for data validity"""
    for key, value in zip(PATTERNS.keys(), row):
        if not re.match(PATTERNS[key], value):
            return False
    return True

def find_invalid_data(data: list) -> None:
    """Find index of invalid data and
    call functions for automated verification of result"""
    list_index = []
    index = 0
    for i in data:
        if not check_valid_data(i):
            list_index.append(index)
        index += 1
    serialize_result(36, calculate_checksum(list_index))


def read_csv_file(file_name) -> list:
    """Read csv file"""
    data = []
    with open(file_name, "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=";")
        for i in reader:
            data.append(i)
        data.pop(0)
    return data

if __name__ == "__main__":
    find_invalid_data(read_csv_file("36.csv"))