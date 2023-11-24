import csv
import json
import logging
import re
from checksum import serialize_result, calculate_checksum


logger = logging.getLogger()
logger.setLevel("INFO")
CSV_PATH = "19.csv"
REGEXPS_PATH = "REGEXPS.json"
VARIANT = 19


def read_csv(path_to_csv: str) -> list:
    data = []
    try:
        with open(path_to_csv, "r", encoding="utf16") as file:
            reader = csv.reader(file, delimiter=";")
            for row in reader:
                data.append(row)
            data.pop(0)
    except FileNotFoundError:
        logging.error(f"Файл {path_to_csv} не найден.")
    except Exception as e:
        logging.error(f"Произошла ошибка при чтении csv файла: {e}")
    return data


def read_json(path_json: str) -> dict:
    data = {}
    try:
        with open(path_json, "r") as json_file:
            data = json.load(json_file)
    except FileNotFoundError:
        logging.error(f"Файл {path_json} не найден.")
    except Exception as e:
        logging.error(f"Произошла ошибка при чтении json файла: {e}")
    return data


def validate_row(row: list, patterns: dict) -> bool:
    for key, value in zip(patterns.keys(), row):
        if not re.match(patterns[key], value):
            return False
    return True


def validate_data(path_json: str, path_csv: str) -> None:
    patterns = read_json(path_json)
    data = read_csv(path_csv)
    nonvalidate_rows = []
    for i in range(len(data)):
        if not validate_row(data[i], patterns):
            nonvalidate_rows.append(i)
    serialize_result(VARIANT, calculate_checksum(nonvalidate_rows))


if __name__ == "__main__":
    validate_data(REGEXPS_PATH, CSV_PATH)
