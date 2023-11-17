import csv
import re


def read_table(path: str) -> list[list[str]]:
    array = []
    with open(path, "r", encoding="utf-16") as csv_file:
        reader = csv.reader(csv_file, delimiter=";")
        for row in reader:
            array.append(row)
    array.pop(0)
    return array


def validate(data):
    re_pattern = re.compile(r"^-?(?:90(?:\.0+)?|[1-8]?\d(?:\.\d+)?)$")
    if re_pattern.match(data):
        return True
    return False


patterns = {
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

arr = [i[5] for i in read_table('15.csv')]

print(sum(1 for i in arr if validate(i) == False)) #101 строчка