import re
import csv
from checksum import calculate_checksum, serialize_result

PATTERNS = {
    "telephone": "\\+7 - \\(\\d{3}\\) - \\d{3} - \\d{2} - \\d{2}",
    "http_status_message": "^\d{3}\s[a-zA-Z0-9_ ]{1,}",
    "snils": "\\d{11}",
    "identifier": "\\d{2} - \\d{2} / \\d{2}",
    "ip_v4": "\\d{1,3} \\. \\d{1,3} \\. \\d{1,3} \\. \\d{1,3}",
    "longitude": "-? \\d{1,3} \\. \\d+",
    "blood_type": "(?: AB | A | B | O) [+|−]",
    "isbn": "\\d+ - \\d+ - \\d+ - \\d+ (?: -\\d+)?",
    "locale_code": "[a-z]{2} (-[a-z]{2})?",
    "date": "\\d{4} - \\d{2} - \\d{2}"
}

def check_row(row: list) -> bool:
    """ Проверяет строку таблицы на валидность

    Args:
        row (list): Строка таблицы для проверки( массив строк-столбцов )

    Returns:
        bool: Результат прохождения/непрохождения проверки
    """
    keys = PATTERNS.keys()
    i = 0
    for key in keys:
        if (not re.fullmatch(PATTERNS[key], row[i], re.X)):
            return False  
        i +=1 
    return True    

def check_data(data: list) -> list:
    """ Проверяет входящие данные таблицы на валидность

    Args:
        data (list): Массив строк с данными

    Returns:
        list: Массив индексов строк с невалидными данными
    """
    list_of_invalid_indexs = []
    index = 0
    for row in data:
        if(not check_row(row)):
            list_of_invalid_indexs.append(index)
        index +=1       
    return list_of_invalid_indexs

if __name__ == '__main__':
    data = []
    with open("18.csv", "r", encoding="utf-16") as file:
        read_data = csv.reader(file, delimiter=";")
        for row in read_data:
            data.append(row)
    data.pop(0)
    list_of_invalid_indexs = check_data(data)
    print(len(check_data(data)))
    serialize_result('18', calculate_checksum(list(list_of_invalid_indexs)))