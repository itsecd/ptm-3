import csv
import re
from checksum import calculate_checksum, serialize_result

PATTERNS = {
    "telephone":"^\+7-\(\d{3}\)-\d{3}-\d{2}-\d{2}$",
    "height":"^(?:0|1|2)\.\d{2}$",
    "snils":"^\d{11}$",
    "indentifier":"^\d{2}-\d{2}/\d{2}$",
    "occupation":"^[a-zA-Zа-яА-ЯёЁ\s-]+$",
    "longitude":"^-?((1[0-7]\d)|([1-9]\d?)|180)(?:\.\d+)$",
    "blood_type":"^[ABO][+-]$",
    "issn":"^\d{4}-\d{4}$",
    "locale_code":"^[a-z]{2}(-[a-z]{2})?$",
    "date":"^[0-9]{4}-(0[1-9]|1[012])-(0[1-9]|1[0-9]|2[0-9]|3[01])$",
}


def read_csv_file(file_name: str) -> list:
    """
    Reads csv file

    Args: file_name - a string representing the name of the csv file to be read

    Return: a list contains the data from the csv file 

    """
    data = []
    with open(file_name, "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=";")
        for i in reader:
            data.append(i)
        data.pop(0)
    return data


def check_valid_data(data: list) -> bool:
    """
    Check string for data validity.

    Args: A list representing the row of data to be checked.
    
    Return: A boolean value indicating whether the row of data is valid or not.

    """
    for key, value in zip(PATTERNS.keys(), data):
        if not re.match(PATTERNS[key], value):
            return False
    return True


def get_invalid_data(data: list) -> list:
    """
    Get invalid data.

    Args: a list representing the data to be checked.
 
    Return: a list containing the row numbers that do not match the regular expressions.
    
    """
    invalid_data = []
    for i, row in enumerate(data):
        if not check_valid_data(row):
            invalid_data.append(i)
    return invalid_data


if __name__ == "__main__":
    invalid_data = get_invalid_data(read_csv_file("28.csv"))
    hash_sum = calculate_checksum(invalid_data)
    serialize_result(28, hash_sum)
