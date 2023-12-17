import re
import csv
from checksum import calculate_checksum, serialize_result


PATTERNS = {
    "telephone": "^\+7-\(\d{3}\)-\d{3}-\d{2}-\d{2}$",
    "height": "^(?:0|1|2)\.\d{2}$",
    "inn": "^\d{12}$",
    "identifier": "^\d{2}-\d{2}/\d{2}$",
    "occupation": "^[a-zA-Zа-яА-ЯёЁ\s-]+$",
    "latitude": "^(-?[1-8]?\d(?:\.\d{1,})?|90(?:\.0{1,})?)$",
    "blood_type": "^(AB|A|B|O)[−+-]?$", 
    "issn": "^\d{4}-\d{4}$",
    "uuid": "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$",
    "date": "^\d{4}-\d{2}-\d{2}$"

}


def check_valid_line(row: list) -> bool:
    '''Проверяет строку на валидность данных'''
    for key, value in zip(PATTERNS.keys(), row):
        if not re.match(PATTERNS[key], value):
            return False
    return True


def find_invalid_data(data: list) -> None:
    '''Находит индексы недопустимых данных и вызывает функции для автоматической проверки результатов'''
    list_index = [index for index, elem in enumerate(data) if not check_valid_line(elem)]
    serialize_result (variant, calculate_checksum(list_index))


def read_csv_data(file_name: str) -> list:
    '''Читает csv-файл и записывает данные в список'''
    with open(file_name, "r", newline="", encoding="utf-16") as file:
        reader = csv.reader(file, delimiter=";")
        next(reader)  # Пропускаем заголовок
        return list(reader)

if __name__ == "__main__":
    '''Initialization of values and 
    call function for finding indexes of invalid data'''
    file_name = "32.csv"
    variant = 32
    find_invalid_data(read_csv_data(file_name))