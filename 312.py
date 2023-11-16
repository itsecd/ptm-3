import csv
import logging

TABLE_PATH = "12.CSV"
PATTERNS = {
    "telephone": "",
    "height": "",
    "snils": "",
    "identifier": "",
    "occupation": "",
    "longitude": "",
    "blood_type": "",
    "issn": "",
    "locale_code": "",
    "date": ""
}


def read_csv(path: str) -> list:
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


if __name__ =="__main__":
    rw = read_csv(TABLE_PATH)
    print(rw[0])