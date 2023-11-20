import re
import csv

from checksum import calculate_checksum, serialize_result


PATTERNS = {
    "email": "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$",
    "height": "^(?:0|1|2)\.\d{2}$",
    "inn": "^\d{12}$",
    "passport": "^\d{2} \d{2} \d{6}$",
    "occupation": "^[a-zA-Zа-яА-ЯёЁ\s-]+$",
    "latitude": "^(-?[1-8]?\d(?:\.\d{1,})?|90(?:\.0{1,})?)$",
    "hex_color": "^#[0-9a-fA-F]{6}$",
    "issn": "^\d{4}-\d{4}$",
    "uuid": "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$",
    "time": "^([01]\d|2[0-3]):([0-5]\d):([0-5]\d)\.(\d{1,6})$"
}


def check_valid_data(row: list) -> bool:
    '''Сheck string for data validity'''
    for key, value in zip(PATTERNS.keys(), row):
        if not re.match(PATTERNS[key], value):
            return False
    return True


def find_invalid_data(data: list) -> None:
    '''Find indexes of invalid data and 
    call functions for automated verification of results'''
    list_index = []
    index = 0
    for elem in data:
        if not check_valid_data(elem):
            list_index.append(index)
        index += 1
    serialize_result(variant, calculate_checksum(list_index))


def read_csv_data(file_name: str) -> list:
    '''Read csv-file and write data in list'''
    list_data = []
    with open(file_name, "r", newline="", encoding="utf-16") as file:
        reader = csv.reader(file, delimiter=";")
        for elem in reader:
            list_data.append(elem)
    list_data.pop(0)
    return list_data


if __name__ == "__main__":
    '''Initialization of values and 
    call function for finding indexes of invalid data'''
    file_name = "31.csv"
    variant = 31
    find_invalid_data(read_csv_data(file_name))
