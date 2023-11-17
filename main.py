import csv
import re

from checksum import calculate_checksum, serialize_result

# "email";"height";"inn";"passport";"occupation";"latitude";"hex_color";"issn";"uuid";"time"
PATTERNS = {
    "email": "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$",
    "height": "^\d\.\d{2}$",
    "inn": "\d{12}",
    "passport": "^\d{2}\s\d{2}\s\d{6}$",
    "occupation": "^[a-zA-Zа-яА-ЯёЁ\s-]+$",
    "latitude": "-?(?:90(?:\.0+)?|[1-8]?\d(?:\.\d+)?)",
    "hex_color": "^#([a-f0-9]{6}|[a-f0-9]{3})$",
    "issn": "^\d{4}-\d{4}$",
    "uuid": "[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}",
    "time": "^([01]\d|2[0-3]):([0-5]\d):([0-5]\d)\.(\d{1,6})$"
}


def cheak_invalid_latitude(item: str) -> bool:
    if not re.match(PATTERNS["latitude"], item) or re.search("[^0-9.+-]", item):
        return False
    return float(item) > -90 or float(item) < 90


def check_invalid_row(row: list) -> bool:
    flag = True
    for patterns, item in zip(PATTERNS.keys(), row):
        if patterns == "latitude":
            flag = cheak_invalid_latitude(item)
        elif not re.search(PATTERNS[patterns], item):
            return False
    return flag


def get_no_invalid_data_index(data: list) -> list:
    data_index = []
    index = 0
    for row in data:
        if not check_invalid_row(row):
            data_index.append(index)
        index += 1
    return data_index


if __name__ == "__main__":
    data = []
    with open("7.csv", "r", newline="", encoding="utf-16") as file:
        read_data = csv.reader(file, delimiter=";")
        for row in read_data:
            data.append(row)
    data.pop(0)
    print(len(get_no_invalid_data_index(data)))
