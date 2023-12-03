import re
import csv

from checksum import calculate_checksum, serialize_result


FILE_NAME = 'ptm-3/37.csv'
VARIANT = 37
REGEX_PATTERNS = {
    "email": "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$",
    "http_status_message": "^\d{3}\s[a-zA-Z0-9_ ]{1,}",
    "inn": "^\d{12}$",
    "passport": "^\d{2} \d{2} \d{6}$",
    "ip_v4": "^'((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[1-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[1-9])",
    "latitude": "^(-?[1-8]?\d(?:\.\d{1,})?|90(?:\.0{1,})?)$",
    "hex_color": "^#[0-9a-fA-F]{6}$",
    "isbn": "^\d+-\d+-\d+-\d+(:?-\d+)?$",
    "uuid": "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$",
    "time": "^([01]\d|2[0-3]):([0-5]\d):([0-5]\d)\.(\d{1,6})$"
}

def check_valid_row(row: list) -> bool:
    '''
    A function that checks the string for validity
    
    :param row: the string to be checked for validity
    :return: True if the string has passed validation, False otherwise
    '''
    for key, value in zip(REGEX_PATTERNS.keys(), row):
        if not re.match(REGEX_PATTERNS[key], value):
            return False
    return True


def get_invalid_data(data: list) -> None:
    '''
    A function that finds indexes of invalid data and calls a function to automatically check the results
    
    param data: data for check
    '''
    list_index = []
    index = 0
    for elem in data:
        if not check_valid_row(elem):
            list_index.append(index)
        index += 1
    serialize_result(VARIANT, calculate_checksum(list_index))


def read_csv_file(file_name: str) -> list:
    '''
    A function that reads data from a csv-file and writes it in list
    
    param file_name: the name of the csv-file to be read
    return: list of data
    '''
    list_data = []
    with open(file_name, "r", newline="", encoding="utf-16") as file:
        reader = csv.reader(file, delimiter=";")
        for elem in reader:
            list_data.append(elem)
    list_data.pop(0)
    return list_data


if __name__ == "__main__":
    get_invalid_data(read_csv_file(FILE_NAME))