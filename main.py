from csv import reader
from re import match

from checksum import calculate_checksum, serialize_result


PATTERNS = {
    "email": "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$",
    "html_status_message": "^\d{3} [a-zA-Z ]+$",
    "snils": "^\d{11}$",
    "passport": "^\d{2} \d{2} \d{6}$",
    "ip_v4": "^((25[0-5]|2[0-4]\d|1\d\d|\d?\d)\.)"
             "{3}(25[0-5]|2[0-4]\d|1\d\d|\d?\d)$",
    "longitude": "^-?((1[0-7]\d|\d?\d)(?:\.\d{1,})?|180(\.0{1,})?)$",
    "hex_color": "^#[0-9a-fA-F]{6}$",
    "isbn": "^\d{3}-\d{1}-\d{5}-\d{3}-\d{1}|\d{1}-\d{5}-\d{3}-\d{1}$",
    "locale_code": "^[a-z][a-z](-[a-z][a-z])?$",
    "time": "^([01]\d|2[0-3]):([0-5]\d):([0-5]\d)\.(\d{1,6})$"
}


def check_valid_data(row: list) -> bool:
    '''Проверка строки на достоверность данных'''
    for key, value in zip(PATTERNS.keys(), row):
        if not match(PATTERNS[key], value):
            return False
    return True


def find_invalid_data(data: list) -> list:
    '''
    Поиск индексов недопустимых данных и вызов функции
    для автоматической проверки контрольной суммы
    '''
    list_index = []
    index = 0
    for elem in data:
        if not check_valid_data(elem):
            list_index.append(index)
        index += 1
    return list_index


def read_csv_data(file_name: str) -> list:
    '''Чтение csv-файла и запись данных в список'''
    list_data = []
    with open(file_name, "r", newline="", encoding="utf-16") as file:
        csv_data = reader(file, delimiter=";")
        for row in csv_data:
            list_data.append(row)
    list_data.pop(0)
    return list_data


if __name__ == "__main__":
    '''
    Инициализация значений и вызов функции
    для поиска индексов недействительных данных
    '''
    file_name = "49.csv"
    variant = 49
    list_index = find_invalid_data(read_csv_data(file_name))
    #serialize_result(variant, calculate_checksum(list_index))
