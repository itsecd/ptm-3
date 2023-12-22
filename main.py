import re
import csv
from checksum import calculate_checksum, serialize_result

EXPRESSIONS = {
    "email": "^[a-zA-Z0-9._+-]+@[a-z]+\.[a-z]{2,}$",
    "http_status_message": "^\d{3}( [a-zA-Z]{2,}){1,}$",
    "inn": "^\d{12}$",
    "passport": "^\d{2} \d{2} \d{6}$",
    "ip_v4": "^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.){3}(25[0-5]|(2[0-4]|1\d|[1-9]|)\d)$",
    "latitude": "^[-]?(90\.0+|[1-8]\d\.\d+|\d\.\d+)$",
    "hex-color": "^#[0-9a-z]{6}$",
    "isbn": "^(\d{3}-|)[0-9]-[0-9]{5}-[0-9]{3}-[0-9]$",
    "uuid": "^[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}$",
    "time": "^([01]\d|2[0-3]):[0-5]\d:[0-5]\d.\d{6}$"
}


def check_valid_row(row: list) -> bool:
    '''Проверяет, соответствует ли строка регулярным выражениям'''
    for key, value in zip(EXPRESSIONS.keys(), row):
        if not re.match(EXPRESSIONS[key], value):
            return False
    return True


def read_csv(file_name: str) -> list:
    '''Читает данные из csv-файла и записывает в список'''
    with open(file_name, "r", newline="", encoding="utf-16") as file:
        reader = csv.reader(file, delimiter=";")
        next(reader)
        return list(reader)


def invalid_data(path_csv: str) -> list:
    ''' Записывает номера строк, которые не соотвествуют регулярным выражениям. '''
    data = read_csv(path_csv)
    invalid_rows_numbers = []
    for i in range(len(data)):
        if not check_valid_row(data[i]):
            invalid_rows_numbers.append(i)
    return invalid_rows_numbers


if __name__ == "__main__":
    variant = 61
    invalid_rows = invalid_data("61.csv")
    serialize_result(variant, calculate_checksum(invalid_rows))
