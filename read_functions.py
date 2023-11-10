import csv
import json
import re
from checksum import calculate_checksum, serialize_result

REGEXPS_PATH = "regex_patterns.json"
CSV_PATH = "11.csv"


def read_regex_patterns(path: str) -> dict[str]:
    """function that reads regex patterns from .json file

    Args:
        path (str): path to regex patterns file

    Returns:
        dict: dictionary with regexes
    """
    try:
        with open(path, "r", encoding="utf-8") as file:
            regex_patterns = json.load(file)
    except Exception as e:
        print(f"Error while reading .json file: {e}")
    return regex_patterns


def read_csv_file(path: str) -> list[dict[str]]:
    """function that reads data from .csv file

    Args:
        path (str): path to dataset file

    Returns:
        list[dict[str]]: list that contains dictionaries
    """
    dataset = []
    try:
        with open(path, "r", newline="", encoding="utf-16") as file:
            csv_reader = csv.reader(file, delimiter=";")
            for row in csv_reader:
                dataset.append(row)
        dataset.pop(0)
    except Exception as e:
        print(f"Error while reading file with dataset: {e}")
    return dataset


def validate_row(row, regex_patterns):
    for header, value in zip(regex_patterns.keys(), row):
        if not re.match(regex_patterns[header], value):
            return False
    return True


def get_invalid_rows_numbers(csv_path: str, regs_path: str):
    invalid_rows_numbers = []
    dataset = read_csv_file(csv_path)
    regs = read_regex_patterns(regs_path)
    for i, row in enumerate(dataset):
        if not validate_row(row, regs):
            invalid_rows_numbers.append(i)
    return invalid_rows_numbers


if __name__ == "__main__":
    regs = read_regex_patterns(REGEXPS_PATH)
    dataset = read_csv_file(CSV_PATH)
    invalid_rows_numbers = get_invalid_rows_numbers(CSV_PATH, REGEXPS_PATH)
    hash_sum = calculate_checksum(invalid_rows_numbers)
    print(hash_sum)
    serialize_result(11, hash_sum)