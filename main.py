import csv
import re

from checksum import calculate_checksum, serialize_result

PATH_TABLE = "15.csv"
PATTERNS = {
    "email": "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$",
    "height": "^\d\.\d{2}$",
    "inn": "^\d{12}$",
    "passport": "^\d{2}\s\d{2}\s\d{6}$",
    "occupation": "^[a-zA-Zа-яА-ЯёЁ\s-]+$",
    "latitude": "^-?(?:90(?:\.0+)?|[1-8]?\d(?:\.\d+)?)$",
    "hex_color": "^#([a-f0-9]{6}|[a-f0-9]{3})$",
    "issn": "^\d{4}-\d{4}$",
    "uuid": "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
    "time": "^([01]?\d|2[0-3]):([0-5]?\d):([0-5]?\d)\.(\d{1,6})$"
}


def read_table(path: str) -> list[list[str]]:
    array = []
    with open(path, "r", encoding="utf-16") as csv_file:
        reader = csv.reader(csv_file, delimiter=";")
        for row in reader:
            array.append(row)
    array.pop(0)
    return array


def valedata_row(row: list[str]) -> bool:
    columns = list(PATTERNS.keys())
    for i in range(len(columns)):
        if not bool(re.match(PATTERNS[columns[i]], row[i])):
            return False
    return True


def find_invalid_numbers(table: list[list[str]]) -> list[int]:
    invalid_rows = []
    for i in range(len(table)):
        if not valedata_row(table[i]):
            invalid_rows.append(i)
    return invalid_rows


if __name__ == "__main__":
    array = read_table(PATH_TABLE)
    array.pop(6402)
    numbers = find_invalid_numbers(array)
    sum = calculate_checksum(numbers)
    serialize_result(15, sum)
