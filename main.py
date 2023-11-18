import os
import csv
import re

from checksum import serialize_result, calculate_checksum

REG_EXP = {
    "telephone": r"\+7-\(\d{3}\)-\d{3}-\d{2}-\d{2}",
    "height": r"\b[0-2]\.\d{1,2}\b",
    "inn": r"^\b\d{12}\b$",
    "identifier": r"\b\d{2}-\d{2}\/\d{2}\b",
    "occupation": r"[A-ZА-Я]+[a-zа-я ^-]+",
    "latitude": r"^-?(?:90(?:\.0+)?|[1-8]?\d(?:\.\d+)?)$",
    "blood_type": r"\b(?:AB|A|B|O)[−+-]{1}",
    "issn": r"\b\d{4}\-\d{4}",
    "uuid": r'\b[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}\b',
    "date": r"\b\d{4}-(0([13578]-(0[1-9]|[1-2]\d|3[0-1])|[469]-(0[1-9]|[1-2]\d|30)|2-(0[1-9]|1\d|2[0-9])|)|1([02]-"
            r"(0[1-9]|[1-2]\d|3[0-1])|1-(0[1-9]|[1-2]\d|30)))\b"
}


def is_valid_line(row: list[str]) -> bool:
    """
    Проверяет строку csv-файла на корректность.
    :param row: list[str]
    :return: bool
    """
    flag = True
    for k, v in zip(REG_EXP.keys(), row):
        if not re.match(REG_EXP[k], v):
            flag = False
            print(f"{k}: {v}")
            return flag
    return flag


def wrong_lines_list(file: str) -> list[int]:
    """
    Создает список индексов строк csv файла, в которых были обнаружены ошибки
    :param file: str
    :return: list[int]
    """
    csv_data = []
    index_list = []
    with open(file, "r", newline="", encoding="utf-16") as f:
        data = csv.reader(f, delimiter=";")
        for row in data:
            csv_data.append(row)
    csv_data.pop(0)
    for i, row in enumerate(csv_data):
        if not is_valid_line(row):
            index_list.append(i)
    return index_list


if __name__ == "__main__":
    csv_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "64.csv")
    wrong_lines = wrong_lines_list(csv_file)
    print(len(wrong_lines))
    serialize_result(64, calculate_checksum(wrong_lines))
