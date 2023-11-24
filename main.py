import re
import csv

from checksum import calculate_checksum, serialize_result

PATTERNS = {
    "telephone":"^\+7-\(\d{3}\)-\d{3}-\d{2}-\d{2}$",
    "height":"^(?:0|1|2)\.\d{2}$",
    "inn":"^\d{12}$",
    "identifier":"^\d{2}-\d{2}/\d{2}$",
    "occupation":"^[a-zA-Zа-яА-ЯёЁ\s-]+$",
    "latitude":"(-?[1-8]?\d(?:\.\d{1,})?|90(?:\.0{1,})?)$",
    "blood_type":"^(?:A|B|AB|O)[−+-]?$",
    "issn":"^\d{4}-\d{4}$",
    "uuid":"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$",
    "date":"^\d{4}-\d{2}-\d{2}",
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
    serialize_result(24, calculate_checksum(list_index))

def read_csv_file(file_name) -> list:
    """Read csv file"""
    data = []
    with open(file_name, "r", newline="", encoding="utf-16") as file:
        reader = csv.reader(file, delimiter=";")
        for i in reader:
            data.append(i)
        data.pop(0)
    return data

if __name__ == "__main__":
    find_invalid_data(read_csv_file("24.csv"))