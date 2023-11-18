import csv
import logging
import re
from checksum import calculate_checksum
from checksum import serialize_result


logger = logging.getLogger()
logger.setLevel("INFO")
TABLE_PATH = "12.CSV"
PATTERNS = {
    "telephone": "^\\+7-\\(\\d{3}\\)-\\d{3}-\\d{2}-\\d{2}$",
    "height": "^(?:0|1|2)\\.\\d{2}$",
    "snils": "^\\d{11}$",
    "identifier": "^\\d{2}-\\d{2}/\\d{2}$",
    "occupation": "^[a-zA-Zа-яА-ЯёЁ\\s-]+$",
    "longitude": "^-?((180(\\.0+)?|1[0-7]?\\d(\\.\\d+)?|\\d{1,2}(\\.\\d+)?)|0(\\.\\d+)?)$",
    "blood_type": "^(?:O|A|B|AB)[\\+\u2212]$",
    "issn": "^\\d{4}-\\d{4}$",
    "locale_code": "^([a-z]{2,3})(?:-([a-zA-Z]{2,4}))?(?:-([a-zA-Z0-9-]+))?$",
    "date": "^(?:19|20)\\d\\d-(?:0[1-9]|1[012])-(?:0[1-9]|[12]\\d|3[01])$"
}
VARIANT = 12


def read_csv(path: str) -> list[list[str]]:
    """
    Функция считывает данные из csv файла
    :param path: путь к файлу
    :return: список строк таблицы
    """
    rows = []
    try:
        with open(path, "r", encoding="utf-16") as file:
            reader = csv.reader(file, delimiter=";")
            for row in reader:
                rows.append(row)
        rows.pop(0)
    except OSError as err:
        logging.warning(f'{err} during reading from {path}')
    return rows


def check_row(row: list) -> bool:
    """
    Функция проверяет строку таблицы на наличие неправильной записи
    :param row: строка таблицы
    :return: Истина, если неправильных записей в строке нет. Ложь - в противном случае
    """
    keys = list(PATTERNS.keys())
    for i in range(len(keys)):
        flag = bool(re.match(PATTERNS[keys[i]], row[i]))
        if not flag:
            return flag
    return True


def find_invalid_rows(path: str) -> list[int]:
    """
    Функция нахождения номеров строк, в которых присутствует неправильная запись
    :param path: путь к таблице
    :return: список номеров неправильных строк
    """
    invalid_rows = []
    data = read_csv(path)
    for i in range(len(data)):
        if not check_row(data[i]):
            invalid_rows.append(i)
    return invalid_rows


if __name__ == "__main__":
    invalid_numbers = find_invalid_rows(TABLE_PATH)
    hash_sum = calculate_checksum(invalid_numbers)
    serialize_result(VARIANT, hash_sum)


