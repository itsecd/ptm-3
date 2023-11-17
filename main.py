import re
import csv
import json


REGEXPS = {
    "email": "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$",
    "http_status_message": "^\d{3}\s[^\n\r]+$",
    "inn": "^\d{12}$",
    "passport": "^\d{2} \d{2} \d{6}$",
    "ip_v4": "^(\d{1,3}\.){3}\d{1,3}$",
    "latitude": "^-?\d+(\.\d+)?$",
    "hex_color": "^#[0-9a-fA-F]{6}$",
    "isbn": "\d+-\d+-\d+-\d+(:?-\d+)?$",
    "uuid": "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$",
    "time": "^([01]\d|2[0-3]):([0-5]\d):([0-5]\d)\.(\d{1,6})$",
}


def read_csv(path_to_csv: str) -> list:
    data = []
    try:
        with open(path_to_csv, "r", encoding="utf16") as file:
            reader = csv.reader(file, delimiter=";")
            for row in reader:
                data.append(row)
            data.pop(0)
    except FileNotFoundError:
        print(f"Файл '{path_to_csv}' не найден.")
    except Exception as e:
        print(f"Произошла ошибка при чтении файла: {e}")
    return data


with open('REGEXPS.json', 'w') as json_file:
    json.dump(REGEXPS, json_file, indent=10)

file_path = "5.csv"